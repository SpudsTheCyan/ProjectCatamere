#sentiment_analysis.py
# https://www.datacamp.com/tutorial/text-analytics-beginners-nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

df = pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')
# df = pd.read_csv('parsed_dataset_catamere.csv')

# create preprocess_text function
def preprocess_text(text):

    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

# apply the function df
df['reviewText'] = df['reviewText'].apply(preprocess_text)
df

# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    
    match scores:
        case _ if scores["pos"] > 0.5:
            sentiment = "Good"
        case _ if scores["neg"] > 0.5:
            sentiment = "Bad"
        case _:
            sentiment = "Neutral"

    return sentiment, scores

# apply get_sentiment function
df['sentiment'] = df['reviewText'].apply(get_sentiment)
df
FROM python:3.12.1-bullseye

COPY requirements.txt /app/
WORKDIR /app/
RUN pip install -r requirements.txt

COPY . .

CMD ["python3","-m","flask", "run","--host=0.0.0.0"]

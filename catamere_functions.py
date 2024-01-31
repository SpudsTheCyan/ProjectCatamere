from tinydb import TinyDB, Query
import random, datetime

db = TinyDB('catamere_db.json')
Query = Query()

def static_select() -> str:
    table = db.table("outcomes")
    result = table.search(Query.static.exists())
    outcome = random.choice(result[0]["static"][0])
    return outcome

def dynamic_select() -> str:
    table = db.table("outcomes")
    result = table.search(Query.static.exists())
    outcome_string = " ".join(result[0]["static"][0])
    outcome_list = outcome_string.split(" ")
    word_one_list = outcome_list[::2]
    word_two_list = outcome_list[1::2]
    outcome = f"{random.choice(word_one_list)} {random.choice(word_two_list)}"
    return outcome

def get_outcomes() -> list[str]:
    table = db.table("outcomes")
    result = table.search(Query.static.exists())
    outcomes = result[0]["static"][0]
    return outcomes

def update_outcomes(outcome_list:list[str]) -> None:
    table = db.table("outcomes")
    table.update({"static": [(outcome_list)]})

    return None

from tinydb import TinyDB, Query
import random

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

def append_outcome(outcome:str) -> list[str]:
    table = db.table("outcomes")
    result = table.search(Query.static.exists())
    outcomes = result[0]["static"][0]
    outcomes.append("test test")

    return outcomes

def update_outcomes(outcome_list:list[str]) -> list[str]:
    table = db.table("outcomes")
    result = table.search(Query.static.exists())
    old_outcomes = set(result[0]["static"][0])
    # diff = [x for x in outcome_list if x not in old_outcomes]

    table.update({"static": [(outcome_list)]})

    return old_outcomes

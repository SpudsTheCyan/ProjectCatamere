import re
from tinydb import TinyDB, Query


def parse_file() -> list[str]:
    with open("wand_outcomes.txt", "r") as file:
        file_contents = file.read()
        static_outcome_list = re.split("[\n]", file_contents)
        dynamic_outcome_list = re.split("[ \n]", file_contents)
    return [static_outcome_list]

outcome_list = parse_file()

db = TinyDB('catamere_db.json')
table = db.table("outcomes")
table.insert({"static": outcome_list})
import json
from pymongo import MongoClient
import os

client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["smartbot"]

with open("data/db.json", encoding="utf-8") as file:
    data = json.load(file)

categories = {}

for item in data:

    category_name = item["categoria"]

    if category_name not in categories:

        category = db.categories.find_one({
            "name": category_name
        })

        if not category:

            result = db.categories.insert_one({
                "name": category_name
            })

            categories[category_name] = result.inserted_id

        else:
            categories[category_name] = category["_id"]

for item in data:

    db.questions.insert_one({
        "question": item["pregunta"],
        "answer": item["respuesta"],
        "category_id": categories[item["categoria"]]
    })

print("Datos cargados correctamente")
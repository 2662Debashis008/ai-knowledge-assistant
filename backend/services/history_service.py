import json
import os

FILE = "storage/chat_history.json"

os.makedirs(
    "storage",
    exist_ok=True
)

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def save_chat(
        question,
        answer
):

    with open(FILE, "r") as f:
        data = json.load(f)

    data.append({
        "question": question,
        "answer": answer
    })

    with open(FILE, "w") as f:
        json.dump(
            data,
            f,
            indent=2
        )

def get_history():

    with open(FILE, "r") as f:
        return json.load(f)
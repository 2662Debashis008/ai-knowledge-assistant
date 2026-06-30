import json
import os
import uuid

FILE = "storage/chat_history.json"

os.makedirs("storage", exist_ok=True)

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


def _normalize_chat(chat):

    if "chat_id" in chat and "messages" in chat:
        return chat

    question = chat.get("question", "")
    answer = chat.get("answer", "")

    return {
        "chat_id": chat.get("id") or str(uuid.uuid4()),
        "title": chat.get("title") or question or "Untitled chat",
        "messages": [
            {
                "question": question,
                "answer": answer
            }
        ] if question or answer else []
    }


def _load_chats():

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = []

    if not isinstance(data, list):
        return []

    return [
        _normalize_chat(chat)
        for chat in data
        if isinstance(chat, dict)
    ]


def _save_chats(chats):

    with open(FILE, "w") as f:
        json.dump(chats, f, indent=2)


def create_chat():

    chat_id = str(uuid.uuid4())

    return {
        "chat_id": chat_id
    }

def save_chat(chat_id, question, answer):

    chats = _load_chats()

    found = False

    for chat in chats:

        if chat.get("chat_id") == chat_id:

            chat["messages"].append({
                "question": question,
                "answer": answer
            })

            found = True
            break

    if not found:

        chats.append({
            "chat_id": chat_id,
            "title": question,
            "messages": [
                {
                    "question": question,
                    "answer": answer
                }
            ]
        })

    _save_chats(chats)

def get_history():

    chats = _load_chats()

    _save_chats(chats)

    return chats


def delete_chat(chat_id):

    data = _load_chats()

    data = [
        chat for chat in data
        if chat.get("chat_id") != chat_id
    ]

    _save_chats(data)

    return {"message": "Chat deleted"}

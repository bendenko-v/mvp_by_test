import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient


def get_db_handle():
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    client = MongoClient(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    db_name = os.getenv("DB_NAME")

    if db_name not in client.list_database_names():
        client[db_name].command("ping")

    db_handle = client[db_name]
    return db_handle, client


def create_user_collection(collection_name, user_data):
    db_handle, client = get_db_handle()

    if collection_name not in db_handle.list_collection_names():
        db_handle.create_collection(collection_name)

    db_handle[collection_name].insert_one(user_data)
    client.close()


if __name__ == "__main__":
    example_user = {
        "username": "Monthy Python",
        "email": "mnty_python@example.com",
        "password": "hashed_password",
    }

    # Example usage
    create_user_collection("users", example_user)

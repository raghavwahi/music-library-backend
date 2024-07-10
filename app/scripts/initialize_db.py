"""
This module initializes the SQLite database with data from a JSON file.
It reads the data from 'playlist.json', adds a 'rating' column, and
inserts the data into an SQLite database.

Raises:
    InitializationError: If the DATABASE_URL environment variable is not set.
"""

import os
import sqlite3

import pandas as pd
from dotenv import load_dotenv


class InitializationError(Exception):
    """Custom exception raised when there is an error during the initialization process."""

    pass


def initialize():
    """
    Initializes the SQLite database with data from 'playlist.json'.

    This function performs the following steps:
    1. Reads the data from 'playlist.json' into a DataFrame.
    2. Adds a 'rating' column to the DataFrame with a default value of 0.
    3. Connects to the SQLite database specified by the DATABASE_URL environment variable.
    4. Inserts the DataFrame into the 'songs' table of the SQLite database.
    5. Verifies that the data was loaded correctly by printing the first few rows of the 'songs' table.

    Raises:
        InitializationError: If the DATABASE_URL environment variable is not set.
    """
    songs_df = pd.read_json("app/data/playlist.json")
    songs_df["rating"] = 0

    env_var = "DATABASE_URL"
    db = os.environ.get(env_var)
    if not db:
        raise InitializationError(f"{env_var} environment variable not set.")

    conn = sqlite3.connect("data.db")
    songs_df.to_sql("songs", conn, if_exists="replace", index=False)

    # Verify that data was loaded correctly
    songs_df = pd.read_sql("SELECT * FROM songs", conn)
    print(songs_df.head())


if __name__ == "__main__":
    load_dotenv()
    initialize()

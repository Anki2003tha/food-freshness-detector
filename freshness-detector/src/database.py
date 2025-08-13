import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='freshness_detector.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS freshness_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_filename TEXT NOT NULL,
                prediction TEXT NOT NULL,
                confidence REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_result(self, image_filename, prediction, confidence):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            INSERT INTO freshness_results (image_filename, prediction, confidence, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (image_filename, prediction, confidence, timestamp))
        self.connection.commit()

    def fetch_results(self):
        self.cursor.execute('SELECT * FROM freshness_results ORDER BY timestamp DESC')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
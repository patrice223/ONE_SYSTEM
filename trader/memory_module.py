import sqlite3
import json
from datetime import datetime

DB_PATH = "memory_logs.db"
JSON_PATH = "memory_logs.json"

class MemoryLogger:
    def __init__(self, mode="sqlite"):
        self.mode = mode
        if mode == "sqlite":
            self.conn = sqlite3.connect(DB_PATH)
            self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                action TEXT,
                agent_signal TEXT,
                outcome TEXT,
                reward_score REAL,
                learning_signal TEXT
            )
            """)

    def log(self, action, agent_signal, outcome, reward_score, 
learning_signal):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "agent_signal": agent_signal,
            "outcome": outcome,
            "reward_score": reward_score,
            "learning_signal": learning_signal
        }

        if self.mode == "sqlite":
            with self.conn:
                self.conn.execute("""
                INSERT INTO memory (timestamp, action, agent_signal, 
outcome, reward_score, learning_signal)
                VALUES (:timestamp, :action, :agent_signal, :outcome, 
:reward_score, :learning_signal)
                """, entry)
        else:
            try:
                with open(JSON_PATH, "r") as f:
                    data = json.load(f)
            except:
                data = []
            data.append(entry)
            with open(JSON_PATH, "w") as f:
                json.dump(data, f, indent=2)

    def close(self):
        if self.mode == "sqlite":
            self.conn.close()
from memory_module import MemoryLogger

memory = MemoryLogger(mode="sqlite")
memory.log(
    action="BUY BTC",
    agent_signal="signal_strong_buy",
    outcome="TP hit",
    reward_score=0.91,
    learning_signal="reinforced_positive"
)
memory.close()
print("✅ memory log saved.")



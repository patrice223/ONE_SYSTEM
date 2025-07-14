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


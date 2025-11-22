import datetime

def log_game(result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("game_history.txt", "a") as f:
        f.write(f"[{timestamp}] Game Result: {result}\n")

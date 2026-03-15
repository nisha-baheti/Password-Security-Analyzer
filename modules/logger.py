import datetime
import os

def log_analysis(password, score, strength):

    os.makedirs("logs", exist_ok=True)

    with open("logs/password_logs.txt", "a") as log:

        log.write(
            f"{datetime.datetime.now()} | "
            f"Password: {password} | "
            f"Score: {score} | "
            f"Strength: {strength}\n"
        )
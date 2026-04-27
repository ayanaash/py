import json
import os

SETTINGS_FILE = "settings.json"
SCORES_FILE = "leaderboard.json"


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"sound": True, "car_color": (0, 0, 255), "difficulty": "normal"}
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)


def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        return json.load(f)


def save_score(name, score, distance):
    scores = load_scores()
    scores.append({"name": name, "score": score, "distance": distance})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]

    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)
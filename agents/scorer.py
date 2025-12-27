def score_friction(friction_text):
    score = 0

    keywords = {
        "manual": 3,
        "reconciliation": 4,
        "approval": 2,
        "spreadsheet": 4,
        "email": 3,
        "delay": 2,
        "error": 3
    }

    for word, value in keywords.items():
        if word in friction_text.lower():
            score += value

    return min(score, 10)


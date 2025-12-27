def analyze_friction(llm, text):
    prompt = f"""
    Identify the highest-friction steps in the following finance process.
    Consider:
    - Manual effort
    - Delays
    - Error risk
    - Compliance risk

    Process:
    {text}

    Output bullet points.
    """

    return llm(prompt)[0]["generated_text"]


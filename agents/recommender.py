def generate_recommendations(llm, friction_text):
    prompt = f"""
    Based on the following finance process friction points,
    suggest automation or AI improvements.

    Friction:
    {friction_text}

    Provide practical recommendations.
    """

    return llm(prompt)[0]["generated_text"]


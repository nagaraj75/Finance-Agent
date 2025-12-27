def classify_workflow(llm, text):
    prompt = f"""
    Classify the following finance process into one category:
    Expense, Close, Audit, or Tax.

    Process description:
    {text}
    """

    response = llm(prompt)[0]["generated_text"]
    return response.strip()


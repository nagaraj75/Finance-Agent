from models.llm import load_llm
from agents.classifier import classify_workflow
from agents.friction_analyzer import analyze_friction
from agents.scorer import score_friction
from agents.recommender import generate_recommendations

def run_agent(user_input):
    llm = load_llm()

    workflow = classify_workflow(llm, user_input)
    friction = analyze_friction(llm, user_input)
    score = score_friction(friction)
    recommendations = generate_recommendations(llm, friction)

    return {
        "workflow": workflow,
        "friction_analysis": friction,
        "friction_score": score,
        "recommendations": recommendations
    }

if __name__ == "__main__":
    text = input("Describe your finance process:\n")
    output = run_agent(text)

    for k, v in output.items():
        print(f"\n{k.upper()}:\n{v}")


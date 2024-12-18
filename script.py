import json

questions = [
    {"question": "What is the boiling point of water?", "choices": ["100°C", "0°C", "50°C", "200°C"], "answer": "100°C"},
    {"question": "What is the chemical formula of glucose?", "choices": ["C6H12O6", "H2O", "CO2", "C12H22O11"], "answer": "C6H12O6"},
]

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4)
print("Questions saved to questions.json")

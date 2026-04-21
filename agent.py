def reflection_agent():
    print("=== Daily Reflection Agent ===")

    event = input("What happened today? ")

    if event.strip() == "":
        print("Invalid input. Please describe something.")
        return

    feeling = input("How did you feel? ")
    outcome = input("Was it positive or negative? ")

    if outcome.lower() == "positive":
        print("Great! Keep doing what worked.")
    elif outcome.lower() == "negative":
        reason = input("Why did it go wrong? ")
        print("Suggestion: Focus on improving:", reason)
    else:
        print("Invalid outcome. Please enter positive/negative.")

reflection_agent()

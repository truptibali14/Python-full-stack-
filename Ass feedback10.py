feedback = {
    "Positive": 45,
    "Neutral": 18,
    "Negative": 7
}
total_feedback = sum(feedback.values())
highest_type = max(feedback, key=feedback.get)
highest_value = feedback[highest_type]
print("Feedback Data:", feedback)
print("Total Feedback:", total_feedback)
print(f"Highest Feedback Type: {highest_type} ({highest_value})")

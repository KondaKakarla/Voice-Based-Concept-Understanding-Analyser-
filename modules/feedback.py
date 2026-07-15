def generate_feedback(score, speech):

    feedback = []

    if score >= 80:
        feedback.append("✅ Excellent Concept Understanding")

    elif score >= 60:
        feedback.append("🙂 Moderate Concept Understanding")

    else:
        feedback.append("❌ Poor Concept Understanding")

    if speech["fillers"] <= 2:
        feedback.append("✅ Very Few Filler Words")

    else:
        feedback.append("⚠ Try to Reduce Filler Words")

    if speech["wpm"] >= 100:
        feedback.append("✅ Good Speaking Speed")

    else:
        feedback.append("🗣 Speak Slightly Faster")

    return feedback

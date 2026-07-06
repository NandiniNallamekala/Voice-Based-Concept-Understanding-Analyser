def calculate_score(semantic_score, fluency_score):

    # Give more importance to semantic understanding
    final_score = (semantic_score * 0.7) + (fluency_score * 0.3)

    return round(final_score, 2)


def classify_performance(score):

    if score >= 85:
        return "Strong Understanding"

    elif score >= 60:
        return "Moderate Understanding"

    else:
        return "Poor Understanding"
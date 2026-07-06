from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Sentence-BERT model (loads only once)
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(reference_text, student_text):
    """
    Compute semantic similarity between
    reference concept and student's explanation.

    Parameters:
        reference_text (str): Correct concept explanation
        student_text (str): Student's spoken explanation

    Returns:
        float: Similarity score (0 - 100)
    """

    # Handle empty input
    if not reference_text.strip() or not student_text.strip():
        return 0.0

    # Generate embeddings
    reference_embedding = model.encode([reference_text])

    student_embedding = model.encode([student_text])

    # Cosine similarity
    similarity = cosine_similarity(
        reference_embedding,
        student_embedding
    )[0][0]

    # Convert to percentage
    score = similarity * 100

    # Normalize
    score = max(0, min(score, 100))

    return round(score, 2)


def understanding_level(score):
    """
    Convert score into qualitative feedback.
    """

    if score >= 85:
        return "Excellent Understanding"

    elif score >= 70:
        return "Good Understanding"

    elif score >= 50:
        return "Moderate Understanding"

    else:
        return "Poor Understanding"


# ----------------------------
# Test Code
# ----------------------------
if __name__ == "__main__":

    reference = """
    Machine Learning is a subset of Artificial Intelligence
    that enables computers to learn from data without being
    explicitly programmed.
    """

    student = """
    Machine learning allows computers to learn from data
    and make predictions automatically.
    """

    score = semantic_similarity(reference, student)

    print("Similarity Score:", score)
    print("Understanding:", understanding_level(score))
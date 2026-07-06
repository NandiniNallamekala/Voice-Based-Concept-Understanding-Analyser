from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load the SBERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(reference_text, user_text):

    reference_embedding = model.encode(reference_text, convert_to_tensor=True)

    user_embedding = model.encode(user_text, convert_to_tensor=True)

    score = util.cos_sim(reference_embedding, user_embedding)

    return float(score)
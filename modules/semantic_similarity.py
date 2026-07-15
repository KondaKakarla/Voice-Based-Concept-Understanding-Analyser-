from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


reference_answers = {

    "Machine Learning":
    "Machine Learning is a subset of Artificial Intelligence that enables computers to learn from data without being explicitly programmed.",

    "Cloud Computing":
    "Cloud Computing provides computing resources over the internet such as storage, servers and databases.",

    "Artificial Intelligence":
    "Artificial Intelligence is the simulation of human intelligence by machines.",

    "Data Science":
    "Data Science extracts meaningful insights from structured and unstructured data.",

    "Cyber Security":
    "Cyber Security protects systems, networks and data from cyber attacks."

}


def calculate_similarity(topic, user_answer):

    reference = reference_answers[topic]

    emb1 = model.encode(reference, convert_to_tensor=True)

    emb2 = model.encode(user_answer, convert_to_tensor=True)

    similarity = cos_sim(emb1, emb2)

    score = float(similarity[0][0]) * 100

    return round(score, 2)

from src.embeddings import generate_embeddings


def retrieve_documents(
    question,
    index,
    chunks,
    top_k=3
):
    """
    Search FAISS for document chunks
    relevant to the user's question.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if index.ntotal == 0:
        return []

    # Generate embedding for the question
    question_embedding = generate_embeddings(
        [question]
    )

    # Search FAISS database
    scores, indices = index.search(
        question_embedding,
        min(top_k, index.ntotal)
    )

    results = []

    # Collect matching document chunks
    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        results.append({
            "text": chunks[idx]["text"],
            "metadata": chunks[idx]["metadata"],
            "score": float(score)
        })

    return results

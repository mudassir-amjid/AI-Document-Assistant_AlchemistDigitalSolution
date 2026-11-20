
import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS index from document embeddings.
    """

    if len(embeddings) == 0:
        raise ValueError("No embeddings provided.")

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    # Get embedding dimensions
    dimension = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatIP(dimension)

    # Add embeddings to the index
    index.add(embeddings)

    return index


def save_vector_store(index, save_path="vector_db"):
    """
    Save FAISS index to disk.
    """

    import os

    os.makedirs(save_path, exist_ok=True)

    faiss.write_index(
        index,
        os.path.join(save_path, "document.index")
    )


def load_vector_store(load_path="vector_db"):
    """
    Load an existing FAISS index.
    """

    import os

    index_file = os.path.join(
        load_path,
        "document.index"
    )

    if not os.path.exists(index_file):
        raise FileNotFoundError(
            "Vector database not found."
        )

    return faiss.read_index(index_file)

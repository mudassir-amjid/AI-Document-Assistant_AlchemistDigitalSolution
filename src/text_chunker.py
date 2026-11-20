
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents, chunk_size=500, chunk_overlap=100):
    """
    Split extracted documents into smaller overlapping chunks.

    Args:
        documents: List of extracted document dictionaries.
        chunk_size: Maximum chunk size in characters.
        chunk_overlap: Number of overlapping characters.

    Returns:
        List of smaller text chunks with metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len
    )

    all_chunks = []

    for document in documents:

        chunks = text_splitter.split_text(
            document["text"]
        )

        for chunk in chunks:

            all_chunks.append({
                "text": chunk,
                "metadata": document["metadata"].copy()
            })

    return all_chunks

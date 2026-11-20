
from src.document_processor import process_document
from src.text_chunker import create_chunks
from src.embeddings import generate_embeddings
from src.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)


# Step 1: Extract document
documents = process_document("data/uploads/sample.txt")


# Step 2: Create chunks
chunks = create_chunks(
    documents,
    chunk_size=100,
    chunk_overlap=20
)


# Step 3: Generate embeddings
texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(texts)


# Step 4: Create FAISS database
index = create_vector_store(embeddings)

print("Total vectors stored:", index.ntotal)


# Step 5: Save database
save_vector_store(index)

print("Vector database saved successfully!")


# Step 6: Load database
loaded_index = load_vector_store()

print("Loaded vectors:", loaded_index.ntotal)

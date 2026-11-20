
from src.document_processor import process_document
from src.text_chunker import create_chunks
from src.embeddings import generate_embeddings


# Step 1: Extract document text
documents = process_document("data/uploads/sample.txt")


# Step 2: Create text chunks
chunks = create_chunks(
    documents,
    chunk_size=100,
    chunk_overlap=20
)


# Step 3: Extract text from chunks
texts = [chunk["text"] for chunk in chunks]


# Step 4: Generate embeddings
embeddings = generate_embeddings(texts)


# Step 5: Display results
print("Number of chunks:", len(texts))

print("Embeddings shape:", embeddings.shape)

print("First embedding dimensions:", len(embeddings[0]))

print("First 5 values:", embeddings[0][:5])

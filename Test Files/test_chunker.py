
from src.document_processor import process_document
from src.text_chunker import create_chunks


# Step 1: Extract document text
documents = process_document("data/uploads/sample.txt")


# Step 2: Create chunks
chunks = create_chunks(
    documents,
    chunk_size=100,
    chunk_overlap=20
)


# Step 3: Display results
print("\nTOTAL CHUNKS:", len(chunks))

for index, chunk in enumerate(chunks):

    print("\nCHUNK:", index + 1)

    print("TEXT:")
    print(chunk["text"])

    print("METADATA:")
    print(chunk["metadata"])

    print("-" * 50)

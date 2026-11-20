
from src.document_processor import process_document
from src.text_chunker import create_chunks
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents

# 1. Load the sample document
documents = process_document("data/uploads/sample.txt")

# 2. Create text chunks
chunks = create_chunks(
    documents,
    chunk_size=100,
    chunk_overlap=20
)

# 3. Generate embeddings
texts = [chunk["text"] for chunk in chunks]
embeddings = generate_embeddings(texts)

# 4. Create vector database
index = create_vector_store(embeddings)

# 5. Test questions
questions = [
    "How many annual leave days are employees entitled to?",
    "Who approves sick leave?",
    "Who should receive leave applications?",
    "What is the company's maternity leave policy?"
]

# 6. Retrieve relevant document sections
for question in questions:
    print("\n" + "=" * 60)
    print("QUESTION:", question)

    results = retrieve_documents(
        question,
        index,
        chunks,
        top_k=2
    )

    for result in results:
        print("\nRetrieved Text:")
        print(result["text"])
        print("Similarity Score:", round(result["score"], 4))
        print("Source:", result["metadata"]["source"])

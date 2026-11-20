
from src.document_processor import process_document
from src.text_chunker import create_chunks
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.answer_generator import generate_answer


# Step 1: Process document
documents = process_document(
    "data/uploads/sample.txt"
)


# Step 2: Create chunks
chunks = create_chunks(
    documents,
    chunk_size=100,
    chunk_overlap=20
)


# Step 3: Generate embeddings
texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(texts)


# Step 4: Create vector database
index = create_vector_store(embeddings)


# Step 5: Ask a question
question = "What is the company's maternity leave policy?"


# Step 6: Retrieve relevant documents
results = retrieve_documents(
    question,
    index,
    chunks,
    top_k=3
)


# Step 7: Generate answer
answer = generate_answer(
    question,
    results
)


# Step 8: Display answer
print("\nQUESTION:")
print(question)

print("\nAI ANSWER:")
print(answer)


import os
from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


# Check API key
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )


# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def generate_answer(question, retrieved_documents):

    MIN_RELEVANCE_SCORE = 0.55

    if not retrieved_documents:
        return (
            "I could not find this information "
            "in the provided documents"
        )

    best_score = max(
        doc.get("score", 0)
        for doc in retrieved_documents
    )

    if best_score < MIN_RELEVANCE_SCORE:
        return (
            "I could not find this information "
            "in the provided documents"
        )
    # Prepare document context
    context = ""

    for doc in retrieved_documents:

        source = doc["metadata"]["source"]
        page = doc["metadata"]["page"]

        context += f"""
Source: {source}
Page: {page}
Content: {doc['text']}
"""

    # Create prompt
    prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY
the information provided in the documents below.

Rules:
1. Do not use outside knowledge.
2. Do not invent information.
3. If the answer is not present in the documents,
   respond exactly:
   I could not find this information in the provided documents
4. Keep the answer clear and concise.
5. Include the source filename and page number
   when available.

DOCUMENTS:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    # Generate response using Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

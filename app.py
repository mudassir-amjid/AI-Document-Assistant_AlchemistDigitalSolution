
import streamlit as st
from pathlib import Path

from src.document_processor import process_document
from src.text_chunker import create_chunks
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.answer_generator import generate_answer


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
    layout="wide"
)


# -------------------------------
# SESSION STATE
# -------------------------------

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------------
# APPLICATION TITLE
# -------------------------------

st.title("📚 AI Knowledge-Base Document Assistant")

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 16px;">
        Developed by <b>Mudassir Amjid</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Upload your company documents and ask questions "
    "to get answers based on their content."
)


# -------------------------------
# SIDEBAR - DOCUMENT UPLOAD
# -------------------------------

with st.sidebar:

    st.header("📁 Document Upload")

    uploaded_files = st.file_uploader(
        "Upload PDF or TXT documents",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

    process_button = st.button(
        "Process Documents",
        type="primary",
        disabled=not uploaded_files
    )


# -------------------------------
# DOCUMENT PROCESSING
# -------------------------------

if process_button:

    all_documents = []

    upload_folder = Path("data/uploads")
    upload_folder.mkdir(parents=True, exist_ok=True)

    try:

        with st.spinner("Processing documents..."):

            for uploaded_file in uploaded_files:

                file_path = upload_folder / Path(
                    uploaded_file.name
                ).name

                file_path.write_bytes(
                    uploaded_file.getvalue()
                )

                documents = process_document(
                    str(file_path)
                )

                all_documents.extend(documents)

            if not all_documents:

                st.error(
                    "No readable text found in the documents."
                )

            else:

                chunks = create_chunks(all_documents)

                texts = [
                    chunk["text"] for chunk in chunks
                ]

                embeddings = generate_embeddings(texts)

                index = create_vector_store(embeddings)

                st.session_state.index = index
                st.session_state.chunks = chunks

                st.session_state.processed_files = [
                    file.name for file in uploaded_files
                ]

                st.session_state.messages = []

                st.success(
                    "Documents processed successfully!"
                )

                st.write(
                    f"Documents processed: {len(uploaded_files)}"
                )

                st.write(
                    f"Text sections extracted: {len(all_documents)}"
                )

                st.write(
                    f"Text chunks created: {len(chunks)}"
                )

                st.write(
                    f"Embeddings generated: {len(embeddings)}"
                )

    except Exception as e:

        st.error(f"Document processing error: {e}")


# -------------------------------
# DOCUMENT STATUS
# -------------------------------

st.subheader("📄 Document Status")

if st.session_state.processed_files:

    st.success("Your knowledge base is ready!")

    for filename in st.session_state.processed_files:

        st.write(f"✅ {filename}")

    st.write(
        f"Total searchable chunks: "
        f"{len(st.session_state.chunks)}"
    )

else:

    st.info(
        "Please upload and process documents first."
    )


# -------------------------------
# CHAT INTERFACE
# -------------------------------

st.subheader("💬 Ask Your Documents")


# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            with st.expander("View Sources"):

                for source in message["sources"]:

                    st.write(source)


# Chat input
question = st.chat_input(
    "Ask a question about your documents...",
    disabled=st.session_state.index is None
)


# -------------------------------
# QUESTION ANSWERING
# -------------------------------

if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI answer
    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "Searching documents and generating answer..."
            ):

                # Retrieve relevant document sections
                results = retrieve_documents(
                    question,
                    st.session_state.index,
                    st.session_state.chunks,
                    top_k=3
                )

                # Generate answer using Gemini
                answer = generate_answer(
                    question,
                    results
                )

            st.markdown(answer)

            # Prepare source information
            fallback = (
                "I could not find this information "
                "in the provided documents"
            )

            sources = []

            if answer.strip() != fallback:

                for result in results:

                    if result["score"] >= 0.55:

                        metadata = result["metadata"]

                        source = metadata["source"]
                        page = metadata.get("page")

                        if page is not None:
                            source_text = (
                                f"{source} — Page {page}"
                            )
                        else:
                            source_text = source

                        if source_text not in sources:
                            sources.append(source_text)

            # Display sources
            if sources:

                with st.expander("View Sources"):

                    for source in sources:
                        st.write(f"📄 {source}")

            # Save conversation
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })

        except Exception as e:

            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:

                st.warning(
                    "⚠️ The AI service has reached its usage limit. "
                    "Please try again later."
                )

            elif "503" in error_message or "UNAVAILABLE" in error_message:

                st.warning(
                    "⚠️ The AI service is temporarily unavailable. "
                    "Please try again in a few minutes."
                )

            else:

                st.error(
                    f"An unexpected error occurred: {e}"
                )

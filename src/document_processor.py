
import pymupdf
from pathlib import Path


def process_document(file_path):
    """
    Extract text from PDF or TXT documents.

    Args:
        file_path: Path of the uploaded document.

    Returns:
        A list of dictionaries containing text and metadata.
    """

    file_path = Path(file_path)

    documents = []

    # Check whether the file exists
    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    # Extract text from PDF
    if file_path.suffix.lower() == ".pdf":

        pdf_document = pymupdf.open(file_path)

        for page_number, page in enumerate(pdf_document):

            text = page.get_text("text").strip()

            if text:
                documents.append({
                    "text": text,
                    "metadata": {
                        "source": file_path.name,
                        "page": page_number + 1
                    }
                })

        pdf_document.close()

    # Extract text from TXT
    elif file_path.suffix.lower() == ".txt":

        text = file_path.read_text(
            encoding="utf-8-sig"
        ).strip()

        if text:
            documents.append({
                "text": text,
                "metadata": {
                    "source": file_path.name,
                    "page": None
                }
            })

    else:
        raise ValueError(
            "Only PDF and TXT files are supported."
        )

    return documents


from src.document_processor import process_document

result = process_document("data/uploads/sample.txt")

for item in result:
    print("Document:", item["metadata"]["source"])
    print("Page:", item["metadata"]["page"])
    print("Extracted Text:")
    print(item["text"])
    print("-" * 40)

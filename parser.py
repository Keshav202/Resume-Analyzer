from pdfminer.high_level import extract_text
import docx


def extract_text_from_resume(file_path):

    text = ""

    if file_path.endswith(".pdf"):
        text = extract_text(file_path)

    elif file_path.endswith(".docx"):

        doc = docx.Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text
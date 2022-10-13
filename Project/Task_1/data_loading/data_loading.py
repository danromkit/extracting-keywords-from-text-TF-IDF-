import fitz


def data_loading(file_name: str) -> str:
    text = ""
    with fitz.open(file_name) as doc:
        for page in doc:
            text += page.get_text()

    return text

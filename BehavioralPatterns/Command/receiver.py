# Receiver
class TextEditor:
    def __init__(self):
        self._text = ""

    def type_text(self, text: str):
        self._text += text
        print(f"Typed: {text}")

    def delete_text(self, count: int):
        deleted = self._text[-count:]
        self._text = self._text[:-count]
        print(f"Deleted: {deleted}")

    def get_text(self):
        return self._text

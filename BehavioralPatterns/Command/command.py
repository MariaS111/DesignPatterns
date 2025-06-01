from abc import ABC, abstractmethod
from receiver import TextEditor


# Command
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self):
        pass


# ConcreteCommand
class TypeTextCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.type_text(self.text)

    def undo(self):
        self.editor.delete_text(len(self.text))


class DeleteTextCommand(Command):
    def __init__(self, editor: TextEditor, count: int):
        self.editor = editor
        self.count = count
        self._deleted_text = ""

    def execute(self):
        self._deleted_text = self.editor.get_text()[-self.count:]
        self.editor.delete_text(self.count)

    def undo(self):
        self.editor.type_text(self._deleted_text)

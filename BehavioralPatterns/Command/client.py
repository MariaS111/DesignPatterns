from receiver import TextEditor
from invoker import EditorInvoker
from command import TypeTextCommand, DeleteTextCommand

if __name__ == "__main__":
    editor = TextEditor()
    invoker = EditorInvoker()

    invoker.execute_command(TypeTextCommand(editor, "Hello "))
    invoker.execute_command(TypeTextCommand(editor, "World"))
    print("Current text:", editor.get_text())
    invoker.undo_last()
    print("After undo type:", editor.get_text())
    invoker.execute_command(DeleteTextCommand(editor, 3))
    print("After delete:", editor.get_text())
    invoker.undo_last()
    print("After undo delete:", editor.get_text())


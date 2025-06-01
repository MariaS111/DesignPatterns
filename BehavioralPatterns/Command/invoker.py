from command import Command


# Invoker
class EditorInvoker:
    def __init__(self):
        self._history: list[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last(self):
        if self._history:
            last = self._history.pop()
            print("Undoing last command")
            last.undo()
        else:
            print("Nothing to undo")

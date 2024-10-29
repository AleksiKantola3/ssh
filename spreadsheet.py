
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
        value = self.get(cell)
        if value.startswith("="):
            if value[1:].isdigit():
                return value[1:]
            elif value[1:].startswith("'") and value[1:].endswith("'"):
                return value[2:-1]
            elif value[1:] in self._cells:
                return self.evaluate(value[1:])
            else:
                return "#ERROR"
        elif value.isdigit():
            return int(value)
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        else:
            return "#ERROR"


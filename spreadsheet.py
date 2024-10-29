
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
        if cell in self._evaluating:
            return "#CIRCULAR"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.startswith("="):
            if value[1:].isdigit():
                result = int(value[1:])
            elif value[1:].startswith("'") and value[1:].endswith("'"):
                result = value[2:-1]
            elif value[1:] in self._cells:
                result = self.evaluate(value[1:])
            elif '*' in value[1:]:
                parts = value[1:].split('*')
                if all(part.strip().isdigit() for part in parts):
                    result = 1
                    for part in parts:
                        result *= int(part.strip())
                else:
                    result = "#ERROR"
            elif '+' in value[1:]:
                parts = value[1:].split('+')
                if all(part.strip().isdigit() for part in parts):
                    result = sum(int(part.strip()) for part in parts)
                else:
                    result = "#ERROR"
            elif '/' in value[1:]:
                parts = value[1:].split('/')
                if all(part.strip().isdigit() for part in parts) and int(parts[1].strip()) != 0:
                    result = int(parts[0].strip()) // int(parts[1].strip())
                else:
                    result = "#ERROR"

            else:
                result = "#ERROR"
        elif value.isdigit():
            result = int(value)
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        else:
            result = "#ERROR"
        
        self._evaluating.remove(cell)
        return result


from figure import Figure
import settings


class Stack(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def replace(self, figure: int, row: int, col: int) -> None:
        self.stack[row][col] = figure

    def clean_line(self):
        pass

    def search_lines(self):
        for row in range(settings.ROWS):
            if self.is_row_full(row):
                return row

    def is_row_full(self, row: int) -> bool:
        for col in range(settings.COLS):
            if self.stack[row][col] == 0:
                return False
        return True

    def add(self, figure: Figure):
        self.stack.append(figure)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def draw(self, win):
        for figure in self.stack:
            figure.draw(win)


if __name__ == '__main__':
    stack = Stack()
    print(stack)

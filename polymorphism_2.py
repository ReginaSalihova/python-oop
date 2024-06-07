class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []
        self.current_line_length = 0

    def add_word(self, word):
        if self.current_line_length + len(word) > self.width:
            print(' '.join(self.paragraph))
            self.paragraph = []
            self.current_line_length = 0
        self.paragraph.append(word)
        self.current_line_length += len(word) + 1

    def end(self):
        if self.paragraph:
            print(' '.join(self.paragraph))


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []
        self.current_line_length = 0

    def add_word(self, word):
        if self.current_line_length + len(word) > self.width:
            print(' '.join(self.paragraph).rjust(self.width))
            self.paragraph = []
            self.current_line_length = 0
        self.paragraph.append(word)
        self.current_line_length += len(word) + 1

    def end(self):
        if self.paragraph:
            print(' '.join(self.paragraph).rjust(self.width))


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
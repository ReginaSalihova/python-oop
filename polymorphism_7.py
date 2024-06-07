class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]
        return None

    def set_value(self, row, col, value):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])

    def delete_row(self, row):
        if 0 <= row < len(self.table):
            del self.table[row]

    def delete_col(self, col):
        if 0 <= col < len(self.table[0]):
            for row in self.table:
                del row[col]

    def add_row(self, row):
        if 0 <= row <= len(self.table):
            self.table.insert(row, [0] * self.n_cols())

    def add_col(self, col):
        if 0 <= col <= len(self.table[0]):
            for row in self.table:
                row.insert(col, 0)


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

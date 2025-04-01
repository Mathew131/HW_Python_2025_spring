class Tensor:
    def __init__(self, dim, data):
        self.dimension = dim
        self.data = data

    def __str__(self):
        return str(self.data)
    
class Matrix(Tensor):
    def __init__(self, *args):
        *dim, data = args 
    
        if len(dim) == 2:
            self.rows, self.cols = dim
        else:
            raise ValueError
        super().__init__(dim, data)

    def Print(self, data, rows, cols):
        if isinstance(data, int):
            return data
    
        maxlen = max(map(len, map(str, data)))
        
        s = "[\n"
        for i in range(rows):
            for j in range(cols):
                s += f"{data[self.conv_rc2i(i, j, cols)]:{maxlen+1}}"
            s += '\n'
        s += "]"
        return s

    def __str__(self):
        return self.Print(self.data, self.rows, self.cols)

    def conv_i2rc(self, x, cols = -1):
        if cols == -1:
            cols = self.cols
        return x // cols, x % cols

    def conv_rc2i(self, i, j, cols = -1):
        if cols == -1:
            cols = self.cols
        return i * cols + j
    
    def __getitem__(self, ind):
        # print(ind, type(ind))
        data = self.data.copy()
        rows = self.rows
        cols = self.cols

        if isinstance(ind, int):
            data = [data[self.conv_rc2i(ind, i)] for i in range(self.cols)]
            rows = 1
            cols = self.cols
        if isinstance(ind, slice):
            data = [data[self.conv_rc2i(i, j)] for i in range(*ind.indices(self.rows)) for j in range(self.cols)]
            rows = len(range(*ind.indices(self.rows)))
            cols = self.cols
        if isinstance(ind, list):
            data = [data[self.conv_rc2i(i, j)] for i in ind for j in range(self.cols)]
            rows = len(ind)
            cols = self.cols
        elif isinstance(ind, tuple):
            if isinstance(ind[0], int) and isinstance(ind[1], int):
                data = data[self.conv_rc2i(ind[0], ind[1])]
                rows = 1
                cols = 1
            elif isinstance(ind[0], int) and isinstance(ind[1], slice):
                data = [data[self.conv_rc2i(ind[0], i)] for i in range(self.cols)][ind[1]]
                rows = 1
                cols = len(data)
            elif isinstance(ind[0], slice) and isinstance(ind[1], int):
                data = [data[self.conv_rc2i(i, ind[1])] for i in range(self.rows)][ind[0]]
                rows = len(data)
                cols = 1
            elif isinstance(ind[0], slice) and isinstance(ind[1], slice):
                data = [
                    self.data[self.conv_rc2i(i, j)]
                    for i in range(self.rows) if i in range(*ind[0].indices(self.rows))
                    for j in range(self.cols) if j in range(*ind[1].indices(self.cols))
                ]
                rows = len(range(*ind[0].indices(self.rows)))
                cols = len(range(*ind[1].indices(self.rows)))

            elif isinstance(ind[0], int) and isinstance(ind[1], list):
                data = [data[self.conv_rc2i(ind[0], i)] for i in ind[1]]
                rows = 1
                cols = len(ind[1])
            elif isinstance(ind[0], list) and isinstance(ind[1], int):
                data = [data[self.conv_rc2i(i, ind[1])] for i in ind[0]]
                rows = len(ind[0])
                cols = 1
            elif isinstance(ind[0], list) and isinstance(ind[1], list):
                data = [data[self.conv_rc2i(i, j)] for i in ind[0] for j in ind[1]]
                rows = len(ind[0])
                cols = len(ind[1])
            elif isinstance(ind[0], list) and isinstance(ind[1], slice):
                data = [data[self.conv_rc2i(i, j)] for i in ind[0] for j in range(*ind[1].indices(self.cols))]
                rows = len(ind[0])
                cols = len(range(*ind[1].indices(self.cols)))
            elif isinstance(ind[0], slice) and isinstance(ind[1], list):
                data = [data[self.conv_rc2i(i, j)] for i in range(*ind[0].indices(self.cols)) for j in ind[1]]
                rows = len(range(*ind[0].indices(self.cols)))
                cols = len(ind[1])

        return self.Print(data, rows, cols)



if __name__ == '__main__':
    data = [i for i in range(100)]
    M = Matrix(10, 10, data)

    print("M\n", M)
    print()
    print("M[1, 1]\n", M[1, 1])
    print()
    print("M[1]\n", M[1])
    print()
    print("M[-1]\n", M[-1])
    print()
    print("M[1:4]\n", M[1:4])
    print()
    print("M[:4]\n", M[:4])
    print()
    print("M[4:]\n", M[4:])
    print()
    print("M[:]\n", M[:])
    print()
    print("M[1:7:2]\n", M[1:7:2])
    print()
    print("M[:, 1]\n", M[:, 1])
    print()
    print("M[1:4, 1:4]\n", M[1:4, 1:4])
    print()
    print("M[1:4, :4]\n", M[1:4, :4])
    print()
    print("M[1:4, 4:]\n", M[1:4, 4:])
    print()
    print("M[1:4, :]\n", M[1:4, :])
    print()
    print("M[-1:]\n", M[-1:])
    print()
    print("M[-2::-2]\n", M[-2::-2])
    print()
    print("M[-2::-2, 1:4]\n", M[-2::-2, 1:4])
    print()
    print("M[:, :]\n", M[:, :])
    print()
    print("M[1, 4]\n", M[[1, 4]])
    print()
    print("M[:, [1:4]]\n", M[:, [1, 4]])
    print()
    print("M[[1, 4], [1, 4]]\n", M[[1, 4], [1, 4]])
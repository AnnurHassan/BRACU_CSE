class Pascal_Triangle:
    def __init__(self, t):
        self.triangle = []
        for i in range(t):
            row = [1]
            if i > 0:
                prev_row = self.triangle[i - 1]

                for j in range(len(prev_row) - 1):
                    row.append(prev_row[j] + prev_row[j + 1])

                row.append(1)  

            self.triangle.append(row)
    
    def display(self):
        for i in self.triangle:
            for j in i:
                print(j, end = " ")
            print()


t = int(input("Number of rows: "))
pascals_triangle = Pascal_Triangle(t)
pascals_triangle.display()
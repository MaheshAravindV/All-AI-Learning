import random
class Matrix:
    def __init__(self,r,c):
        self.rows = r
        self.cols = c
        self.data = []
        for i in range(r):
            self.data.append([])
            for j in range(c):
                self.data[i].append(0)

    def random(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.random()*2-1


    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j],end = ' ')
            print()
        print()


    def addScalar(self,n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += n


    @staticmethod
    def add(m1,m2):
        res = Matrix(m1.rows,m1.cols)
        for i in range(m1.rows):
            for j in range(m1.cols):
                res.data[i][j] = m1.data[i][j] + m2.data[i][j]
        return res
    
    def mulScalar(self,n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n
    
    @staticmethod
    def multiply(m1,m2):
        res = Matrix(m1.rows,m2.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                for k in range(m1.cols):
                    res.data[i][j] += m1.data[i][k]*m2.data[k][j]
        return res
    
    def multiplyElementWise(self,m1):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= m1.data[i][j]
    
    def set(self,a):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = a[i][j]
    
    def setArray(self,a):
        for i in range(self.rows):
            self.data[i][0] = a[i]
        return self
    
    def transpose(self):
        res = Matrix(self.cols,self.rows)
        for i in range(res.rows):
            for j in range(res.cols):
                res.data[i][j] = self.data[j][i]
        return res
    
    @staticmethod
    def map(mat,fn):
        res = Matrix(mat.rows,mat.cols)
        for i in range(mat.rows):
            for j in range(mat.cols):
                res.data[i][j] = fn(mat.data[i][j])
        return res
   
    @staticmethod
    def copy(source):
        res = Matrix(source.rows,source.cols)
        for i in range(source.rows):
            for j in range(source.cols):
                res.data[i][j] = source.data[i][j]
        return res
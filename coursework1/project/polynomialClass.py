import sympy as sym
import numpy as np
import pyqtgraph as pg
class Polynomial:
    def GetIter(self):
        return self.itter
    def __init__(self,arrX=[],arrY=[]):
        self.arr_x=arrX
        self.arr_y=arrY
        self.size=len(self.arr_x)
    def lagrange(self):#Знаходження поліному методом Лагранжа
        point=sym.Symbol('x')#Використовуємо бібліотеку sympy для позначення point як символ
        polyL = 0
        self.itter=0
        for i in range(self.size):
           p = 1
           self.itter+=1
           for j in range(self.size):
               self.itter+=1
               if i != j:
                   p = p * (point - self.arr_x[j]) / (self.arr_x[i] - self.arr_x[j]) #Формула базисного поліному
           polyL = polyL + p * self.arr_y[i]
        self.polynomial=sym.expand(polyL) #Поєднання частин формули
        return self.polynomial
    def aitken(self): #Знаходження поліному схемою Ейткена
        point=sym.Symbol('x')
        self.itter=0
        p = [[0]*self.size for i in range(self.size)]
        for i in range(self.size):
            p[0][i]=self.arr_y[i]
            self.itter+=1
        for k in range(0,self.size-1):
            self.itter+=1
            for i in range(k+1,self.size):
                self.itter+=1
                p[k+1][i] = ((point-self.arr_x[k])*p[k][i]-(point-self.arr_x[i])*p[k][k])/(self.arr_x[i]-self.arr_x[k])
        self.outAitken(p)
        self.polynomial=sym.expand(p[self.size-1][self.size-1])
        return self.polynomial
    def grafic(self):#Метод знаходження меж графіка і функції для його побудови
        px=sym.lambdify(sym.Symbol('x'),self.polynomial)#Перетворення функції в лямбда-функцію для швидкого обчислення числових значень
        a=min(self.arr_x)
        b=max(self.arr_x)
        p_xi=np.linspace(a,b,50)#Масив значень х в потрібних межах
        pfi=px(p_xi)#Масив значень функції в точках х
        return p_xi,pfi
    def outAitken(self,matrix):#Додаткова функція(не метод класу) для виведення схеми Ейткена у вигляді таблиці
        print()
        for row in range(self.size):
            for elem in range(self.size):
                 if row==0:
                   print(round(matrix[row][elem],3),end='\t')
                 else:
                   print(sym.expand(matrix[row][elem]),end='\t')
            print()
        print()
    


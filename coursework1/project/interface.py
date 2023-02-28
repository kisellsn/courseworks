from polynomialClass import *
from window import *
from pyqtgraph import PlotWidget, plot
class Interface(Ui_MainWindow,QtWidgets.QMainWindow):#Робота з інтерфейсом
    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi (self)
        self.p1= self.buildGraph() 
        self.toCalculate.clicked.connect(self.Result)
        self.Save.clicked.connect(self.SaveIn)
        self.outFile.clicked.connect(self.Load)
        
    def Init_Polynomial(self):#Приймання програмою введених значень координат
        strX=self.inputX.text().split()
        strY=self.inputY.text().split()
        if self.Check(strX,strY):#Метод для перевірки значень
            self.arrX = list(map(float,strX))
            self.arrY = list(map(float,strY))
            return Polynomial(self.arrX,self.arrY)
        return 0
    def Message(self):#Ф-ція визначення помилки
        Message=QMessageBox()
        Message.setWindowTitle("Oops!")
        Message.setText("Некоректно введені дані.")
        Message.setIcon(QMessageBox.Warning)
        Message.setStandardButtons(QMessageBox.Ok)
        return Message

    def Check(self,arr1,arr2):#Метод для перевірки значень
        error=self.Message()
        for i in range(len(arr1)):
            if arr1[i].lstrip('-').replace('.','',1).isdigit()==False :
                 error.exec_()
                 return False
        for i in range(len(arr2)):
            if arr2[i].lstrip('-').replace('.','',1).isdigit()==False :
                 error.exec_()
                 return False
        if len(arr1)!=len(arr2) or len(arr1)<2:
            error.setText("Кількість значень Х та У не співпадають або менше 2х.")
            error.exec_()
            return False
        elif len(arr1)>10:
            error.setText("Кількість значень більше 10ти.")
            error.exec_()
            return False
        for i in range(len(arr1)-1):
            for j in range(i+1,len(arr1)):
                if arr1[i]==arr1[j]:
                    error.setText("Значення Х не можуть повторюватись.")
                    error.exec_()
                    return False
        if all(i==arr2[0] for i in arr2):
            error.setText("Значення Y не можуть бути всі однакові.")
            error.exec_()
            return False
        return True

    def Result(self):#Ф-ція для виводу результату, що викликається при нажиманні кнопки РОЗРАХУВАТИ
        if self.Init_Polynomial()!=0:
            self.textEdit.clear()
            func=self.Init_Polynomial()
            if self.radioLagrange.isChecked():#Перевірка на вибір методу
                polynom=func.lagrange()
            elif self.radioAitken.isChecked():
                polynom=func.aitken()
            else:
                error=self.Message()
                error.setText("Оберіть метод обчислення.")
                error.exec_()
                return
            self.textEdit.insertPlainText(str(polynom))#Вивід результату
            p_xi,pfi=func.grafic() #Виклик ф-ції з класу polynomialClass
            self.plotGraph(p_xi,pfi)
            itter=func.GetIter()
            statistic=self.Message()
            statistic.setWindowTitle("Statistic")
            statistic.setText("Під час рішення задачі інтерполяції обраним методом ми маємо "+str(itter)+ " ітерацій.")
            statistic.setIcon(QMessageBox.Information)
            statistic.exec_()

    def buildGraph(self): #Створення і підготовка полотна для графіка
        pg.setConfigOptions (antialias = True)         #створення змінної pyqtgraph, antialias =згладжування кривої
        win = pg.GraphicsLayoutWidget ()               # макет pg для реалізації автоматичного управління макетом інтерфейса даних 
        self.graf.addWidget(win)
        p1 = win.addPlot ()                            # Додаємо вікно графіка
        p1.setLabel ('left', text = 'Y') 
        p1.showGrid (x = True, y = True)
        p1.setLogMode (x = False, y = False) 
        p1.setLabel ('bottom', text = 'X') 
        return p1

    def plotGraph(self,p_xi,pfi):#Малювання графіка з заданими значеннями
        pen = pg.mkPen(color=(206, 199, 240),width=5)
        self.p1.plot(self.arrX,self.arrY,symbolBrush=(237, 177, 32),symbol='star',symbolPen=(86, 80, 115), symbolSize=25 ,clear=True)
        self.p1.plot(p_xi,pfi,pen=pen)

    def SaveIn(self):
        with open("polynom.txt", 'w') as file:
            file.write("x:\n"+self.inputX.text())           
            file.write("\ny:\n"+self.inputY.text())
            file.write("\npolynomial is "+self.textEdit.toPlainText())
    def Load(self):
        with open("polynom.txt", 'r') as file:
            text=file.readlines()
        self.inputX.setText(text[1])
        self.inputY.setText(text[3])


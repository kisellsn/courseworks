from interface import *

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myWin = Interface()
    myWin.show()
    sys.exit(app.exec_())

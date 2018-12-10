import sys
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        self.pushButton_0.clicked.connect(self.run)
        self.pushButton_1.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.run)
        self.pushButton_5.clicked.connect(self.run)
        self.pushButton_6.clicked.connect(self.run)
        self.pushButton_7.clicked.connect(self.run)
        self.pushButton_8.clicked.connect(self.run)
        self.pushButton_9.clicked.connect(self.run)
        self.pushButton_plus.clicked.connect(self.calc)
        self.pushButton_minus.clicked.connect(self.calc)
        self.pushButton_pros.clicked.connect(self.calc)
        self.pushButton_del.clicked.connect(self.calc)
        self.pushButton_dot.clicked.connect(self.run)
        self.pushButton_sqrt.clicked.connect(self.sqrt)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_fact.clicked.connect(self.fact)
        self.pushButton_st.clicked.connect(self.calc)
        self.pushButton_result.clicked.connect(self.result)


        self.data = ''
        self.data_eval = ''


    def real_fact(self,n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            print(self.data_eval)
            self.result()

    ## Сброс всех данных, очистка экрана
    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.lcdNumber.display('')

    def run(self):
        if self.sender().text()=='.':
            if '.' in self.data:
                return
        if self.data!='0' or (self.data=='0' and self.sender().text()=='.'):
            self.data = self.data+self.sender().text()
            self.data_eval = self.data_eval+self.sender().text()
            self.log.setText(self.data_eval)
            self.lcdNumber.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.lcdNumber.display(self.data)

    def sqrt(self):
        if self.data_eval:
            self.data_eval +='**0.5'
            self.result()

    def result(self):
        try:
            float(self.data_eval)
        except:
            try:

                self.data = eval(self.data_eval)
                self.data_eval = str(self.data)
                self.lcdNumber.display(self.data)
            except ZeroDivisionError:
                self.lcdNumber.display('Error')
            except:
                pass
        self.data = ''

    def calc(self):
        if self.data_eval:
            self.result()
            if (self.data_eval[-1] not in ['+','-','/','*']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval)-1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^','**')

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
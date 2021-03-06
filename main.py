import sys
import socket
from PySide.QtUiTools import*
from PySide.QtCore import *
from PySide.QtGui import *
from pyswip import Prolog


class My_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.count=0
        self.setWindowTitle("Sudoku")
        self.count=0
        self.count1=0
        loader = QUiLoader()
        self.setMinimumSize(500,480)
        form = loader.load("./untitled.ui",self)
        self.setCentralWidget(form)
        
        
        
        self.a1 = form.findChild(QLineEdit, "a1")
        self.a2 = form.findChild(QLineEdit, "a2")
        self.a3 = form.findChild(QLineEdit, "a3")
        self.a4 = form.findChild(QLineEdit, "a4")
        self.a5 = form.findChild(QLineEdit, "a5")
        self.a6 = form.findChild(QLineEdit, "a6")
        self.a7 = form.findChild(QLineEdit, "a7")
        self.a8 = form.findChild(QLineEdit, "a8")
        self.a9 = form.findChild(QLineEdit, "a9")
        self.b1 = form.findChild(QLineEdit, "b1")
        self.b2 = form.findChild(QLineEdit, "b2")
        self.b3 = form.findChild(QLineEdit, "b3")
        self.b4 = form.findChild(QLineEdit, "b4")
        self.b5 = form.findChild(QLineEdit, "b5")
        self.b6 = form.findChild(QLineEdit, "b6")
        self.b7 = form.findChild(QLineEdit, "b7")
        self.b8 = form.findChild(QLineEdit, "b8")
        self.b9 = form.findChild(QLineEdit, "b9")
        self.c1 = form.findChild(QLineEdit, "c1")
        self.c2 = form.findChild(QLineEdit, "c2")
        self.c3 = form.findChild(QLineEdit, "c3")
        self.c4 = form.findChild(QLineEdit, "c4")
        self.c5 = form.findChild(QLineEdit, "c5")
        self.c6 = form.findChild(QLineEdit, "c6")
        self.c7 = form.findChild(QLineEdit, "c7")
        self.c8 = form.findChild(QLineEdit, "c8")
        self.c9 = form.findChild(QLineEdit, "c9")
        self.d1 = form.findChild(QLineEdit, "d1")
        self.d2 = form.findChild(QLineEdit, "d2")
        self.d3 = form.findChild(QLineEdit, "d3")
        self.d4 = form.findChild(QLineEdit, "d4")
        self.d5 = form.findChild(QLineEdit, "d5")
        self.d6 = form.findChild(QLineEdit, "d6")
        self.d7 = form.findChild(QLineEdit, "d7")
        self.d8 = form.findChild(QLineEdit, "d8")
        self.d9 = form.findChild(QLineEdit, "d9")
        self.e1 = form.findChild(QLineEdit, "e1")
        self.e2 = form.findChild(QLineEdit, "e2")
        self.e3 = form.findChild(QLineEdit, "e3")
        self.e4 = form.findChild(QLineEdit, "e4")
        self.e5 = form.findChild(QLineEdit, "e5")
        self.e6 = form.findChild(QLineEdit, "e6")
        self.e7 = form.findChild(QLineEdit, "e7")
        self.e8 = form.findChild(QLineEdit, "e8")
        self.e9 = form.findChild(QLineEdit, "e9")
        self.f1 = form.findChild(QLineEdit, "f1")
        self.f2 = form.findChild(QLineEdit, "f2")
        self.f3 = form.findChild(QLineEdit, "f3")
        self.f4 = form.findChild(QLineEdit, "f4")
        self.f5 = form.findChild(QLineEdit, "f5")
        self.f6 = form.findChild(QLineEdit, "f6")
        self.f7 = form.findChild(QLineEdit, "f7")
        self.f8 = form.findChild(QLineEdit, "f8")
        self.f9 = form.findChild(QLineEdit, "f9")
        self.g1 = form.findChild(QLineEdit, "g1")
        self.g2 = form.findChild(QLineEdit, "g2")
        self.g3 = form.findChild(QLineEdit, "g3")
        self.g4 = form.findChild(QLineEdit, "g4")
        self.g5 = form.findChild(QLineEdit, "g5")
        self.g6 = form.findChild(QLineEdit, "g6")
        self.g7 = form.findChild(QLineEdit, "g7")
        self.g8 = form.findChild(QLineEdit, "g8")
        self.g9 = form.findChild(QLineEdit, "g9")
        self.h1 = form.findChild(QLineEdit, "h1")
        self.h2 = form.findChild(QLineEdit, "h2")
        self.h3 = form.findChild(QLineEdit, "h3")
        self.h4 = form.findChild(QLineEdit, "h4")
        self.h5 = form.findChild(QLineEdit, "h5")
        self.h6 = form.findChild(QLineEdit, "h6")
        self.h7 = form.findChild(QLineEdit, "h7")
        self.h8 = form.findChild(QLineEdit, "h8")
        self.h9 = form.findChild(QLineEdit, "h9")
        self.i1 = form.findChild(QLineEdit, "i1")
        self.i2 = form.findChild(QLineEdit, "i2")
        self.i3 = form.findChild(QLineEdit, "i3")
        self.i4 = form.findChild(QLineEdit, "i4")
        self.i5 = form.findChild(QLineEdit, "i5")
        self.i6 = form.findChild(QLineEdit, "i6")
        self.i7 = form.findChild(QLineEdit, "i7")
        self.i8 = form.findChild(QLineEdit, "i8")
        self.i9 = form.findChild(QLineEdit, "i9")


        

        self.ng_button = form.findChild(QPushButton, "newgame")
        self.ng_button.clicked.connect(self.gen)
        self.ans_button = form.findChild(QPushButton, "solve")
        self.ans_button.clicked.connect(self.solve)


        
    def reset(self):
        self.a1.setText("")
        self.a2.setText("")
        self.a3.setText("")
        self.a4.setText("")
        self.a5.setText("")
        self.a6.setText("")
        self.a7.setText("")
        self.a8.setText("")
        self.a9.setText("")
        self.b1.setText("")
        self.b2.setText("")
        self.b3.setText("")
        self.b4.setText("")
        self.b5.setText("")
        self.b6.setText("")
        self.b7.setText("")
        self.b8.setText("")
        self.b9.setText("")
        self.c1.setText("")
        self.c2.setText("")
        self.c3.setText("")
        self.c4.setText("")
        self.c5.setText("")
        self.c6.setText("")
        self.c7.setText("")
        self.c8.setText("")
        self.c9.setText("")
        self.d1.setText("")
        self.d2.setText("")
        self.d3.setText("")
        self.d4.setText("")
        self.d5.setText("")
        self.d6.setText("")
        self.d7.setText("")
        self.d8.setText("")
        self.d9.setText("")
        self.e1.setText("")
        self.e2.setText("")
        self.e3.setText("")
        self.e4.setText("")
        self.e5.setText("")
        self.e6.setText("")
        self.e7.setText("")
        self.e8.setText("")
        self.e9.setText("")
        self.f1.setText("")
        self.f2.setText("")
        self.f3.setText("")
        self.f4.setText("")
        self.f5.setText("")
        self.f6.setText("")
        self.f7.setText("")
        self.f8.setText("")
        self.f9.setText("")
        self.g1.setText("")
        self.g2.setText("")
        self.g3.setText("")
        self.g4.setText("")
        self.g5.setText("")
        self.g6.setText("")
        self.g7.setText("")
        self.g8.setText("")
        self.g9.setText("")
        self.h1.setText("")
        self.h2.setText("")
        self.h3.setText("")
        self.h4.setText("")
        self.h5.setText("")
        self.h6.setText("")
        self.h7.setText("")
        self.h8.setText("")
        self.h9.setText("")
        self.i1.setText("")
        self.i2.setText("")
        self.i3.setText("")
        self.i4.setText("")
        self.i5.setText("")
        self.i6.setText("")
        self.i7.setText("")
        self.i8.setText("")
        self.i9.setText("")

        self.a1.setStyleSheet('color: black')
        self.a2.setStyleSheet('color: black')
        self.a3.setStyleSheet('color: black')
        self.a4.setStyleSheet('color: black')
        self.a5.setStyleSheet('color: black')
        self.a6.setStyleSheet('color: black')
        self.a7.setStyleSheet('color: black')
        self.a8.setStyleSheet('color: black')
        self.a9.setStyleSheet('color: black')
        self.b1.setStyleSheet('color: black')
        self.b2.setStyleSheet('color: black')
        self.b3.setStyleSheet('color: black')
        self.b4.setStyleSheet('color: black')
        self.b5.setStyleSheet('color: black')
        self.b6.setStyleSheet('color: black')
        self.b7.setStyleSheet('color: black')
        self.b8.setStyleSheet('color: black')
        self.b9.setStyleSheet('color: black')
        self.c1.setStyleSheet('color: black')
        self.c2.setStyleSheet('color: black')
        self.c3.setStyleSheet('color: black')
        self.c4.setStyleSheet('color: black')
        self.c5.setStyleSheet('color: black')
        self.c6.setStyleSheet('color: black')
        self.c7.setStyleSheet('color: black')
        self.c8.setStyleSheet('color: black')
        self.c9.setStyleSheet('color: black')
        self.d1.setStyleSheet('color: black')
        self.d2.setStyleSheet('color: black')
        self.d3.setStyleSheet('color: black')
        self.d4.setStyleSheet('color: black')
        self.d5.setStyleSheet('color: black')
        self.d6.setStyleSheet('color: black')
        self.d7.setStyleSheet('color: black')
        self.d8.setStyleSheet('color: black')
        self.d9.setStyleSheet('color: black')
        self.e1.setStyleSheet('color: black')
        self.e2.setStyleSheet('color: black')
        self.e3.setStyleSheet('color: black')
        self.e4.setStyleSheet('color: black')
        self.e5.setStyleSheet('color: black')
        self.e6.setStyleSheet('color: black')
        self.e7.setStyleSheet('color: black')
        self.e8.setStyleSheet('color: black')
        self.e9.setStyleSheet('color: black')
        self.f1.setStyleSheet('color: black')
        self.f2.setStyleSheet('color: black')
        self.f3.setStyleSheet('color: black')
        self.f4.setStyleSheet('color: black')
        self.f5.setStyleSheet('color: black')
        self.f6.setStyleSheet('color: black')
        self.f7.setStyleSheet('color: black')
        self.f8.setStyleSheet('color: black')
        self.f9.setStyleSheet('color: black')
        self.g1.setStyleSheet('color: black')
        self.g2.setStyleSheet('color: black')
        self.g3.setStyleSheet('color: black')
        self.g4.setStyleSheet('color: black')
        self.g5.setStyleSheet('color: black')
        self.g6.setStyleSheet('color: black')
        self.g7.setStyleSheet('color: black')
        self.g8.setStyleSheet('color: black')
        self.g9.setStyleSheet('color: black')
        self.h1.setStyleSheet('color: black')
        self.h2.setStyleSheet('color: black')
        self.h3.setStyleSheet('color: black')
        self.h4.setStyleSheet('color: black')
        self.h5.setStyleSheet('color: black')
        self.h6.setStyleSheet('color: black')
        self.h7.setStyleSheet('color: black')
        self.h8.setStyleSheet('color: black')
        self.h9.setStyleSheet('color: black')
        self.i1.setStyleSheet('color: black')
        self.i2.setStyleSheet('color: black')
        self.i3.setStyleSheet('color: black')
        self.i4.setStyleSheet('color: black')
        self.i5.setStyleSheet('color: black')
        self.i6.setStyleSheet('color: black')
        self.i7.setStyleSheet('color: black')
        self.i8.setStyleSheet('color: black')
        self.i9.setStyleSheet('color: black')

    def solve(self):
        p=Prolog()
        if(self.count%3==1):
            p = Prolog()
            p.consult('func.pl')
            
            #X = (list(p.query('sudoku(Solution,[[_,_,_,_,3,8,_,_,_],[_,8,_,9,_,_,2,7,_],[3,_,4,_,_,_,_,_,1],[9,4,_,1,7,_,_,_,5],[_,_,7,_,6,_,_,_,_],[_,5,_,_,_,_,_,2,6],[_,9,_,_,_,_,_,5,_],[_,_,_,6,8,_,_,4,_],[_,6,_,_,1,_,9,_,7]])')))


            X = ((p.query('sudoku(Solution,[[_,_,_,_,_,_,_,3,1],[_,1,_,_,6,2,4,_,_],[5,_,3,7,_,_,_,_,_],[_,9,_,8,2,_,_,_,_],[6,_,_,_,_,_,_,8,_],[_,5,4,9,_,_,7,6,_],[_,_,_,_,5,_,8,1,_],[_,8,_,6,_,4,_,7,_],[_,4,_,_,9,_,_,_,_]])')))

            #X = (list(p.query('sudoku(Solution,[_,_,_,_,_,_,_,3,1,_,1,_,_,6,2,4,_,_,5,_,3,7,_,_,_,_,_,_,9,_,8,2,_,_,_,_,6,_,_,_,_,_,_,8,_,_,5,4,9,_,_,7,6,_,_,_,_,_,5,_,8,1,_,_,8,_,6,_,4,_,7,_,_,4,_,_,9,_,_,_,_])')))
            A = X.next()
            Z = list(A['Solution'])

            print(Z)

            self.a1.setText(str(Z[0]))
            self.a2.setText(str(Z[1]))
            self.a3.setText(str(Z[2]))
            self.a4.setText(str(Z[3]))
            self.a5.setText(str(Z[4]))
            self.a6.setText(str(Z[5]))
            self.a7.setText(str(Z[6]))
            self.a8.setText(str(Z[7]))
            self.a9.setText(str(Z[8]))

            self.b1.setText(str(Z[9]))
            self.b2.setText(str(Z[10]))
            self.b3.setText(str(Z[11]))
            self.b4.setText(str(Z[12]))
            self.b5.setText(str(Z[13]))
            self.b6.setText(str(Z[14]))
            self.b7.setText(str(Z[15]))
            self.b8.setText(str(Z[16]))
            self.b9.setText(str(Z[17]))

            self.c1.setText(str(Z[18]))
            self.c2.setText(str(Z[19]))
            self.c3.setText(str(Z[20]))
            self.c4.setText(str(Z[21]))
            self.c5.setText(str(Z[22]))
            self.c6.setText(str(Z[23]))
            self.c7.setText(str(Z[24]))
            self.c8.setText(str(Z[25]))
            self.c9.setText(str(Z[26]))

            self.d1.setText(str(Z[27]))
            self.d2.setText(str(Z[28]))
            self.d3.setText(str(Z[29]))
            self.d4.setText(str(Z[30]))
            self.d5.setText(str(Z[31]))
            self.d6.setText(str(Z[32]))
            self.d7.setText(str(Z[33]))
            self.d8.setText(str(Z[34]))
            self.d9.setText(str(Z[35]))

            self.e1.setText(str(Z[36]))
            self.e2.setText(str(Z[37]))
            self.e3.setText(str(Z[38]))
            self.e4.setText(str(Z[39]))
            self.e5.setText(str(Z[40]))
            self.e6.setText(str(Z[41]))
            self.e7.setText(str(Z[42]))
            self.e8.setText(str(Z[43]))
            self.e9.setText(str(Z[44]))

            self.f1.setText(str(Z[45]))
            self.f2.setText(str(Z[46]))
            self.f3.setText(str(Z[47]))
            self.f4.setText(str(Z[48]))
            self.f5.setText(str(Z[49]))
            self.f6.setText(str(Z[50]))
            self.f7.setText(str(Z[51]))
            self.f8.setText(str(Z[52]))
            self.f9.setText(str(Z[53]))

            self.g1.setText(str(Z[54]))
            self.g2.setText(str(Z[55]))
            self.g3.setText(str(Z[56]))
            self.g4.setText(str(Z[57]))
            self.g5.setText(str(Z[58]))
            self.g6.setText(str(Z[59]))
            self.g7.setText(str(Z[60]))
            self.g8.setText(str(Z[61]))
            self.g9.setText(str(Z[62]))

            self.h1.setText(str(Z[63]))
            self.h2.setText(str(Z[64]))
            self.h3.setText(str(Z[65]))
            self.h4.setText(str(Z[66]))
            self.h5.setText(str(Z[67]))
            self.h6.setText(str(Z[68]))
            self.h7.setText(str(Z[69]))
            self.h8.setText(str(Z[70]))
            self.h9.setText(str(Z[71]))

            self.i1.setText(str(Z[72]))
            self.i2.setText(str(Z[73]))
            self.i3.setText(str(Z[74]))
            self.i4.setText(str(Z[75]))
            self.i5.setText(str(Z[76]))
            self.i6.setText(str(Z[77]))
            self.i7.setText(str(Z[78]))
            self.i8.setText(str(Z[79]))
            self.i9.setText(str(Z[80]))

            

        elif(self.count%3==2):
            
            X = (list(p.query('sudoku(Solution,[7,_,8,6,_,_,_,_,_,6,_,_,5,_,3,4,1,_,_,_,_,_,1,_,_,7,_,_,_,_,_,_,_,_,9,2,_,8,1,2,_,_,3,_,_,4,_,_,_,5,9,_,_,_,_,_,5,_,_,_,7,2,_,1,3,_,7,_,_,_,4,_,_,_,6,3,_,_,_,_,_])')))
            #Y = dict(X[0])
            #Z = list(Y['Solution'])
            X = ((p.query('sudoku(Solution,[[7,_,8,6,_,_,_,_,_],[6,_,_,5,_,3,4,1,_],[_,_,_,_,1,_,_,7,_],[_,_,_,_,_,_,_,9,2],[_,8,1,2,_,_,3,_,_],[4,_,_,_,5,9,_,_,_],[_,_,5,_,_,_,7,2,_],[1,3,_,7,_,_,_,4,_],[_,_,6,3,_,_,_,_,_]])')))
            
            

            A = X.next()
            Z = list(A['Solution'])
            print(Z)
            
            self.a1.setText(str(Z[0]))
            self.a2.setText(str(Z[1]))
            self.a3.setText(str(Z[2]))
            self.a4.setText(str(Z[3]))
            self.a5.setText(str(Z[4]))
            self.a6.setText(str(Z[5]))
            self.a7.setText(str(Z[6]))
            self.a8.setText(str(Z[7]))
            self.a9.setText(str(Z[8]))

            self.b1.setText(str(Z[9]))
            self.b2.setText(str(Z[10]))
            self.b3.setText(str(Z[11]))
            self.b4.setText(str(Z[12]))
            self.b5.setText(str(Z[13]))
            self.b6.setText(str(Z[14]))
            self.b7.setText(str(Z[15]))
            self.b8.setText(str(Z[16]))
            self.b9.setText(str(Z[17]))

            self.c1.setText(str(Z[18]))
            self.c2.setText(str(Z[19]))
            self.c3.setText(str(Z[20]))
            self.c4.setText(str(Z[21]))
            self.c5.setText(str(Z[22]))
            self.c6.setText(str(Z[23]))
            self.c7.setText(str(Z[24]))
            self.c8.setText(str(Z[25]))
            self.c9.setText(str(Z[26]))

            self.d1.setText(str(Z[27]))
            self.d2.setText(str(Z[28]))
            self.d3.setText(str(Z[29]))
            self.d4.setText(str(Z[30]))
            self.d5.setText(str(Z[31]))
            self.d6.setText(str(Z[32]))
            self.d7.setText(str(Z[33]))
            self.d8.setText(str(Z[34]))
            self.d9.setText(str(Z[35]))

            self.e1.setText(str(Z[36]))
            self.e2.setText(str(Z[37]))
            self.e3.setText(str(Z[38]))
            self.e4.setText(str(Z[39]))
            self.e5.setText(str(Z[40]))
            self.e6.setText(str(Z[41]))
            self.e7.setText(str(Z[42]))
            self.e8.setText(str(Z[43]))
            self.e9.setText(str(Z[44]))

            self.f1.setText(str(Z[45]))
            self.f2.setText(str(Z[46]))
            self.f3.setText(str(Z[47]))
            self.f4.setText(str(Z[48]))
            self.f5.setText(str(Z[49]))
            self.f6.setText(str(Z[50]))
            self.f7.setText(str(Z[51]))
            self.f8.setText(str(Z[52]))
            self.f9.setText(str(Z[53]))

            self.g1.setText(str(Z[54]))
            self.g2.setText(str(Z[55]))
            self.g3.setText(str(Z[56]))
            self.g4.setText(str(Z[57]))
            self.g5.setText(str(Z[58]))
            self.g6.setText(str(Z[59]))
            self.g7.setText(str(Z[60]))
            self.g8.setText(str(Z[61]))
            self.g9.setText(str(Z[62]))

            self.h1.setText(str(Z[63]))
            self.h2.setText(str(Z[64]))
            self.h3.setText(str(Z[65]))
            self.h4.setText(str(Z[66]))
            self.h5.setText(str(Z[67]))
            self.h6.setText(str(Z[68]))
            self.h7.setText(str(Z[69]))
            self.h8.setText(str(Z[70]))
            self.h9.setText(str(Z[71]))

            self.i1.setText(str(Z[72]))
            self.i2.setText(str(Z[73]))
            self.i3.setText(str(Z[74]))
            self.i4.setText(str(Z[75]))
            self.i5.setText(str(Z[76]))
            self.i6.setText(str(Z[77]))
            self.i7.setText(str(Z[78]))
            self.i8.setText(str(Z[79]))
            self.i9.setText(str(Z[80]))

        elif(self.count%3==0):
            
            X = (list(p.query('sudoku(Solution,[_,_,_,1,2,_,7,4,_,_,_,_,5,7,3,_,_,2,3,_,_,_,_,_,_,_,_,7,1,_,_,_,_,2,_,6,_,5,2,_,_,_,8,9,_,6,_,8,_,_,_,_,7,4,_,_,_,_,_,_,_,_,5,8,_,_,3,4,1,_,_,_,_,6,3,_,5,9,_,_,_])')))
            #Y = dict(X[0])
            #Z = list(Y['Solution'])
            X = ((p.query('sudoku(Solution,[[_,_,_,1,2,_,7,4,_],[_,_,_,5,7,3,_,_,2],[3,_,_,_,_,_,_,_,_],[7,1,_,_,_,_,2,_,6],[_,5,2,_,_,_,8,9,_],[6,_,8,_,_,_,_,7,4],[_,_,_,_,_,_,_,_,5],[8,_,_,3,4,1,_,_,_],[_,6,3,_,5,9,_,_,_]])')))
            
            
            A = X.next()
            Z = list(A['Solution'])
            print(Z)
            
            self.a1.setText(str(Z[0]))
            self.a2.setText(str(Z[1]))
            self.a3.setText(str(Z[2]))
            self.a4.setText(str(Z[3]))
            self.a5.setText(str(Z[4]))
            self.a6.setText(str(Z[5]))
            self.a7.setText(str(Z[6]))
            self.a8.setText(str(Z[7]))
            self.a9.setText(str(Z[8]))

            self.b1.setText(str(Z[9]))
            self.b2.setText(str(Z[10]))
            self.b3.setText(str(Z[11]))
            self.b4.setText(str(Z[12]))
            self.b5.setText(str(Z[13]))
            self.b6.setText(str(Z[14]))
            self.b7.setText(str(Z[15]))
            self.b8.setText(str(Z[16]))
            self.b9.setText(str(Z[17]))

            self.c1.setText(str(Z[18]))
            self.c2.setText(str(Z[19]))
            self.c3.setText(str(Z[20]))
            self.c4.setText(str(Z[21]))
            self.c5.setText(str(Z[22]))
            self.c6.setText(str(Z[23]))
            self.c7.setText(str(Z[24]))
            self.c8.setText(str(Z[25]))
            self.c9.setText(str(Z[26]))

            self.d1.setText(str(Z[27]))
            self.d2.setText(str(Z[28]))
            self.d3.setText(str(Z[29]))
            self.d4.setText(str(Z[30]))
            self.d5.setText(str(Z[31]))
            self.d6.setText(str(Z[32]))
            self.d7.setText(str(Z[33]))
            self.d8.setText(str(Z[34]))
            self.d9.setText(str(Z[35]))

            self.e1.setText(str(Z[36]))
            self.e2.setText(str(Z[37]))
            self.e3.setText(str(Z[38]))
            self.e4.setText(str(Z[39]))
            self.e5.setText(str(Z[40]))
            self.e6.setText(str(Z[41]))
            self.e7.setText(str(Z[42]))
            self.e8.setText(str(Z[43]))
            self.e9.setText(str(Z[44]))

            self.f1.setText(str(Z[45]))
            self.f2.setText(str(Z[46]))
            self.f3.setText(str(Z[47]))
            self.f4.setText(str(Z[48]))
            self.f5.setText(str(Z[49]))
            self.f6.setText(str(Z[50]))
            self.f7.setText(str(Z[51]))
            self.f8.setText(str(Z[52]))
            self.f9.setText(str(Z[53]))

            self.g1.setText(str(Z[54]))
            self.g2.setText(str(Z[55]))
            self.g3.setText(str(Z[56]))
            self.g4.setText(str(Z[57]))
            self.g5.setText(str(Z[58]))
            self.g6.setText(str(Z[59]))
            self.g7.setText(str(Z[60]))
            self.g8.setText(str(Z[61]))
            self.g9.setText(str(Z[62]))

            self.h1.setText(str(Z[63]))
            self.h2.setText(str(Z[64]))
            self.h3.setText(str(Z[65]))
            self.h4.setText(str(Z[66]))
            self.h5.setText(str(Z[67]))
            self.h6.setText(str(Z[68]))
            self.h7.setText(str(Z[69]))
            self.h8.setText(str(Z[70]))
            self.h9.setText(str(Z[71]))

            self.i1.setText(str(Z[72]))
            self.i2.setText(str(Z[73]))
            self.i3.setText(str(Z[74]))
            self.i4.setText(str(Z[75]))
            self.i5.setText(str(Z[76]))
            self.i6.setText(str(Z[77]))
            self.i7.setText(str(Z[78]))
            self.i8.setText(str(Z[79]))
            self.i9.setText(str(Z[80]))








            
    def gen(self):
        if(self.count%3==0):
            self.reset()
            self.a8.setText("3")
            self.a9.setText("1")
            self.b2.setText("1")
            self.b5.setText("6")
            self.b6.setText("2")
            self.b7.setText("4")
            self.c1.setText("5")
            self.c3.setText("3")
            self.c4.setText("7")
            self.d2.setText("9")
            self.d4.setText("8")
            self.d5.setText("2")
            self.e1.setText("6")
            self.e8.setText("8")
            self.f2.setText("5")
            self.f3.setText("4")
            self.f4.setText("9")
            self.f7.setText("7")
            self.f8.setText("6")
            self.g5.setText("5")
            self.g7.setText("8")
            self.g8.setText("1")
            self.h2.setText("8")
            self.h4.setText("6")
            self.h6.setText("4")
            self.h8.setText("7")
            self.i2.setText("4")
            self.i5.setText("9")

            self.a8.setStyleSheet('color: blue')
            self.a9.setStyleSheet('color: blue')
            self.b2.setStyleSheet('color: blue')
            self.b5.setStyleSheet('color: blue')
            self.b6.setStyleSheet('color: blue')
            self.b7.setStyleSheet('color: blue')
            self.c1.setStyleSheet('color: blue')
            self.c3.setStyleSheet('color: blue')
            self.c4.setStyleSheet('color: blue')
            self.d2.setStyleSheet('color: blue')
            self.d4.setStyleSheet('color: blue')
            self.d5.setStyleSheet('color: blue')
            self.e1.setStyleSheet('color: blue')
            self.e8.setStyleSheet('color: blue')
            self.f2.setStyleSheet('color: blue')
            self.f3.setStyleSheet('color: blue')
            self.f4.setStyleSheet('color: blue')
            self.f7.setStyleSheet('color: blue')
            self.f8.setStyleSheet('color: blue')
            self.g5.setStyleSheet('color: blue')
            self.g7.setStyleSheet('color: blue')
            self.g8.setStyleSheet('color: blue')
            self.h2.setStyleSheet('color: blue')
            self.h4.setStyleSheet('color: blue')
            self.h6.setStyleSheet('color: blue')
            self.h8.setStyleSheet('color: blue')
            self.i2.setStyleSheet('color: blue')
            self.i5.setStyleSheet('color: blue')

            self.a8.setReadOnly(True)
            self.a9.setReadOnly(True)
            self.b2.setReadOnly(True)
            self.b5.setReadOnly(True)
            self.b6.setReadOnly(True)
            self.b7.setReadOnly(True)
            self.c1.setReadOnly(True)
            self.c3.setReadOnly(True)
            self.c4.setReadOnly(True)
            self.d2.setReadOnly(True)
            self.d4.setReadOnly(True)
            self.d5.setReadOnly(True)
            self.e1.setReadOnly(True)
            self.e8.setReadOnly(True)
            self.f2.setReadOnly(True)
            self.f3.setReadOnly(True)
            self.f4.setReadOnly(True)
            self.f7.setReadOnly(True)
            self.f8.setReadOnly(True)
            self.g5.setReadOnly(True)
            self.g7.setReadOnly(True)
            self.g8.setReadOnly(True)
            self.h2.setReadOnly(True)
            self.h4.setReadOnly(True)
            self.h6.setReadOnly(True)
            self.h8.setReadOnly(True)
            self.i2.setReadOnly(True)
            self.i5.setReadOnly(True)

            self.count+=1
        elif(self.count%3==1):
            self.reset()
            self.a1.setText("7")
            self.a3.setText("8")
            self.a4.setText("6")
            self.b1.setText("6")
            self.b4.setText("5")
            self.b6.setText("3")
            self.b7.setText("4")
            self.b8.setText("1")
            self.c5.setText("1")
            self.c8.setText("7")
            self.d8.setText("9")
            self.d9.setText("2")
            self.e2.setText("8")
            self.e3.setText("1")
            self.e4.setText("2")
            self.e7.setText("3")
            self.f1.setText("4")
            self.f5.setText("5")
            self.f6.setText("9")
            self.g3.setText("5")
            self.g7.setText("7")
            self.g8.setText("2")
            self.h1.setText("1")
            self.h2.setText("3")
            self.h4.setText("7")
            self.h8.setText("4")
            self.i3.setText("6")
            self.i4.setText("3")

            self.a1.setStyleSheet('color: blue')
            self.a3.setStyleSheet('color: blue')
            self.a4.setStyleSheet('color: blue')
            self.b1.setStyleSheet('color: blue')
            self.b4.setStyleSheet('color: blue')
            self.b6.setStyleSheet('color: blue')
            self.b7.setStyleSheet('color: blue')
            self.b8.setStyleSheet('color: blue')
            self.c5.setStyleSheet('color: blue')
            self.c8.setStyleSheet('color: blue')
            self.d8.setStyleSheet('color: blue')
            self.d9.setStyleSheet('color: blue')
            self.e2.setStyleSheet('color: blue')
            self.e3.setStyleSheet('color: blue')
            self.e4.setStyleSheet('color: blue')
            self.e7.setStyleSheet('color: blue')
            self.f1.setStyleSheet('color: blue')
            self.f5.setStyleSheet('color: blue')
            self.f6.setStyleSheet('color: blue')
            self.g3.setStyleSheet('color: blue')
            self.g7.setStyleSheet('color: blue')
            self.g8.setStyleSheet('color: blue')
            self.h1.setStyleSheet('color: blue')
            self.h2.setStyleSheet('color: blue')
            self.h4.setStyleSheet('color: blue')
            self.h8.setStyleSheet('color: blue')
            self.i3.setStyleSheet('color: blue')
            self.i4.setStyleSheet('color: blue')

            self.a1.setReadOnly(True)
            self.a3.setReadOnly(True)
            self.a4.setReadOnly(True)
            self.b1.setReadOnly(True)
            self.b4.setReadOnly(True)
            self.b6.setReadOnly(True)
            self.b7.setReadOnly(True)
            self.b8.setReadOnly(True)
            self.c5.setReadOnly(True)
            self.c8.setReadOnly(True)
            self.d8.setReadOnly(True)
            self.d9.setReadOnly(True)
            self.e2.setReadOnly(True)
            self.e3.setReadOnly(True)
            self.e4.setReadOnly(True)
            self.e7.setReadOnly(True)
            self.f1.setReadOnly(True)
            self.f5.setReadOnly(True)
            self.f6.setReadOnly(True)
            self.g3.setReadOnly(True)
            self.g7.setReadOnly(True)
            self.g8.setReadOnly(True)
            self.h1.setReadOnly(True)
            self.h2.setReadOnly(True)
            self.h4.setReadOnly(True)
            self.h8.setReadOnly(True)
            self.i3.setReadOnly(True)
            self.i4.setReadOnly(True)

            self.count+=1
        elif(self.count%3==2):
            self.reset()
            self.a4.setText("1")
            self.a5.setText("2")
            self.a7.setText("7")
            self.a8.setText("4")
            self.b4.setText("5")
            self.b5.setText("7")
            self.b6.setText("3")            
            self.b9.setText("2")
            self.c1.setText("3")
            self.d1.setText("7")
            self.d2.setText("1")
            self.d7.setText("2")
            self.d9.setText("6")
            self.e2.setText("5")
            self.e3.setText("2")
            self.e7.setText("8")
            self.e8.setText("9")
            self.f1.setText("6")
            self.f3.setText("8")
            self.f8.setText("7")
            self.f9.setText("4")
            self.g9.setText("5")
            self.h1.setText("1")
            self.h4.setText("3")
            self.h5.setText("4")
            self.h6.setText("1")
            self.i2.setText("6")
            self.i3.setText("3")
            self.i5.setText("5")
            self.i6.setText("9")

            self.a4.setStyleSheet('color: blue')
            self.a5.setStyleSheet('color: blue')
            self.a7.setStyleSheet('color: blue')
            self.a8.setStyleSheet('color: blue')
            self.b4.setStyleSheet('color: blue')
            self.b5.setStyleSheet('color: blue')
            self.b6.setStyleSheet('color: blue')            
            self.b9.setStyleSheet('color: blue')
            self.c1.setStyleSheet('color: blue')
            self.d1.setStyleSheet('color: blue')
            self.d2.setStyleSheet('color: blue')
            self.d7.setStyleSheet('color: blue')
            self.d9.setStyleSheet('color: blue')
            self.e2.setStyleSheet('color: blue')
            self.e3.setStyleSheet('color: blue')
            self.e7.setStyleSheet('color: blue')
            self.e8.setStyleSheet('color: blue')
            self.f1.setStyleSheet('color: blue')
            self.f3.setStyleSheet('color: blue')
            self.f8.setStyleSheet('color: blue')
            self.f9.setStyleSheet('color: blue')
            self.g9.setStyleSheet('color: blue')
            self.h1.setStyleSheet('color: blue')
            self.h4.setStyleSheet('color: blue')
            self.h5.setStyleSheet('color: blue')
            self.h6.setStyleSheet('color: blue')
            self.i2.setStyleSheet('color: blue')
            self.i3.setStyleSheet('color: blue')
            self.i5.setStyleSheet('color: blue')
            self.i6.setStyleSheet('color: blue')


            self.a4.setReadOnly(True)
            self.a5.setReadOnly(True)
            self.a7.setReadOnly(True)
            self.a8.setReadOnly(True)
            self.b4.setReadOnly(True)
            self.b5.setReadOnly(True)
            self.b6.setReadOnly(True)            
            self.b9.setReadOnly(True)
            self.c1.setReadOnly(True)
            self.d1.setReadOnly(True)
            self.d2.setReadOnly(True)
            self.d7.setReadOnly(True)
            self.d9.setReadOnly(True)
            self.e2.setReadOnly(True)
            self.e3.setReadOnly(True)
            self.e7.setReadOnly(True)
            self.e8.setReadOnly(True)
            self.f1.setReadOnly(True)
            self.f3.setReadOnly(True)
            self.f8.setReadOnly(True)
            self.f9.setReadOnly(True)
            self.g9.setReadOnly(True)
            self.h1.setReadOnly(True)
            self.h4.setReadOnly(True)
            self.h5.setReadOnly(True)
            self.h6.setReadOnly(True)
            self.i2.setReadOnly(True)
            self.i3.setReadOnly(True)
            self.i5.setReadOnly(True)
            self.i6.setReadOnly(True)
            self.count+=1


    

       
def main():
    app = QApplication(sys.argv)
    w = My_window()
    w.show()
 
    #p.consult('func.pl')
    #X = (list(p.query('sudoku(Solution,[_,_,_,_,3,8,_,_,_,_,8,_,9,_,_,2,7,_,3,_,4,_,_,_,_,_,1,9,4,_,1,7,_,_,_,5,_,_,7,_,6,_,_,_,_,_,5,_,_,_,_,_,2,6,_,9,_,_,_,_,_,5,_,_,_,_,6,8,_,_,4,_,_,6,_,_,1,_,9,_,7])')))
            

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

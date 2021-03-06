# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sitios.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sitio(object):
    def setupUi(self, sitio):
        sitio.setObjectName("sitio")
        sitio.resize(773, 580)
        sitio.setMinimumSize(QtCore.QSize(773, 580))
        sitio.setMaximumSize(QtCore.QSize(773, 580))
        self.widget = QtWidgets.QWidget(sitio)
        self.widget.setGeometry(QtCore.QRect(30, 50, 461, 504))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_sitio = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sitio.setFont(font)
        self.lb_sitio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sitio.setObjectName("lb_sitio")
        self.gridLayout.addWidget(self.lb_sitio, 0, 0, 1, 2)
        self.foto_sitio = QtWidgets.QLabel(self.widget)
        self.foto_sitio.setText("")
        self.foto_sitio.setPixmap(QtGui.QPixmap("bocasdeltoro.png"))
        self.foto_sitio.setScaledContents(True)
        self.foto_sitio.setObjectName("foto_sitio")
        self.gridLayout.addWidget(self.foto_sitio, 1, 0, 1, 2)
        self.desc_sitio = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        self.desc_sitio.setFont(font)
        self.desc_sitio.setTextFormat(QtCore.Qt.AutoText)
        self.desc_sitio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.desc_sitio.setWordWrap(True)
        self.desc_sitio.setObjectName("desc_sitio")
        self.gridLayout.addWidget(self.desc_sitio, 2, 0, 1, 2)
        self.btn_reservar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reservar.setFont(font)
        self.btn_reservar.setObjectName("btn_reservar")
        self.gridLayout.addWidget(self.btn_reservar, 3, 0, 1, 1)
        self.btn_salir = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 23, 27);")
        self.btn_salir.setObjectName("btn_salir")
        self.gridLayout.addWidget(self.btn_salir, 3, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(sitio)
        self.widget1.setGeometry(QtCore.QRect(500, 50, 258, 501))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_beneficios = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_beneficios.setFont(font)
        self.lb_beneficios.setObjectName("lb_beneficios")
        self.gridLayout_2.addWidget(self.lb_beneficios, 0, 0, 1, 1)
        self.lista_beneficios = QtWidgets.QListWidget(self.widget1)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lista_beneficios.setFont(font)
        self.lista_beneficios.setObjectName("lista_beneficios")
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lista_beneficios.addItem(item)
        self.gridLayout_2.addWidget(self.lista_beneficios, 1, 0, 1, 1)

        self.retranslateUi(sitio)
        QtCore.QMetaObject.connectSlotsByName(sitio)

    def retranslateUi(self, sitio):
        _translate = QtCore.QCoreApplication.translate
        sitio.setWindowTitle(_translate("sitio", "Form"))
        self.lb_sitio.setText(_translate("sitio", "Nombre del Sitio"))
        self.desc_sitio.setText(_translate("sitio", "\n"
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed ornare mauris, eget condimentum dolor. Vestibulum commodo sem non augue fringilla, sed lobortis quam euismod. Praesent posuere lacus eu tortor commodo, nec bibendum augue cursus. Suspendisse potenti. Etiam varius ornare ligula eget laoreet. Nullam mattis vestibulum massa, vitae ultrices erat tincidunt et. Nullam in felis eu felis convallis vestibulum."))
        self.btn_reservar.setText(_translate("sitio", "Reservar"))
        self.btn_salir.setText(_translate("sitio", "Salir"))
        self.lb_beneficios.setText(_translate("sitio", "Beneficios"))
        __sortingEnabled = self.lista_beneficios.isSortingEnabled()
        self.lista_beneficios.setSortingEnabled(False)
        item = self.lista_beneficios.item(0)
        item.setText(_translate("sitio", "Comida"))
        item = self.lista_beneficios.item(1)
        item.setText(_translate("sitio", "Transporte"))
        item = self.lista_beneficios.item(2)
        item.setText(_translate("sitio", "Hospedaje"))
        item = self.lista_beneficios.item(3)
        item.setText(_translate("sitio", "Guía Turistico"))
        item = self.lista_beneficios.item(4)
        item.setText(_translate("sitio", "Paquete de Eventos"))
        item = self.lista_beneficios.item(5)
        item.setText(_translate("sitio", "Fotografo"))
        self.lista_beneficios.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sitio = QtWidgets.QWidget()
    ui = Ui_sitio()
    ui.setupUi(sitio)
    sitio.show()
    sys.exit(app.exec_())

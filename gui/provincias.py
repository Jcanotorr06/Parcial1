# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'provincias.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_provincias(object):
    def setupUi(self, provincias):
        provincias.setObjectName("provincias")
        provincias.resize(698, 442)
        provincias.setMinimumSize(QtCore.QSize(698, 442))
        provincias.setMaximumSize(QtCore.QSize(698, 442))
        self.verticalLayoutWidget = QtWidgets.QWidget(provincias)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 650, 394))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.provincia_nombre = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.provincia_nombre.setFont(font)
        self.provincia_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.provincia_nombre.setObjectName("provincia_nombre")
        self.verticalLayout.addWidget(self.provincia_nombre)
        self.provincia_foto = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.provincia_foto.setText("")
        self.provincia_foto.setPixmap(QtGui.QPixmap("bocasdeltoro.png"))
        self.provincia_foto.setScaledContents(True)
        self.provincia_foto.setObjectName("provincia_foto")
        self.verticalLayout.addWidget(self.provincia_foto)
        self.lista_sitios = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        self.lista_sitios.setFont(font)
        self.lista_sitios.setObjectName("lista_sitios")
        self.lista_sitios.addItem("")
        self.lista_sitios.addItem("")
        self.lista_sitios.addItem("")
        self.lista_sitios.addItem("")
        self.verticalLayout.addWidget(self.lista_sitios)

        self.retranslateUi(provincias)
        QtCore.QMetaObject.connectSlotsByName(provincias)

    def retranslateUi(self, provincias):
        _translate = QtCore.QCoreApplication.translate
        provincias.setWindowTitle(_translate("provincias", "Form"))
        self.provincia_nombre.setText(_translate("provincias", "Provincia"))
        self.lista_sitios.setItemText(0, _translate("provincias", "Isla Bastimentos"))
        self.lista_sitios.setItemText(1, _translate("provincias", "Isla Colon"))
        self.lista_sitios.setItemText(2, _translate("provincias", "Taboga"))
        self.lista_sitios.setItemText(3, _translate("provincias", "Meteti"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    provincias = QtWidgets.QWidget()
    ui = Ui_provincias()
    ui.setupUi(provincias)
    provincias.show()
    sys.exit(app.exec_())
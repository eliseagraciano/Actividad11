# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(525, 539)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.Id_spinBox = QSpinBox(self.groupBox)
        self.Id_spinBox.setObjectName(u"Id_spinBox")

        self.gridLayout.addWidget(self.Id_spinBox, 0, 1, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")

        self.gridLayout.addWidget(self.Green_spinBox, 8, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.Origen_y_spinBox = QSpinBox(self.groupBox)
        self.Origen_y_spinBox.setObjectName(u"Origen_y_spinBox")

        self.gridLayout.addWidget(self.Origen_y_spinBox, 2, 1, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")

        self.gridLayout.addWidget(self.Red_spinBox, 7, 1, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout.addWidget(self.Mostrar_pushButton, 14, 0, 1, 2)

        self.Destino_y_spinBox = QSpinBox(self.groupBox)
        self.Destino_y_spinBox.setObjectName(u"Destino_y_spinBox")

        self.gridLayout.addWidget(self.Destino_y_spinBox, 5, 1, 1, 1)

        self.Agregar_final_pushButton = QPushButton(self.groupBox)
        self.Agregar_final_pushButton.setObjectName(u"Agregar_final_pushButton")

        self.gridLayout.addWidget(self.Agregar_final_pushButton, 15, 0, 1, 2)

        self.Origen_x_spinBox = QSpinBox(self.groupBox)
        self.Origen_x_spinBox.setObjectName(u"Origen_x_spinBox")

        self.gridLayout.addWidget(self.Origen_x_spinBox, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")

        self.gridLayout.addWidget(self.Blue_spinBox, 9, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")

        self.gridLayout.addWidget(self.Velocidad_spinBox, 6, 1, 1, 1)

        self.Agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_inicio_pushButton.setObjectName(u"Agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.Agregar_inicio_pushButton, 10, 0, 1, 2)

        self.Destino_x_spinBox = QSpinBox(self.groupBox)
        self.Destino_x_spinBox.setObjectName(u"Destino_x_spinBox")

        self.gridLayout.addWidget(self.Destino_x_spinBox, 3, 1, 1, 1)

        self.ordenar_id_pushButton = QPushButton(self.groupBox)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.gridLayout.addWidget(self.ordenar_id_pushButton, 11, 0, 1, 2)

        self.Ordenar_distancia_pushButton = QPushButton(self.groupBox)
        self.Ordenar_distancia_pushButton.setObjectName(u"Ordenar_distancia_pushButton")

        self.gridLayout.addWidget(self.Ordenar_distancia_pushButton, 12, 0, 1, 2)

        self.pOrdenar_velocidad_pushButton = QPushButton(self.groupBox)
        self.pOrdenar_velocidad_pushButton.setObjectName(u"pOrdenar_velocidad_pushButton")

        self.gridLayout.addWidget(self.pOrdenar_velocidad_pushButton, 13, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.puntos_pushButton = QPushButton(self.tab_3)
        self.puntos_pushButton.setObjectName(u"puntos_pushButton")

        self.gridLayout_5.addWidget(self.puntos_pushButton, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 525, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen x", None))
        self.Agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Id", None))
        self.Ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Distancia", None))
        self.pOrdenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo de particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.puntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Puntos cercanos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


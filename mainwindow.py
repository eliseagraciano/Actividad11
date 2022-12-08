from PySide2.QtWidgets import QLabel,QMainWindow, QFileDialog, QMessageBox,QTableWidgetItem,QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from particulas import Particulas,Punto
from PySide2.QtGui import QPen,QColor,QTransform
from random import randint
from algoritmos import distancia_euclidiana

#pyside2-uic mainwindow.ui para pasar de .ui a python
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas= Particulas()
        self.puntos=[]
        self.puntos_cercanos=[]


        self.ui=Ui_MainWindow()

        self.ui.setupUi(self)
        
        self.label=QLabel()
        self.ui.statusbar.addWidget(self.label)
        self.ui.Agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.Ordenar_distancia_pushButton.clicked.connect(self.ordenar_d)
        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.pOrdenar_velocidad_pushButton.clicked.connect(self.ordenar_v)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)    
        self.ui.puntos_pushButton.clicked.connect(self.get_puntos)
        self.ui.pushButton.clicked.connect(self.calcular_puntos_mas_cercanos)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    

    def ordenar_d(self):
        self.particulas.sort_list(2)
   
    def ordenar_id(self):
        self.particulas.sort_list(1)

    def ordenar_v(self):
        self.particulas.sort_list(3)
    def wheelEvent(self, event):
        if event.delta() < 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
        
    @Slot()
    def dibujar(self,opc=0):
        pen=QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            
            origen_x=particula.origen_x
            origen_y=particula.origen_y
            destino_x=particula.destino_x
            destino_y=particula.destino_y
            velocidad= particula.destino_y
        #for i in range(200):
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            color=QColor(r,g,b)
            pen.setColor(color)

            #origen_x=randint(0,500)
            #origen_y=randint(0,500)
            #destino_x=randint(0,500)
            #destino_y=randint(0,500)

            self.scene.addEllipse(origen_x,origen_y,3,3,pen)
            self.scene.addEllipse(destino_x,destino_y,3,3,pen)
            if opc==0:
                self.scene.addLine(origen_x+3,origen_y+3,destino_x,destino_y,pen)

    @Slot()
    def puntos_d(self):
        pen=QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            
            origen_x=particula.origen_x
            origen_y=particula.origen_y
            destino_x=particula.destino_x
            destino_y=particula.destino_y
            velocidad= particula.destino_y
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            color=QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(origen_x,origen_y,3,3,pen)
            self.scene.addEllipse(destino_x,destino_y,3,3,pen)
            


    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_id(self):
        id=self.ui.buscar_lineEdit.text()
        encontrado=False
        for particula in self.particulas:
            if id==particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget= QTableWidgetItem(str(particula.id))
                origen_x_widget= QTableWidgetItem(str(particula.origen_x))
                origen_y_widget= QTableWidgetItem(str(particula.origen_y))
                destino_x_widget= QTableWidgetItem(str(particula.destino_x))
                destino_y_widget= QTableWidgetItem(str(particula.destino_y))
                velocidad_widget= QTableWidgetItem(str(particula.destino_y))
                red_widget= QTableWidgetItem(str(particula.red))
                green_widget= QTableWidgetItem(str(particula.green))
                blue_widget= QTableWidgetItem(str(particula.blue))
                distancia_widget= QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_x_widget)
                self.ui.tabla.setItem(0,2,origen_y_widget)
                self.ui.tabla.setItem(0,3,destino_x_widget)
                self.ui.tabla.setItem(0,4,destino_y_widget)
                self.ui.tabla.setItem(0,5,velocidad_widget)
                self.ui.tabla.setItem(0,6,red_widget)
                self.ui.tabla.setItem(0,7,green_widget)
                self.ui.tabla.setItem(0,8,blue_widget)
                self.ui.tabla.setItem(0,9,distancia_widget)
                encontrado=True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula"{id}"no fue encontrada'
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers=["Id","Origen_x","Origen_y","Destino_x","Destino_y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulas))
        row=0
        for particula in self.particulas:
            id_widget= QTableWidgetItem(str(particula.id))
            origen_x_widget= QTableWidgetItem(str(particula.origen_x))
            origen_y_widget= QTableWidgetItem(str(particula.origen_y))
            destino_x_widget= QTableWidgetItem(str(particula.destino_x))
            destino_y_widget= QTableWidgetItem(str(particula.destino_y))
            velocidad_widget= QTableWidgetItem(str(particula.destino_y))
            red_widget= QTableWidgetItem(str(particula.red))
            green_widget= QTableWidgetItem(str(particula.green))
            blue_widget= QTableWidgetItem(str(particula.blue))
            distancia_widget= QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_x_widget)
            self.ui.tabla.setItem(row,2,origen_y_widget)
            self.ui.tabla.setItem(row,3,destino_x_widget)
            self.ui.tabla.setItem(row,4,destino_y_widget)
            self.ui.tabla.setItem(row,5,velocidad_widget)
            self.ui.tabla.setItem(row,6,red_widget)
            self.ui.tabla.setItem(row,7,green_widget)
            self.ui.tabla.setItem(row,8,blue_widget)
            self.ui.tabla.setItem(row,9,distancia_widget)
            row+=1
    @Slot()
    def action_abrir_archivo(self):
        #print("abrir")
        ubicacion=QFileDialog.getOpenFileName(
            self,
            "Abrir Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo"
            )
    @Slot()
    def action_guardar_archivo(self):
        #print("guardar")
        ubicacion=QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)"

        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"
            )
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
    
    @Slot()
    def click_agregar(self):
        id=self.ui.Id_spinBox.text()
        origen_x=self.ui.Origen_x_spinBox.value()
        origen_y=self.ui.Origen_y_spinBox.value()
        destino_x=self.ui.Destino_x_spinBox.value()
        destino_y=self.ui.Destino_y_spinBox.value()
        velocidad=self.ui.Velocidad_spinBox.value()
        red=self.ui.Red_spinBox.value()
        green=self.ui.Green_spinBox.value()
        blue=self.ui.Blue_spinBox.value()

        Particula1=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulas.agregar_final(Particula1)

    @Slot()
    def click_agregar_inicio(self):
        id=self.ui.Id_spinBox.text()
        origen_x=self.ui.Origen_x_spinBox.value()
        origen_y=self.ui.Origen_y_spinBox.value()
        destino_x=self.ui.Destino_x_spinBox.value()
        destino_y=self.ui.Destino_y_spinBox.value()
        velocidad=self.ui.Velocidad_spinBox.value()
        red=self.ui.Red_spinBox.value()
        green=self.ui.Green_spinBox.value()
        blue=self.ui.Blue_spinBox.value()

        Particula1=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulas.agregar_inicio(Particula1)

    def calcular_puntos_mas_cercanos(self):
        for punto01 in self.puntos:
            distMin=1000
            punto=Punto()
            for todos in self.puntos:
                if punto01 == todos:
                    continue
                dist=distancia_euclidiana(punto01.x,punto01.y,todos.x,todos.y)
                if dist < distMin:
                    distMin = dist
                    punto=todos
            self.puntos_cercanos.append([punto01,punto])
        self.dibujar_puntos_mas_cercanos()
    
    def get_puntos(self):
        self.puntos=self.particulas.get_puntos()
        self.dibujar_puntos()
        self.actualizar_particulas()

    def dibujar_puntos(self):
        for punto in self.puntos:
            x=punto.x
            y=punto.y
            red=punto.red
            green=punto.green
            blue=punto.blue
            color=QColor(red,green,blue)
            pen=QPen()
            pen.setColor(color)
            self.scene.addEllipse(x,y,10,10,pen)
        #self.dibujar_puntos_mas_cercanos()

    def dibujar_puntos_mas_cercanos(self):
        for punto01,punto02 in self.puntos_cercanos:
                    pen=QPen()
                    color=QColor(punto01.red,punto01.green,punto01.blue)
                    pen.setColor(color)
                    self.scene.addLine(punto01.x+5,punto01.y+5,punto02.x+5,punto02.y+5,pen)
                

    def actualizar_particulas(self):
        self.label.setText(f"Particulas:{self.particulas.cantidad()}")
    def cercanos(self):
        self.calcular_puntos_mas_cercanos()
        
        #self.particulas.fuerza_bruta()
        
        """ 
        cont=1
        id_par1=0
        id_par2=0
        guardar_candidato1=0
        guardar_candidato2=0
        cercano1=[]
        cercano2=[]

        estudio=[]
        estudio2=[]

        auxiliar=[]
        auxiliar2=[]
        for particula in self.particulas:
            for cont  in range(len(self.particulas)):
                print(cont)
                particula2=self.particulas.recorrer(cont)

                if cont ==1:
                    id_par1=particula2.id
                    id_par2=particula2.id
                    guardar_candidato1=particula2
                    guardar_candidato2=particula2

                    #punto1
                    if particula.origen_x < particula2.origen_x:
                        estudio.append(particula2.origen_x/particula.origen_x)
                    if particula.origen_y < particula2.origen_y:
                        estudio.append(particula2.origen_y/particula.origen_y)
                    #punto2
                    if particula.destino_x < particula2.destino_x:
                        estudio2.append(particula2.destino_x/particula.destino_x)
                    if particula.destino_y < particula2.destino_y:
                        estudio2.append(particula2.destino_y/particula.destino_y)
                    else:   
                        id_par1=particula2.id
                        id_par2=particula2.id
                        guardar_candidato1=particula2
                        guardar_candidato2=particula2
                        #punto1
                        estudio.append(particula.origen_x/particula2.origen_x)
                        estudio.append(particula.origen_y/particula2.origen_y)
                        #punto2
                        estudio2.append(particula.destino_x/particula2.destino_x)
                        estudio2.append(particula.destino_y/particula2.destino_y)
                    #estudio2.append(particula.destino_x-particula2.destino_x)
                    #estudio2.append(particula.destino_y-particula2.destino_y)
                if cont>1:
                    
                    #punto1
                    
                    
                    if particula.origen_x < particula2.origen_x:
                        auxiliar.append(particula2.origen_x/particula.origen_x)
                    if particula.origen_y < particula2.origen_y:
                        auxiliar.append(particula2.origen_y/particula.origen_y)
                    #punto2
                    if particula.destino_x < particula2.destino_x:
                        auxiliar2.append(particula2.destino_x/particula.destino_x)
                    if particula.destino_y < particula2.destino_y:
                        auxiliar2.append(particula2.destino_y/particula.destino_y)
                    else:   
                        #punto1
                        auxiliar.append(particula.origen_x/particula2.origen_x)
                        auxiliar.append(particula.origen_y/particula2.origen_y)
                        #punto2
                        auxiliar2.append(particula.destino_x/particula2.destino_x)
                        auxiliar2.append(particula.destino_y/particula2.destino_y)
                    
                    if auxiliar[0]<=estudio[0] and auxiliar[1]<=estudio[1]:
                        id_par1=particula2.id
                        guardar_candidato1=particula2
                        estudio[0]=auxiliar[0]
                        estudio[1]=auxiliar[1]

                    if auxiliar[0]<=estudio2[0] and auxiliar[1]<=estudio2[1]:
                        id_par1=particula2.id
                        guardar_candidato1=particula2
                        estudio[0]=auxiliar[0]
                        estudio[1]=auxiliar[1]

                    if auxiliar2[0]<=estudio2[0] and auxiliar2[1]<=estudio2[1]:
                        id_par1=particula2.id
                        guardar_candidato2=particula2
                        estudio2[0]=auxiliar2[0]
                        estudio2[1]=auxiliar2[1]
                    
                    if auxiliar2[0]<=estudio[0] and auxiliar2[1]<=estudio[1]:
                        id_par1=particula2.id
                        guardar_candidato2=particula2
                        estudio2[0]=auxiliar2[0]
                        estudio2[1]=auxiliar2[1]
            
            pen=QPen()
            pen.setWidth(2)
            origen_xp1=particula.origen_x
            origen_yp1=particula.origen_y
            destino_xp1=particula.destino_x
            destino_yp1=particula.destino_y

            origen_xp2=guardar_candidato1.origen_x
            origen_yp2=guardar_candidato1.origen_y
            destino_xp2=guardar_candidato2.destino_x
            destino_yp2=guardar_candidato2.destino_y

            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            color=QColor(r,g,b)
            pen.setColor(color)

            self.scene.addEllipse(origen_xp1,origen_yp1,3,3,pen)
            self.scene.addEllipse(origen_xp2,origen_yp2,3,3,pen)
            self.scene.addLine(origen_xp1+3,origen_yp1+3,origen_xp2,origen_yp2,pen)

            self.scene.addEllipse(destino_xp1,destino_yp1,3,3,pen)
            self.scene.addEllipse(destino_xp2,destino_yp2,3,3,pen)
            self.scene.addLine(destino_xp1+3,destino_yp1+3,destino_xp2,destino_yp2,pen)

            print(particula.origen_x,particula.origen_y)
            print(particula.destino_x,particula.destino_y)
    """
                
                
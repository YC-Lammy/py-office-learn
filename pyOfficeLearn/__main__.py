import gc, sys, joblib,os, typing
import pyOfficeSheet
from os import close
from typing import Any

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import pandas as pd
import numpy as np
from webbrowser import open as webbrowser_open
from inspect import getfile
from json import loads as json_loads
from json import dumps as json_dumps
from inspect import getfile
import pyOfficeLearn

def pyofficelearn(screen_width,screen_height):
    image_path = os.path.join(getfile(pyOfficeLearn).replace('__init__.py',''),'pic','icon')

############################################################################################################################################################
############################## read stuff ##################################################################################################################
############################################################################################################################################################
#                                                                    dddddddd                                                                                                        
#                                                                    d::::::d                               tttt                               ffffffffffffffff    ffffffffffffffff  
#                                                                    d::::::d                            ttt:::t                              f::::::::::::::::f  f::::::::::::::::f 
#                                                                    d::::::d                            t:::::t                             f::::::::::::::::::ff::::::::::::::::::f
#                                                                    d:::::d                             t:::::t                             f::::::fffffff:::::ff::::::fffffff:::::f
# rrrrr   rrrrrrrrr       eeeeeeeeeeee    aaaaaaaaaaaaa      ddddddddd:::::d          ssssssssss   ttttttt:::::ttttttt    uuuuuu    uuuuuu   f:::::f       fffffff:::::f       ffffff
# r::::rrr:::::::::r    ee::::::::::::ee  a::::::::::::a   dd::::::::::::::d        ss::::::::::s  t:::::::::::::::::t    u::::u    u::::u   f:::::f             f:::::f             
# r:::::::::::::::::r  e::::::eeeee:::::eeaaaaaaaaa:::::a d::::::::::::::::d      ss:::::::::::::s t:::::::::::::::::t    u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
# rr::::::rrrrr::::::re::::::e     e:::::e         a::::ad:::::::ddddd:::::d      s::::::ssss:::::stttttt:::::::tttttt    u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  r:::::r     r:::::re:::::::eeeee::::::e  aaaaaaa:::::ad::::::d    d:::::d       s:::::s  ssssss       t:::::t          u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  r:::::r     rrrrrrre:::::::::::::::::e aa::::::::::::ad:::::d     d:::::d         s::::::s            t:::::t          u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
#  r:::::r            e::::::eeeeeeeeeee a::::aaaa::::::ad:::::d     d:::::d            s::::::s         t:::::t          u::::u    u::::u   f:::::f             f:::::f             
#  r:::::r            e:::::::e         a::::a    a:::::ad:::::d     d:::::d      ssssss   s:::::s       t:::::t    ttttttu:::::uuuu:::::u   f:::::f             f:::::f             
#  r:::::r            e::::::::e        a::::a    a:::::ad::::::ddddd::::::dd     s:::::ssss::::::s      t::::::tttt:::::tu:::::::::::::::uuf:::::::f           f:::::::f            
#  r:::::r             e::::::::eeeeeeeea:::::aaaa::::::a d:::::::::::::::::d     s::::::::::::::s       tt::::::::::::::t u:::::::::::::::uf:::::::f           f:::::::f            
#  r:::::r              ee:::::::::::::e a::::::::::aa:::a d:::::::::ddd::::d      s:::::::::::ss          tt:::::::::::tt  uu::::::::uu:::uf:::::::f           f:::::::f            
#  rrrrrrr                eeeeeeeeeeeeee  aaaaaaaaaa  aaaa  ddddddddd   ddddd       sssssssssss              ttttttttttt      uuuuuuuu  uuuufffffffff           fffffffff            
                                                                                                                                                                           
    def importJoblib(pick=True,filename=None,filter=None,widget=None): # main importer to load binary file
        global pandas_data
        if pick:
            filter = 'Python Object(*.npobj *.pdobj)'
            filename, filter = QFileDialog.getOpenFileName(None, 'Open File', filter=filter)
        if '.npobj' in filename:
            data = joblib.load(filename)
            header = None
        elif '.pdobj' in filename:
            dataframe = joblib.load(filename)
            header = list(dataframe.keys())
            data = np.array(dataframe)

        if widget !=None:
            widget.setText(filename)

############################################################################################################################################################
############################# save stuff ###################################################################################################################
############################################################################################################################################################
#                                                                                                                                                                                   
#                                                                                                          tttt                               ffffffffffffffff    ffffffffffffffff  
#                                                                                                       ttt:::t                              f::::::::::::::::f  f::::::::::::::::f 
#                                                                                                       t:::::t                             f::::::::::::::::::ff::::::::::::::::::f
#                                                                                                       t:::::t                             f::::::fffffff:::::ff::::::fffffff:::::f
#     ssssssssss     aaaaaaaaaaaaavvvvvvv           vvvvvvv eeeeeeeeeeee             ssssssssss   ttttttt:::::ttttttt    uuuuuu    uuuuuu   f:::::f       fffffff:::::f       ffffff
#   ss::::::::::s    a::::::::::::av:::::v         v:::::vee::::::::::::ee         ss::::::::::s  t:::::::::::::::::t    u::::u    u::::u   f:::::f             f:::::f             
# ss:::::::::::::s   aaaaaaaaa:::::av:::::v       v:::::ve::::::eeeee:::::ee     ss:::::::::::::s t:::::::::::::::::t    u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
# s::::::ssss:::::s           a::::a v:::::v     v:::::ve::::::e     e:::::e     s::::::ssss:::::stttttt:::::::tttttt    u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  s:::::s  ssssss     aaaaaaa:::::a  v:::::v   v:::::v e:::::::eeeee::::::e      s:::::s  ssssss       t:::::t          u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#    s::::::s        aa::::::::::::a   v:::::v v:::::v  e:::::::::::::::::e         s::::::s            t:::::t          u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
#       s::::::s    a::::aaaa::::::a    v:::::v:::::v   e::::::eeeeeeeeeee             s::::::s         t:::::t          u::::u    u::::u   f:::::f             f:::::f             
# ssssss   s:::::s a::::a    a:::::a     v:::::::::v    e:::::::e                ssssss   s:::::s       t:::::t    ttttttu:::::uuuu:::::u   f:::::f             f:::::f             
# s:::::ssss::::::sa::::a    a:::::a      v:::::::v     e::::::::e               s:::::ssss::::::s      t::::::tttt:::::tu:::::::::::::::uuf:::::::f           f:::::::f            
# s::::::::::::::s a:::::aaaa::::::a       v:::::v       e::::::::eeeeeeee       s::::::::::::::s       tt::::::::::::::t u:::::::::::::::uf:::::::f           f:::::::f            
#  s:::::::::::ss   a::::::::::aa:::a       v:::v         ee:::::::::::::e        s:::::::::::ss          tt:::::::::::tt  uu::::::::uu:::uf:::::::f           f:::::::f            
#   sssssssssss      aaaaaaaaaa  aaaa        vvv            eeeeeeeeeeeeee         sssssssssss              ttttttttttt      uuuuuuuu  uuuufffffffff           fffffffff           
# 
# 
 
    def save_project_file(saveAs = False): # save project as a dictionary object using joblib
        filter = "py-office-learn(*.polprj)"
        if saveAs:
            directory, filter = QFileDialog.getSaveFileName(None, 'Save File',filter=filter)

        elif current_file_name !=None:
            directory= current_file_name

        
############################################################################################################################################################
################################# operational functions ##########################################################################################################
############################################################################################################################################################
#                                                                                                                                                                
#     ffffffffffffffff                                                                 tttt            iiii                                                      
#    f::::::::::::::::f                                                             ttt:::t           i::::i                                                     
#   f::::::::::::::::::f                                                            t:::::t            iiii                                                      
#   f::::::fffffff:::::f                                                            t:::::t                                                                      
#   f:::::f       ffffffuuuuuu    uuuuuunnnn  nnnnnnnn        ccccccccccccccccttttttt:::::ttttttt    iiiiiii    ooooooooooo   nnnn  nnnnnnnn        ssssssssss   
#   f:::::f             u::::u    u::::un:::nn::::::::nn    cc:::::::::::::::ct:::::::::::::::::t    i:::::i  oo:::::::::::oo n:::nn::::::::nn    ss::::::::::s  
#  f:::::::ffffff       u::::u    u::::un::::::::::::::nn  c:::::::::::::::::ct:::::::::::::::::t     i::::i o:::::::::::::::on::::::::::::::nn ss:::::::::::::s 
#  f::::::::::::f       u::::u    u::::unn:::::::::::::::nc:::::::cccccc:::::ctttttt:::::::tttttt     i::::i o:::::ooooo:::::onn:::::::::::::::ns::::::ssss:::::s
#  f::::::::::::f       u::::u    u::::u  n:::::nnnn:::::nc::::::c     ccccccc      t:::::t           i::::i o::::o     o::::o  n:::::nnnn:::::n s:::::s  ssssss 
#  f:::::::ffffff       u::::u    u::::u  n::::n    n::::nc:::::c                   t:::::t           i::::i o::::o     o::::o  n::::n    n::::n   s::::::s      
#   f:::::f             u::::u    u::::u  n::::n    n::::nc:::::c                   t:::::t           i::::i o::::o     o::::o  n::::n    n::::n      s::::::s   
#   f:::::f             u:::::uuuu:::::u  n::::n    n::::nc::::::c     ccccccc      t:::::t    tttttt i::::i o::::o     o::::o  n::::n    n::::nssssss   s:::::s 
#  f:::::::f            u:::::::::::::::uun::::n    n::::nc:::::::cccccc:::::c      t::::::tttt:::::ti::::::io:::::ooooo:::::o  n::::n    n::::ns:::::ssss::::::s
#  f:::::::f             u:::::::::::::::un::::n    n::::n c:::::::::::::::::c      tt::::::::::::::ti::::::io:::::::::::::::o  n::::n    n::::ns::::::::::::::s 
#  f:::::::f              uu::::::::uu:::un::::n    n::::n  cc:::::::::::::::c        tt:::::::::::tti::::::i oo:::::::::::oo   n::::n    n::::n s:::::::::::ss  
#  fffffffff                uuuuuuuu  uuuunnnnnn    nnnnnn    cccccccccccccccc          ttttttttttt  iiiiiiii   ooooooooooo     nnnnnn    nnnnnn  sssssssssss    
        

    class StdoutRedirector:
        '''A class for redirecting stdout to this Text widget.'''
        def __init__(self,text):
            self.text = text
        def write(self,str):
            self.text.setText(self.text.text()+str)

    
    class rounded_corner_Widget(QWidget):
        def __init__(self, *args, **kwargs):
            QWidget.__init__(self, *args, **kwargs)
            self.setWindowOpacity(0.9)
            #self.setWindowFlags(QtCore.Qt.Popup|QtCore.Qt.FramelessWindowHint)

            radius = 50.0
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()), radius, radius)
            mask = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(mask)
            self.show()


##############################################################################################################################################
############################ set up ##########################################################################################################
##############################################################################################################################################
#                                               tttt                                               
#                                            ttt:::t                                               
#                                            t:::::t                                               
#                                            t:::::t                                               
#     ssssssssss       eeeeeeeeeeee    ttttttt:::::ttttttt    uuuuuu    uuuuuu ppppp   ppppppppp   
#   ss::::::::::s    ee::::::::::::ee  t:::::::::::::::::t    u::::u    u::::u p::::ppp:::::::::p  
# ss:::::::::::::s  e::::::eeeee:::::eet:::::::::::::::::t    u::::u    u::::u p:::::::::::::::::p 
# s::::::ssss:::::se::::::e     e:::::etttttt:::::::tttttt    u::::u    u::::u pp::::::ppppp::::::p
#  s:::::s  ssssss e:::::::eeeee::::::e      t:::::t          u::::u    u::::u  p:::::p     p:::::p
#    s::::::s      e:::::::::::::::::e       t:::::t          u::::u    u::::u  p:::::p     p:::::p
#       s::::::s   e::::::eeeeeeeeeee        t:::::t          u::::u    u::::u  p:::::p     p:::::p
# ssssss   s:::::s e:::::::e                 t:::::t    ttttttu:::::uuuu:::::u  p:::::p    p::::::p
# s:::::ssss::::::se::::::::e                t::::::tttt:::::tu:::::::::::::::uup:::::ppppp:::::::p
# s::::::::::::::s  e::::::::eeeeeeee        tt::::::::::::::t u:::::::::::::::up::::::::::::::::p 
#  s:::::::::::ss    ee:::::::::::::e          tt:::::::::::tt  uu::::::::uu:::up::::::::::::::pp  
#   sssssssssss        eeeeeeeeeeeeee            ttttttttttt      uuuuuuuu  uuuup::::::pppppppp    
#                                                                               p:::::p            
#                                                                               p:::::p            
#                                                                              p:::::::p           
#                                                                              p:::::::p           
#                                                                              p:::::::p           
#                                                                              ppppppppp  
    class DraggableLabel(QLabel):

        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.drag_start_position = event.pos()

        def mouseMoveEvent(self, event):
            if not (event.buttons() & Qt.LeftButton):
                return
            if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
                return
            drag = QDrag(self)
            mimedata = QMimeData()
            mimedata.setText(self.text())
            #mimedata.setImageData(self.pixmap().toImage())

            drag.setMimeData(mimedata)
            pixmap = QPixmap(self.size())
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)


    class DropAcceptWidget(QWidget):
        def __init__(self,layout):
            super().__init__()
            self.setAcceptDrops(True)
            self.setLayout(layout)
            self.currentLayout = layout

        def dragEnterEvent(self, event: QDragEnterEvent):
            if event.mimeData().hasText():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event: QDropEvent):
            if event.mimeData().hasText():
                text = event.mimeData().text()
                
                block = LayerBlockWidget(text)
                if text == 'Sequential Model' and keras_model['sequential']==False:
                    self.currentLayout.insertWidget(1,block)
                    keras_model['sequential'] = True
                elif text != 'Sequential Model':
                    self.currentLayout.addWidget(block)
                    keras_model['layers'].append(block)


    class LayerBlockWidget(QLabel):
        def __init__(self,blockType:str):
            super().__init__()
            self.index = len(keras_model['layers'])
            self.blockType = blockType

            self.setFixedHeight(int(screen_height/8))
            self.setStyleSheet('background-color:#303030;color:white;')
            self.setAttribute(Qt.WA_DeleteOnClose)
            self.layout = QGridLayout()
            self.layout.setAlignment(Qt.AlignLeft)
            self.setLayout(self.layout)

            def deleteBlock():
                if self.blockType != 'Sequential Model':
                    del keras_model['layers'][self.index]
                else:
                    keras_model['sequential'] = False
                self.close()
                self.parentWidget().update()

            blockLabel = QLabel(blockType)
            blockLabel.setStyleSheet('font-size:30px;')
            closeButton = QPushButton()
            closeButton.setIcon(self.style().standardIcon(self.style().SP_DialogCloseButton))
            closeButton.setFlat(True)
            closeButton.clicked.connect(deleteBlock)
            self.layout.addWidget(blockLabel,0,0,1,20)
            self.layout.addWidget(closeButton,0,21,1,1)
            if blockType == 'Sequential Model':
                self.setFixedHeight(int(screen_height/16))
            if blockType == 'Embedding Layer':
                self.input_dim = QLineEdit()
                self.input_dim.setValidator(QIntValidator())
                self.input_dim.setMaximumWidth(int(screen_width/20))
                self.output_dim = QLineEdit()
                self.output_dim.setValidator(QIntValidator())
                self.output_dim.setMaximumWidth(int(screen_width/20))
                self.initializer = QComboBox()
                self.initializer.addItems(['uniform'])
                self.regularizer = QComboBox()
                self.regularizer.addItems(['None'])
                self.mask_zero = QCheckBox('mask_zero')
                self.input_length = QLineEdit()
                self.input_length.setValidator(QIntValidator())
                self.input_length.setPlaceholderText('None')
                self.input_length.setMaximumWidth(int(screen_width/20))
                self.constraint = QComboBox()
                self.constraint.addItems(['None'])

                self.layout.addWidget(QLabel('input dim: '),1,0,1,1)
                self.layout.addWidget(self.input_dim,1,1,1,1)
                self.layout.addWidget(QLabel('output dim: '),1,2,1,1)
                self.layout.addWidget(self.output_dim,1,3,1,1)
                self.layout.addWidget(QLabel('  initializer: '),1,4,1,1)
                self.layout.addWidget(self.initializer,1,5,1,1)
                self.layout.addWidget(QLabel('  regularizer: '),1,6,1,1)
                self.layout.addWidget(self.regularizer,1,7,1,1)
                self.layout.addWidget(self.mask_zero,2,0,1,1)
                self.layout.addWidget(QLabel('  input Length: '),2,2,1,1)
                self.layout.addWidget(self.input_length,2,3,1,1)
                self.layout.addWidget(QLabel('  constraint: '),2,4,1,1)
                self.layout.addWidget(self.constraint,2,5,1,2)

            elif blockType == 'Dropout Layer':
                self.rate = QDoubleSpinBox()
                self.rate.setRange(0.00,1.00)
                self.rate.setSingleStep(0.01)
                self.rate.setDecimals(2)
                self.rate.setValue(0.20)
                self.layout.addWidget(QLabel('rate: '),1,0,1,1)
                self.layout.addWidget(self.rate,1,1,1,1)

            elif blockType == 'Dense Layer':
                self.units = QLineEdit()
                self.units.setValidator(QIntValidator())
                self.units.setMaximumWidth(int(screen_width/20))

                self.layout.addWidget(QLabel('units: '),1,0,1,1)
                self.layout.addWidget(self.units,1,1,1,1)

        def check_submit(self):
            return True

    class ModelCompilerBlock(QLabel):
        def __init__(self):
            super().__init__()
            self.layout = QGridLayout()
            self.layout.setAlignment(Qt.AlignLeft)

            self.setLayout(self.layout)
            self.setStyleSheet('background-color:#303030;color:white;')
            
            self.setFrameStyle(QFrame.StyledPanel)
            self.setFrameShadow(QFrame.Sunken)
            self.setFrameShape(QFrame.StyledPanel)
            self.setFixedHeight(int(screen_height/6))

            label = QLabel('compiler')
            label.setStyleSheet('font-size:30px;')
            self.optimizer = QComboBox()
            self.optimizer.addItems(['adam','rsmprop','sgd','adadelta','adagrad','adamax','nadam','ftrl'])

            self.loss = QComboBox()
            self.loss.addItems(['None','mean_squared_error','mean_absolute_error','mean_absolute_percentage_error'
            ,'mean_squared_logarithmic_error','cosine_similarity','huber','log_cosh','binary_crossentropy'
            ,'categorical_crossentropy','sparse_categorical_crossentropy','poisson','kl_divergence','hinge'
            ,'squared_hinge','categorical_hinge'])

            

            
            self.metricButton = QToolButton()
            self.metricButton.setText('None')
            self.metricButton.setPopupMode(QToolButton.InstantPopup)

            metricsMenu = QMenu(self.metricButton)
            self.metricButton.setMenu(metricsMenu)

            self.metrics = []

            def setMetrics(metric:str):
                if metric not in self.metrics:
                    self.metrics.append(metric)
                else:
                    self.metrics.remove(metric)
                self.metricButton.setText(str(self.metrics).replace("'",''))
                    
            metric = ['Accuracy','BinaryAccuracy','CategoricalAccuracy','TopKCategoricalAccuracy'
            ,'SparseTopKCategoricalAccuracy','BinaryCrossentropy','CategoricalCrossentropy'
            ,'SparseCategoricalCrossentropy','KLDivergence','Poisson','MeanSquaredError'
            ,'RootMeanSquaredError','MeanAbsoluteError','MeanAbsolutePercentageError'
            ,'MeanSquaredLogarithmicError','CosineSimilarity','LogCoshError','AUC','Precision'
            ,'Recall','TruePositives','TrueNegatives','FalsePositives','FalseNegatives'
            ,'PrecisionAtRecall','SensitivityAtSpecificity','SpecificityAtSensitivity','MeanIoU'
            ,'Hinge','SquaredHinge','CategoricalHinge']
            for i in metric:
                action = metricsMenu.addAction(i)
                action.setCheckable(True)
                exec(f"action.triggered.connect(lambda:setMetrics('{i}'))",locals())

            self.stepsPerExec = QSpinBox()
            self.stepsPerExec.setRange(1,10)

            self.layout.addWidget(label,0,0,1,2)
            self.layout.addWidget(QLabel('optimizer: '),1,0,1,1)
            self.layout.addWidget(self.optimizer,1,1,1,1)
            self.layout.addWidget(QLabel('   loss: '),1,2,1,1)
            self.layout.addWidget(self.loss,1,3,1,1)
            self.layout.addWidget(QLabel('   Metrics: '),1,4,1,1)
            self.layout.addWidget(self.metricButton,1,5,1,1)
            self.layout.addWidget(QLabel('Steps per execution: '),2,0,1,2)
            self.layout.addWidget(self.stepsPerExec,2,2,1,1)

    frameLayout = QVBoxLayout()
    frameLayout.setAlignment(Qt.AlignTop)

    icon_size = int(screen_height/18)

    mainLayout = QHBoxLayout()
    ######################## menu bar ##############################################################

    bar = QToolBar()
    bar.setFixedHeight(int(screen_height/20))
    frameLayout.addWidget(bar)
    
    frameLayout.addLayout(mainLayout)

    bar.addAction('run')

##################### left menu widget ###################################################################################

    def setMenuChecked(index):
        def setCheckFalse():
            left_menuButton.setChecked(False)
            left_codeButton.setChecked(False)

        if index == 0:
            setCheckFalse()
            left_menuButton.setChecked(True)
            left_code_widget.hide()
            left_menu_mainWidget.show()

        if index == 2:
            setCheckFalse()
            left_codeButton.setChecked(True)
            left_menu_mainWidget.hide()
            left_code_widget.show()

    left_menu_widget = QWidget()
    left_menu_widget.setFixedWidth(int(screen_width/5))
    left_menu_layout = QGridLayout()
    left_menu_widget.setLayout(left_menu_layout)

    
    left_menuButton  = QPushButton()
    left_menuButton.setToolTip('Menu')
    left_menuButton.setIcon(QIcon(os.path.join(image_path,'menu.png')))
    left_menuButton.setIconSize(QSize(icon_size,icon_size))
    left_menuButton.setFlat(True)
    left_menuButton.setCheckable(True)
    left_menuButton.setChecked(True)
    left_menuButton.clicked.connect(lambda:setMenuChecked(0))
    left_menu_layout.addWidget(left_menuButton,0,0,1,1)
    
    left_codeButton = QPushButton()
    left_codeButton.setToolTip('code template')
    left_codeButton.setIcon(QIcon(os.path.join(image_path,'code.png')))
    left_codeButton.setIconSize(QSize(icon_size,icon_size))
    left_codeButton.setFlat(True)
    left_codeButton.setCheckable(True)
    left_codeButton.clicked.connect(lambda:setMenuChecked(2))
    left_menu_layout.addWidget(left_codeButton,1,0,1,1)


    # menu

    left_menu_mainWidget = QWidget()
    #left_menu_mainWidget.setStyleSheet('background-color:#303030;')
    left_menu_layout.addWidget(left_menu_mainWidget,0,1,10,6)
    

    # first menu layou
    left_menu_mainlayout = QVBoxLayout(left_menu_mainWidget)
    left_menu_mainlayout.setAlignment(Qt.AlignTop)
    left_menu_mainWidget.setLayout(left_menu_mainlayout)

    layerLabel = QLabel('Layers')
    layerLabel.setStyleSheet('font-size:40px;')
    left_menu_mainlayout.addWidget(layerLabel)

    left_menu_mainlayout.addSpacing(int(screen_height/60))

    layers = {'Sequential Model':'Sequential groups a linear stack of layers into a tf.keras.Model and provides training and inference features on this model.'
    ,'Input':'Input is used to instantiate a Keras tensor.'
    ,'Embedding Layer':'Embedding layer: Categorical, text'
    ,'Dense Layer':'Dense layer: All scenario'
    ,'Dropout Layer':'Dropout layer: prevent over fitting'
    ,'LSTM Layer':'LSTM layer: text, time series'
    ,'Activation Layer': 'Applies an activation function to an output.'
    ,'Masking Layer': 'Masks a sequence by using a mask value to skip timesteps.'
    }

    for x,y in layers.items():
        label = DraggableLabel(x)
        label.setToolTip(y)
        left_menu_mainlayout.addWidget(label)


    mainLayout.addWidget(left_menu_widget)


    # code

    left_code_widget = QWidget()
    left_code_widget.hide()
    left_menu_layout.addWidget(left_code_widget,0,1,10,6)
    # code template layout
    left_code_layout = QVBoxLayout()
    left_code_layout.setAlignment(Qt.AlignTop)
    codeLabel = QLabel('Code Template')
    codeLabel.setStyleSheet('font-size:30px;')
    left_code_layout.addWidget(codeLabel)
    left_code_widget.setLayout(left_code_layout)

##################### block scroll area #########################################################################

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    vsb = scroll.verticalScrollBar()
    vsb.rangeChanged.connect(lambda:vsb.setValue(vsb.maximum()))

    areaLayout = QVBoxLayout()
    areaLayout.setAlignment(Qt.AlignTop)

    areaWidget = DropAcceptWidget(areaLayout)

    scroll.setWidget(areaWidget)


    genesisblock  = ModelCompilerBlock()
    keras_model['compiler'] = genesisblock

    areaLayout.addWidget(genesisblock)

    mainLayout.addWidget(scroll)

########################## right menu widget ######################################################################

    right_menu_widget = QWidget()
    right_menu_widget.setFixedWidth(int(screen_width/4))
    right_menu_layout = QGridLayout()
    right_menu_widget.setLayout(right_menu_layout)
    mainLayout.addWidget(right_menu_widget)

    return frameLayout



# EEEEEEEEEEEEEEEEEEEEEE                                                                                  tttt                              
# E::::::::::::::::::::E                                                                               ttt:::t                              
# E::::::::::::::::::::E                                                                               t:::::t                              
# EE::::::EEEEEEEEE::::E                                                                               t:::::t                              
#   E:::::E       EEEEEExxxxxxx      xxxxxxx eeeeeeeeeeee        ccccccccccccccccuuuuuu    uuuuuuttttttt:::::ttttttt        eeeeeeeeeeee    
#   E:::::E              x:::::x    x:::::xee::::::::::::ee    cc:::::::::::::::cu::::u    u::::ut:::::::::::::::::t      ee::::::::::::ee  
#   E::::::EEEEEEEEEE     x:::::x  x:::::xe::::::eeeee:::::ee c:::::::::::::::::cu::::u    u::::ut:::::::::::::::::t     e::::::eeeee:::::ee
#   E:::::::::::::::E      x:::::xx:::::xe::::::e     e:::::ec:::::::cccccc:::::cu::::u    u::::utttttt:::::::tttttt    e::::::e     e:::::e
#   E:::::::::::::::E       x::::::::::x e:::::::eeeee::::::ec::::::c     cccccccu::::u    u::::u      t:::::t          e:::::::eeeee::::::e
#   E::::::EEEEEEEEEE        x::::::::x  e:::::::::::::::::e c:::::c             u::::u    u::::u      t:::::t          e:::::::::::::::::e 
#   E:::::E                  x::::::::x  e::::::eeeeeeeeeee  c:::::c             u::::u    u::::u      t:::::t          e::::::eeeeeeeeeee  
#   E:::::E       EEEEEE    x::::::::::x e:::::::e           c::::::c     cccccccu:::::uuuu:::::u      t:::::t    tttttte:::::::e           
# EE::::::EEEEEEEE:::::E   x:::::xx:::::xe::::::::e          c:::::::cccccc:::::cu:::::::::::::::uu    t::::::tttt:::::te::::::::e          
# E::::::::::::::::::::E  x:::::x  x:::::xe::::::::eeeeeeee   c:::::::::::::::::c u:::::::::::::::u    tt::::::::::::::t e::::::::eeeeeeee  
# E::::::::::::::::::::E x:::::x    x:::::xee:::::::::::::e    cc:::::::::::::::c  uu::::::::uu:::u      tt:::::::::::tt  ee:::::::::::::e  
# EEEEEEEEEEEEEEEEEEEEEExxxxxxx      xxxxxxx eeeeeeeeeeeeee      cccccccccccccccc    uuuuuuuu  uuuu        ttttttttttt      eeeeeeeeeeeeee  
            
def main():
    print('in construction')
    global plt_setting, saved_file, current_file_name, settings, mainWidget, prjdict, keras_model

######################### handle sys argvs ###########################################################################################################

    print('argvs:'+str(sys.argv))

    if '-help' in sys.argv or '--help' in sys.argv or 'help' in sys.argv:
        print("""Usage: py-office-learn [<option>...]
py-office-learn cross-platform spreadsheet based on keras and numpy for easy machine learning\n
for more information, visit https://github.com/YC-Lammy/py-office-learn
        """)
        return 0


    if '-uninstall' in sys.argv or '--uninstall' in sys.argv or 'uninstall' in sys.argv:

        print('after this operation, py-office-sheet will be uninstalled')

        ans = input('\r\nare you sure you want to uninstall? y/n')

        if ans not in ('y','n'):
            while ans not in ('y','n'): # loop until user anser
                ans = input('are you sure you want to uninstall? y/n')

        if ans == 'y':
            from subprocess import run
            run([sys.executable,'-m','pip','uninstall','py-office-sheet'])
        elif ans == 'n':
            print('\r\n action abort.')
        
        return 0

######################### set up GUI ######################################################################################################################## 
    file = None

    for i in sys.argv:
        if '.pdobj' in i or '.npobj' in i or '.csv' in i:
            file = i 

    saved_file = True #state if the file is modified, notice user to save file
    current_file_name = None #current file name is the file user opened using open file function
    plt_setting = {'set':False}
    settings = {}
    prjdict = {}
    keras_model = {'sequential':False,'layers':[],'compiler':None,'trainer':None}


    def closeEventHandler(event): # this function is called when user tries to close app, line 559

        if saved_file == True: # is nothing is modified, quit normally
            event.accept()
        else:
            m = QMessageBox()
            m.setWindowTitle('file not save')
            ret = m.question(mainWidget,'', "Exit without saving?", m.Yes | m.No,m.No) # default as No

            if ret == m.Yes:
                event.accept() # if user choose yes, exit without saving
            else:
                event.ignore() # when user choose no, stop exit event


    app = QApplication(['-style fusion']+sys.argv)

    screensize= app.primaryScreen().size()
    screen_height = screensize.height()
    screen_width = screensize.width()

    mainWidget = QWidget() # spreedsheet returns a layout
    layout = pyofficelearn(screen_width,screen_height)
    mainWidget.setLayout(layout)
    mainWidget.closeEvent = closeEventHandler # reassign the app's close event
    mainWidget.setWindowState(Qt.WindowMaximized)
    mainWidget.setWindowTitle('py-office-learn') # actual title not desided
    mainWidget.show()
    app.exec_()

    jsonpath = os.path.join(getfile(pyOfficeLearn).replace('__init__.py',''),'config.json')

    with open(jsonpath,'w') as f:
        f.write(json_dumps(settings))
        f.close()
    
    gc.collect()
    sys.exit()
if __name__ == '__main__':
    main()
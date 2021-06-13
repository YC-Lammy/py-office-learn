import gc, sys, joblib,os
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
    global plt_setting, saved_file, current_file_name, settings, mainWidget

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

    mainWidget = QWidget()
    mainWidget.setLayout(QVBoxLayout()) # spreedsheet returns a layout
    mainWidget.show()
    mainWidget.closeEvent = closeEventHandler # reassign the app's close event
    mainWidget.setWindowState(Qt.WindowMaximized)
    mainWidget.setWindowTitle('py-office-sheet') # actual title not desided

    app.exec_()

    jsonpath = os.path.join(getfile(pyOfficeLearn).replace('__init__.py',''),'config.json')

    with open(jsonpath,'w') as f:
        f.write(json_dumps(settings))
        f.close()
    
    gc.collect()
    sys.exit()
if __name__ == '__main__':
    main()
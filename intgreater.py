from PyQt4 import QtCore, QtGui
from db import *
import hamster_threads
import Queue
import threading

import sys, os #, getopt
import time  # sleep
import signal
from HamsterAPI.comm_usb import RobotComm
import OrderItems
import configu

def myorder():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = OrderItems.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #myQueue = ui.event_queue
    sys.exit(app.exec_())

def myorder2Ro():
    hamster_threads.main()

def putItem(item):
    #global event_queue
    configu.event_queue.put(item)
    
def checkQueue():
    #global event_queue
    value = configu.event_queue.empty()
    return value
def getItem():
    #global event_queue
    value2 = configu.event_queue.get()
    return value2
def getSize():
    value3 = configu.event_queue.qsize()
    return value3

def main(argv=None):

    #import sys
    #global shfNum #,row
    #global event_queue
    #event_queue = Queue.Queue()
    #row = 0
    # start a behavior tread
    behavior_thread11 = threading.Thread(target=myorder())
    behavior_thread11.daemon = True
    behavior_thread11.start()
    #behavior_thread11.join()
    #behavior_thread11.stop()
    #if behavior_thread11.isAlive():
    #    print'inside if 1'
    print('aaaaaaaaaaa')
    #myorder()
    print('2222 after aaa')

    #behavior_thread13 = threading.Thread(target=hamster_threads.main,  args=())
    #behavior_thread13.daemon = True
    #behavior_thread13.start()
    #behavior_thread13.join()
    #behavior_square()
    #print('thrd started')
    #print('thrd started and passed')
    # start a behavior tread
    #behavior_thread2 = threading.Thread(target=hamster_threads.main())
    #behavior_thread2.daemon = True
    #behavior_thread2.start()
    #cleaning up when terminated
    print('zzzzzzzzzz')

if __name__ == "__main__":
    #sys.exit(main())
    main()

import sys, os #, getopt
import time  # sleep
import signal
import threading
from HamsterAPI.comm_usb import RobotComm
import Queue
import OrderItems
import finalMain
import configu

from PyQt4 import QtCore, QtGui
from db import *

if (sys.platform == 'darwin'):
    from PyObjCTools import AppHelper

#gMaxRobotNum = 2; # max number of robots to control
#grobotList = []
#gRobotList = None
#global event_queue

def behavior_blink():
    global gRobotList
 
    while not gQuit:
        if (len(gRobotList) > 0):
          for robot in gRobotList:
            robot.set_led(0, 3)
            robot.set_led(1, 3)
            time.sleep(0.1)
            robot.set_led(0, 0)
            robot.set_led(1, 0)
            time.sleep(0.1)
        time.sleep(0.01)
    print "robot stops blinking"

def set_variables(rrStop,rrLTurn,rrRTurn1,rrRTurn2,rrRTurn3,rrDelivery,rrBackStation,roNum):
    global rStop,rLTurn,rRTurn1,rRTurn2,rRTurn3,rDelivery,rBackStation
    global rStop1,rLTurn1,rRTurn11,rRTurn21,rRTurn31,rDelivery1,rBackStation1
    if(roNum==0):
        rStop = rrStop
        rLTurn=rrLTurn
        rRTurn1=rrRTurn1
        rRTurn2=rrRTurn2
        rRTurn3=rrRTurn3
        rDelivery=rrDelivery
        rBackStation=rrBackStation
    else:
        rStop1 = rrStop
        rLTurn1=rrLTurn
        rRTurn11=rrRTurn1
        rRTurn21=rrRTurn2
        rRTurn31=rrRTurn3
        rDelivery1=rrDelivery
        rBackStation1=rrBackStation
def orderRobot(shelf_num,rNum):
    print('Shelf Number:',shelf_num)
    if(shelf_num==1):
        set_variables(2,-1,3,6,-1,9,10,rNum)
    elif(shelf_num==2):
        set_variables(4,-1,5,8,-1,13,14,rNum)
    elif(shelf_num==3):
        set_variables(6,-1,7,10,-1,17,18,rNum)
    elif(shelf_num==4):
        set_variables(8,-1,9,12,-1,21,22,rNum)
    elif(shelf_num==5):
        set_variables(3,2,1,4,6,9,10,rNum)
    elif(shelf_num==6):
        set_variables(5,2,1,6,8,13,14,rNum)
    elif(shelf_num==7):
        set_variables(7,2,1,8,10,17,18,rNum)
    elif(shelf_num==8):
        set_variables(9,2,1,10,12,21,22,rNum)
    elif(shelf_num==9):
        set_variables(4,3,1,5,6,9,10,rNum)
    elif(shelf_num==10):
        set_variables(6,3,1,7,8,13,14,rNum)
    elif(shelf_num==11):
        set_variables(8,3,1,9,10,17,18,rNum)
    else:
        set_variables(10,3,1,11,12,21,22,rNum)
    #Queue.put(shelf_num)
    #hamster_threads.behavior_square()
        
def behavior_square():
    pass
def behavior_robot_zero():
    global count#, gQuit#, grobotList
    global rStop,rLTurn,rRTurn1,rRTurn2,rRTurn3,rDelivery,rBackStation
    while not configu.gQuit:
        #print('inside while loop gQuit')
        if(True):#len(grobotList) > 0):
            #print('inside if gRobotList')
            #for robot in grobotList[0]:
            #for i in range(0,1):
            robot = configu.grobotList[0]
            #print('P0 value',robot.get_proximity(0), 

robot.get_proximity(1))
            #print('P0 value',robot.get_floor(0), robot.get_floor(1))
            if(robot.get_proximity(0)<40 and robot.get_proximity(1)<40):
                #print('inside for loop robot')
                if(robot.get_floor(0)>75 and robot.get_floor(1)>75):
                    robot.set_wheel(0,30)
                    robot.set_wheel(1,30)
                    time.sleep(0.005)
                elif((robot.get_floor(0) < 25 and robot.get_floor(1) < 25) and (count <=25)):
                    count += 1
                    #print('count: ', count)
                    time.sleep(0.1)
                    robot.set_wheel(0,30)
                    robot.set_wheel(1,30)
                    time.sleep(0.5)
                    if(count==rStop):
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        time.sleep(0.1)
                        for i in range(50,55):
                            robot.set_musical_note(i)   # 1 ~ 88
                            time.sleep(0.5)
                            robot.set_musical_note(0)
                            time.sleep(0.5)
                        robot.set_musical_note(0)
                        time.sleep(0.1)
                        if(count==30 or count==31):
                            robot.set_wheel(0,-30)
                            robot.set_wheel(1,30)
                            time.sleep(1.6)
                            robot.set_wheel(0,30)
                            robot.set_wheel(1,30)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.5)
                    elif(count==rRTurn1 or count==rRTurn2 or count==rRTurn3):
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                    elif(count==rLTurn):
                        robot.set_wheel(0,-30)
                        robot.set_wheel(1,30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                    elif(count ==rDelivery):
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        robot.set_musical_note(40)   # 1 ~ 88
                        time.sleep(1)
                        robot.set_musical_note(0)
                        time.sleep(4)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        #time.sleep(0.7)
                    elif(count ==rBackStation):
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.8)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.3)
                        if(robot.get_proximity(0)>40 and robot.get_proximity(1)>40):
                            time.sleep(1)
                        elif(robot.get_proximity(0)>40 or robot.get_proximity(1)>40):
                            time.sleep(1)
                        else:
                            time.sleep(2.5)
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        robot.set_musical_note(87)   # 1 ~ 88
                        time.sleep(1)
                        robot.set_musical_note(0)
                        time.sleep(5)
                        configu.gQuit = True
                        count = 0
                        #stopThrd = 1
                        #sys.exit(main())
                    else:
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.005)
                elif(robot.get_floor(0)>75 and robot.get_floor(1) <25):
                    robot.set_wheel(0, 30)
                    robot.set_wheel(1, 13)
                    time.sleep(0.005)
                elif(robot.get_floor(0)<25 and robot.get_floor(1) >75):
                    robot.set_wheel(0, 13)
                    robot.set_wheel(1, 30)
                    time.sleep(0.005)
            elif(robot.get_proximity(0) > 40 and robot.get_proximity(1) > 40):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                #print('obstacle0 both')
                time.sleep(0.3)
                #else:
                    #robot.set_wheel(0, 0)
                    #robot.set_wheel(1, 0)
                    #time.sleep(0.1)
            '''
            elif(robot.get_proximity(0) > 75 and robot.get_proximity(1) >= 0):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                print('obstacle 0 left')
                time.sleep(1)
            elif(robot.get_proximity(0) >= 0 and robot.get_proximity(1) > 75):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                print('obstacle 1 right')
                time.sleep(1)
            '''
    time.sleep(0.01)
    print "robot stops moving"
def behavior_robot_one():
    global count1#, gQuit#, grobotList
    global rStop1,rLTurn1,rRTurn11,rRTurn21,rRTurn31,rDelivery1,rBackStation1
    print('inside def loop gQuit111')
    while not configu.gQuit1:
        #print('inside while loop gQuit1')
        if(True):#len(grobotList) > 0):
            #print('inside if gRobotList')
            #for robot in grobotList[0]:
            #for i in range(0,1):
            robot = configu.grobotList[1]
            #print('P1 value',robot.get_proximity(0), robot.get_proximity(1))
            if(robot.get_proximity(0)<40 and robot.get_proximity(1)<40):
                #print('inside for loop robot')
                #def get_proximity(self):
                """Return the values of the proximity sensors.

                Return:
                A 2-tuple of the left and right proximity values.
                """
                #return (self._hamster.get_proximity(0), self._hamster.get_proximity(1))
                if(robot.get_floor(0)>75 and robot.get_floor(1)>75):
                    robot.set_wheel(0,30)
                    robot.set_wheel(1,30)
                    time.sleep(0.005)
                elif((robot.get_floor(0) < 25 and robot.get_floor(1) < 25) and (count1 <=25)):
                   
                count1 += 1
                    #print('count 1 : ', count1)
                    time.sleep(0.1)
                    robot.set_wheel(0,30)
                    robot.set_wheel(1,30)
                    time.sleep(0.5)
                    if(count1==rStop1):
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        time.sleep(0.1)
                        for i in range(50,55):
                            robot.set_musical_note(i)   # 1 ~ 88
                            time.sleep(0.5)
                            robot.set_musical_note(0)
                            time.sleep(0.5)
                        robot.set_musical_note(0)
                        time.sleep(0.1)
                        if(count1==30 or count1==31):
                            robot.set_wheel(0,-30)
                            robot.set_wheel(1,30)
                            time.sleep(1.6)
                            robot.set_wheel(0,30)
                            robot.set_wheel(1,30)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.5)
                    elif(count1==rRTurn11 or count1==rRTurn21 or count1==rRTurn31):
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                    elif(count1==rLTurn1):
                        robot.set_wheel(0,-30)
                        robot.set_wheel(1,30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                    elif(count1 ==rDelivery1):
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        robot.set_musical_note(40)   # 1 ~ 88
                        time.sleep(1)
                        robot.set_musical_note(0)
                        time.sleep(4)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.7)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        #time.sleep(0.7)
                    elif(count1 ==rBackStation1):
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,-30)
                        time.sleep(0.8)
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.3)
                        if(robot.get_proximity(0)>40 and robot.get_proximity(1)>40):
                            time.sleep(1)
                        elif(robot.get_proximity(0)>40 or robot.get_proximity(1)>40):
                            time.sleep(1)
                        else:
                            time.sleep(2.5)
                        robot.set_wheel(0,0)
                        robot.set_wheel(1,0)
                        robot.set_musical_note(87)   # 1 ~ 88
                        time.sleep(1)
                        robot.set_musical_note(0)
                        time.sleep(5)
                        configu.gQuit1 = True
                        count1 = 0
                        #stopThrd = 1
                        #sys.exit(main())
                    else:
                        robot.set_wheel(0,30)
                        robot.set_wheel(1,30)
                        time.sleep(0.005)
                elif(robot.get_floor(0)>75 and robot.get_floor(1) <25):
                    robot.set_wheel(0, 30)
                    robot.set_wheel(1, 13)
                    time.sleep(0.005)
                elif(robot.get_floor(0)<25 and robot.get_floor(1) >75):
                    robot.set_wheel(0, 13)
                    robot.set_wheel(1, 30)
                    time.sleep(0.005)
            elif(robot.get_proximity(0) > 40 and robot.get_proximity(1) > 40):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                #print('obstacle1 both')
                time.sleep(0.3)
            elif(robot.get_proximity(0) > 40 or robot.get_proximity(1) > 40):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                #print('obstacle1 one side')
                time.sleep(0.1)
                #else:
                    #robot.set_wheel(0, 0)
                    #robot.set_wheel(1, 0)
                    #time.sleep(0.1)
            '''
            elif(robot.get_proximity(0) > 75 and robot.get_proximity(1) >= 0):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                print('obstacle1 0 left')
                time.sleep(1)
            elif(robot.get_proximity(0) >= 0 and robot.get_proximity(1) > 75):
                robot.set_wheel(0, 0)
                robot.set_wheel(1, 0)
                print('obstacle1 1 right')
                time.sleep(1)
            '''

    time.sleep(0.01)
    print "robot stops moving"
#house keeping
def clean_up():
    print "cleaning up..."
    if (sys.platform == 'darwin'):
       AppHelper.stopEventLoop()
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    clean_up()
signal.signal(signal.SIGINT, signal_handler)
def main(argv=None):

    while(not(finalMain.checkQueue())):
        print 'inside main hams'
        #global gQuit
        #gQuit = False
        #global myQueue
        #self.event_queue = Queue.Queue()
        # instantiate COMM object
        #global gMaxRobotNum
        global count,count1 #,stopThrd
        count = 0
        count1 = 0
        comm = RobotComm(configu.gMaxRobotNum)
        comm.start()
        print 'Bluetooth starts'
        # instanciate Robot
        #global grobotList, gRobotArray
        #gRobotList = comm.robotList
        configu.grobotList = comm.get_robotList()
        #azx = comm.get_myRobot()
        #gRobotArray = comm.robotArray
        global rStop,rLTurn,rRTurn1,rRTurn2,rRTurn3,rDelivery,rBackStation
        global rStop1,rLTurn1,rRTurn11,rRTurn21,rRTurn31,rDelivery1,rBackStation1
        # start a behavior tread
        '''
        behavior_thread1 = threading.Thread(target=behavior_square)
        behavior_thread1.daemon = True
        behavior_thread1.start()
        '''
        #while(not(event_queue.empty())):
        #behavior_thread1 = threading.Thread(target=behavior_square)
        #behavior_thread1.daemon = True
        #behavior_thread1.start()
        #behavior_square()
        while(finalMain.checkQueue()):
            pass

        conT = finalMain.checkQueue()
        print('queue empty in hamsterTh:', conT)
        if(not conT):
            configu.gQuit = False
            shelfNumber = finalMain.getItem()
            print('queue item:', shelfNumber)
            orderRobot(shelfNumber,0)

        #robot = configu.grobotList[0]
        behavior_thread1 = threading.Thread(target=behavior_robot_zero, args=())
        behavior_thread1.daemon = True
        behavior_thread1.start()
        #behavior_robot_zero()
        #a = raw_input('Enter sth:')
        #print('value: ',a)

        #while(finalMain.checkQueue()):
            #pass

        print('thrd started and passed')
        conT = finalMain.checkQueue()
        if(not conT):
            configu.gQuit1 = False
            shelfNumber = finalMain.getItem()
            print('queue item:', shelfNumber)
            orderRobot(shelfNumber,1)
            # start a behavior tread
            #robot = configu.grobotList[1]
            behavior_thread2 = threading.Thread(target=behavior_robot_one(), args=())
            behavior_thread2.daemon = True
            behavior_thread2.start()
            behavior_thread2.join()
        behavior_thread1.join()
        #behavior_robot_one()

        #print('thrd started')
        #print('thrd started and passed')
        #start a behavior tread
        #behavior_thread2 = threading.Thread(target=behavior_blink)
        #behavior_thread2.daemon = True
        #behavior_thread2.start()
        #cleaning up when terminated
        if (sys.platform == 'win32' or os.name == 'nt'):
            #print('inside if stmt...win32')
            #os.system("pause")
            pass
            #print('inside if stmt...win32 2')
        elif os.name == 'posix':
            if (sys.platform == 'darwin'):
                print('inside if stmt...posix')
                AppHelper.runConsoleEventLoop()
                print('inside if stmt...posix 2')
            else:
                while True:
                    time.sleep(0.1)
                    print('inside if stmt...sleep')
        else:
            print "Error: Unknown OS"

        print('Finishing...')
        #gQuit = True
        #behavior_thread1.join()
        #behavior_thread2.join()
        #behavior_thread1.stop()
        for robot in configu.grobotList:
            robot.reset()
        time.sleep(1.0)
        comm.stop()
        comm.join()

        print("terminated!")

if __name__ == "__main__":
    #sys.exit(main())
    #finalMain()
    main()

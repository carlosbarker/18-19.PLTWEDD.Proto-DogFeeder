import RPi.GPIO as GPIO
import time

from RpiMotorLib import rpiservolib

myservotest = rpiservolib.SG90servo("servo", 50, 3, 11)

# ===== tests for servo SG90 ==========
# initialize
#  name="SG90servoX", freq=50, y_one=2, y_two=12

# section 1
# servo_pin, start=10, end=170, stepdelay=1,
# stepsize=1, initdelay=1, verbose=False
#print("test 1 test method servo_move_step")
#input("Press <Enter> to continue Test1a")
#myservotest.servo_move_step(4, 10, 180, .1, 5, 1, True)
#time.sleep(1)
#input("Press <Enter> to continue Test1b")
#myservotest.servo_move_step(4, 170, 10, .5, 20, 1, True)
#time.sleep(1)
#input("Press <Enter> to continue Test1b")
#myservotest.servo_move_step(4, 10, 180, .1, 5, 1, True)
#time.sleep(1)

print("test 4 test method servo_move")
input("Press <Enter> to continue Test4b1")
time.sleep(1)
myservotest.servo_move(4, 12, .5, True) #Move to 180 degrees
input("Press <Enter> to continue Test4b2")
time.sleep(1)
myservotest.servo_move(4, 2, .5, True) #Move to 0 degrees
input("Press <Enter> to continue Test4b3")
time.sleep(1)
myservotest.servo_move(4, 7.5, .5, True) #Move to 90 degrees


#
#servo_pwm = 4
#
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servo_pwm, GPIO.OUT)
#p = GPIO.PWM(servo_pwm, 50)
#p.start(9)
#
##p.ChangeDutyCycle(7.5) = turn toward 90 degree
##p.ChangeDutyCycle(2.5) = turn toward 0 degree
##p.ChangeDutyCycle(12.5) = turn toward 180 degree
#
#def turn_90degree():
#    p.ChangeDutyCycle(7.5)
#    
#def turn_0degree():
#    p.ChangeDutyCycle(2.5)
#        
#def turn_180degree():
#    p.ChangeDutyCycle(12.5)
#        
##turn_90degree()
##time.sleep(2)
##turn_0degree()
##time.sleep(2)
##turn_180degree()
##time.sleep(2)
#
#time.sleep(10)
#
#p.stop()
#GPIO.cleanup()
import RPi.GPIO as GPIO
import os
import time

ena = 12
in1 = 6
in2 = 13

enb = 21
in3 = 19
in4 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

pwm_a = GPIO.PWM(ena, 500)
pwm_b = GPIO.PWM(enb, 500)

pwm_a.start(0)
pwm_b.start(0)

def MotorA_Clockwise():
    GPIO.output(in1, False)
    GPIO.output(in2, True)
def MotorA_CounterClockwise():
    GPIO.output(in1, True)
    GPIO.output(in2, False)

def MotorB_Clockwise():
    GPIO.output(in3, False)
    GPIO.output(in4, True)
def MotorB_CounterClockwise():
    GPIO.output(in3, True)
    GPIO.output(in4, False)
    
os.system('clear')
print("Elija motor[A-B], el sentido [F-R] y la velocidad [0-100]")
print("Ejemplo 'AF50 MOTOR A Forward a 50% de velocidad")
print("CTRL-C para salir")
print
try:
    while True:
        cmd = input("inserte el comando ")
        cmd = cmd.lower()
        motor = cmd[0]
        direccion = cmd[1]
        velocidad = cmd[2:5]
        
        if motor == "a":
            if direccion == "f":
                MotorA_Clockwise()
                print("Motor A, CW, vel=" + velocidad)
            elif direccion == "r":
                MotorA_CounterClockwise()
                print("Motor A, CCW, vel=" + velocidad)
            else:
                print("comando no reconocido")
            pwm_a.ChangeDutyCycle(int(velocidad))
            print
            
        elif motor == "b":
            if direccion == "f":
                MotorB_Clockwise()
                print("Motor B, CW, vel=" + velocidad)
            elif direccion == "r":
                MotorB_CounterClockwise()
            else:
                print("comando no reconocido")
            pwm_b.ChangeDutyCycle(int(velocidad))
            print
        else:
            print
            print("comando no reconocido")
            print
except KeyboardInterrupt:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
    os.system('clear')
    print
    print("Programa terminado por el usuario")
    print
    exit()
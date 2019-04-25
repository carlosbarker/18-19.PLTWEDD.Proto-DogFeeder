import RPi.GPIO as GPIO

class Motor:
    GPIO.setmode(GPIO.BOARD)

    # Motor 1 pins
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)
    pwm = GPIO.PWM(40, 100)
    pwm.start(0)
    
    def move_forward(power):
        GPIO.output(36, True)
        GPIO.output(38, False)
        Motor.pwm.ChangeDutyCycle(power)
        GPIO.output(40, True)
    
    def move_back(power):
        GPIO.output(36, False)
        GPIO.output(38, True)
        Motor.pwm.ChangeDutyCycle(power)
        GPIO.output(40, True)
    
    def stop():
        GPIO.output(40, False)
        Motor.pwm.stop()
        GPIO.cleanup()
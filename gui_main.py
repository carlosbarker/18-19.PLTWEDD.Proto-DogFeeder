from guizero import App, PushButton, Box, Text, Window, TextBox, Combo
import sys, os
import RPi.GPIO as GPIO
import time

class GlobalVariables:
    dog_name = " "
    dog_size = 0 #1 = Toy, 2 = Small, 3 = Medium, 4 = Large
    first_meal_time = " "
    second_meal_time = " "
    foodres_level = 0 #0-100 (percentage) food in food reservoir
    waterres_level = 0 #0-100 (percentage) food in water reservoir
    waterplt_level = 0 #0-100 (percentage) food in water plate
    foodplt_pos_state = 0 #0 = Closed, 1 = Open/Ejected
    autorefill_percent = 50 #25 or 50% level at which water plate is refilled back to 100%
    
class Motor:
    #PIN 17 AND 22 IS LEFT 2 PINS ON L293N
    #PIN 23 AND 24 IS RIGHT 2 PINS ON L293N
    
    def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
    
    def food_plate_out(duration):
        Motor.init()
        GPIO.output(17, False)
        GPIO.output(22, True)
        GPIO.output(23, False)
        GPIO.output(24, False)
        time.sleep(duration)
        GPIO.cleanup()
        
    def food_plate_in(duration):
        Motor.init()
        GPIO.output(17, True)
        GPIO.output(22, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
        time.sleep(duration)
        GPIO.cleanup()
    
    def water_pump_forward(duration):
        Motor.init()
        GPIO.output(17, False)
        GPIO.output(22, False)
        GPIO.output(23, False)
        GPIO.output(24, True)
        time.sleep(duration)
        GPIO.cleanup()
    
    def water_pump_reverse(duration):
        Motor.init()
        GPIO.output(17, False)
        GPIO.output(22, False)
        GPIO.output(23, True)
        GPIO.output(24, False)
        time.sleep(duration)
        GPIO.cleanup()
        
class Servo:
    #STILL NEED TO FIGURE OUT DUTY CYCLE FOR SERVO AND STUFF
    def init():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        p = GPIO.PWM(12, 50)
        p.start(7.5) #7.5 = 90 degrees)
    
    def open_feed():
        init()
        p.ChangeDutyCycle(12.5) #turn towards 180 degrees
        p.stop()
        GPIO.cleanup()
    
    def close_feed():
        init()
        p.ChangeDutyCycle(2.5) #turn towards 0 degrees
        p.stop()
        GPIO.cleanup()

app = App(title="Dog Feeder", width="800", height="480", bg="white")
app.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN

def show_keyboard():
    app.exit_full_screen()
    os.system("florence")
    app.set_full_screen()

def dev_settings():
    def set_auto_refill(selected_value):
        if selected_value == "50%":
            GlobalVariables.autorefill_percent = 50
        if selected_value == "25%":
            GlobalVariables.autorefill_percent = 25
    
    def close_window():
        GlobalVariables.dog_name = dog_name_textbox.value
        dev_settings_window.destroy()
    
    dev_settings_window=Window(app, height=480, width=600, title="Device Settings", bg="white")
    dev_settings_window.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN
    title_box = Box(dev_settings_window, align="top", width="fill", border=False)
    title = Text(dev_settings_window, text="Device Settings", size=24, font="Arial")
    dog_name_box = Box(dev_settings_window, align="top", border=False)
    spacer_6 = Text(dog_name_box, text=" ", size=20)
    dog_name_text = Text(dog_name_box, align="left", text="Dog Name: ", font="arial", size=14)
    dog_name_textbox = TextBox(dog_name_box, align="left", width=15)
    
    waterplt_refill_box = Box(dev_settings_window, align="top", border=False)
    spacer_14 = Text(waterplt_refill_box, text=" ", size=8)
    auto_refill_text = Text(waterplt_refill_box, align="left", text="Auto-Refill Water Plate at: ", font="Arial", size="14")
    auto_refill_combo = Combo(waterplt_refill_box, align="left", options=["", "50%", "25%"], command=set_auto_refill)
    
    menu_box = Box(dev_settings_window, align="bottom", width="fill", border=False)
    close_button = PushButton(menu_box, command=close_window, text="Close", align="right")
    keyboard_button = PushButton(menu_box, command=show_keyboard, text="On-Screen Keyboard", align="right")
    
def schedule_amount():
    def show_food_amount(selected_value):
        if selected_value == "Toy":
            GlobalVariables.dog_size = 1
            final_food_amount.clear()
            final_food_amount.append("Food amount to be fed daily: 1/2 cup")
            warning_text.clear()
        if selected_value == "Small":
            GlobalVariables.dog_size = 2
            final_food_amount.clear()
            final_food_amount.append("Food amount to be fed daily: 1 cup")
            warning_text.clear()
        if selected_value == "Medium":
            GlobalVariables.dog_size = 3
            final_food_amount.clear()
            final_food_amount.append("Food amount to be fed daily: 2 1/4 cups")
            warning_text.clear()
            warning_text.append("WARNING: Device is not designed for dogs this size!")
        if selected_value == "Large":
            GlobalVariables.dog_size = 4
            final_food_amount.clear()
            final_food_amount.append("Food amount to be fed daily: 4 1/4 cups")
            warning_text.clear()
            warning_text.append("WARNING: Device is not designed for dogs this size!")
            
    def close_window():
        GlobalVariables.first_meal_time = first_meal_time_textbox.value
        GlobalVariables.second_meal_time = second_meal_time_textbox.value
        schedule_window.destroy()
    
    schedule_window=Window(app, height=480, width=600, title="Schedule", bg="white")
    schedule_window.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN
    title_box = Box(schedule_window, align="top", width="fill", border=True)
    title = Text(schedule_window, text="Schedule", size=24, font="Arial")
    number_meals_notice = Text(schedule_window, text="2 MEALS PER DAY FOR AN ADULT DOG", font="Arial", size=14)
    first_meal_box = Box(schedule_window, align="top", border=False)
    spacer_1 = Text(first_meal_box, text=" ", size=20)
    format_notice = Text(first_meal_box, text="(24-hour format)", font="Arial", size=10)
    first_meal_time_text = Text(first_meal_box, align="left", text="Time of first meal: ", font="Arial", size=14)
    first_meal_time_textbox = TextBox(first_meal_box, align="left", width=15)
    second_meal_box = Box(schedule_window, align="top", border=False)
    spacer_2 = Text(second_meal_box, text=" ", size=10)
    second_meal_time_text = Text(second_meal_box, align="left", text="Time of second meal: ", font="Arial", size=14)
    second_meal_time_textbox = TextBox(second_meal_box, align="left", width=15) 
    title2_box = Box(schedule_window, align="top", border=False)
    spacer_3 = Text(title2_box, text=" ", size=20)
    title2 = Text(title2_box, text="Amount", size=20, font="Arial")
    dog_size_box = Box(schedule_window, align="top", border=False)
    dog_size_text = Text(dog_size_box, align="left", text="Size of dog: ", font="Arial", size=14)
    dog_size_select = Combo(dog_size_box, align="left", options=["", "Toy", "Small", "Medium", "Large"], command=show_food_amount)
    food_amount_box = Box(schedule_window, align="top", border=False)
    spacer_4 = Text(food_amount_box, text=" ", size=10)
    final_food_amount = Text(food_amount_box, align="bottom", text="", font="Arial", size=14)
    warning_box = Box(schedule_window, align="top", border=False)
    warning_text = Text(warning_box, align="left", text=" ", font="Arial", size=16, color="red")
    
    menu_box = Box(schedule_window, align="bottom", width="fill", border=False)
    close_button = PushButton(menu_box, command=close_window, text="Close", align="right")
    keyboard_button = PushButton(menu_box, command=show_keyboard, text="On-Screen Keyboard", align="right")

def restart_prompt(): # FULL SCREEN NOT NEEDED FOR THIS WINDOW!
    restart_window = Window(app, height=60, width=450, title="Restart", bg="white")
    text = Text(restart_window, text="Would you like to restart the entire system or just the interface?", align="top")
    restart_device_button = PushButton(restart_window, command=restart_device, text="Restart Device", align="left")
    restart_interface_button = PushButton(restart_window, command=restart_interface, text="Restart Interface", align="right")

def restart_interface():
    os.execl(sys.executable, sys.executable, * sys.argv)
    app.destroy()
    quit()

def restart_device():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output=process.communicate()[0]
    print(output)
    
def quit_function():
    app.destroy()
    os.system("sudo shutdown -h now")
    quit()
    
def update_home(): #SECTION IS ALSO RESPONSIBLE FOR EVENT TRIGGERS LIKE A FEEDING SESSION
    #Dog Name Section
    dog_name.value = "Dog Name: " + GlobalVariables.dog_name
    
    #Dog Size Section
    if GlobalVariables.dog_size == 0:
        home_dog_size.clear()
        home_dog_size.text_color = "red"
        home_dog_size.size = 18
        home_dog_size.append("POWER WAS LOST! RECONFIGURE SETTINGS ASAP.")
    if GlobalVariables.dog_size == 1:
        home_dog_size.clear()
        home_dog_size.text_color = "black"
        home_dog_size.size = 14
        home_dog_size.append("Dog Size: Toy")
    if GlobalVariables.dog_size == 2:
        home_dog_size.clear()
        home_dog_size.text_color = "black"
        home_dog_size.size = 14
        home_dog_size.append("Dog Size: Small")
    if GlobalVariables.dog_size == 3:
        home_dog_size.clear()
        home_dog_size.text_color = "black"
        home_dog_size.size = 14
        home_dog_size.append("Dog Size: Medium")
    if GlobalVariables.dog_size == 4:
        home_dog_size.text_color = "black"
        home_dog_size.size = 14
        home_dog_size.clear()
        home_dog_size.append("Dog Size: Large")
        
    #Food Amount Section
    if GlobalVariables.dog_size == 1:
        daily_food_amount.clear()
        daily_food_amount.append("Food amount to be fed daily: 1/2 cup")
        food_warning.clear()
    if GlobalVariables.dog_size == 2:
        daily_food_amount.clear()
        daily_food_amount.append("Food amount to be fed daily: 1 cup")
        food_warning.clear()
    if GlobalVariables.dog_size == 3:
        daily_food_amount.clear()
        daily_food_amount.append("Food amount to be fed daily: 2 1/4 cups")
        food_warning.clear()
        food_warning.append("WARNING: Device is not designed for dogs this size!")
    if GlobalVariables.dog_size == 4:
        daily_food_amount.clear()
        daily_food_amount.append("Food amount to be fed daily: 4 1/4 cups")
        food_warning.clear()
        food_warning.append("WARNING: Device is not designed for dogs this size!")
        
    #Meal Times Section
    first_meal_time.value = "First Meal Time: " + GlobalVariables.first_meal_time
    second_meal_time.value = "Second Meal Time: " + GlobalVariables.second_meal_time
    
    #Food and Water Levels Section
    foodres_level.value = "Food Reservoir Level: " + str(GlobalVariables.foodres_level) + "%"
    waterres_level.value = "Water Reservoir Level: " + str(GlobalVariables.waterres_level) + "%"
    waterplt_level.value = "Water Plate Level: " + str(GlobalVariables.waterplt_level) + "%"
    
    home_dog_size.after(250, update_home) #ULTIMATE RECURSIVE CALL TO UPDATE EVERYTHING. BASED ON DOG SIZE TEXT.
    
title_box = Box(app, align="top", width="fill", border=False)
title = Text(title_box, text="Home", size=24, font="Arial")

dog_name_box = Box(app, align="top", width="fill", border=False)
spacer_5 = Text(dog_name_box, text=" ", size=8)
dog_name = Text(dog_name_box, font="Arial", size=14)

dog_size_box = Box(app, align="top", width="fill", border=False)
home_dog_size = Text(dog_size_box, font="Arial", size=14)
daily_food_amount = Text(dog_size_box, font="Arial", size=14)
food_warning = Text(dog_size_box, font="Arial", size=14, color="red")

meal_times_box = Box(app, align="top", width="fill", border=False)
spacer_7 = Text(meal_times_box, text=" ", size=8)
first_meal_time = Text(meal_times_box, font="Arial", size=14)
second_meal_time = Text(meal_times_box, font="Arial", size=14)
format_notice = Text(meal_times_box, text="(24-hour format)", font="Arial", size=10)

fw_levels_box = Box(app, align="top", border=False)
spacer_9 = Text(fw_levels_box, text=" ", size=8)
foodres_level = Text(fw_levels_box, font="Arial", size=14)
waterres_level = Text(fw_levels_box, align="left", font="Arial", size=14)
spacer_10 = Text(fw_levels_box, align="left", text="      ", size=14)
waterplt_level = Text(fw_levels_box, align="left", font="Arial", size=14)

home_dog_size.after(250, update_home) #HOME MASSIVE UPDATE

def eject_food_plate():
    if GlobalVariables.foodplt_pos_state == 1:
        return

def fill_food_plate():
    return None

def close_food_plate():
    if GlobalVariables.foodplt_pos_state == 0:
        return

#INSERT EJECT TRAY BUTTON ABOVE MENU BAR
eject_box = Box(app, align="top", border=False)
spacer_11 = Text(eject_box, text=" ", size=20)
eject_food_plate_button = PushButton(eject_box, align="left", text="Eject Food Plate", command=eject_food_plate)
spacer_12 = Text(eject_box, align="left", text="   ", size=14)
fill_food_plate_button = PushButton(eject_box, align="left", text="Fill Food Plate", command=fill_food_plate)
spacer_13 = Text(eject_box, align="left", text="   ", size=14)
close_food_plate_button = PushButton(eject_box, align="left", text="Close Food Plate", command=close_food_plate)

menu_box = Box(app, align="bottom", width="fill", border=False)
exit_button = PushButton(menu_box, command=quit_function, text="Exit", width=10, align="right")
restart_button = PushButton(menu_box, command=restart_prompt, text="Restart", width=10, align="right")
dev_settings_button = PushButton(menu_box, command=dev_settings, text="Device Settings", width=15, align="right")
schedule_amount_button = PushButton(menu_box, command=schedule_amount, text="Schedule/Amount", width=15, align="right")
keyboard_button = PushButton(menu_box, command=show_keyboard, text="On-Screen Keyboard", align="right")

app.display()

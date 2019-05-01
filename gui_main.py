from guizero import App, PushButton, Box, Text, Window, TextBox, Combo
import sys, os

app = App(title="Dog Feeder", width="800", height="480", bg="white")
# app.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN

def show_keyboard():
    os.system("florence")

def dev_settings():
    dev_settings_window=Window(app, height=480, width=800, title="Device Settings", bg="white", layout="grid")
    # dev_settings_window.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN
    
def schedule_amount():
    schedule_window=Window(app, height=480, width=800, title="Schedule", bg="white")
    # schedule_window.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN
    title_box = Box(schedule_window, align="top", width="fill", border=True)
    title = Text(schedule_window, text="Schedule", size=20, font="Arial")
    number_meals_notice = Text(schedule_window, text="2 MEALS PER DAY FOR AN ADULT DOG", font="Arial", size=14)
    first_meal_box = Box(schedule_window, align="top", border=False)
    spacer_1 = Text(first_meal_box, text=" ", size=20)
    first_meal_time_text = Text(first_meal_box, align="left", text="Time of first meal: ", font="Arial", size=14)
    first_meal_time_textbox = TextBox(first_meal_box, align="left", width=15) # MUST SHOW SET TIME AS THE VALUE IN THE BOX!
    second_meal_box = Box(schedule_window, align="top", border=False)
    spacer_2 = Text(second_meal_box, text=" ", size=10)
    second_meal_time_text = Text(second_meal_box, align="left", text="Time of second meal: ", font="Arial", size=14)
    second_meal_time_textbox = TextBox(second_meal_box, align="left", width=15)
    
    title2_box = Box(schedule_window, align="top", border=False)
    spacer_3 = Text(title2_box, text=" ", size=20)
    title2 = Text(title2_box, text="Amount", size=20, font="Arial")
    dog_size_box = Box(schedule_window, align="top", border=False)
    dog_size_text = Text(dog_size_box, align="left", text="Size of dog: ", font="Arial", size=14)
    dog_size_select = Combo(dog_size_box, align="left", options=["Toy", "Small", "Medium", "Large", "Giant"])
    
    menu_box = Box(schedule_window, align="bottom", width="fill", border=True)
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
    quit()
    
title_box = Box(app, align="top", width="fill", border=True)
title = Text(title_box, text="Home", size=20, font="Arial")

menu_box = Box(app, align="bottom", width="fill", border=True)
exit_button = PushButton(menu_box, command=quit_function, text="Exit", width=10, align="right")
restart_button = PushButton(menu_box, command=restart_prompt, text="Restart", width=10, align="right")
dev_settings_button = PushButton(menu_box, command=dev_settings, text="Device Settings", width=15, align="right")
schedule_amount_button = PushButton(menu_box, command=schedule_amount, text="Schedule/Amount", width=15, align="right")
keyboard_button = PushButton(menu_box, command=show_keyboard, text="On-Screen Keyboard", align="right")

app.display()

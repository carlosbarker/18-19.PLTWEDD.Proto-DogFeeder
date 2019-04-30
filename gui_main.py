from guizero import App, PushButton, Box, Text, Window
import sys, os

app = App(title="Dog Feeder", layout="grid", width="800", height="480", bg="white")
# app.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN


def settings():
    settings_window=Window(app, height=480, width=800, title="Settings", bg="white", layout="grid")
    # settings_window.set_full_screen() # WILL USE THIS WHEN I HAVE SCREEN
    text = Text(settings_window, text="Schedule", align="top", size=16, grid=[0, 300])
    

def restart_prompt(): # FULL SCREEN NOT NEEDED FOR THIS WINDOW!
    restart_window = Window(app, height=100, width=450, title="Restart", bg="white")
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
    
menu_box = Box(app, layout="grid", grid=[0, 0], width=100, height=480)
settings_button = PushButton(menu_box, command=settings, text="Settings", grid=[0, 0], width=10)
restart_button = PushButton(menu_box, command=restart_prompt, text="Restart", grid=[0, 1], width=10)
exit_button = PushButton(menu_box, command=quit_function, text="Exit", grid=[0, 2], width=10)

home_box = Box(app, layout="grid", grid=[1, 0])
home_title = Text(home_box, text="Home", size=16, font="Arial", grid=[1, 5])

app.display()

from guizero import App, PushButton, Box, Text, Window

app = App(title="Dog Feeder", layout="grid", width="800", height="480", bg="white")
# app.set_full_screen() WILL USE THIS WHEN I HAVE SCREEN


def settings():
    return ''


def restart_prompt():
    restart_window = Window(app, height=100, width=500)
    text = Text(restart_window, text="Would you like to restart the entire system or just the interface?")
    restart_device_button = PushButton(restart_window, command=restart_device, text="Restart Device")
    restart_interface_button = PushButton(restart_window, command=restart_interface, text="Restart Interface")

def restart_interface():
    return ''

def restart_device():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output=process.communicate()[0]
    print(output)

menu_box = Box(app, layout="grid", grid=[0, 0], width=100, height=480)
settings_button = PushButton(menu_box, command=settings, text="Settings", grid=[0, 0], width=10)
restart_button = PushButton(menu_box, command=restart_prompt, text="Restart", grid=[0, 1], width=10)

home_box = Box(app, layout="grid", grid=[1, 0])
home_title = Text(home_box, text="Home", size=16, font="Arial")

app.display()

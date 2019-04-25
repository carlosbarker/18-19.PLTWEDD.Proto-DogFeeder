from guizero import App, PushButton, Box, Text

app = App(title="Dog Feeder", layout="grid", width="640", height="480", bg="white")
# app.set_full_screen() WILL USE THIS WHEN I HAVE SCREEN


def settings():
    return ''


def restart_prompt():
    return ''


menu_box = Box(app, layout="grid", grid=[0, 0], width=100, height=480)
settings_button = PushButton(menu_box, command=settings, text="Settings", grid=[0, 0], width=10)
restart_button = PushButton(menu_box, command=restart_prompt, text="Restart", grid=[0, 1], width=10)

home_box = Box(app, layout="grid", grid=[1, 0])
home_title = Text(home_box, text="Home", size=16, font="Arial")

app.display()

def on_pin_pressed_p0():
    basic.show_number(randint(0, 100))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p2():
    basic.show_number(100)
    basic.show_string("You found the cheat in the system!")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

basic.show_string("Love Meter")

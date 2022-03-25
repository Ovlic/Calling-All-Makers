input.onPinPressed(TouchPin.P0, function () {
    basic.showNumber(randint(0, 100))
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showNumber(100)
    basic.showString("You found the cheat in the system!")
})
basic.showString("Love Meter")

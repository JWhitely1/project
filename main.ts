let servoDegree = 0
while (servoDegree <= 180) {
    pins.servoWritePin(AnalogPin.P0, servoDegree)
    servoDegree += 1
    basic.pause(50)
    if (input.buttonIsPressed(Button.A)) {
        servoDegree = 0
        pins.servoWritePin(AnalogPin.P0, servoDegree)
        basic.pause(1000)
        basic.clearScreen()
    }
}

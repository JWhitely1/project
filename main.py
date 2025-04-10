def lightRow(rowValue: number):
    for i in range(5):
        led.plot(i, rowValue)
distance = 0

def on_forever():
    global distance
    basic.clear_screen()
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.INCHES)
    if distance >= 18 and distance < 20:
        lightRow(0)
    elif distance >= 16 and distance < 18:
        lightRow(1)
    elif distance >= 14 and distance < 16:
        lightRow(2)
    elif distance >= 12 and distance < 14:
        lightRow(3)
    elif distance < 12:
        lightRow(4)
basic.forever(on_forever)

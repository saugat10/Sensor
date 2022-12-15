from sense_hat import SenseHat

sense = SenseHat()


def humidity_check():
    humidity = sense.humidity
    return humidity

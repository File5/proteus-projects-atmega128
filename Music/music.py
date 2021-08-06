CLOCK_IN_SEC = 15625
CLOCK_IN_SEC = 31250
CLOCK_IN_SEC = 12500
PRESCALER = 64

def millis(x):
    return int(round(x * CLOCK_IN_SEC / 1000.0)) - 1

def herz(x):
    return int(round(CLOCK_IN_SEC / x)) - 1

if __name__ == "__main__":
    print(millis(1))
    print(herz(470))

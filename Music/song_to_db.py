from music import millis, herz

fout = open("music.txt", "w")

def tone(pin, frequency, duration):
    d = millis(duration)
    dH = d // 256
    dL = d % 256
    print(hex(dH), hex(dL), hex(herz(frequency)), sep=',', end=',', file=fout)

def delay(duration):
    d = millis(duration)
    dH = d // 256
    dL = d % 256
    print(hex(dH), hex(dL), hex(0), sep=',', end=',', file=fout)


tonePin = 11;
tone(tonePin, 1244, 156.2499375);

delay(173.611041667);

tone(tonePin, 1479, 624.99975);

delay(694.444166667);

delay(520.833125);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 1244, 624.99975);

delay(694.444166667);

delay(520.833125);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 1864, 624.99975);

delay(694.444166667);

delay(520.833125);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 234.37490625);

delay(260.4165625);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(260.4165625);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 234.37490625);

delay(260.4165625);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

delay(260.4165625);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1864, 234.37490625);

delay(260.4165625);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

delay(260.4165625);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 234.37490625);

delay(260.4165625);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 311, 156.2499375);

delay(173.611041667);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 234.37490625);

delay(260.4165625);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 246, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 207, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 156.2499375);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1864, 234.37490625);

delay(260.4165625);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 246, 78.12496875);

delay(86.8055208333);

delay(173.611041667);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 369, 78.12496875);

delay(86.8055208333);

tone(tonePin, 155, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 77, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 155, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 65, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 369, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1244, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 92, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 123, 78.12496875);

delay(86.8055208333);

tone(tonePin, 466, 78.12496875);

delay(86.8055208333);

tone(tonePin, 116, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 311, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1479, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);

delay(86.8055208333);

tone(tonePin, 1661, 78.12496875);

delay(86.8055208333);

tone(tonePin, 493, 78.12496875);
fout.close()

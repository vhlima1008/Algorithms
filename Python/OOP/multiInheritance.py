class Device:
    def conect(self):
        print('Conecting to generic device...')

class Printer(Device):
    def conect(self):
        print('Conecting to a Printer using USB...')

    def print(self):
        print('Printing document...')

class Scanner(Device):
    def conect(self):
        print('Conecting to a Scanner using Wi-Fi...')

    def scan(self):
        print('Scanning image...')

class Multifunctional(Printer, Scanner):
    pass

hp = Multifunctional()
hp.print()
hp.scan()

hp.conect()
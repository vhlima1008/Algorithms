class Client:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.account = 0
        self.extract = []

    def profile(self):
        print('Name:',self.name,'\n','E-mail:',self.email,'\n','Age:',self.age,'\n','Balance:',self.account,'\n',)

    def deposit(self, value):
        self.value = value
        self.account += value
        self.extract.append(value)

    def withdraw(self, value):
        self.value = value
        if float(self.account) - float(value) >= 0:
            self.account -= value
            self.extract.append(-value)
        else:
            print('ALERT! WITHDRAW:',self.value,'BALANCE:',self.account)
            self.extract.append(f'Refused {self.value}')
    
    def balance(self):
        print('BALANCE:',self.account,'\n')
    
    def extract(self):
        print('EXTRACT:',self.extract,'\n')

    
client_1 = Client('Victor', 'vhlima1008@gmail.com', 19)


while True:
    try:
        value = float(input(f'Desposit a value {client_1.name}: '))

        client_1.deposit(value)
        client_1.balance()

        value = float(input(f'Withdraw a value {client_1.name}: '))

        client_1.withdraw(value)
        client_1.balance()

    except ValueError:
        print('Ops! Wrong value.')
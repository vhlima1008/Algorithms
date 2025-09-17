class Client:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.account = 0
        self.extract = []

    def profile(self):
        print('\nProfile:\n Name:',self.name,'\n','E-mail:',self.email,'\n','Age:',self.age,'\n','Balance:',self.account,'\n',)

    def deposit(self, value):
        self.value = value
        self.account += value
        self.extract.append(f'Deposited: {value}')

    def withdraw(self, value):
        self.value = value
        if float(self.account) - float(value) >= 0:
            self.account -= value
            self.extract.append(f'Withdrawed: {value}')
        else:
            print('ALERT! WITHDRAW:',self.value,'BALANCE:',self.account)
            self.extract.append(f'Refused: {value}')
    
    def balance(self):
        print('BALANCE:',self.account,'\n')
    
    def extractAcc(self):
        for i in self.extract:
            print(i)

    
client_1 = Client('Victor', 'vhlima1008@gmail.com', 19)


while True:
    try:
        print('\n',f'Hi, {client_1.name}!','\n\n','1 - Profile','\n','2 - Deposit','\n','3 - Withdraw','\n','4 - Balance','\n','5 - Extract','\n','6 - Exit','\n')
        service = int(input('Service: '))

        if service == 1:
            client_1.profile()
        elif service == 2:
            print()
            value = float(input(f'Desposit a value {client_1.name}: '))
            client_1.deposit(value)
        elif service == 3:
            print()
            value = float(input(f'Withdraw a value {client_1.name}: '))
            client_1.withdraw(value)
        elif service == 4:
            client_1.balance()
        elif service == 5:
            client_1.extractAcc()
        elif service == 6:
            break
        else: 
            print('Invalid!')
        

    except ValueError:
        print('Ops! Wrong value.')
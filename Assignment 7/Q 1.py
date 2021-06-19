class Bank:
    def interest(self):
        return "Bank Interset is "+str(0)

class SBI(Bank):
    def interest(self):
        return "Bank Interset of SBI is "+str(2.5)

class PNB(Bank):
    def interest(self):
        return "Bank Interset of PNB is "+str(4.5)

if __name__ == '__main__':
    bank = Bank()
    bank1 = SBI()
    bank2 = PNB()

    print(bank.interest())
    print(bank1.interest())
    print(bank2.interest())
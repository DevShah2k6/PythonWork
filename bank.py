from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,name,accno,inital_bal):
        self.name = name
        self.accno =accno
        self.inital_bal = inital_bal
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class HDFC(Bank):
    current_bal =0
    #here hdfc current balance is the intal balance which is intialized here and 
    #name and ll that taken from parent class
    def __init__(self, name, accno, inital_bal):
        super().__init__(name, accno, inital_bal)
        self.current_bal = inital_bal
    def pay(self):
        pass
    def intial_balance(self):
        self.current_bal+=super().inital_bal
    def deposit(self,depo_amt):
        self.depo_amt = depo_amt
        self.current_bal+=depo_amt
    def withdraw(self,with_amt):
        if self.current_bal<with_amt:
            print("you can not with draw")
        else:
         self.current_bal=self.current_bal-with_amt
    def get_balance(self):
        return self.current_bal
    
    def show_details(self):
        return self.name,self.accno,self.current_bal
    


name = input("Enter Name:-")
accno = input("Enter accno:-")
inital_bal = int(input("Enter Inital Balance Amt:-"))
h = HDFC(name,accno,inital_bal)

choice = int(input(("Enter 1(for deposit) 2 (for withdraw) 3(to get details):-")))

if choice==1:
    deposited_amt = int(input("Enter amt to be deposited:-"))
    h.deposit(deposited_amt)
    print(h.get_balance())
elif choice==2:
    with_amt = int(input("Enter Withdraw Amount:-"))
    h.withdraw(with_amt)
    print(h.get_balance())
elif choice==3:
    print("---------------Summary--------------")
    print(h.show_details())

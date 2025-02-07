class Account:
    def __init__(self, owner : str, balance = 0) -> None:
        self.__owner = owner
        self.__balance = balance
    

    def deposit(self, deposit : int) -> None:
        self.__balance += deposit
    

    def withdraw(self, withdraw) -> None:
        if self.__balance < withdraw:
            raise Exception("Сумма превышает баланс")
        else:
            self.__balance-=withdraw
    

    def get_balance(self):
        return self.__balance


    def owner(self):
        return self.__owner

def main():
    koshelek =  Account(owner = input())
    print(f"Здравствуйте {koshelek.owner()}")
    koshelek.deposit(deposit = 5)
    print(koshelek.get_balance())
    koshelek.withdraw(2)
    print(koshelek.get_balance())

if __name__ == "__main__":
    main()


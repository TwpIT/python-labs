class str_handle:
    def __init__(self,string: str) -> None:
        self.__string = string
    
    def getString(self):
        return self.__string
    
    def printString(self):
        print(self.__string.upper())

        
def main():
    string = str_handle(string = input())
    string.printString()

if __name__ == "__main__":
    main()

def fahrenheit_to_centigrade(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def main():
    fahrenheit = int(input("Farenheit: "))
    print(f"centigrade: {fahrenheit_to_centigrade(fahrenheit)}")
if __name__ == "__main__":
    main()

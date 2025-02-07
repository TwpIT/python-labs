def is_it_palindrome(string):
    return string == string[::-1]

def main():
    print(is_it_palindrome(input))

if __name__ == "__main__":
    main()
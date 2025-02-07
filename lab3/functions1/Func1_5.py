import itertools

def all_permutations(string):
    return [''.join(i) for i in itertools.permutations(string)]

def main():
    string = input()
    print(*all_permutations(string))

if __name__ == "__main__":
    main()

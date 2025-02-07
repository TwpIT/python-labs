def gram_to_ounc(grams):
    return 28.3495231 * grams

def main():
    grams = int(input("Grams: "))
    print(f"Ounces: {gram_to_ounc(grams)}")

if __name__ == "__main__":
    main()
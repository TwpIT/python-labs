def solve(heads, legs):
    return [int((legs - heads * 2) / 2), int((heads - (legs - heads * 2) / 2))]

def main():
    print(*solve(int(input()), int(input())))

if __name__ == "__main__":
    main()
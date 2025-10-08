def main():
    numbers =[]
    for _ in range(5):
        num = float(input("Enter a numbers: "))
        numbers.append(num)
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    print(f"Numbers: {numbers}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Average: {average:.2f}")
    print(f"Sorted: {sorted(numbers)}")
if __name__ =="__main__":
    main()

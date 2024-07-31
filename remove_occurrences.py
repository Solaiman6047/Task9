def remove_occurrences(numbers,number):
    return [i for i in numbers if i != number]
numbers=list(eval(input("Enter numbers: ")))
number=int(input("Enter number: "))
print(remove_occurrences(numbers,number))
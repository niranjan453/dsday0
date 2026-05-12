def add_numbers(a, b):
    return a + b


def get_middle_value(lst):
    middle_index = len(lst) // 2
    return middle_index, lst[middle_index]


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lst = list(map(int, input("Enter list elements separated by space: ").split()))

total = add_numbers(num1, num2)

middle_index, middle_value = get_middle_value(lst)

print("Sum =", total)
print("Middle Value =", middle_value)

if total > middle_value:
    result = set(lst[:middle_index + 1])
    print("Set:", result)

elif total == middle_value:
    result = {middle_index: middle_value}
    print("Dictionary:", result)

else:
    result = tuple(lst[middle_index + 1:])
    print("Tuple:", result)

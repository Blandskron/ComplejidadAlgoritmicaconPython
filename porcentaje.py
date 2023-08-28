def calculate_percentage(value, maximum):
    percentage = (value / maximum) * 100
    return percentage

value = float(input("Enter the value: "))
maximum = float(input("Enter the maximum value: "))

percentage = calculate_percentage(value, maximum)
print(f"{value} is {percentage:.2f}% of {maximum}")

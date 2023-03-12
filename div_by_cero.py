"""
Handling 0 division error (Exception)
"""

try:
    numbers = [0, 1, 2, 3, 4, 5]
    number1 = numbers[5]
    nubmer2 = numbers[0]
    result = number1 / nubmer2

except Exception as error:
    print("Operation error:", error)

else:
    print("{} / {} = {}".format(number1, nubmer2, result))

finally:
    print("\nCode has finished")

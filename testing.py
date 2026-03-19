def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

nums = [10, 20, 30, 40]
print("Average is:", calculate_average(nums))

# Buggy part below
def find_max(numbers):
    max_num = 0   # BUG: assumes all numbers are positive
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

nums2 = [-5, -2, -9, -1]
print("Max is:", find_max(nums2))

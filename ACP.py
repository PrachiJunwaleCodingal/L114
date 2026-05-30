# 1. Must be greater than 0
# 2. Must be a power of 2: n & (n - 1) == 0
# 3. The set bit must be at a position divisible by 3: (n - 1) % 7 == 0

def is_power_of_eight(n):
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 7 == 0

num = 64
if is_power_of_eight(num):
    print(f"{num} is a power of 8")
else:
    print(f"{num} is not a power of 8")

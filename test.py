def function(a, b):
    total = 0
    if a % b != 0 and b % a != 0:
        total += a * b
    return total
print(function(3, 4))

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "-> Even")
    else:
        print(num, "-> Odd")

n = int(input("Enter n: "))

for i in range(1, n + 1):
    check_even_odd(i)
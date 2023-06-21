def print_digit_sum(n):
    if n < 10:
        print(n)
    else:
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        print(sum)
n = int(input())
print_digit_sum(n)
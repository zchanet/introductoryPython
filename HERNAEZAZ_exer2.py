# Application of learnings in iterative statements through a programming exercise in Python:

n = int(input("Enter an integer: \n"))
m = int(input("Enter another integer: \n"))

sum_of_even = 0
sum_of_odd = 0

while n != m:
    if n < m:
        for number in range(n, m+1):
            if number % 2 == 0:
                sum_of_even = sum_of_even + number
            else:
                sum_of_odd = sum_of_odd + number
        print("The sum of even numbers from", n, "to", m, "is", sum_of_even)
        print("The sum of odd numbers from", n, "to", m, "is", sum_of_odd)
        break
    elif n > m:
        for number in range(m, n+1):
            if number % 2 == 0:
                sum_of_even = sum_of_even + number
            else:
                sum_of_odd = sum_of_odd + number
        print("The sum of even numbers from", m, "to", n, "is", sum_of_even)
        print("The sum of odd numbers from", m, "to", n, "is", sum_of_odd)
        break
else:
    print("The two integers cannot be equal.")

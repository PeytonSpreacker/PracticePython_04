ran = range(2,101)
div = list()

# asks user for a number to query for divisors between 2 and 100
num = int(input('Enter a number to query: '))
# searches for the divisors in the applied range and appends divisors to the list
for i in ran:
    if num % i == 0:
        div.append(i)
    else:
        continue
# print results
print(div)
def fun1(n):
    return n*(n+1)/2
print(fun1(3))
# time complexity equals to 1
# time taken will remian constant for any n

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(fun2(3))
# time complexity equals to n
# time taken will increase linear for every n

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
    return sum
print(fun3(3))
# time complexity will be n^2
# the time taken will increase quadrity for every n
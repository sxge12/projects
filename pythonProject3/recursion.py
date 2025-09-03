def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)

#print(sum_n(5))

def fibo(e):
    if e == 1:
        return 1
    elif e == 0:
        return 0
    else:
        return fibo(e-1) + fibo(e-2)

#print(fibo(6))

def baseexp(base, exp):
    if exp == 0:
        return 1
    base * baseexp(base,exp - 1)



#print(baseexp(2,3))

def binary_search(arr,target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid-1, high)




arrr = [1, 2, 3, 4, 5]
print(binary_search(arrr, 3, 0, len(arrr) - 1))


def print_binary_strings(n , current=""):
    
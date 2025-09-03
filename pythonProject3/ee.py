class BankAccount:
  def __init__(self, name, initAmt):
   self.name = name
   self.balance = initAmt

  def deposit(self, amt):
   self.balance += amt

  def withdraw(self, amt):
   self.balance -= amt

p1 = BankAccount("blair", 500)
p2 = BankAccount("sammy", 200)

def accounttransfer(person1, person2, trnsframt):
  if person1.balance > 0 and trnsframt:
   person2.deposit(trnsframt)
   person1.withdraw(trnsframt)
  return person2.balance, person1.balance

#print(accounttransfer(p1, p2,50))


def binary_search(arr, item):
    lo = 0
    hi = len(arr) - 1
    while hi >= lo:
        mid = ( lo + hi ) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

#print(binary_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13], 11))

def recursive_binary_search(arr, item, lo , hi):

     mid = (lo + hi)//2
     if lo > hi:
         return -1

     if arr[mid] == item:
         return mid
     elif arr[mid] > item:
         recursive_binary_search(arr, item, lo, mid - 1)
     elif arr[mid] < item:
         recursive_binary_search(arr, item, mid + 1, hi)






def bubble_search(arr):
    indexing_length  = len(arr)-1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                is_sorted = True
                arr[i],  arr[i + 1] = arr[i+1] , arr[i]
                print(arr)
                is_sorted = False
    return arr


#print(bubble_search([1,4,5,6,2,8,3,6]))





def selection_sort(arr):
    indexinglength = range(0 , len(arr) -1 )
    for i in indexinglength:
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value], arr[i] = arr[i] , arr[min_value]
    return arr

print(selection_sort([1,2,4,7,9,2,4,5,6]))
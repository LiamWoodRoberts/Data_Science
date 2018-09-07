#Another Hackerrank Challenge, creating a simple Bubble sort Algorithm and printing the number of steps
#As well as the first and last element of the array

def BubbleSort(a):
    count = 0
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                count +=1
    print('Array is sorted in',count, 'swaps.')
    print('First Element:',a[0])
    print('Last Element:',a[n-1])
    return

array = [6,4,1]
BubbleSort(array)

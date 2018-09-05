#More Hackerrank stuff, creates a function that shifts an
#array n places to the left

def leftrotation(array,rotations):
    for i in range(rotations):
        new_array  = [0]*len(array)
        for j in range(len(array)):
            if j == len(array)-1:
                new_array[j] = array[0]
            else:
                new_array[j] = array[j+1]
        array = new_array
    return array

array = [1,2,3,4,5]
shifted_array = leftrotation(array,4)
print(shifted_array)

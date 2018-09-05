#Previous rotations function didnt scale well to higher rotations
#This is a "smarter" function that determines the actual shift
#before blindly looping through the number of rotations

def fast_left_rotation(array,rotations):
    new_array = [0]*len(array)
    shift = rotations%len(array)
    for j in range(len(array)):
        if j == len(array)-shift:
            new_array[j] = array[shift-1]
        else:
            new_array[j] = array[j+shift]
    return new_array

array = [1,2,3,4,5]
shifted = fast_left_rotation(array,31)
print(shifted)

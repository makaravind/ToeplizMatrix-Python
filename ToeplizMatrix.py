# representing in 1D for better search and performance
#input = [6, 7, 8, 9, 2, 4, 6, 7, 8, 9, 1, 4, 6, 7, 8, 0, 1, 4, 6, 7]
input = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# input = [6]

# assuming a sqmat always
size = 5

def isToeplizMatrix(input_matrix, size):

    #initializing with first row
    init_pattern = input[:size - 1]
    observed_pattern = []

    #looping through row wise in 1D list
    for i in range(size, len(input), size):
        #print(input[i: i+size])
        observed_pattern = input[i: i + size] #cosidering all the elements in the row
        to_append_ele = observed_pattern[0] #taking the first ele away from the pattern
        observed_pattern == observed_pattern[1:]
        if init_pattern == observed_pattern: #checking if the toepliz nature holds
            observed_pattern.insert(0, to_append_ele)
            init_pattern = observed_pattern[:len(observed_pattern)-1] #reading the init_pattern for next round
        else:
            return False
    return True


if(isToeplizMatrix(input, size)):
    print("the given input is toepliz matrix")
else:
    print("the given input is not toepliz matrix")



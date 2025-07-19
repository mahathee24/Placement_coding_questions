#how to find the cube of the number 
def cube_of_number(n):
    #Input: n = 27
#Output: true
#Explanation: 27 = 33
    return round(n ** (1/3)) ** 3 == n

# Example usage
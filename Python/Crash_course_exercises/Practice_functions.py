#Practice 1
# Finding the max of three numbers.
def maxfunc(*num):
    """Displays the maximum of three numbers"""
    result = max(num)
    return result
max_num = maxfunc(23,-42,12)     
print(f"\nThe Maximum number is: {max_num}")  

#Practice 2
# Suming all the numbers in a list
def sumfunc(numList):
    """Iterates over the list, sums up all the numbers and store them in a variable called total"""
    total = 0
    for num in numList:
        total += num
    return total

sampleList = [2,4,6,8,10]    
result = sumfunc(sampleList)
print(f"The total sum is: {result}")

#Practice 3
# Multiplying all the numbers in a list
def mulfunc(num_list):
    """Iterates over the list, multiplies up all the numbers and store them in a variable called total"""
    total = 1
    for num in num_list:
        total *= num
    return total

#sampleList is declared and assigned on line 19
result = mulfunc(sampleList)    
print(f"The total multiplication: {result}")  


#Practice 4
#Reversing a string 
def reversefunc(s_str):
    new_str = ''
    str_index = len(s_str)
    while str_index:
        new_str += s_str[str_index - 1]
        str_index -= 1
    return new_str
    
result = reversefunc("Spotify")
print(result)



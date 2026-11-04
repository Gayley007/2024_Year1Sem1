'''l= int(input("length: " ))
w= int(input("width: " ))
A= (l * w)
print (f"The Area of the Rectangle is: {A}")'''
#TwoSum
def twoSum( nums, target):
    for i in range (len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return([i,j])

#

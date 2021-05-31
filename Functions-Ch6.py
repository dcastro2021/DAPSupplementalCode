#Here is an example of using functions in Python code

#Here is the function code
def square(x):
    y = x * x
    return y


#Here is the root code
v = 3
z = multiply_by_three(v)
print("")
print(z)

#Adding Sentences
print ("Hello, my name is David.")
sentence2 = "Here are some Python algorithms")

# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
print(solution(B)) 
print(solution(C)) 
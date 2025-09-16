# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}





class A:
    def countMultiples(self, nums):
        res = {}
        for i in range(1, 10):
            cnt = 0
            for num in nums:
                if num % i == 0:
                    cnt += 1
            
            res[i] = cnt
        
        return res    
                    
        
# nums  = list(map(int, input("enter the list :").split(",")))
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

obj = A()  
res = obj.countMultiples(nums)
print(res)






###################################################
#### Output
# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}


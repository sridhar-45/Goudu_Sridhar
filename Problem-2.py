# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......




class A:
    def findSeries(self, nums):
        res = []
        for i in range(n):
            res.append(2 * i + 1)
        
        # for val in res:
        #     print(val, end = ", ")
        
        return ", ".join(map(str,res))
        
        

n  = int(input("enter the number :"))
obj = A()  
print(obj.findSeries(n))





#########################################
## Output
# enter the number :4
# 1, 3, 5, 7
    
    

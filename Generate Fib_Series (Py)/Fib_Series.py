def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))


n = int(input("Enter the value of n : ")) 
if n <= 0: 
   print("Please enter a valid integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(FibRecursion(i),end ="")

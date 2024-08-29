
#!/usr/bin/env python3
#test for factorial 

def factorial(number) -> int:
 if number==0 or number==1:
    return 1
 
 elif number<0:
  raise TypeError("Failed")

 else:
    return number*factorial(number-1)  
       




def main():  
   print(f"Factorial: {factorial(5)}") 
   print(f"Factorial: {factorial(4)}")


if __name__ == "__main__":
   main()  
    

 

import math
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     
      
def decimalToBinary(num):  
    
    if(num > 1):  
          
        decimalToBinary(num//2)  
  
      
    print(num%2, end=' ')



 
def decToOctal(n): 
      
     
    octalNum = [0] * 100; 
  
    i = 0; 
    while (n != 0): 
  
       
        octalNum[i] = n % 8; 
        n = int(n / 8); 
        i += 1; 
  
     
    for j in range(i - 1, -1, -1): 
        print(octalNum[j], end = "");





def octalToDecimal(n): 
      
    num = n; 
    dec_value = 0; 
  
     
    base = 1; 
  
    temp = num; 
    while (temp): 
  
         
        last_digit = temp % 10; 
        temp = int(temp / 10); 
  
        
        dec_value += last_digit * base; 
  
        base = base * 8; 
  
    return dec_value;


def decimaltohexadecimal(n):

    hex1 = hex(n)

    print("The equivalent hexadecimal value is: ", hex1)


 
def hexTodecimal(string1):  


    res = "{0:08b}".format(int("1a", 16)) 
  
    binaryToDecimal(int((res)))
while(True):
    print("1.Binary To decimal 2. Decimal to Binary 3.Decimal to Octal 4. Octal to Decimal 5.Decimal to Hexadecimal 6.HexaDecimalToDecimal")
    choice = int(input("To which system do you want to convert?"))
    if choice >=1 and choice <=5:
        number1 = int(input("Enter your choice"))
        if choice == 1:
            binaryToDecimal(number1)
        elif choice == 2:
            decimalToBinary(number1)
        elif choice == 3:
            decToOctal(number1)
        elif choice == 4:
            octalToDecimal(number1)
        elif choice == 5:
            decimaltohexadecimal(number1)
    elif choice == 6:
        string1 = str(input("Enter String to be converted"))
        hexTodecimal(string1)
    print()

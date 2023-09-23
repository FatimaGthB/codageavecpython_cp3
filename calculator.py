
def calculator(num1, num2):
    
    while True:
        print("-----Calculator-----")
        print("1- Addition")
        print("2- subtraction")
        print("3- Multiplication")
        print("4- Division")
        try : 
            
            operation = int(input("operation selection : "))      #user selects an operation to perform
            
        except ValueError:                               #error management   
            print ("Warning: you must enter a  whole number between 1 and 4 ! ")
            continue                        #the loop repeats until the condition to enter an eniter number is met.
        
        try:
                    
            num1 = float(input("enter the first term : "))  #the user enters the terms of his operation
            num2 = float(input("enter the second term : ")) 
            
        except ValueError:                                 
            print ("Warning: you must enter a  number !")
            continue
        
        
        #block of instructions to be executed according to the choice of operation
        if operation == 1 :         
            print("the result is : " , num1+num2)
        elif operation == 2:
            print("the result is : " , num1-num2)
        elif operation == 3:
            print("the result is : " , num1*num2)
        elif operation == 4:
            if num2 != 0 :
                print("the result is : " ,num1/num2 )
            else :
                print("division by zero impossible")
        else:
            print("operator selection impossible")
            
        reponse = input ("would you like to do another calculation? : Y/N ")    #at the end of the operation, the user can choose whether or not to perform another calculation
        if reponse != "Y" and reponse != "N":
            print (input ("CHOOSE Y or N "))                
        elif reponse == "Y": 
            continue            #perform another operation by typing Y  et the loop is executed again 
        else:
            print("Bye !!!")   #exit the calculator
            break       
             

calculator(any,any)  

         
    
   
    
        
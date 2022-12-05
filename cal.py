#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2


#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
import operator
history_List=[]
def select_op(choice):
    operators=["+","-","*","/","%","$","#","?"]
    if (not choice in operators):
        print ("Unrecognized operation")
        return ("$")
    else:
        return(choice)
    
def get_input():
        input_first_number=input("Enter first number: ")
        print(input_first_number)
        input_second_number=""
        try:
            input_first_number=int(input_first_number)
            input_second_number=(input("Enter second number: "))
            print(input_second_number)                
        except:
            
            if input_first_number =="#":
                input_first_number="#"
                input_second_number="#"
            if input_second_number=="#":
                input_second_number="#"
                input_first_number="#"
            if input_first_number =="$":
                input_first_number="$"
                input_second_number="$"
            if input_second_number=="$":
                input_second_number="$"
                input_first_number="$"            
                        
        return (input_first_number,input_second_number)
    
def operation(input_first_operand, input_second_operand,choice):
    if (input_first_operand or input_second_operand)=="S":
        return("$")
    else:
        functions={"+":operator.add,
                   "-":operator.sub,
                   "*":operator.mul,
                   "/":operator.truediv,
                   "^":operator.pow,
                   "%":operator.mod }
        result=functions[choice](input_first_operand,input_second_operand)
        return(result)
    
def History(history,history_List):
    history_List.append(history)
    return(history_List)
    
    
    
    

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print (choice)
  choice=select_op(choice)
  if(choice)== "$":
      #program restaring
      print("Done. Resetting")
      continue
  if(choice)== "#":
      #program ends here
      print("Done. Terminating")
      exit()


  else:
      try:
          if (choice=="?" and len(history_List)==0):
              print ("No past calculations to show")
              continue
          elif(choice=="?" and len(history_List)!=0):
              for i in history_List:
                  print (i)
              continue
          
          
          input_first_operand, input_second_operand=get_input()
          if int(input_second_operand)==0:
              
               print("float division by zero")
               print(float(input_first_operand),"/",0.0,"= None")
          else:
              input_first_operand=float(input_first_operand)
              input_second_operand=float(input_second_operand)
              result=operation(input_first_operand, input_second_operand,(choice))
              history= str(input_first_operand)+" " +str((choice))+ " "+str(input_second_operand)+" = "+ str(result)
              history_List=History(history,history_List)
              print (history)
                                
 
      except:
          if input_second_operand=='#':
              print ("Done. Terminating")
              exit()
          #print("Not a valid number,please enter again")
            #program restaring
          #print("Done. Resetting")
          else:continue
          

      

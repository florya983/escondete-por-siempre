
def check_position(position,matrix)-> str|None:
    if position<1 or position>9:
       print("invalid position😵.Enter a number from 1 to 9.")
       return None
    row=(position-1) // 3
    column=(position-1)%3            
    return matrix[row][column]

def find_frank(attempts,matrix,cellfrank) -> tuple[bool, int]:
    try:
        frank_position=int(input("Where do you think Frank is?\n"))
    except ValueError:
        print("You must enter a number!")
        return False,attempts
    frank_result=check_position(frank_position,matrix)
    if frank_result is None:
        return False,attempts
    if frank_result!=cellfrank:
        attempts+=1
        print(frank_result)
        print("Frank isn't here! Try again!😨\n") 
        return False,attempts  
    if frank_result==cellfrank:    
        print(frank_result)
        print("You found Frank! Now let's find Max! The monster is getting closer!🏃\n")  
        return True,attempts

def find_max(attempts,matrix,cellmax)-> tuple[bool, int]:
    try:
        max_position=int(input("Where is Max?🥺\n"))
    except ValueError:
        print("You must enter a number!")
        return False,attempts
    max_result=check_position(max_position,matrix)
    if max_result is None:
        return False,attempts
    if max_result==cellmax:
        return True,attempts
    if max_result!=cellmax:
        attempts+=1 
        print("Max isn't here yet! Try again!😨\n")
        return False,attempts

    


    


       

    


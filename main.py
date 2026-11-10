
def check_position(position):
    if position<1 or position>9:
       print("invalid position😵.Enter a number from 1 to 9.")
       return None
    row=(position-1) // 3
    column=(position-1)%3            
    return matrix[row][column]
               
  

matrix=[
    ["Steve","Tom","Max"],
    ["john","Michael","Brad"],
    ["Frank","Robbie","George"],
]
cellfrank="Frank"
cellmax="Max"

if __name__ == "__main__":

    attempts=0
    print("""😮‍💨 Escondete por siempre 😮‍💨

   You must find Frank first, then find his friend Max.
   You have six attempts to win the game.
   Good luck! Frank and Max are hiding in different cells.

    [👨‍🦰👨‍🦱👨‍🦳] 
    [👨🧔👱]
    [🧒👦🧔]
    positions:
    1,2,3 
    4,5,6 
    7,8,9
    """)

    victory=False
    while attempts<6 and victory==False:
        frank_position=int(input("Where do you think Frank is?\n"))
        frank_result=check_position(frank_position)
        if frank_result is None:
            continue
        if frank_result!=cellfrank:
             attempts+=1
             print(frank_result)
             print("Frank isn't here! Try again!😨\n")   
        if frank_result==cellfrank:    
            print(frank_result)
            print("You found Frank! Now let's find Max! The monster is getting closer!🏃\n")   
            while attempts<6 and victory==False:
                max_position=int(input("Where is Max?🥺\n"))
                max_result=check_position(max_position)
                if max_result is None:
                    continue
                if max_result==cellmax:
                    victory=True
                    break
                if max_result!=cellmax:
                    attempts+=1 
                    print("Max isn't here yet! Try again!😨\n")
if victory==False:
    print("Game Over!😭") 
else:
    print("Max is here!! Run! you escaped! Congratulations! 🙃🙃🙃")


  



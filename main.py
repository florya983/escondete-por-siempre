
def check_position(position):
    if position<1 or position>9:
       print("invalid position😵")
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
    print("""😮‍💨 Escondete por siempre 😮‍💨"""\n
    You must find Frank and then find his friend Max.🫠\n
    You have six attempts to win the game.😱\n
    Good luck!\n Frank is in one cell and his friend is in another cell🤪 \n
    [👨‍🦰👨‍🦱👨‍🦳] \n
    [👨🧔👱 ]\n 
    [🧒👦🧔]\n 
    positions:\n
    1,2,3\n 
    4,5,6\n 
    7,8,9\n""")

    while attempts<6:
        frank_position=int(input("Where do you think Frank is?\n"))
        frank_result=check_position(frank_position)
        if frank_result is None:
            continue
        if frank_result==cellfrank:    
            print(frank_result)
            print("Frank is here! Let's go to find Max!, monster is close to🏃\n")
            max_position=int(input("Where is Max?🥺\n"))
            max_result=check_position(max_position)
            if max_result is None:
                continue
            if max_result==cellmax:
                print("Max is here!! Run away here, the monster coming for us!!")
                break
            if max_result!=cellmax:
                print("Max isn't here.Try again😨\n")
                attempts+=1
        if frank_result!=cellfrank:
            attempts+=1
            print(frank_result)
            print("Frank isn't here!Try again😨\n")
        
    print("Game Over 😭")



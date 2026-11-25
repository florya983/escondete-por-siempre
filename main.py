
from funciones import check_position
from funciones import find_frank
from funciones import find_max        

matrix=[
    ["Steve","Tom","Max"],
    ["John","Michael","Brad"],
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

    [👨 🧔 👱] 
    [👨 🧔 👱]
    [🧒 👦 🧔]
    positions:
    1,2,3 
    4,5,6 
    7,8,9
    """)

    victory=False
    while attempts<6 and victory==False:
        valfrank,attemptsfrank=find_frank(attempts,matrix,cellfrank)
        attempts=attemptsfrank
        if valfrank:
            while attempts<6 and victory==False:
                valmax,attemptsmax=find_max(attempts,matrix,cellmax)
                attempts=attemptsmax
                if valmax:
                    print("Max is here!! Run! you escaped! Congratulations! 🙃🙃🙃")
                    victory=True
    if attempts==6:
           print("Game over!!")    
            

           
            


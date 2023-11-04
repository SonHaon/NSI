total_distance=0
while total_distance < 45:
    distance = int(input(f"distance actuelle : {total_distance} km\ndistance parcourue (en kilomètre) : "))
    total_distance+=distance
print(f"Félicitations vous avez parcourues plus de 45km ajourd'hui ({total_distance}km)")
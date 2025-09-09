import math
x1, y1 , z1 = 2, 1, 4
x2, y2 , z2 = 3, 1, 0
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
distance = round(distance, 2)
print("The Euclidean distance in 3D is:", distance)
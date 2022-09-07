import math
from turtle import down

point1 = [-53.246907985969685, -505.3958058512147, -168.40981937664958]
point2 = [-53.246907985969685, -505.3958058512147, -168.40981937664958]

phi = 45

def direction_vector(point1, point2):
    if len(point1) == len(point2):
        length = len(point1)
        result = []
        for i in range(length):
            result.append(-point2[i] + point1[i])
        return result

def plane_normal(phi, position): # the position argument specifies the upper or lower mirror
    if position == "down":
        return [0, math.sin(phi * (math.pi / 180)), -math.cos(phi * (math.pi / 180))]
    elif position == "up":
        return [0, -math.sin(phi * (math.pi / 180)), -math.cos(phi * (math.pi / 180))]
    else:
        return 'Error'

def absolute_vector_value(vector):
    if len(vector) == 3:
        return math.sqrt((vector[1])**2 + (vector[0])**2 + (vector[2])**2)

def scalar_product(vector1, vector2):
    sUm = 0
    for i in range(3):
        sUm += vector1[i] * vector2[i]
    return sUm
        
def angle_between_vectors(vector1, vector2):
    if (absolute_vector_value(vector1) == 0 or absolute_vector_value(vector2) == 0):
        print("Zero")
    else:
        return math.acos(scalar_product(vector1, vector2) / (absolute_vector_value(vector1) * absolute_vector_value(vector2))) * (180 / math.pi)

def angle_BeamPlane(point1, point2, phi, position): # position is either a string "down" or "up"
    if (len(point1) and len(point2)) == 3:
        vec1 = direction_vector(point1, point2)
        vec2 = plane_normal(phi, position)
        result = angle_between_vectors(vec1, vec2)
        if result != None:
            return round(result, 3)

# print(round(angle_between_vectors([1, 5, 6], [6, 7, 4]), 3))
print(angle_BeamPlane(point1, point2, phi, down))

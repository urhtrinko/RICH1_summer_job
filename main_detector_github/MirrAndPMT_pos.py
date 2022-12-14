import math
from loop_over_files import replacetext
from loop_over_files import betweentxt
import os

# Python file that changes the tilt of the spherical (mirror 1) and flat (mirror 2) mirrors. The problem
# occurs when trying to move/rotate them, because you are moving the large sphere of which the mirror is
# only a part of. In the following code specificaly functions change_Mirror1/change_Mirror2 you specify
# the angle at which you want to tilit the Mirror 1 or 2 and the code auromaticaly geneates the
# position of the center of the sphere so that the mirror always stays at the same position, which can
# be specified with the parameters z and y, while x is always eaqual to zero.

alpha = 0.08333333333333333 # in radians
r1 = 5001 # in millimeters
def position_Mirror1(phi, z): # input in degrees
    y0 = r1 * math.sin(phi * (math.pi / 180) + alpha)
    d = alpha*r1*math.cos(phi * (math.pi / 180) + alpha)
    d = r1 * (1 - math.cos(phi * (math.pi / 180) + alpha))
    yu = r1*(math.sin(phi*(math.pi/180)) + (math.tan(alpha) * math.cos(phi*math.pi/180)))
    # print("y_0:", -y0, "z_0:", d + z - r1)
    return [-y0, yu, d + z - r1]

r2 = 5003 # in milimeters
def y_position_Mirror2(phi, y):
    y0 = r2 * math.sin(phi*(math.pi / 180))
    return y0 - y
def z_position_Mirror2(phi, z):
    d = r2 * (1 - math.cos(phi*(math.pi / 180)))
    if d > z:
        return -(r2 - (d - z))
    else:
        return -(r2 + (z - d))

# Changing the position of Mirror 1
# here the upper part of the mirror is always at the positon (0, 0, z). With the phi parameter you can
# rotate it around this point.
# p.s. The code automaticaly corrects the main_detector3.tg file and runs the main_detector macro.

def change_Mirror1(D_phi1, U_phi1, z1): # inputa angle for lower (D_phi) and upper spherical mirror 
    filename = "geometries/main_detector3.tg"# (U_phi) in degrees and position in millimeters.
    new_positionD = position_Mirror1(D_phi1, z1)
    new_positionU = position_Mirror1(U_phi1, z1)
    input_listD = [betweentxt(filename, 'rX00_3a', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_3a", "//")[0]]
    output_listD = ['rX00_3a ' + str(D_phi1) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_3a 0 ' + str(new_positionD[0]) + ' ' + str(new_positionD[2]) + ' //']
    input_listU = [betweentxt(filename, 'rX00_3b', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_3b", "//")[0]]
    output_listU = ['rX00_3b ' + '-' + str(U_phi1) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_3b 0 ' + str(new_positionU[1]) + ' ' + str(new_positionU[2]) + ' //']
    
    # print(input_listU)
    # print(output_listU)
    replacetext(filename, input_listD + input_listU, output_listD + output_listU)

# Changing the position of Mirror 2
# The center position of the mirror is constant and you can rotate it around this point.

# def change_Mirror2(phi, y = 650, z = 200): #inputa angle in degrees and position im millimeters
#     filename = "geometries/main_detector3.tg"
#     new_position_y = y_position_Mirror2(phi, y)
#     new_position_z = z_position_Mirror2(phi, z)
#     input_list = [betweentxt(filename, 'rXY0_5', '90.0')[0], betweentxt(filename, "RichTbContainerVesselBox rXY0_5", "//")[0]]
#     output_list = ['rXY0_5 -' + str(phi) + ' 90.0', 'RichTbContainerVesselBox rXY0_5 0 ' + str(new_position_y) + ' ' + str(new_position_z) + ' //']
#     # print(input_list)
#     # print(output_list)
#     replacetext(filename, input_list, output_list)

#Changing the posritions of the box which is substitutuing the spherical version of the flat mirror - reflection in visualization is now normal

def change_MirrorBOX(D_phi3, U_phi3, y3, z3):# inputa angle, again for uppper and lower position,
    filename = "geometries/main_detector3.tg" # in degrees and position im millimeters
    input_listD = [betweentxt(filename, 'rX00_5a', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_5a", "//")[0]]
    output_listD = ['rX00_5a ' + str(-D_phi3) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_5a 0 ' + str(-y3) + ' -' + str(z3) + ' //']
    input_listU = [betweentxt(filename, 'rX00_5b', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_5b", "//")[0]]
    output_listU = ['rX00_5b ' + str(U_phi3) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_5b 0 ' + str(y3) + ' -' + str(z3) + ' //']
    # print(input_listU)
    # print(output_listU)
    replacetext(filename, input_listD + input_listU, output_listD + output_listU)

# Same thing just for PMT(with the  detector planes) boxes.
def change_PMT(D_phi, U_phi, y, z):# inputa angle, again for uppper and lower position,
    filename = "geometries/main_detector3.tg" # in degrees and position im millimeters
    input_listD = [betweentxt(filename, 'rX00_9', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_9", "//")[0]]
    output_listD = ['rX00_9 ' + str(-D_phi) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_9 0 ' + str(-y) + ' ' + str(z) + ' //']
    input_listU = [betweentxt(filename, 'rX00_10', '0.0')[0], betweentxt(filename, "RichTbContainerVesselBox rX00_10", "//")[0]]
    output_listU = ['rX00_10 ' + str(U_phi) + ' 0.0 0.0', 'RichTbContainerVesselBox rX00_10 0 ' + str(y) + ' ' + str(z) + ' //']
    
    # # Simultanious movement of the agle planes not working yet.
    # dz_D = d * math.sin(D_phi*(math.pi/180))
    # dy_D = d * math.cos(D_phi*(math.pi/180))
    # dz_U = d * math.sin(U_phi*(math.pi/180))
    # dy_U = d * math.cos(U_phi*(math.pi/180))
    # input_list_plane = [betweentxt(filename, '11 RichTbContainerVesselBox rX00_9 0 ', '//')[0], betweentxt(filename, "12 RichTbContainerVesselBox rX00_10 0 ", "//")[0]]
    # output_list_plane = ['11 RichTbContainerVesselBox rX00_9 0 ' + str(-y + dy_D) + ' ' + str(z - dz_D) + ' //', '12 RichTbContainerVesselBox rX00_10 0 ' + str(y - dy_U) + ' ' + str(z - dz_U) + ' //']

    # print(input_list_plane)
    # print(output_list_plane)
    replacetext(filename, input_listD + input_listU, output_listD + output_listU)
    
#z = 500, z1 = 300, y3 = 500, z3 = 4500, y = 2500, z = 1000
def run_macro(D_phi1, U_phi1, D_phi3, U_phi3, D_phi, U_phi, z1 = 300, y3 = 850, z3 = 400, y = 1800, z = 500):
    change_Mirror1(D_phi1, U_phi1, z1)
    change_MirrorBOX(D_phi3, U_phi3, y3, z3)
    change_PMT(D_phi, U_phi, y, z)
    os.system("main_detector.mac")

# PART OF THE CODE WHERE YOU CAN CHANGE THE TILT AND POSITION OF THE MIRRORS AND PMT DETECTORS (p.s.
# if you don't need to run the command for a certain mirror comment it otherwise the code will run
# more times than needed)

# Positon of the spherical mirrors <tilt of lower sph mirror> <tilt of uper sph mirror> <tilt of flat
#  lower mirror> <tilt of flat uper mirror> <tilt of the upper PMT detector> <tilt of the lower PMT
#  detector>, <optional z position, default z is 100> <optional z position, default is 200>, <optional
#  y position, default y = 1600> <optional z position, default z = 200># change_Mirror1(20, 20) 
# # Interval Sph [25-20] and Flat [10-5]

run_macro(11, 11, 6, 6, 34, 34)


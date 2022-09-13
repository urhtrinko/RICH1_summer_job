from encodings import utf_8
import re
  
def replacetext(filename, search_list, replace_list):
    with open(filename, 'r+', encoding="utf8") as f:

        if (len(search_list) != len(replace_list)):
            return "Input ERROR"
  
        file = f.read()
          
        for i in range(0, len(search_list)):

            if re.search(search_list[i], file) is None:
                input("Input ERROR")
                break
            else:
                file = re.sub(search_list[i], replace_list[i], file)
  
        f.seek(0)
          
        f.write(file)
  
        f.truncate()

        input("Everything okay? Press ENTER")

# def times(string):
#     new_string = ''
#     for element in string:
#         if element != "*":
#             new_string += element
#         else:
#             new_string += "\*"
#     return new_string

def betweentxt(filename, start_text, end_text):
    with open(filename, 'r', encoding = 'utf_8') as input_file:
        RES = []
        for line in input_file:
            result = re.search(start_text + '(.*)' + end_text, line)
            if result != None:
                RES.append((result.group(0)))
        return RES

# print(betweentxt("geometry/main_detector3.tg", 'rXY0_3', '*deg '))

def betweenLinesFill(filename, start_text, end_text, replacelines): #replace lines are lists
    lines = []
    with open(filename, 'r') as data:
        for line in data:
            lines.append(line)

    with open(filename, 'w') as new_data:    
        i = 0
        inRecordingMode = False
        for line in lines:
            if not inRecordingMode:
                if line.startswith(start_text):
                    inRecordingMode = True
            elif line.startswith(end_text):
                inRecordingMode = False
            if inRecordingMode:
                if i == 0:
                    new_data.write(line)
                else:
                    new_data.write(replacelines[i - 1])
                i += 1
                # new_data.write(replacelines[0])
            else:
                if i != (len(replacelines) + 1):
                    new_data.write(line)
                else:
                    new_data.write("\n" + line)
                    i += 1

# print(betweenlines("main_detector.mac", "#Start prop", "#End prop"))

# filename = 'geometry/main_detector3.tg'
# il_pars = ['rXY0_3 15.0 0.0', 'rXY0_3 0 -412.8199856546609 -748.2454874477346 //']
# il_rot = ['RichTbR1FlatMirrRotX', "RichTbR1FlatMirrRotY"]
# il_pos = ["RichTbR1FlatMirrPosX", "RichTbR1FlatMirrPosY", "RichTbR1FlatMirrPosZ"]

# delta_theta = math.asin(1480/5000)
# delta_phi = math.asin(880/5000)
# vertTilt = 0.25656
# # Flat Mirror

# RichTbR1FlatMirrInnerRadius = 5000.0
# RichTbR1FlatMirrThickness = 6.0
# RichTbR1FlatMirrOuterRadius =  RichTbR1FlatMirrInnerRadius + RichTbR1FlatMirrThickness
# RichTbR1FlatMirrSegmentSizeX = 1480.0
# RichTbR1FlatMirrSegmentSizeY = 880.0
# RichTbR1FlatMirrBotInLHCbPosY = 337.90
# RichTbR1FlatMirrBotInLHCbPosZ = 1323.31
# RichTbR1FlatMirrVertTilt = 0.25656 
# RichTbR1FlatMirrRotX = -1.0 * RichTbR1FlatMirrVertTilt
# RichTbR1FlatMirrRotY = 0.5 * math.pi

# RichTbR1FlatMirrInLHCbPosY = RichTbR1FlatMirrBotInLHCbPosY + 0.5 * RichTbR1FlatMirrSegmentSizeY * math.cos(RichTbR1FlatMirrVertTilt) +RichTbR1FlatMirrOuterRadius * math.sin( RichTbR1FlatMirrVertTilt)
# RichTbR1FlatMirrInLHCbPosZ = RichTbR1FlatMirrBotInLHCbPosZ - 0.5 *  RichTbR1FlatMirrSegmentSizeY * math.sin(RichTbR1FlatMirrVertTilt) + RichTbR1FlatMirrOuterRadius * math.cos(RichTbR1FlatMirrVertTilt)

# ol_pars = ['rXY0_3 6.0 0.0', 'rXY0_3 0 -228.1123180320152 -798.6879537069108 //']
# ol_rot = [str(-1.0 * vertTilt) + "*rad", str(0.5 * math.pi)  + "*rad"]
# ol_pos = ['0.0', str(RichTbR1FlatMirrInLHCbPosY), str(RichTbR1FlatMirrInLHCbPosZ)]

# replacetext('main_detector.mac', '/gps/" + particle + "\n/gps/pos/type Beam', betweenlines("main_detector.mac", "#Start prop", "#End prop"))

# print(re.findall('rXY0_3 6.0\*deg -0.0\*deg', ":rotm rXY0_3 5.0\*deg -0.0\*deg 0.0" + "\n" + 
# ":rotm rXYZ 0 0 0 // What is rXYZ (r000 is only a placeholder"))

# sez = ["/gps/particle proton\n", "/gps/pos/type Beam\n", "/gps/pos/shape Circle\n", "/gps/pos/centre 0.0 0.0 -5. m\n", "/gps/pos/radius 0. mm\n", "/gps/pos/sigma_r 5. mm\n", "/gps/direction 0 0 1"]
# betweenLinesFill("main_detector.mac", "#Start prop", "#End prop", sez)

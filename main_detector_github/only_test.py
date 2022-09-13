from loop_over_files import betweenlines

findlines = betweenlines("backup.mac", "#Start prop", "#End prop").split("\n")
replacelines = "/gps/proton\n/gps/pos/type Beam\n/gps/pos/shape Circle\n/gps/pos/centre 0.0 0.0 -5. m\n/gps/pos/radius 0. mm\n/gps/pos/sigma_r 5. mm\n/gps/direction 0 0 1".split("\n")
find_replace = dict(zip(findlines, replacelines))

def replace_file_lines(find_replace):
    lines = []
    with open('backup.mac', "r") as data:
        for line in data:
            lines.append(line)
    with open('backup.mac', 'w') as new_data:
        for line in lines:
            for key in find_replace:
                    if key in line:
                        line = line.replace(key, find_replace[key])
            new_data.write(line)

# replace_file_lines(find_replace)

print(find_replace)


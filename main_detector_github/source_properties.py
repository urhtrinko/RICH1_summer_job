from loop_over_files import replace_file_lines
from loop_over_files import betweenlines

def source(filename, particle, type, angular_distribution): # type-beam,point,plane,volume
    if type == "beam": # the numer of lines in input_tex and replace_text MUST be the same
        findlines = betweenlines(filename, "#Start prop", "#End prop").strip("\n")
        replacelines = ["/gps/particle " + particle + "\n", "/gps/pos/type Beam\n", "/gps/pos/shape Circle\n", "/gps/pos/centre 0.0 0.0 -5. m\n", "/gps/pos/radius 0. mm\n", "/gps/pos/sigma_r 5. mm\n", "/gps/direction 0 0 1"]
        find_replace = dict(zip(findlines, replacelines))

        replace_file_lines(filename, find_replace)

source("main_detector.mac", "mion", "beam", [-15, 15])


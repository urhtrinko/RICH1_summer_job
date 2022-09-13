from loop_over_files import betweenLinesFill

def source(filename, particle, type, angular_distribution): # type-beam,point,plane,volume
    if type == "beam": # the numer of lines in input_tex and replace_text MUST be the same
        replacelines = ["/gps/particle " + particle + "\n", "/gps/pos/type Beam\n", "/gps/pos/shape Circle\n", "/gps/pos/centre 0.0 0.0 -5. m\n", "/gps/pos/radius 0. mm\n", "/gps/pos/sigma_r 5. mm\n", "/gps/direction 0 0 1"]
        betweenLinesFill(filename, "#Start prop", "#End prop", replacelines)
    elif type == "point":
        replacelines = ["/gps/particle " + particle + "\n", "/gps/pos/centre 0 0 -600 mm\n", "/gps/ang/type iso\n", "/gps/ang/mintheta -195 deg\n", "/gps/ang/maxtheta 195 deg\n", "#\n", "#"]
        betweenLinesFill(filename, "#Start prop", "#End prop", replacelines)

source("main_detector.mac", "proton", "point", [-15, 15])


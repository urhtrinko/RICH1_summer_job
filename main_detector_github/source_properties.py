from loop_over_files import betweenLinesFill

def source(filename, properties, boundry): # type-beam,point properties a dictionary
    if properties["type"] == "beam": # the numer of lines in input_tex and replace_text MUST be the same
        replacelines = ["/gps/particle " + properties["particle"] + "\n", "/gps/pos/type Beam\n",
         "/gps/pos/shape Circle\n", "/gps/pos/centre 0.0 0.0 -5. m\n", "/gps/pos/radius 0. mm\n",
         "/gps/pos/sigma_r 5. mm\n", "/gps/direction 0 0 1"]
    elif properties["type"] == "point":
        replacelines = ["/gps/particle " + properties["particle"] + "\n", "/gps/pos/centre 0 0 " 
        + str(properties["point pos"]) + " mm\n", "/gps/ang/type " + properties["ang type"] + "\n", 
        "/gps/ang/mintheta " + str(properties["mintheta"]) + " deg\n", 
        "/gps/ang/maxtheta " + str(properties["maxtheta"]) + " deg\n", "/gps/ang/rot1 0 1 0\n",
         "/gps/ang/rot2 1 0 0"]
    betweenLinesFill(filename, boundry[0], boundry[1], replacelines)

def sources(filename, properties):
    boundries = [["# Start prop 1", "# End prop 1"], ["# Start prop 2", "# End prop 2"],
     ["# Start prop 3", "# End prop 3"]]
    for i in range(3):
        source(filename, properties[i], boundries[i])

# Change values for a specific source
# SOURCE 1
keys1 = ["type", "particle", "point pos", "ang type", "mintheta", "maxtheta"]
values1 = ["point", "proton", -1000, "iso", -5, 5]
properties1 = dict(zip(keys1, values1))
# SOURCE 2
keys2 = ["type", "particle", "point pos", "ang type", "mintheta", "maxtheta"]
values2 = ["point", "pi+", -1000, "iso", -3, 3]
properties2 = dict(zip(keys2, values2))
# SOURCE 3
keys3 = ["type", "particle", "point pos", "ang type", "mintheta", "maxtheta"]
values3 = ["point", "pi-", -1000, "iso", -1, 1]
properties3 = dict(zip(keys3, values3))

properties = [properties1, properties2, properties3]

sources("main_detector.mac", properties)


# Useful .mac code

#/gps/particle proton
#/gps/number 1

# Point source
#/gps/pos/centre 0 0 -600 mm #for some reason best position z = -601 mm

# Plane source
#/gps/pos/type Plane
#/gps/pos/shape Square
#/gps/pos/centre 0 0 -600 mm
#/gps/pos/halfx 2. cm
#/gps/pos/halfy 2. cm

# Spherical volume source
#/gps/pos/type Volume
#/gps/pos/shape Sphere
#/gps/pos/centre 0 0 -601 mm
#/gps/pos/radius 10 mm

#/gps/ang/type iso
#/gps/ang/mintheta -195 deg
#/gps/ang/maxtheta 195 deg

#/gps/energy 180 GeV

# BEAM
#/gps/particle proton
#/gps/energy 180 GeV
#/gps/pos/type Beam
#/gps/pos/shape Circle
#/gps/pos/centre 0.0 0.0 -5. m
#/gps/pos/radius 0. mm
#/gps/pos/sigma_r 5. mm

#/gps/direction 0 0 1














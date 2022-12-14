import ROOT
from ROOT import TCanvas, TH1F, TFile
from subsidiary_code import angle_BeamPlane

#The maximum tilt of the flat mirror in the default position is 20 \degrees

def generate_angles(root_file, phi = 45): # specify a root file, range of the,
    f = TFile("root_files/" + root_file, "READ")                    # number of bins and angle of the PMT
    t = f.Get("t;1")                                                # plane

    nEntries = t.GetEntries()

    angles = []

    for i in range(0, nEntries):
        a = t.GetEntry(i)
        # print(i, "- n_steps:", t.n)
        for j in range(0, t.n): # second point is always the point on the detector
            point1d = []
            point2d = []
            point1u = []
            point2u = []
            if (t.vlm[j] == 5):
                point1d = [t.x[j], t.y[j], t.z[j]]
                korak_d = t.stp[j]
                if j + 1 <= (t.n - 1):
                    if (t.stp[j + 1] == korak_d + 1):
                        point2d = [t.x[j + 1], t.y[j + 1], t.z[j +1]]
                        if (len(point1d) != 0 and len(point2d) != 0):
                            angle = angle_BeamPlane(point1d, point2d, phi, "down")
                            angles.append(angle)
            if (t.vlm[j] == 6):
                point1u = [t.x[j], t.y[j], t.z[j]]
                korak_u = t.stp[j]
                if j + 1 <= (t.n - 1):
                    if (t.stp[j + 1] == korak_u + 1):
                        point2u = [t.x[j + 1], t.y[j + 1], t.z[j +1]]
                        if (len(point1u) != 0 and len(point2u) != 0):
                            angle = angle_BeamPlane(point1u, point2u, phi, "up")
                            angles.append(angle)

    return angles

def draw_histogram(filename, n_bins, start = 0, end = 0):
    h_angle = TH1F("Angualr distribution of beams", "Angels in degrees", n_bins, start, end)
    angles = generate_angles(filename, 75)
    for angle in angles:
        if angle != None:
            h_angle.Fill(angle)
    # IF YOU WANT TO DRAW THE HISTOGRAM
    c1 = TCanvas( 'c1', 'Hits_detector', 100, 100, 900, 550)
    c1.SetGridx()
    c1.SetGridy()
    c1.GetFrame().SetFillColor( 21 )
    c1.GetFrame().SetBorderMode(-1 )
    c1.GetFrame().SetBorderSize( 5 )
    c1.SetFixedAspectRatio()
    c1.Range(-10, -10, 10, 10)# (xmin,ymin,xmax,ymax)
    h_angle.Draw('colz')
    c1.Update()

    input("Press ENTER to continue.")

    # input("You want to SAVE this?")
    # c1.SaveAs("graphics/three_sources_angle2.jpg")

    # return [h_angle.GetMean(), h_angle.GetStdDev()]

# print(draw_histogram('iso_point_cone.root', 90, 0, 0))


import ROOT
from ROOT import TCanvas, TF2, TH1F, TFile, TH2F
from subsidiary_code import angle_BeamPlane



def fill_angles_histogram(root_file, n_bins, start, end, phi = 45): # specify a root file, range of the,
    f = TFile("root_files/" + root_file, "READ")                    # number of bins and angle of the PMT 
    t = f.Get("t;1")                                                # plane

    nEntries = t.GetEntries()

    h_angle = TH1F("Angualr distribution of beams", "Angels in degrees", n_bins, start, end)
    
    for i in range(0, nEntries):
        a = t.GetEntry(i)
        # print(i, "- n_steps:", t.n)
        for j in range(0, t.n): # second point is always the point on the detector
            point1 = []
            point2 = []
            if (t.vlm[j] == 5):
                point1 = [t.x[j], t.y[j], t.z[j]]
                korak = t.stp[j]
                if j + 1 <= (t.n - 1):
                    if (t.stp[j + 1] == korak + 1):
                        point2 = [t.x[j + 1], t.y[j + 1], t.z[j +1]]
                        if (len(point1) != 0 and len(point2) != 0):
                            angle = angle_BeamPlane(point1, point2, phi, "down")
                            h_angle.Fill(angle)
    
    # # IF YOU WANT TO DRAW THE HISTOGRAM
    # c1 = TCanvas( 'c1', 'Hits_detector', 100, 100, 900, 550)
    # c1.SetGridx()
    # c1.SetGridy()
    # c1.GetFrame().SetFillColor( 21 )
    # c1.GetFrame().SetBorderMode(-1 )
    # c1.GetFrame().SetBorderSize( 5 )
    # c1.SetFixedAspectRatio()                                    
    # c1.Range(-10, -10, 10, 10)# (xmin,ymin,xmax,ymax)          
    # h_angle.Draw('colz')                                       
    # c1.Update()                                                
    
    # input('Press enter to continue.')
    # #c1.SaveAs("graphics/angular_distribution.jpg")

    return [h_angle.GetMean(), h_angle.GetStdDev()]


print(fill_angles_histogram('r0001.root', 14, 25.0, 32.0))


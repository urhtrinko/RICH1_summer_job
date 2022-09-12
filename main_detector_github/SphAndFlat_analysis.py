import ROOT
from ROOT import TCanvas, TGraph2D
import math
from array import array
from MirrAndPMT_pos import run_macro
from subsidiary_code import range_list
from root_angle import fill_angles_histogram


def different_mirror_positions(phi1_start, phi1_end, phi2_start, phi2_end, d_phi, PMTphi=75): #phi_range are the two border values of the tilt of the other one
    c1 = TCanvas("c","Graph2D example",0,0,600,400)
    graph2D = TGraph2D()
    graph2D.SetTitle("Standard deviation for mirror tilts; Spherical mirror tilt; Flat mirror tilt; Standard deviation")
    means, distributions, angles1, angles2 = array("d"), array("d"), array("d"), array("d")
    i = 0
    for phi1 in range_list(phi1_start, phi1_end, d_phi):
        for phi2 in range_list(phi2_start, phi2_end, d_phi):
            run_macro(phi1, phi1, phi2, phi2, PMTphi, PMTphi)
            mean = fill_angles_histogram('r0001.root', 20, 0, 0, PMTphi)[0]
            distribution = fill_angles_histogram('r0001.root', 20, 0, 0, PMTphi)[1]
            means.append(mean)
            distributions.append(distribution)
            angles1.append(phi1)
            angles2.append(phi2)
            graph2D.SetPoint(i, phi1, phi2, distribution)
            i += 1

    graph2D.Draw("colz")
    c1.Update()

    input('Please press enter to continue.')
    c1.SaveAs("graphics/flat_100_different positions.png")

    minimum = min(list(distributions))
    index_min = distributions.index(minimum)
    min_angles = [angles1[index_min], angles2[index_min]]
    return [minimum, min_angles]

print(different_mirror_positions(20, 25, 5, 10, 0.5))

#the smallest distributions is  0.6413128643642546 at angle1:25.0 and angle2:10.0

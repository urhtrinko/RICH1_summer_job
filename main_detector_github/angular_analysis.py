from __future__ import print_function
from root_angle import fill_angles_histogram
from MirrAndPMT_pos import change_Mirror1
from ROOT import TCanvas, TGraph
from array import array

def different_mirror_positions(phi_start, phi_end, d_phi): #phi_range are the two border values of the tilt of the other one
    phi = phi_start
    x, y = array( 'd' ), array( 'd' )
    means = []
    while phi <= phi_end:
        change_Mirror1(phi, phi)
        distribution = fill_angles_histogram('r0001.root', 20)[1]
        mean = fill_angles_histogram('r0001.root', 20)[0]
        x.append(phi)
        means.append(mean)
        y.append(distribution)
        phi += d_phi
    c1 = TCanvas( 'c1', 'Standard deviation for angels of the sph mirror, while flat always at 10', 200, 10, 700, 500 )
    
    c1.SetFillColor( 42 )
    c1.SetGrid()
    
    n = int(len(x))

    gr = TGraph( n, x, y )
    gr.SetLineColor( 2 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerColor( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle('Standard deviation for a range of spehrical mirror tilts, while the flat mirror is stationary')
    gr.GetXaxis().SetTitle('Angles [degrees]')
    gr.GetYaxis().SetTitle('Standard deviation [degrees]')
    gr.Draw('AP')
    
    # TCanvas.Update() draws the frame, after which one can change it
    c1.Update()
    c1.GetFrame().SetFillColor(21)
    c1.GetFrame().SetBorderSize(12)
    c1.Modified()
    c1.Update()

    input("Press enter to continue")
    c1.SaveAs('graphics/distributions_tilt_SphMirr.jpg')

    Min = min(list(y))
    indx = y.index(Min)
    return [Min, x[indx]]

print(different_mirror_positions(16, 24, 0.25)) 
 

# If the graph does not appear, try using the "i" flag, e.g. "python3 -i graph.py"
# This will access the interactive mode after executing the script, and thereby persist
# long enough for the graph to appear.

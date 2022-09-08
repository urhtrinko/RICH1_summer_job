from __future__ import print_function
from root_angle import fill_angles_histogram
from MirrAndPMT_pos import change_Mirror1
from ROOT import TCanvas, TGraph
from array import array

def different_mirror_positions(phi_start, phi_end, d_phi): #phi_range are the two border values of the tilt of the other one
    phi = phi_start
    angles, distributions = array('d'), array('d')
    relative_error = array('d')
    while phi <= phi_end:
        change_Mirror1(phi, phi)
        distribution = fill_angles_histogram('r0001.root', 20)[1]
        mean = fill_angles_histogram('r0001.root', 20)[0]
        angles.append(phi)
        relative_error.append(distribution/mean)
        distributions.append(distribution)
        phi += d_phi
    
    c1 = TCanvas( 'c1', 'Standard deviation for angels of the sph mirror, while flat always at 10', 100, 100, 1200, 700)
    c1.Divide(2, 1)

    c1.SetFillColor( 21 )
    c1.SetGrid()
    
    n = int(len(angles))

    c1.cd(1)
    gr_dist = TGraph( n, angles, distributions)
    # gr_dist.SetLineColor( 2 )
    # gr_dist.SetLineWidth( 4 )
    gr_dist.SetMarkerColor( 4 )
    gr_dist.SetMarkerStyle( 21 )
    gr_dist.SetTitle('Standard deviation')
    gr_dist.GetXaxis().SetTitle('Angles [degrees]')
    gr_dist.GetYaxis().SetTitle('Standard deviation [degrees]')
    gr_dist.Draw('AP')
    
    c1.cd(2)
    gr_rel = TGraph( n, angles, relative_error)
    # gr_dist.SetLineColor( 2 )
    # gr_dist.SetLineWidth( 4 )
    gr_rel.SetMarkerColor( 4 )
    gr_rel.SetMarkerStyle( 21 )
    gr_rel.SetTitle('Relative error')
    # gr_rel.SetTitleFontSize(10)
    gr_rel.GetXaxis().SetTitle('Angles [degrees]')
    gr_rel.GetYaxis().SetTitle('Relative erroe [degrees]')
    gr_rel.Draw('AP')

    # TCanvas.Update() draws the frame, after which one can change it
    c1.Update()
    # c1.GetFrame().SetFillColor(21)
    # c1.GetFrame().SetBorderSize(12)
    # c1.Modified()
    # c1.Update()

    # input("Press enter to continue")
    # c1.SaveAs('graphics/DeviationAndRelativeError.jpg')

    dit_min = min(list(distributions))
    rel_min = min(list(relative_error))
    dit_indx = distributions.index(dit_min)
    rel_indx = relative_error.index(rel_min)
    return ["Distribution:", dit_min, angles[dit_indx], "relative_error:", rel_min, angles[rel_indx]]

print(different_mirror_positions(16, 24, 0.1)) 
 


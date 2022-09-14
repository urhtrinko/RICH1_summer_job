import ROOT
from ROOT import TCanvas, TFile, TH1F, TH2F 
from root_angle import draw_histogram

c1 = TCanvas( 'c1', 'Hits_detector', 100, 100, 900, 550)
c1.Divide(2, 1)
c1.SetGridx()
c1.SetGridy()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderMode(-1 )
c1.GetFrame().SetBorderSize( 5 )
c1.SetFixedAspectRatio()
c1.Range(-10, -10, 10, 10)# (xmin,ymin,xmax,ymax)

f = TFile("root_files/three_sources.root", "READ")
t = f.Get("t;1")

nEntries = t.GetEntries()

h1 = TH2F("Analysis1", "xx:yy", 100, -1000, 1000, 100, -1000, 1000)
h2 = TH2F("Analysis2", "xx:yy", 100, 0, 0, 100, 0, 0)
h1D = TH1F("Analysis1D", "k", 100, 0, 0)

for i in range(0, nEntries):
    a = t.GetEntry(i)
    # print(i, "- n_steps:", t.n)
    for j in range(0, t.n):
        if ((t.trk[j] == 1 and t.vlm[j] == 7)): #t.pdg[j] == 2212 and
            h2.Fill(t.xx[j], t.yy[j])
        if ((t.trk[j] == 1 and t.stp[j] == 0 and t.pdg[j] == 2212)):
            h1D.Fill(t.k[j])
        if ((t.vlm[j] == 9)):
            h1.Fill(t.xx[j], t.yy[j])
        # if ((t.vlm[j] == 5)):
        #     hM_D.Fill(t.xx[j], t.yy[j])
        # if ((t.vlm[j] == 6)):
        #     hM_U.Fill(t.xx[j], t.yy[j])
        # # if ((t.trk[j] == 2)):
        #     h_yz.Fill(t.y[j], t.z[j])

c1.cd(1)
h1.Draw("colz")
c1.cd(2)
h1D.Draw()
# c1.cd(3)
# hM_D.Draw('colz')
# c1.cd(4)
# hM_U.Draw('colz')
# c1.cd(2)
# h3.Draw()

c1.Update()

input('Press ENTER to continue')

# input("You want to SAVE this?")
# c1.SaveAs("graphics/three_sources2.png")

# print((h1.GetEntries(), h2.GetEntries()))

print(draw_histogram("three_sources.root", 90))

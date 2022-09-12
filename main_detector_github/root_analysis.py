import ROOT
from ROOT import TCanvas, TF2, TH1F, TFile, TH2F 

c1 = TCanvas( 'c1', 'Hits_detector', 100, 100, 900, 550)
c1.Divide(2, 1)
c1.SetGridx()
c1.SetGridy()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderMode(-1 )
c1.GetFrame().SetBorderSize( 5 )
c1.SetFixedAspectRatio()
c1.Range(-10, -10, 10, 10)# (xmin,ymin,xmax,ymax)

f = TFile("root_files/r0001.root", "READ")
t = f.Get("t;1")

nEntries = t.GetEntries()

h1 = TH2F("Lower PMT detector", "xx:yy", 80, -400, 400, 80, -400, 400)
h2 = TH2F("Upper PMT detector", "xx:yy", 80, -400, 400, 80, -400, 400)
hM_D = TH2F("Lower Flat mirror", "xx:yy", 80, -400, 400, 80, -400, 400)
hM_U = TH2F("Upper Flat mirror", "xx:yy", 80, -400, 400, 80, -400, 400)

for i in range(0, nEntries):
    a = t.GetEntry(i)
    print(i, "- n_steps:", t.n)
    for j in range(0, t.n):
        if ((t.vlm[j] == 9)): 
            h1.Fill(t.xx[j], t.yy[j])
        if ((t.vlm[j] == 10)):
            h2.Fill(t.xx[j], t.yy[j])
        # if ((t.vlm[j] == 5)):
        #     hM_D.Fill(t.xx[j], t.yy[j])
        # if ((t.vlm[j] == 6)):
        #     hM_U.Fill(t.xx[j], t.yy[j])
        # # if ((t.trk[j] == 2)):
        #     h_yz.Fill(t.y[j], t.z[j])

c1.cd(1)
h1.Draw('colz')
c1.cd(2)
h2.Draw('colz')
# c1.cd(3)
# hM_D.Draw('colz')
# c1.cd(4)
# hM_U.Draw('colz')
# c1.cd(2)
# h3.Draw()

c1.Update()

c1.SaveAs("graphics/PMT_xx_yy_251075.png")
input('Press ENTER to continue')

print((h1.GetEntries(), h2.GetEntries()))

import ROOT
import math
from ROOT import TCanvas, TF2, TGraph2D, TRandom

c1 = TCanvas("c","Graph2D example",0,0,600,400)

#Double_t x, y, z,
P = 6.
n = 200
dt = TGraph2D()
dt.SetTitle("Graph title; X axis title; Y axis title; Z axis title")
r = TRandom()
for i in range(n):
    x = 2*P*(r.Rndm(i)) - P
    y = 2*P*(r.Rndm(i)) - P
    z = (math.sin(x)/x)*(math.sin(y)/y) + 0.2
    dt.SetPoint(i,x,y,z)
#gStyle.SetPalette(1)
dt.Draw("surf1")

c1.Update()

input('Please press enter to continue.')

#   return c;

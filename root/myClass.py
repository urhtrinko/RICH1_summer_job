from ROOT import TFile, TBranch, TTree, TString, TH1F, TH2F, TCanvas

input_file0 = "layered_mirror.root"
input_file1 = "layered_mirror_detector.root"

hh = TH1F("hh", "x", 100, 0, 0) #ce so meje 0,0 potem bo range automatsko nastavljen glede na podatke 
h2 = TH2F("h2", "x:z{trk==1}", 100, 0, 0, 100, 0, 0)


myfile = TFile(input_file0, "READ")
myTree = myfile.Get("t")

nEntries = myTree.GetEntries()

# # Display the branches (x, y, z, xx...)
# for b in myTree.GetListOfBranches():
#     print("branch: ", b.GetName ())
    
# input("Please press ENTER to continue")

for i in range(0, nEntries):
    a = myTree.GetEntry(i)
    print(i, "- n_steps:", myTree.n)
    for x_koordinata in myTree.x:
        hh.Fill(x_koordinata)
        #print(x_koordinata, end=", ")
    for j in range(0, myTree.n):
        if(myTree.trk[j] == 1):
            h2.Fill(myTree.z[j], myTree.x[j])
    #print()
c_mycanvas = TCanvas("c_mycanvas", "c_mycanvas", 600, 550)
c_mycanvas.Divide(2,1)
# c_mycanvas.cd(1)
# hh.Draw("")
# c_mycanvas.cd(2)
h2.Draw("COLZ")
c_mycanvas.Update()
c_mycanvas.SaveAs("layered_mirror.png")
input("Press ENTER to close.")
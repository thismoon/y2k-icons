import os
import sys
import cairosvg
import shutil

#checks for "pngs" folder existance
if (os.path.exists("pngs")):
    deleteanswer = input("folder \"pngs\" exitst, delete it? [y/n]:\n-> ")
    if(deleteanswer == "n"):
        exit()
    elif(deleteanswer == "y"):
        shutil.rmtree("pngs")
    else:
        print("invalid answer, exiting\n")
        exit()

#ask user for the png resolution
resolution = int(input("type the png resolution (100 to 1000):\n-> "))
if (resolution < 100):
    print("\033[91merror:\033[0m resolution too small\n")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif (resolution > 1000):
    print("\033[91merror:\033[0m resolution too big\n")
    os.execl(sys.executable, sys.executable, *sys.argv)

#get list of svg files in the icons folder
svgsfolder = "./icons/"
svgs = []
for x in os.listdir(svgsfolder):
    if x.endswith(".svg"):
        svgs.append(x)

#create pngs folder
os.mkdir("./pngs")

#convert svgs to pngs
for x in svgs:
    svgpath = "./icons/" + x
    pngpath = "./pngs/" + x[:-3] + "png"
    cairosvg.svg2png(url=svgpath, write_to=pngpath, scale=resolution/100)

#print result
print(
    "converted "
    + str(len(svgs))
    + " svgs to pngs in "
    + str(resolution)
    + "x"
    + str(resolution)
    + "px resolution"
)
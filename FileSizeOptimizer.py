import os
import shutil
import gzip
shutil.move("content/FileSizeList.txt", "FileSizeList.txt")
try:
    shutil.move("content/FileSizeList.txt.bak", "FileSizeList.txt.bak")
except FileNotFoundError:
    print("No FileSizeList.txt.bak file found. Creating bak file...")
fyle = open("FileSizeList.txt", "rb+")
flylyle = open("FileSizeList.txt.bak", "wb+")
fayle = fyle.read()
flylyle.write(fayle)
flylyle.close()
#lyle = "Audiores/Seqs"
#print(os.path.abspath(lyle))
#os.chdir("./Audiores/Waves")
#os.chdir("../../DebugSaves/QASaves")
lyle = os.path.abspath(os.curdir)
loyal = lyle
print(lyle, "\n\n\n")
offset = 0
num = 0
bun = 0
gum = 0
fyle.seek(0)
choice = int(input("Enter 0 to adjust filesize for nearly all files except stage files. Or enter 1 to adjust filesize for a specific stage: "))
if choice > 1 or choice < 0:
    shutil.move("FileSizeList.txt", "content/FileSizeList.txt")
    shutil.move("FileSizeList.txt.bak", "content/FileSizeList.txt.bak")
    input("Unacceptable input. Press ENTER to close...")
    exit()

def packin_GZs(x):
    omelet = 0
    omepic = 0
    omelat = 0
    l = b'\x70\x61\x63\x6B'
    m = b'\x67\x74\x78'
    der = os.path.abspath(os.curdir)
    if choice == 0 and num != 31:
        os.chdir("../..")
    elif choice == 1:
        os.chdir("../../..")
    g = open(os.curdir+"/DecompressedSizeList.txt", "rb+")
    h = g.read()
    g.seek(0)
    x = os.path.splitext(basename)
    if x[1] == '.gz':
        print(x)
        b = open(f"{os.path.abspath(der)}\\{y[0]}.gz", "rb")
        c = open(f"{os.path.abspath(der)}\\{y[0]}", "wb")
        A = gzip.decompress(b.read())
        c.write(A)
        c.close()
        e = os.path.getsize(f"{der}/{x[0]}")
        d = os.path.getsize(f"{der}/{basename}")
        print(d)
        print(e)
        f = round(abs((d/e)*100-100), 1)
        print(f)
        k = f"{d}\00{e}\00{f}%"
        os.remove(f"{der}/{x[0]}")
        if y[0] != "cardicon.pack":
            omepic = h.find(bytes(x[0], 'ascii'), 0, 108844)
            if x[0].endswith(".pack"):
                omelet = h.rfind((l), 0, omepic)
                omelet += 5
            elif x[0].endswith(".gtx"):
                omelet = h.rfind((m), 0, omepic)
                omelet += 4
            print(omelet)
        else:
            omepic = 108844
        
        omelat = h.find(b'\x00\x2E\x2F', omelet+1, omepic)
        g.seek(omelat)
        boy = g.read()
        g.seek(omelet)
        g.truncate()
        g.write(bytes(k, 'ascii'))
        g.write(boy)
        g.seek(0)
        h = g.read()
        g.close()
        os.chdir(der)
try:
    if choice == 0:
        while (num <= 33):
            if num == 0:
                os.chdir("./content/Audiores/Seqs")
                gum = 1
            elif num == 1:
                os.chdir("../Stream")
                gum = 128
            elif num == 2:
                os.chdir("../Waves")
                gum = 238
            elif num == 3:
                os.chdir("..")
                gum = 2
            elif num == 4:
                os.chdir("..")
                gum = 1
            elif num == 5:
                os.chdir("./DebugSaves/CSSaves")
                gum = 700
            elif num == 6:
                os.chdir("../QASaves/HeroMode")
            elif num == 7:
                os.chdir("..")
            elif num == 8:
                os.chdir("..")
            elif num == 9:
                os.chdir("..")
                gum = 6
            elif num == 10:
                os.chdir("./res/ActorDat")
                gum = 1
            elif num == 11:
                os.chdir("../CardIcon")
                gum = 2
            elif num == 12:
                os.chdir("../FieldMap")
                gum = 23
            elif num == 13:
                os.chdir("../Fonteu")
                gum = 4
            elif num == 14:
                os.chdir("../Fontjp")
            elif num == 15:
                os.chdir("../Fontus")
            elif num == 16:
                os.chdir("../ItemTable")
                gum = 2
            elif num == 17:
                os.chdir("../Layout")
                gum = 55
            elif num == 18:
                os.chdir("../LayoutRevo")
                gum = 41
            elif num == 19:
                os.chdir("../Menu")
                gum = 2
            elif num == 20:
                os.chdir("../Msgde")
                gum = 10
            elif num == 21:
                os.chdir("../Msgfr")
            elif num == 22:
                os.chdir("../Msgit")
            elif num == 23:
                os.chdir("../Msgjp")
            elif num == 24:
                os.chdir("../Msgsp")
            elif num == 25:
                os.chdir("../Msguk")
            elif num == 26:
                os.chdir("../Msgus")
            elif num == 27:
                os.chdir("../Msgusfr")
            elif num == 28:
                os.chdir("../Msgussp")
            elif num == 29:
                os.chdir("../Object")
                gum = 2629
            elif num == 30:
                os.chdir("../Particle")
                gum = 66
            elif num == 31:
                os.chdir("../..")
                gum = 1
            elif num == 32:
                os.chdir("./tex/Particle")
                gum = 66
            elif num == 33:
                os.chdir("../..")
                gum = 1
            lyle = os.path.abspath(os.curdir)
            print("*********************************                *********************************                *********************************                *********************************\n----------------------------",lyle,"----------------------------\n*********************************                *********************************                *********************************                *********************************")
            bossfolder = os.listdir(lyle)
            if num == 9:
                bossfolder.pop(1)
            elif num == 31:
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(1)
                #bossfolder = bossfolder.pop(-2)
                print(bossfolder)
            elif num == 33:
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(0)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                bossfolder.pop(1)
                #bossfolder = bossfolder.pop(3)
            for basename in filter(os.path.isfile, bossfolder):
                y = os.path.splitext(basename)
                N = len(bytes(y[1], 'ascii'))                                                   # how many digits the extension name is (including the ".")
                baytes = bytes(y[1], 'ascii')                                                   # bytes of the extension
                n = N+1                                                                         # offset right before the size value
                if y[0] == "DecompressedSizeList":
                    sunset = fayle.find(baytes, offset+N, 200000)
                #print(baytes, N, n)
                if bun < gum:                                                                   # How many files in that folder to check filesize (based on how many from that folder are next to each other in offset of FileSizeList.txt)
                    if num < 31:
                        offset = fayle.find(baytes, offset+N, 200000)                               # offset that contains beginning of extension for the file
                    elif num == 33:
                        offset = sunset
                    else:
                        offset = fayle.find(bytes(y[0], 'ascii'), offset, 200000)
                        offset = fayle.find(baytes, offset+N, 200000)
                    print("---------------------------\noffset: ",offset + n)
                    a = offset + n
                    offsat = fayle.find(b'\x00', offset+n, 200000)                              # offset right after the file's filesize value
                    fyle.seek(offset + n)
                    fyleSize = int(fyle.read(offsat-(offset+n)))                                # reading the file's filesize in FileSizeList.txt
                    boi = fyle.read()

                    lyleSize = os.path.getsize(f"{lyle}/"+basename)                             # reading the filesize of the actual file
                    print(f"\n{basename} filesize: ", lyleSize)
                    if lyleSize != fyleSize:                                                    # comparing the actual size of the file with the value in FileSizeList.txt and updating the value in FileSizeList.txt if different
                        if y[1] == ".gz":
                            packin_GZs(y)
                        print(f"\n\nUPDATING {basename}'s filesize in FileSizeList.txt!\n")
                        fyle.seek(a)
                        fyle.truncate()
                        fyle.write(bytes(str(lyleSize), 'ascii'))
                        fyle.write(boi)
                        fyle.seek(0)
                        fayle = fyle.read()
                    bun += 1
            num += 1
            bun = 0
    elif choice == 1:
        os.chdir("./content/res/Stage")
        staage = input("Enter name of a stage folder (example: D_MN01): ")
        os.chdir("./"+staage)
        lyle = os.path.abspath(os.curdir)
        print("*********************************                *********************************                *********************************                *********************************\n----------------------------",lyle,"----------------------------\n*********************************                *********************************                *********************************                *********************************")
        bossfolder = os.listdir(lyle)
        gum = len(bossfolder)
        for basename in filter(os.path.isfile, bossfolder):
            y = os.path.splitext(basename)
            N = len(bytes(y[1], 'ascii'))                                                   # how many digits the extension name is (including the ".")
            baytes = bytes(y[1], 'ascii')                                                   # bytes of the extension
            n = N+1                                                                         # offset right before the size value
            #print(baytes, N, n)
            offset = fayle.find(bytes(staage+"/"+y[0], 'ascii'), offset, 200000)
            if bun < gum:                                                                   # How many files in that folder to check filesize (based on how many from that folder are next to each other in offset of FileSizeList.txt)
                offset = fayle.find(baytes, offset+N, 200000)
                print("---------------------------\noffset: ",offset + n)
                a = offset + n
                offsat = fayle.find(b'\x00', offset+n, 200000)                              # offset right after the file's filesize value
                fyle.seek(offset + n)
                fyleSize = int(fyle.read(offsat-(offset+n)))                                # reading the file's filesize in FileSizeList.txt
                boi = fyle.read()

                lyleSize = os.path.getsize(f"{lyle}/"+basename)                             # reading the filesize of the actual file
                print(f"\n{basename} filesize: ", lyleSize)
                if lyleSize != fyleSize:                                                    # comparing the actual size of the file with the value in FileSizeList.txt and updating the value in FileSizeList.txt if different
                    if y[1] == ".gz":
                        packin_GZs(y)
                    print(f"\n\nUPDATING {basename}'s filesize in FileSizeList.txt!\n")
                    fyle.seek(a)
                    fyle.truncate()
                    fyle.write(bytes(str(lyleSize), 'ascii'))
                    fyle.write(boi)
                    fyle.seek(0)
                    fayle = fyle.read()
                bun += 1
        # For DecompressedSizeList.txt
        os.chdir("../../..")
        offset = 0
        lyle = os.path.abspath(os.curdir)
        print("*********************************                *********************************                *********************************                *********************************\n----------------------------",lyle,"----------------------------\n*********************************                *********************************                *********************************                *********************************")
        y = os.path.splitext("DecompressedSizeList.txt")
        N = len(bytes(y[1], 'ascii'))
        baytes = bytes(y[1], 'ascii')
        n = N+1
        offset = fayle.find(bytes(y[0], 'ascii'), offset, 200000)
        offset = fayle.find(baytes, offset+N, 200000)
        print("---------------------------\noffset: ",offset + n)
        a = offset + n
        offsat = fayle.find(b'\x00', offset+n, 200000)
        fyle.seek(offset+n)
        fyleSize = int(fyle.read(offsat-(offset+n)))
        boi = fyle.read()

        lyleSize = os.path.getsize(f"{lyle}/DecompressedSizeList.txt")
        print(f"\nDecompressedSizeList.txt filesize: ", lyleSize)
        if lyleSize != fyleSize:
            print(f"\n\nUPDATING DecompressedSizeList.txt's filesize in FileSizeList.txt!\n")
            fyle.seek(a)
            fyle.truncate()
            fyle.write(bytes(str(lyleSize), 'ascii'))
            fyle.write(boi)
            fyle.seek(0)
            fayle = fyle.read()
        num += 1
        bun = 0

except ValueError:
    print("Done!")
fyle.close()
os.chdir("..")
shutil.move("FileSizeList.txt", "content/FileSizeList.txt")
shutil.move("FileSizeList.txt.bak", "content/FileSizeList.txt.bak")
input("Press ENTER to close...")
import sys
fp1 = open(sys.argv[1],"r")
fp2 = open(sys.argv[2],"r")
x = fp1.readline()
while x:
        y = fp2.readline()
        print x.strip() + " ||| " + y.strip()
        x = fp1.readline()

fp1.close()
fp2.close()

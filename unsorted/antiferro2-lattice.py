#!/usr/bin/env python3

n =10
y = n* "        " + " "
x1=(n//2) * "U   +   D   +   " + "U"
z1=(n//2) * "+   D   +   U   " + "+"
x2=(n//2) * "D   +   U   +   " + "D"
z2=(n//2) * "+   U   +   D   " + "+"
print(x1)
print(x2)
print(z1)
print(z2)
print("S = B site"+"\n"+"+ = B' site"+"\n"+"U = upspin B site"+"\n"+"D = downspin B site"+"\n")
print((n//2) * (x1+"\n"+y+"\n"+z1+"\n"+y+"\n"+x2+"\n"+y+"\n"+z2+"\n"+y+"\n")+x1)

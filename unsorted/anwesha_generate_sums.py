#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:19:12 2022

@author: rajarshi
"""

import numpy as np
#from fpdf import FPDF
import os

ndigit = 11
nnum = 3

def get_sum(ndigit, nnum, num=12):
    Qs = []
    As = []
    for i in range(num):
        nlist = np.random.randint(low=10**ndigit, high=10**(ndigit+1) - 1, size=nnum)
        ss = ''
        for n in nlist[:-1]:
            ss += 2 * ' ' + str(n) + '\n'
        ss += '+ ' + str(nlist[-1]) + '\n'
        ss += (ndigit + 3) * '_' + '\n'
        ss += (ndigit + 3) * ' ' + '\n'
        ss += (ndigit + 3) * '_' + '\n'
        #ans = '|' + ' + '.join([str(i) for i in nlist]) + ' = ' + str(sum(nlist)) + '|'
        #ans = len(ans) * '_' + '\n' + ans + len(ans) * '_'
        Qs.append(ss)
        ss = ''
        for n in nlist[:-1]:
            ss += 2 * ' ' + str(n) + '\n'
        ss += '+ ' + str(nlist[-1]) + '\n'
        ss += (ndigit + 3) * '_' + '\n'
        ssum = str(sum(nlist))
        ss += (ndigit + 3 - len(ssum)) * ' ' + ssum + '\n'
        ss += (ndigit + 3) * '_' + '\n'
        #ans = '|' + ' + '.join([str(i) for i in nlist]) + ' = ' + str(sum(nlist)) + '|'
        As.append(ss)
    return Qs, As
#

Qs, As = get_sum(ndigit, nnum)

#for ss in Qs:
#    print(ss)

qq=np.array(Qs).reshape(4,3)
txt1 = ''
for q in qq:
    a = ['|' + '| |'.join(i) + '|' for i in zip(*[_.split('\n') for _ in q])]
    a.pop()
    a = '\n'.join(a)
    #print(a)
    txt1 += a + '\n'
#

n1 = len(txt1.split('\n'))


qq=np.array(As).reshape(4,3)
txt2 = ''
for q in qq:
    a = ['|' + '| |'.join(i) + '|' for i in zip(*[_.split('\n') for _ in q])]
    a.pop()
    a = '\n'.join(a)
    #print(a)
    txt2 += a + '\n'
#
n2 = len(txt2.split('\n'))

"""
ans = '\n'.join(As)
#print(3 * '\n')
#print(ans)
txt2 = ''
txt2 += 3 * '\n' + '\n'
txt2 += ans
n2 = len(txt2.split('\n'))
txt2 += (n1 - n2) *'\n'
"""
print(txt1 + txt2)
with open('sums.txt', 'a') as f:
    f.write(txt1 + txt2)
#

#cmd = 'a2ps --output=- --columns=1 --borders=0 --no-header --landscape --medium=a5 sums.txt gs -o sums.pdf -sDEVICE=pdfwrite -g1000x2500 -dAutoRotatePages=/None -'
cmd = 'a2ps --columns=1 --borders=1 --landscape -f 18 -L 24 --medium=a4 sums.txt gs -o sums.pdf'
os.system(cmd)

"""
pdf = FPDF()      
# Add a page 
pdf.add_page(orientation='p')  
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 9)
# insert the texts in pdf 
for i, t in enumerate(txt1.split('\n')):
    pdf.cell(15, 5, txt = t + '\n', ln = 12, align = 'C', fill=12)

pdf.add_page()
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 15)
# insert the texts in pdf 
for t in txt2.split('\n'):
    pdf.cell(50,15, txt = t, ln = 11, align = 'C', border=105)

# save the pdf with name .pdf 
pdf.output("sums.pdf")

"""


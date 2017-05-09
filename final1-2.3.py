#!/usr/bin/python

__author__ = "Jiawei Wang"
__copyright__ = "Copyright 2017"
__credits__ = ["Jiawei Wang"]
__license__ = "GPL"
__version__ = "1.3.0"
__maintainer__ = "Jiawei Wang"
__email__ = "jiawei.wang@yale.edu"

### Usage:      python final1-2.3.py -i <input folder> -m <mutation file>
### Example:    python final1-2.3.py -i GTEx_Analysis_v6p_eQTL -m Z.variantCall.SNPs_filt.vcf
### Note:       eQTL analysis of Zimmerome

### shell filters for Zimmerome SNPs
# awk '!/hs37d5/' Z.variantCall.SNPs_Only.vcf > Z.variantCall.SNPs_filtered.vcf
# awk '!/GL000/' Z.variantCall.SNPs_filtered.vcf > Z.variantCall.SNPs_filt.vcf

import argparse
#import numpy as np
#import matplotlib.pyplot as plt
#import fileinput
import pandas as pd
import os
# os.chdir('C:/Users/wangj/Documents/Biology/Yale-CSC/Studies/CBB752 Biomedical Data Analysis $ Mining & Modeling/FinalProjects/Project1.2')

### This is one way to read in arguments in Python. We need to read input folder and mutation file.
parser = argparse.ArgumentParser(description='SNP finder')
parser.add_argument('-i', '--ifolder', help='input folder', required=True)
parser.add_argument('-m', '--mutfile', help='mutation file', required=True)
# parser.add_argument('-t', '--tissue', help='tissue name', required=True)
args = parser.parse_args()

def runAGEP(ifolder, mutfile):#, tissue):
    zmut = pd.read_table(mutfile)#, dtype={'#CHROM':int})
    zmut = zmut[['#CHROM','POS','REF','ALT']]
    zx = zmut.index
    zids = dict()
    for z in zx:
        chrom = zmut.loc[z,'#CHROM']
        if chrom in range(1,23) or ['X','Y']:
            pos = zmut.loc[z,'POS']
            ref = zmut.loc[z,'REF']
            alt = zmut.loc[z,'ALT']
            if chrom not in zids.keys():
                zids[chrom] = dict()
            if pos not in zids[chrom].keys():
                zids[chrom][pos] = [[ref,alt]]
            else:
                zids[chrom][pos].append([ref,alt])
    # zids = ['_'.join([str(zmut.loc[i,'#CHROM']),str(zmut.loc[i,'POS']),zmut.loc[i,'REF'],zmut.loc[i,'ALT']])+'_b37' for i in zx]
    # zmut = dict()
    # for line in fileinput.input(mutfile):
    #    if '#' not in line:
    #        line = line.strip().split()
    #        zmut[num(line[1])] = tuple(line[])
    # zsnp = pd.read_table(mutfile)

    paths = os.listdir(ifolder)
    # for path in paths:
    #     if 'filtered' in path:
    #     if 'signif' in path:
    #         tismut = pd.read_table(os.path.join(ifolder, path))
    paths = [p for p in paths if 'signif' in p]
    # path = [p for p in paths if tissue in p][0]
    for path in paths:
        tismut = pd.read_table(os.path.join(ifolder, path))
        tisid = tismut['variant_id']
        tisname = ' '.join(path.split('_')[0:-3])
        # tisname = ' '.join(path.split('_')[:-1]
        tx = tismut.index
        mids = []
        for t in tx: ##compare each line in GTEx database if consistent with Zimmerome SNPs
            line = tisid[t].split('_')
            chrom = line[0]
            if chrom.isdigit():
                chrom = int(chrom)
            pos = line[1]
            if pos.isdigit():
                pos = int(pos)
            ref = line[2]
            alt = line[3]
            if chrom in zids.keys():
                if pos in zids[chrom].keys():
                    # if [ref,alt] in zids[chrom][pos]:
                    if [ref,alt] == zids[chrom][pos]:
                    # if line[2] == zmut.loc[k,'REF'] & line[3] == zmut.loc[k,'ALT']:
                        mids.append(t)
        selected = mids
        # mids = [list(tismut.loc[t,'variant_id']) in zids for t in tx]
        # selected = [i for i,x in enumerate(mids) if x == True]
        zselec = tismut.loc[selected,]
        zselec['tissue'] = tisname
        # np.savetxt('selected.txt',zselec)
        zselec.to_csv('ZSNPs_'+tisname+'.txt', header=True, index=False, sep=' ')

runAGEP(args.ifolder, args.mutfile)#, args.tissue)

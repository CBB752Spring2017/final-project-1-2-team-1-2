#!/usr/bin/python

### this program gets some statistics of the generated snp-gene_pairs

import os
import pandas as pd
import fileinput

## cut the variant_id into more informative pieces
os.chdir('C:/Users/wangj/Documents/Biology/Yale-CSC/Studies/CBB752 Biomedical Data Analysis $ Mining & Modeling/FinalProjects/Project1.2')
paths = os.listdir('.')
path = [p for p in paths if 'ZSNPs' in p]
for p in path:
    fname = p.split('.')[0]+'_sep.txt'
    tname = p.split('.')[0].split('_')[1]
    with open(fname, 'w') as f:
        for line in fileinput.input(p):
            words = line.strip('\t').split()
            if fileinput.isfirstline():
                word1 = ['chr','pos','ref','alt']
                wordn = 'tissue'
            else:
                word1 = words[0].split('_')[0:4]
                wordn = tname
            if tname in ['Liver','Pancreas']:
                f.write('\t'.join(word1+words[1:-1]+[wordn]+['\n']))
            else:
                f.write('\t'.join(word1+words[1:-2]+[wordn]+['\n']))

## get the intersect snp-gene_pairs of the tissues and print them out
folder = './GTEx_Analysis_v6p_eQTL'
path = [p for p in paths if 'ZSNPs' in p and 'sep' not in p and 'stat' not in p]
ints = dict()
for p in path:
    tname = p.split('.')[0].split('_')[1]
    tmut = pd.read_table(p,sep=' ')
    ints[tname] = set(tmut['variant_id'])
inset = set(tmut['variant_id'])
for k in ints.keys():
    inset = inset & ints[k]
inset = list(inset)
with open('ZSNPs_intersect.txt','w') as fi:
    firstline = '\t'.join(tmut.columns)+'\n'
    fi.write(firstline)
    for p in path:
        for line in fileinput.input(p):
            for i in inset:
                if i in line:
                    fi.write(line)
zint = pd.read_table('ZSNPs_intersect.txt')
zid = list(zint['variant_id'])
ind = sorted(range(len(zid)),key=lambda x:zid[x])
with open('ZSNPs_intersect_ordered.txt','w') as fo:
    fo.write(firstline)
    for j in range(len(ind)):
        jj = ind[j]
        line = '\t'.join(zint.loc[jj,'variant_id'].split())
        if '\"' in line:
            lines = line.split('\"')
            line = lines[0]+' '.join(lines[1].split())
        fo.write(line+'\n')

## get the statistics of the ZSNPs: tissues, numbers and percentages
folder = './GTEx_Analysis_v6p_eQTL'
path = [p for p in paths if 'ZSNPs' in p and 'sep' not in p]
with open('ZSNPs_statistics.txt','w') as fs:
    fs.write('\t'.join(['tissue','#zsnps','#snp-gene_paris','pct'])+'\n')
    for p in path:
        tname = p.split('.')[0].split('_')[1]
        zmut = pd.read_table(p,sep=' ')
        zmut = zmut.shape[0]
        tps = os.listdir(folder)
        tp = [t for t in tps if tname.split()[0] in t and 'signif' in t][0]
        tsnp = pd.read_table(os.path.join(folder,tp))
        tmut = tsnp.shape[0]
#        fname = p.split('.')[0]+'_sep.txt'
        pct = float(zmut)/tmut
        fs.write('\t'.join([tname,str(zmut),str(tmut),str(pct)])+'\n')

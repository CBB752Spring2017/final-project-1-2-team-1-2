---
layout: page
title: CBB752 Spring 2017
tagline: Final Project
---

Project Title
------------------
Compare the variants in Carl’s genome with those found in the GTEx database. Use the results to predict gene expression in various tissues and better estimate the impact of noncoding variants in Carl’s genome.

Table of Contents
-----------------------




**Contributors**
 -Writing:
 -Coding: Jiawei Wang
 -Pipeline:

### Introduction:





### Writing:








### Coding:

#### Documentation:
##### final1-2.2.py
Version 2. This is a tissue-specific version of last code. Added a -t tissue specifier to achieve that. Also, a time indicator (by the lines read) is added to estimate required time.

##### final1-2.3.py
Version 3. Here version 3 is literally the same with version 1 (because during polishing up version 1 becomes the same with 3). Integral code to run through all tissues. But not actually so much used in consideration of time.

##### final1-2.x.py
This code is not the code for generation of consistent records, but to analyze the generated records for general overview. It includes three parts:
  1. cut the variant_id into more informative pieces;
  2. get the intersect snp-gene_pairs of the tissues and print them out;
  3. get the statistics of the ZSNPs: tissues, numbers and percentages.

Since the files are large, they run not so fast. Maybe it would be faster to read in GTEx SNP records as dictionary and compare the two dictionaries, but hard to include the rest information (e.g. effect size).

##### Usage
The most useful version is version 2: tissue specific comparison between Zimmerome and GTEx eQTL record.

Command line example of final1-2.2.py:
> python final1-2.2.py -i <input folder> -m <mutation file> -t <tissue name> ###USAGE

> python final1-2.2.py -i GTEx_Analysis_v6p_eQTL -m Z.variantCall.SNPs_filt.vcf -t 'Whole_Blood' ###EXAMPLE

> ###eQTL analysis of Zimmerome

##### Requirement
Here I use Python 2.7. Files needed include Zimmerome SNP file (Z.variantCall.SNPs.vcf, from https://zimmerome.gersteinlab.org/2016/05/06/part01_gerstein/, but its comment was removed to generate a readable table), GTEx eQTL of different tissues (V6P, downloaded from GTEx portal, https://www.gtexportal.org/home/). 

#### Results:
Results divide into three parts:
 1. I ran the code on five tissues of GTEx database: Adipose Subcutaneous, Brain Cortex, Live, Pancreas and Whole Blood. In this way, I filtered out those Zimmerome SNPs that are recorded in GTEx eQTL database: ZSNPs_*_sep.txt
 2. I then generate the intersect of SNPs across the five tissues (existing in all the five tissues): ZSNPs_intersect.txt
 3. After that, I generate a statistical report to summarize the SNP information of these five tissues: ZSNPs_statistics.txt






### Pipeline:


#### Documentation:


#### Results:









#### Conclusions:








#### References:

 References can be included here or at the end of each relevant section.
 
 

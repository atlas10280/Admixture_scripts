# Admixture
This repository contains scripts used to plot results from Admixture.

Results were generated via the use of PGD Spider, Plink, and Admixture

Basic workflow:

1) Convert genepop file of SNP data to .ped
    make sure population delimiters are present

1.2) If you wish to run admixture on subsets of your data use the subset_PED.py program (I like to use Spyder as my IDE)
		See documentation within script for further instructions on how to use subset_PED.py
		for example input files, see ./example_data/"

2) Use Plink to produce .bed file
    e.g. >plink --file 'filename(no extension)' --make-bed

3) Run Admixture
    e.g. > admixture 'filename.bed' K_to_test(int)

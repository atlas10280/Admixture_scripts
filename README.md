# Admixture
This repository contains scripts used to plot results from Admixture.

Results were generated via the use of PGD Spider, Plink, and Admixture

Basic workflow:

1) Convert genepop file of SNP data to .ped
2) Use Plink to produce .bed file
    e.g. >plink --file 'filename(no extension)' --make-bed
3) Run Admixture
    e.g. > admixture 'filename.bed' K_to_test(int)

#! /bin/bash
for K in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
'/home/garrett/Documents/Source Files/admixture_linux-1.3.0/admixture' --cv ./v6_novoseq2_snps_genomic.bed $K | tee log${K}.out
done
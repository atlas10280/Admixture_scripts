# Admixture
This repository contains scripts used to plot results from Admixture.

Results were generated via the use of PGD Spider, Plink, and Admixture

Basic workflow:

1) Convert genepop file of SNP data to .ped using PGD spider (see .slurm and .spid, adjust path and names as needed)
    make sure population delimiters are present

1.2) If you wish to run admixture on subsets of your data use the subset_PED.py program (I like to use Spyder as my IDE)
		(adjust path and name of input/global PED file in the script, build whitelists with the suffix ".awl" (admixture whitelist), and it should work from there)
		See documentation within script for further instructions on how to use subset_PED.py		
		for example input files, see ./example_data/"

2) Use Plink to produce .bed file, for each .PED you convert (if running subsets) you need a .MAP with a matching prefix. 
	e.g. >plink --file 'filename(no extension)' --make-bed --noweb
		subset_PED.py should generate a .sh script to make a command for copying the .MAP with the correct prefix, adjust as needed or do by hand
		the plink outputs have, in my experience, been produced with "plink" prefix. 
		I've built the subset_PED.py program to also make batch scripts for quickly renaming these, adjust the code here for your system (these blocks are at the base of the script)
	

3) Run Admixture
    e.g. > admixture 'filename.bed' K_to_test(int)
	can loop, see example in admixture_1_15.sh
	you get 3*K outputs from admixture so consider running each subset in a subfolder

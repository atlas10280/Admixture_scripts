# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:16:02 2019

@author: mboot217

This script is designed to optimize the process of producing multiple subsets of your full data for heirarchical Admixture analyses
Consider running your admixture subsets in independent folders, as there will be at least k*3 files produced for each subset

        ############READ_ME##################
        
        For input you should take a genepop with all populations (reffered to as the global data) 
            delimited with "Pop\n" and convert this to .ped in PGD spider, this will also supply a .map file
        
        IMPORTANT: Both .ped and .map files should have the same name for admixture to properly run
        
        TO RUN THIS SCRIPT:
            1) Build whitelists of the populatons you wish to subset FOR EACH subset you wish to analyze. 
            
                IMPORTANT: this program identifies whitelists using 2 conditions
            
                A) The list is in the same directory as your global.ped
                B) The list is a .awl (admixture white list) extension 
                    e.g. whitelist_one.awl
                    
                NOTE: This program will always produce a subset for ALL available .awl files, 
                    so if you have some produced and wish to make new ones, hide the processed .awl files in a whitelist folder
            
                If you open the global.ped you will see the "pop_n" delimiter for each population. 
                Use these "pop_n" delimiters in your list (only supply one per pop) as the arguments (one pop per line) in the whitelists 
                    e.g. (5 pop global file "L_Superior", "L_Michigan", "L_Huron", "L_Erie", "L_Ontario")
                        subset1.awl (Superior, Huron)
                            "pop_1"
                            "pop_3"
                        subset2.awl (Michigan, Erie)
                            "pop_2"
                            "pop_4"
            2) Place these in the directory with the global.ped
            
            3) Change the input directory and global filename below, then run.
        
        #####################################
    
"""
###########INPUT REQUIRED#########

#provide the directory with your global.ped (should also contain global.map)
global_dir = "I:/WAE_RAD_Data/novoseq2/SNPs/Genomics/Admixture"

#provide the name and extension of your global.ped
global_filename = "v6_novoseq2_snps_genomic.ped"

##############################

#setting working directory == global_dir
import os
import re
os.getcwd()
os.chdir(global_dir)

#read in the global.ped file
global_PED_file = open(global_filename, "r")
global_PED = global_PED_file.readlines()
global_PED_file = global_PED_file.close()

#builds list of files in global_dir
file_list = os.listdir(global_dir)

#Loop through each file in global_dir
for filename in file_list:
    #if file is identified as a whitelist
    if filename.endswith(".awl"):
        
        #first make a file to write results to, this is one of our subsets
        out_name_n = re.sub(".awl","",filename)
        out_file_n = open(out_name_n + ".ped","w")
    
        #then open the whitelist and read in the lines, then close the file
        readFile = open(str(filename), "r")
        whitelist = readFile.readlines()
        readFile.close()
        #next, for each line (individual) in the global.ped, check if it matches any of the whitelisted pop_n delimiters
        #I choose to loop through the whitelist names second, as I can add a break to the loop and effectively reduce the number or iterations
        
        for individual in global_PED:
            for pop_n in whitelist:
                #this takes a line (individual) and breaks it down into just the pop_n prefix
                pop_n = pop_n.rstrip()
                ind_match = individual.rstrip().split(" ")
                ind_match = ind_match[0]
                
                #the line already has a \n appended so we don't need to tell the program to add a new line
                if ind_match == pop_n:
                    out_file_n.write(individual)
        
        out_file_n.close()        
        #This section builds a quick batch script to rename your plink outputs, 
        #as they will likely come out with "plink.bed" instead of "subset_n.bed"
        rename_out_name_n = out_name_n + "_rename_plinkOut"
        rename_script = open(rename_out_name_n + ".sh","w", newline='')
        rename_script.write("#! /bin/bash" + "\n")
        rename_script.write("mv ./plink.bim ./" + out_name_n + ".bim" + "\n")
        rename_script.write("mv ./plink.fam ./" + out_name_n + ".fam" + "\n")
        rename_script.write("mv ./plink.nosex ./" + out_name_n + ".nosex" + "\n")
        rename_script.write("mv ./plink.bed ./" + out_name_n + ".bed" + "\n")
        rename_script.write("mv ./plink.log ./" + out_name_n + ".log" + "\n")
        rename_script.close()
        #This section builds a quick batch script to copy your .map file with a name that matches your .ped for each subset, 
        #as they are required to have the same name for PLINK --make-bed
        copy_map_name_n = out_name_n + "copy_map"
        copy_map_script = open(copy_map_name_n + ".sh", "w", newline='')
        copy_map_script.write("#! /bin/bash" + "\n")
        ped_name = re.sub(".ped","",global_filename)
        copy_map_script.write("cp ./" + ped_name + ".map ./" + out_name_n + ".map")
        copy_map_script.close()

    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:47:16 2019

@author: aaronatkinson
"""

import glob, os

#Assign directory to change or us within directory
directory="/Users/aaronatkinson/Desktop/FoundationWorkUp/Foundation_072019/Vcfscopy2/F_clin_Filtered_VCFs/UpdatedVCFs"
path="/Users/aaronatkinson/Desktop/FoundationWorkUp/Foundation_072019/Vcfscopy2/F_clin_Filtered_VCFs/UpdatedVCFs"

#create filelist
for filename in glob.glob('**.vcf'):
    open(filename)
    with open (filename, 'r') as f_in:
        f_out = os.path.splitext(filename)[0]+"_clin.vcf"
        with open (f_out, 'w') as f_out2:
            for line in f_in:
                if "#" in line:
                    f_out2.write(line)
                elif "Foundation" in line:
                    f_out2.write(line)
                    
                
                
                         
                        
                
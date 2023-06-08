#! /usr/bin/env python3.8

"""
# File: RUN-U-histogram-from-NGCode.py
# Date: Tue 06 Jun 2023 07:14:19 AM +08

DESCRIPTION
Read a parametric NGC file.
Create a histogram in 10 bins (intervals) for u=0.0 to u=1.0
The 10 intervals 
RANGE_01 = [0.0, 0.1) = count lines (interpolated points in NGC file)
RANGE_02 = [0.1, 0.2) = count lines 
...
RANGE_09 = [0.8, 0.9) = count lines
RANGE_10 = [0.9, 1.0] = count lines
Write data to cnc_histogram.txt
Plot histogram using GNUplot

# NOTE 1: numpy version conflict for python3.9, use python3.8 OK
# NOTE 2: Python does not have a switch statement functionality.
#
"""
# INPFILE = "Algo20-TEARDROP-FC10-data_ngcode.ngc"
# OUTFILE = "Histo-Algo20-TEARDROP-FC10-data_ngcode.txt"

# INPFILE = "Algo20-TEARDROP-FC20-data_ngcode.ngc"
# OUTFILE = "Histo-Algo20-TEARDROP-FC20-data_ngcode.txt"

# INPFILE = "Algo20-TEARDROP-FC25-data_ngcode.ngc"
# OUTFILE = "Histo-Algo20-TEARDROP-FC25-data_ngcode.txt"

# INPFILE = "Algo20-TEARDROP-FC30-data_ngcode.ngc"
# OUTFILE = "Histo-Algo20-TEARDROP-FC30-data_ngcode.txt"

INPFILE = "Algo20-TEARDROP-FC40-data_ngcode.ngc"
OUTFILE = "Histo-Algo20-TEARDROP-FC40-data_ngcode.txt"


import numpy as np
## import datetime
from datetime import datetime

# =========================================================
# MAIN PROGRAM
# =========================================================
print("Bismillah Hirrahma Nirrahim WRY \n")
"""
## INPUT FILE
## INPFILE   = input("Enter  input  filename.txt: \t") 
## LINES_INP is a list with [] index range(0 to NUM_READ_LINES)
"""


INPUT_FILE_HDL  = open(INPFILE,'r')
LINES_INP       = INPUT_FILE_HDL.readlines()  
NUM_READ_LINES  = len(LINES_INP)
READ_RANGE      = range(0, NUM_READ_LINES, 1) 
print('Total lines in input file:\t', NUM_READ_LINES)

"""
## OUTPUT FILE
## OUTFILE  = input("Enter  output filename.txt: \t")
## output_file_HDL.write(line-to-write xxx)
"""
OUTPUT_FILE_HDL = open(OUTFILE,'w')

## INSPECT THE NGC CODE FILE
START_LINENUM = 13
END_LINENUM   = (NUM_READ_LINES - 6)
TOTAL_G01_LINES = (END_LINENUM - START_LINENUM) + 1
print('Total G01 lines to process:\t', TOTAL_G01_LINES)

LINE_RANGE_TOPROCESS = range(START_LINENUM, END_LINENUM + 1, 1) 

## INITIALIZATION
U_VAL = 2.0
count_G01_lines = 0

## INITIALIZE COUNTS
U_COUNT_TOTAL1 = 0
U_COUNT_TOTAL2 = 0
U_COUNT_TOTAL  = 0
U_COUNT_01 = 0 
U_COUNT_02 = 0
U_COUNT_03 = 0 
U_COUNT_04 = 0
U_COUNT_05 = 0 
U_COUNT_06 = 0
U_COUNT_07 = 0 
U_COUNT_08 = 0
U_COUNT_09 = 0 
U_COUNT_10 = 0
U_COUNT_UNKNOWN = 0


print("PROCESSING ... \n")
for currentline_num in range(START_LINENUM, END_LINENUM + 1, 1):
    
    ### CHECK FIRST COLUMN SHOULD BE "G01"
    readline_string = LINES_INP[currentline_num]
    if (readline_string[:3] == 'G01' and U_VAL != 1.0):
        ## print("LINE = ", currentline_num, " ", LINES_INP[currentline_num])
        ## print("line_as_list[7] = ", line_as_list[7])
        ## print("line_as_list[8] = ", line_as_list[8]) ## THIS ONE WRY
        ## print("line_as_list[9] = ", line_as_list[9])
        
        count_G01_lines = count_G01_lines + 1
        line_as_list = readline_string.split()
        U_VAL = float(line_as_list[8])
        ## print("line = ", currentline_num, " U_VAL = ", U_VAL, "\n")
        
    else:
        pass
        
    ## COLLECT COUNT INTO RESPECTIVE BIN INTERVALS
       
    if (0.00 <= U_VAL < 0.10):
        U_COUNT_01 = U_COUNT_01 + 1
        
    elif (0.10 <= U_VAL < 0.20):
        U_COUNT_02 = U_COUNT_02 + 1
        
    elif (0.20 <= U_VAL < 0.30):
        U_COUNT_03 = U_COUNT_03 + 1
          
    elif (0.30 <= U_VAL < 0.40):
        U_COUNT_04 = U_COUNT_04 + 1   
        
    elif (0.40 <= U_VAL < 0.50):
        U_COUNT_05 = U_COUNT_05 + 1
        
    elif (0.50 <= U_VAL < 0.60):
        U_COUNT_06 = U_COUNT_06 + 1
        
    elif (0.60 <= U_VAL < 0.70):
        U_COUNT_07 = U_COUNT_07 + 1   
        
    elif (0.70 <= U_VAL < 0.80):
        U_COUNT_08 = U_COUNT_08 + 1
        
    elif (0.80 <= U_VAL < 0.90):
        U_COUNT_09 = U_COUNT_09 + 1
        
    elif (0.90 <= U_VAL <= 1.00):
        U_COUNT_10 = U_COUNT_10 + 1       
   
    else: 
        U_COUNT_UNKNOWN = U_COUNT_UNKNOWN + 1
        print("U_COUNT_UNKNOWN = ", U_COUNT_UNKNOWN, " AT LINE = ", currentline_num)
        
U_TOTAL1 = U_COUNT_01 + U_COUNT_02 + U_COUNT_03 + U_COUNT_04 + U_COUNT_05
U_TOTAL2 = U_COUNT_06 + U_COUNT_07 + U_COUNT_08 + U_COUNT_09 + U_COUNT_10

U_COUNT_TOTAL  = U_TOTAL1 + U_TOTAL2    

print("U_COUNT_01 = \t", U_COUNT_01)
print("U_COUNT_02 = \t", U_COUNT_02)    
print("U_COUNT_03 = \t", U_COUNT_03)
print("U_COUNT_04 = \t", U_COUNT_04)
print("U_COUNT_05 = \t", U_COUNT_05)
print("U_COUNT_06 = \t", U_COUNT_06)
print("U_COUNT_07 = \t", U_COUNT_07)    
print("U_COUNT_08 = \t", U_COUNT_08)
print("U_COUNT_08 = \t", U_COUNT_09)
print("U_COUNT_10 = \t", U_COUNT_10)
print("U_COUNT_TOTAL   = ", U_COUNT_TOTAL)
        
print("count_G01_lines = ", count_G01_lines + 1)        

### CONCATENATE LINE TO WRITE AS A STRING
### BECAUSE write() TO FILE ONLY HAS ONE PARAMETER


the_now  = datetime.now() 
the_date = the_now.strftime("%Y-%m-%d")
the_time = the_now.strftime("%H:%M:%S")

line_str_A1 = "#  Date : " + the_date + "\n"
line_str_A2 = "#  Time : " + the_time + " MYT (+8 UTC)\n"
line_str_A3 = "#  Code : " + "RUN-U-Histogram-on-NGCode.py" + "\n"
line_str_A4 = "#  File : " + OUTFILE + "\n"

line_str_01 = " 1  U_COUNT_01   \t" + str(U_COUNT_01) + "\t\t\t 0.00      \t\t  0.10 \n"
line_str_02 = " 2  U_COUNT_02   \t" + str(U_COUNT_02) + "\t\t\t 0.10      \t\t  0.20 \n"
line_str_03 = " 3  U_COUNT_03   \t" + str(U_COUNT_03) + "\t\t\t 0.20      \t\t  0.30 \n"
line_str_04 = " 4  U_COUNT_04   \t" + str(U_COUNT_04) + "\t\t\t 0.30      \t\t  0.40 \n"
line_str_05 = " 5  U_COUNT_05   \t" + str(U_COUNT_05) + "\t\t\t 0.40      \t\t  0.50 \n"
line_str_06 = " 6  U_COUNT_06   \t" + str(U_COUNT_06) + "\t\t\t 0.50      \t\t  0.60 \n"
line_str_07 = " 7  U_COUNT_07   \t" + str(U_COUNT_07) + "\t\t\t 0.60      \t\t  0.70 \n"
line_str_08 = " 8  U_COUNT_08   \t" + str(U_COUNT_08) + "\t\t\t 0.70      \t\t  0.80 \n"
line_str_09 = " 9  U_COUNT_09   \t" + str(U_COUNT_09) + "\t\t\t 0.80      \t\t  0.90 \n"
line_str_10 = "10  U_COUNT_10   \t" + str(U_COUNT_10) + "\t\t\t 0.90      \t\t  1.00 \n"

line_str_11 = "#   U_COUNT_TOTAL   = " + str(U_COUNT_TOTAL) + "\n"
line_str_12 = "#   TOTAL_GO1_LINES = " + str(TOTAL_G01_LINES) + "\n"

## WRITE TO OUTPUT FILE  
OUTPUT_FILE_HDL.write("#  Bismillah Hirrahma Nirrahim \n")
OUTPUT_FILE_HDL.write(line_str_A1)
OUTPUT_FILE_HDL.write(line_str_A2)
OUTPUT_FILE_HDL.write(line_str_A3)
OUTPUT_FILE_HDL.write(line_str_A4)
OUTPUT_FILE_HDL.write("# \n")
OUTPUT_FILE_HDL.write("#  Brief description:\n")
OUTPUT_FILE_HDL.write("#  Counts of interpolated points over the independent parameter u \n")
OUTPUT_FILE_HDL.write("#  within the range of u-values [0.00, 1.00]. The sharp turns and corners \n")
OUTPUT_FILE_HDL.write("#  generates higher number of interpolated points due to shorter \n")
OUTPUT_FILE_HDL.write("#  chord lengths, i.e. to maintain error tolerance below 10(-6) mm. \n")
OUTPUT_FILE_HDL.write("# \n")
OUTPUT_FILE_HDL.write("#   U_COUNT_BIN   U_COUNT_VALUE  LOW  <=u-range<  HIGH \n")
OUTPUT_FILE_HDL.write(line_str_01)
OUTPUT_FILE_HDL.write(line_str_02)
OUTPUT_FILE_HDL.write(line_str_03)
OUTPUT_FILE_HDL.write(line_str_04)
OUTPUT_FILE_HDL.write(line_str_05)
OUTPUT_FILE_HDL.write(line_str_06)
OUTPUT_FILE_HDL.write(line_str_07)
OUTPUT_FILE_HDL.write(line_str_08)
OUTPUT_FILE_HDL.write(line_str_09)
OUTPUT_FILE_HDL.write(line_str_10)
OUTPUT_FILE_HDL.write("# \n")
OUTPUT_FILE_HDL.write(line_str_11)
OUTPUT_FILE_HDL.write(line_str_12)
OUTPUT_FILE_HDL.write("# \n")
OUTPUT_FILE_HDL.write("#  Note: Each line represents a single interpolated point.\n")

OUTPUT_FILE_HDL.write("#  Alhamdulillah Hirrabil Alamin \n")


INPUT_FILE_HDL.close()
OUTPUT_FILE_HDL.close()

print("\nAlhamdulillah Hirrabil Alamin WRY \n")  
## ========================================================
"""
EXECUTION
wruslan@HPLaptop-01-ub20:~/github/wruslancnc/CNC-Execution-Plan/python-tools/
histogram-from-NGC-Code$  ==>  python3 06-RUN-u-histogram-from-NGCode.py 

Bismillah Hirrahma Nirrahim WRY 

Total lines in input file:	 7368
Total G01 lines to process:	 7350
PROCESSING ... 

U_COUNT_01 = 	 749
U_COUNT_02 = 	 792
U_COUNT_03 = 	 794
U_COUNT_04 = 	 711
U_COUNT_05 = 	 628
U_COUNT_06 = 	 629
U_COUNT_07 = 	 711
U_COUNT_08 = 	 794
U_COUNT_08 = 	 791
U_COUNT_10 = 	 751
U_COUNT_TOTAL   =  7350
count_G01_lines =  7350

Alhamdulillah Hirrabil Alamin WRY 

wruslan@HPLaptop-01-ub20:~/github/wruslancnc/CNC-Execution-Plan/python-tools/histogram-from-NGC-Code$ 

"""


#! /usr/bin/env python3

# File: remove-line-in-file.py
# Date: wruslan@HPLaptop-01-ub20:~$ date
# Mon 05 Jun 2023 11:40:21 AM +08


# =========================================================
def fxn_remove_line(INPFILE, OUTFILE, lineToSkip):

    """ Removes a given line from a file """
    with open(INPFILE,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(OUTFILE,'w') as write_file:

        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
	
            currentLine += 1

## ========================================================
def fxn_total_lines_input_file(INPFILE):

    with open(INPFILE, 'r') as fpIN:
        x = len(fpIN.readlines())
        print('Total lines in input file:\t', x) 
    

## ========================================================
def fxn_total_lines_output_file(OUTFILE):

    with open(OUTFILE, 'r') as fpOUT:
        x = len(fpOUT.readlines())
        print('Total lines in output file:\t', x) 



# =========================================================
# MAIN PROGRAM
# =========================================================
print("Bismillah Hirrahma Nirrahim WRY \n")

## INPUT FILE
INPFILE         = input("Enter  input  filename.txt: \t")
INPUT_FILE_HDL  = open(INPFILE,'r')

## LINES_INP is a list with [] index range(0 to num-read-lines)
LINES_INP       = INPUT_FILE_HDL.readlines()  
NUM_READ_LINES  = len(LINES_INP)
READ_RANGE      = range(0, NUM_READ_LINES, 1) 

## OUTPUT FILE
OUTFILE         = input("Enter  output filename.txt: \t")
OUTPUT_FILE_HDL = open(OUTFILE,'w')
## output_file_HDL.write(line-to-write xxx)

## LINES REMOVED FILE
REMOVED_LINES     = input("Enter removed filename.txt: \t")
REMOVED_LINES_HDL = open(REMOVED_LINES,'w')
## removed_lines_HDL.write(line-to-write xxx)

print('Total lines in input file:\t', NUM_READ_LINES)

## RANGE OF LINE NUMBERS TO REMOVE
START_LINE   = int (input("Start line number to remove (int): "))
END_LINE     = int (input("End   line number to remove (int): "))
REMOVE_RANGE = range(START_LINE, END_LINE , 1)
NUM_LINES_TO_REMOVE = len(REMOVE_RANGE)
print('Total lines to remove in input file:\t', NUM_LINES_TO_REMOVE)

print("PROCESSING ... \n")
count_maintained_lines = 0
count_removed_lines    = 0

## for line_to_remove in REMOVE_RANGE:
    ## DEBUG
    ## print("\t To remove line number: \t", line_to_remove)  


for currentline_num in READ_RANGE:
    ## NOTE: LINES_INP is a list with [] index range(0 to num-read-lines)
    ## LINES_INP = INPUT_FILE_HDL.readlines()
    
    if currentline_num not in REMOVE_RANGE:
        ## print("currentline_num NOT INSIDE remove list \t", currentline_num)  
        print("\t MAINTAIN currentline_num: \t", currentline_num)  
        
        ## WRITE TO OUTPUT FILE    
        OUTPUT_FILE_HDL.write(LINES_INP[currentline_num])   
        count_maintained_lines = count_maintained_lines + 1
           
    if currentline_num in REMOVE_RANGE:
        ## print("currentline_num INSIDE remove list \t", currentline_num)            
        print("\t REMOVE currentline_num: \t", currentline_num )           

        ## WRITE TO REMOVED LINES FILE 
        REMOVED_LINES_HDL.write(LINES_INP[currentline_num])
        count_removed_lines = count_removed_lines + 1

print("\t Total REMOVED    lines: \t", count_removed_lines)    
print("\t Total MAINTAINED lines: \t", count_maintained_lines) 
print("\t Total INPUT      lines: \t", NUM_READ_LINES) 

INPUT_FILE_HDL.close()
OUTPUT_FILE_HDL.close()
REMOVED_LINES_HDL.close()

print("\nAlhamdulillah Hirrabil Alamin WRY \n")  
## ========================================================
"""
wruslan@HPLaptop-01-ub20:~/github/wruslancnc/SNAHYP-parametric-curve/SNAHYP-c-and-ngc-codes$ python3 03-RUN-remove-lines-in-file-INPfile-OUTfile.py 
Bismillah Hirrahma Nirrahim WRY 

Enter  input  filename.txt: 	input.txt
Enter  output filename.txt: 	output.txt
Enter removed filename.txt: 	removed.txt
Total lines in input file:	 8
Start line number to remove (int): 3
End   line number to remove (int): 6
Total lines to remove in input file:	 3
PROCESSING ... 

	 MAINTAIN currentline_num: 	 0
	 MAINTAIN currentline_num: 	 1
	 MAINTAIN currentline_num: 	 2
	 REMOVE currentline_num: 	 3
	 REMOVE currentline_num: 	 4
	 REMOVE currentline_num: 	 5
	 MAINTAIN currentline_num: 	 6
	 MAINTAIN currentline_num: 	 7
	 Total REMOVED    lines: 	 3
	 Total MAINTAINED lines: 	 5
	 Total INPUT      lines: 	 8

Alhamdulillah Hirrabil Alamin WRY 

wruslan@HPLaptop-01-ub20:~/github/wruslancnc/SNAHYP-parametric-curve/SNAHYP-c-and-ngc-codes$ 

"""


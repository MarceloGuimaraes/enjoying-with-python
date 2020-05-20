import sys,os
import argparse
import csv
from pyutil import filereplace
import json

def main(args):

    if not os.path.isfile(args.csvInputFile):
        sys.exit("File '{}' not found".format(args.csvInputFile))

    if args.csvInputFile is None: 
        sys.exit('Choose option -i and add the file input.') 

    input_file = args.csvInputFile
    dest_folder = os.path.dirname(input_file)
    input_filename = os.path.basename(input_file)
    (file, ext) = os.path.splitext(input_filename)
    
    output_file_replaced = file + "_replaced" + ext

    target_filepath = os.path.join(dest_folder, output_file_replaced).encode('UTF-8')

    search_replace(input_file,target_filepath)

    return 0;
    

def search_replace(file_input,target_file):
    print("file_input: {},  file_output: {}".format(file_input,target_file) );

    #filereplace(file_input,"\n","")
    #read input file
    fin = open(file_input, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('\n', '')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(target_file, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()

def montaParser():
    parser = argparse.ArgumentParser(description='Replace new line with blank space')
    parser.add_argument('--csvInputFile', '-i', required = True, help = "Input file to replace new line with blank space.")
    return parser.parse_args()

if __name__ == '__main__':
    args = montaParser()
    main(args)
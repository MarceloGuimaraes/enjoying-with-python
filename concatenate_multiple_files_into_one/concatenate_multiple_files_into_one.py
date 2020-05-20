import sys,os
import argparse
import fileinput
import glob
import pathlib
import shutil


EXTENSAO = "*.json"

def main(args):

    if not os.path.isdir(args.directory):
        sys.exit("File '{}' not found".format(args.directory))

    source_folder = args.directory
    
    listFileNames = glob.glob('./*.json')
   
    output_file_joined = "file_joined.json__"

    target_filepath = os.path.join(source_folder, output_file_joined).encode('UTF-8')
    
    with open(target_filepath,'wb') as wfd:
        for f in listFileNames:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
   

def montaParser():
    parser = argparse.ArgumentParser(description='Concatenate sql files')
    parser.add_argument('--directory', '-d', required = True, help = "input path to list files to join.")
    return parser.parse_args()

if __name__ == '__main__':
    args = montaParser()
    main(args)
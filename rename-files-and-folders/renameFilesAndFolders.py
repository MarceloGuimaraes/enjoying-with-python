import sys,os
import argparse


listExists=[]

def main(args):

    if not os.path.isdir(args.path):
        sys.exit("Path '{}' not found".format(args.path))

    if args.directory is None and args.files is None:
        sys.exit('Choose option -d to update directories and/or option -f to update filenames.') 

    search = args.search
    replace = args.replace

    for root, dirs, files in os.walk(args.path):    

        if args.directory:              
            for thedir in dirs:
                fullPath = os.path.join(root, thedir).encode('UTF-8')
                if search in thedir:
                    newNameDir = thedir.replace(search,replace)
                    fullPathNewNameFile = os.path.join(root,newNameDir)
                    if os.path.isdir(fullPathNewNameFile):
                        listExists.append(fullPathNewNameFile)
                    else:
                        os.rename(os.path.join(root, thedir),fullPathNewNameFile)


        if args.files:    
            for arquivo in files:
                fullPath = os.path.join(root, arquivo).encode('UTF-8')
                if search in arquivo:
                    newNameFile = arquivo.replace(search,replace)
                    fullPathNewNameFile = os.path.join(root,newNameFile)
                    if os.path.exists(fullPathNewNameFile):
                        listExists.append(fullPathNewNameFile)
                    else:
                        os.rename(os.path.join(root, arquivo),os.path.join(root,newNameFile))




def montaParser():
    parser = argparse.ArgumentParser(description='Search and rename char in files/folders')
    parser.add_argument('--directory', "-d",nargs="?", const = True, help = "Enable rename in directories")
    #parser.add_argument('--search', "-s", required = True, help = "word to search")
    #parser.add_argument('--replace', "-r", required = True, help = "word to replace")
    #parser.add_argument('--files', "-f", nargs="?", const = True, help = "Enable rename in files") 
    #parser.add_argument('--path', "-p", required = True, help = "path to search")


    return parser.parse_args()

if __name__ == '__main__':
    args = montaParser()
    main(args)
    print("Files that already exist")
    print(listExists, end=' ')
            
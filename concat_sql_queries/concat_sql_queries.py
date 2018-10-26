import sys,os
import argparse


def main(args):
    print(args)

    if not os.path.isdir(args.directory):
        sys.exit("Diretory '{}' not found".format(args.directory))

    if args.directory is None: 
        sys.exit('Choose option -d and directory.') 

    search = args.search
    path = args.directory

	#new file
    arquivoSql = open('Script_Queries.sql','w')

    for root, _, files in os.walk(path):
        for arquivo in files:
            if search in arquivo:
                fullPath = os.path.join(root, arquivo).encode('UTF-8')
                print(fullPath)
                arquivoSqlOpen = open(fullPath,'r')
                arquivoSql.write('-- ' + arquivo)
                for linha in arquivoSqlOpen:
                    arquivoSql.write(linha)
                arquivoSqlOpen.close()
                arquivoSql.write('-- novo arquivo \n')
                
    arquivoSql.close()



    

def montaParser():
    parser = argparse.ArgumentParser(description='Concatenate sql files')
    parser.add_argument('--directory', "-d",nargs="?", const = True, help = "Directory")
    parser.add_argument('--search', "-s", required = True, help = "word to search")


    return parser.parse_args()

if __name__ == '__main__':
    args = montaParser()
    main(args)
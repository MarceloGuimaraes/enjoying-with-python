import openpyxl

sheetIniciar='INICIAR'
projectName='GESTAO_VIGENCIA_CONTRATUAL'

file='C:\\DADOS\\projetos\\git\\enjoying-with-python\\working-with-excel\\02_SURF_Campos_Formularios_Alteracao_Vigencia_V06.xlsx'

#lendo o excel
book = openpyxl.load_workbook(file)

#total de sheets
sheet_number = len(book.worksheets)
#print(sheet_number)

dictSheets = {} 
sum = 1

for Worksheets in book.worksheets:
    dictSheets[Worksheets.title]=sum
    sum = sum + 1

#print o dicionario dict('INICIAR',4)
#print(dictSheets)

#posicao da sheet INICIAR
positionSheetIniciar = dictSheets.get(sheetIniciar)

print(positionSheetIniciar)


##### -> DE -> PARA -> TIPO CAMPO
#SIM OU NÃO:				[nvarchar](3) 
#ANEXO:					(max) 
#NÚMERO INTEIRO:			[int] 
#NÚMERO CNPJ:			[nvarchar](18) 
#TEXTO OBSERVAÇÃO:		[nvarchar](1000) 
#TEXTO RAZÃO SOCIAL:		[nvarchar](100) 
#TEXTO ENDEREÇO:			[nvarchar](100) 
#TEXTO BAIRRO:			[nvarchar](50) 
#TEXTO CIDADE:			[nvarchar](50) 
#TEXTO UMA LINHA:		[nvarchar](100)
#UF SELEÇÃO ÚNICA:		[int] 
#NÚMERO CEP:				[nvarchar](9) 
#ESCOLHA SELEÇÃO ÚNICA:	[int] 
#DATA:					[date]
#DATA DO REGISTRO:		[datetime]

#ler da sheet INICIAR em diante
for key, value in dictSheets.items():
    if value == positionSheetIniciar:
        print('worksheetName: ' + key)
        worksheet = book[key]
        print(worksheet)
        #here you iterate over the rows in the specific column
        for row in range(1,worksheet.max_row+1):  
            for column in "CAMPO":  #Here you can add or reduce the columns
                cell_name = "{}{}".format(column, row)
                worksheet[cell_name].value # the value of the specific cell



        


import openpyxl

sheetIniciar='INICIAR'

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

#ler da sheet INICIAR em diante
for key, value in dictSheets.items():
    if value >= positionSheetIniciar:
        print(key)




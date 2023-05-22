palavras = ('rap', 'rock', 'samba', 'paralelepipedo')
iPalavra = 0
iLetra = 0
contVogal = 0
while True:
    if palavras[iPalavra][iLetra] in 'aeiou':
        if contVogal < 1:
            print(f'\nA palavra {palavras[iPalavra].upper()} contem as vogais:', end=' ')
            contVogal += 1
        print(f'{palavras[iPalavra][iLetra]}', end=' ')
        iLetra += 1
    else:
        iLetra += 1
    if iLetra == len(palavras[iPalavra]):
        iPalavra += 1
        iLetra = 0
        contVogal = 0
    if iPalavra == len(palavras):
        break
print('\nFIM')
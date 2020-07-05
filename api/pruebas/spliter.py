
from Bio import SeqIO
# from model.fastaResult import FastaResult
# from model.fastaSequence import FastaSequence
from model.FastaResult import FastaResult
from model.FastaSequence import FastaSequence

my_file = "ejemCon2.fasta"
#my_file = "emptyFasta.fasta"

valid_characters = ['-', 'A', 'C', 'G','T']

fasta_sequences = SeqIO.parse(open(my_file),'fasta')

result = FastaResult(False, True, 0, [], "OK")

with open("out_file.fasta") as out_file:
    #print(str(result.isValid))
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)

        print(sequence)

        if( result.isValid ):

            validSequence = True
            # con esto valido que todos los caracteres de la secuencia esten dentro de los permitidos, sino lo marco invalido
            for char in sequence:
                validSequence = validSequence and char in valid_characters
        
            if(not validSequence):
                result.isValid = False
                result.message = "El archivo esta corrupto, encontramos dentro de las secuencias elementos que no son nucleótidos"
                break
        
        # si detecto que dentro de la secuencia hay un '-' asumo que esta alineado. Con encontrar uno, ya no lo vuelvo a evaluar
        if( not result.isAlign and "-" in sequence ):
            result.isAlign = True
        
        # instancio un FastaSequence con su header y body respectivamente 
        sequ = FastaSequence(name, sequence)
        # agrego el FastaSequence a la lista del FastaResult
        result.sequences.append(sequ)
        #print(sequ.header)
        print(sequ.body)

    print(len(result.sequences))
    print("msg: " + result.message)
    print(str(result))







# 1)Validar Rebotar el archivo:
# Distintas las  cantidad de signo con secuencias
# Hay  una sequencia que no es nucleotido 
# La extension no es .fasta 
# Cantidad de secuencias a menor 3 y mayor a 600



    
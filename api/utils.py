from Bio import SeqIO, AlignIO
from Bio.Align.Applications import ClustalwCommandline
from .fastaResult import FastaResult
from .fastaSequence import FastaSequence
import os
import decimal
from django.conf import settings

def readSequence(pathFasta):
        valid_characters = ['-', 'A', 'C', 'G', 'T']
        fasta_sequences = SeqIO.parse(open(pathFasta), 'fasta')
        num = len([1 for line in open(pathFasta) if line.startswith(">")])
        result = FastaResult(False,True, num, [], "OK","")
        with open(pathFasta) as out_file:
            count_sequences=0
            for fasta in fasta_sequences:
                name, sequence = fasta.id, str(fasta.seq)

                #print(sequence)

                if( result.isValid ):
                    validSequence = True
                # con esto valido que todos los caracteres de la secuencia esten dentro de los permitidos, sino lo marco invalido
                    for char in sequence:
                        validSequence = validSequence and char in valid_characters
                count_sequences= count_sequences + 1  
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
                print(sequ.header)
                print(sequ.body)
        #result.isValid= num == count_sequences
        #result.message = "No coincide la cantidad de headers con la secuencias que tiene el archivo"
        print(result.isValid)
        # print("msg: " + result.message)
        # print(str(result))
        return result
    

    
def generateAlignamient(pathFasta):
        outfilePath = os.path.join(settings.ALIGNAMENT_ROOT, pathFasta.split(sep='/')[8]) # Revisar si se puede mejorar esto        
        result = readSequence(pathFasta)
        if( not result.isAlign and result.isValid):
            cline = ClustalwCommandline("clustalw2", infile=pathFasta,outfile=outfilePath)
            cline()
            result.alignroute = outfilePath
        elif ( result.isAlign and result.isValid):
               result.alignroute = pathFasta
        else:
             pass         
        return result

def convertPathFastaTOAln(path):
      newpath  = os.path.splitext(path)[0]+".aln"
      return newpath    

def getNameHeader(header) :
    aux = header.split(sep='|')
    return aux[0]

def getLatitud(header):
    aux = header.split(sep='|')
    return is_valid_lat(aux[1])


def getLongitud(header):
    aux = header.split(sep='|')
    return is_valid_lon(aux[2])

def getID(header) :
    aux = header.split(sep='|')
    return aux[3]


def is_valid_lon(lon):
    try:
        londec = decimal.Decimal(lon)
        if londec >= -180 and londec <= 180:
            return londec
        else:
            print("Es correcto el formato,no esta entre los rangos solicitados")
            return None
    except Exception as e:
        print("falllloooooo!!!LATITUD {} por: {}".format(lon, str(e)))
        return None


def is_valid_lat(lat):
    try:
        latdec = decimal.Decimal(lat)
        if latdec >= -90 and latdec <= 90:
            return latdec
        else:
            print("Es correcto el formato,no esta entre los rangos solicitados")
            return None
    except Exception as e:
        print("falllloooooo!!!LATITUD {} por: {}".format(lat, str(e)))
        return None
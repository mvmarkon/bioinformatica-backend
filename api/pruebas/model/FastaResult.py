


class FastaResult(object):

    isAlign = False
    isValid = True
    cantSymbols = 0
    sequences = []
    message = ""


    #def _init_():



    def __init__(self, isAlign, isValid, cantSymbols, sequences, message):
        self.isAlign = isAlign
        self.isValid = isValid
        self.cantSymbols = cantSymbols
        self.sequences = sequences
        self.message = message


    
    # def make_fastaResult(isAlign, isValid, cantSymbols, sequences):
    #     fastaResult = FastaResult(isAlign, isValid, cantSymbols, sequences)
    #     return fastaResult

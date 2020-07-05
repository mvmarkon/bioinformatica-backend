from Bio import SeqIO

my_file = "ejem.txt"  # Obviously not FASTA

def is_fasta(filename):
    with open(filename, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        print "algo.."
        return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

is_fasta(my_file)
# False
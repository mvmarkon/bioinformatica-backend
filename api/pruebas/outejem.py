
from Bio import SeqIO

my_file = "ejemCon2.fasta"

fasta_sequences = SeqIO.parse(open(my_file),'fasta')
with open("out_file.fasta") as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        #new_sequence = some_function(sequence)
        print(name)
        print(sequence)
        #write_fasta(out_file)
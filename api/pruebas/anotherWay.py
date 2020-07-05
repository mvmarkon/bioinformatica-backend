
my_file = "ejemCon2.fasta" 

def is_fasta(filename):
    with open("Fasta/ejemCon2.fasta") as handle:
        for record in FastaIterator(handle):
            print(record.id)

is_fasta(my_file)

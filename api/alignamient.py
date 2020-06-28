from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import Entrez

seqArray=[]

for seq_record in SeqIO.parse("SecuenciasCytocromoC.fasta", "fasta"):
    print(seq_record)
    seqArray.append(seq_record)


Entrez.email = "cuococarlos@gmail.com"
handle = Entrez.efetch(db="accession", id=seqArray[0].id, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()


#print("charlie")
#print(seqArray[0].id)
#print(record)
for a in pairwise2.align.globalxx(seqArray[0], seqArray[1]):
     print(format_alignment(*a,full_sequences=False))
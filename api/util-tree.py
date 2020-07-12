import subprocess

process = subprocess.Popen(['iqtree','-s', '/home/charlie/facultad/BioIng/bioinformatica-backend/uploaded/align/seqs_ejemplo_jLo3dEC.fst'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout, stderr

#from utils import show_file

#alignment = "align/seqs_ejemplo.fasta"
#tree = ""

# Open tree and link alignment to it
#t = PhyloNode(tree)
#t.link_to_alignment(alignment)
#
#show_file(alignment)
#show_file(tree)
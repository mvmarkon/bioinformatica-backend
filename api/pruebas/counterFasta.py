
my_file = "ejemCon2.fasta" 

num = len([1 for line in open("test_fasta.fasta") if line.startswith(">")])

print(num)
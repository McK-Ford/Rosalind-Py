ros_file = 'rosalind_rna.txt'
f        = open(ros_file)
DNA_str  = f.read()
RNA_str = DNA_str.replace("T","U")
txt_f = open("outputpy.txt", "w")
txt_f.write(RNA_str)
txt_f.close()

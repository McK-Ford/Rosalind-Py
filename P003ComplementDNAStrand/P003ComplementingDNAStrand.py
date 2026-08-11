ros_file = 'rosalind_revc.txt'
f        = open(ros_file)
DNA_str  = f.read()

revcomp_str = DNA_str.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

txt_f = open("outputpy.txt", "w")
txt_f.write(revcomp_str)
txt_f.close()

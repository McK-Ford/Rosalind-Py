ros_file = 'rosalind_dna.txt'
f        = open(ros_file)
DNA_str  = f.read()
a_cnt = 0
g_cnt = 0
c_cnt = 0
t_cnt = 0
for char in DNA_str:
    if   char == "A":
        a_cnt += 1
    elif char == "G":
        g_cnt += 1
    elif char == "C":
        c_cnt += 1
    elif char == "T":
        t_cnt += 1
cnt_str = str(a_cnt) + " " + str(c_cnt) + " " + str(g_cnt) + " " + str(t_cnt)
txt_f = open("outputpy.txt", "w")
txt_f.write(cnt_str)
txt_f.close()

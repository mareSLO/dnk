infile = open('C:/Users/metka/PycharmProjects/Phyton_Vaje/vaja6/dna.txt')
outfile = open('C:/Users/metka/PycharmProjects/Phyton_Vaje/vaja6/krivec.txt', 'w')
outfile.write('Krivec je Miha!\n')


replacements = {'CCAGCAATCGC':'Crna', 'GCCAGTGCCG':'Rjava', 'TTAGCTATCGC':'Korencek', "GCCACGG" : "Kvadraten", "ACCACAA" : "Okrogel", "AGGCCTCA" : "Ovalen", "TTGTGGTGGC" : "Modra", "GGGAGGTGGC" : "Zelena", "AAGTAGTGAC" : "Rjava", "TGCAGGAACTTC" : "Moski", "TGAAGGACCTTC" : "Zenska", "AAAACCTCA" : "Belec", "CGACTACAG" : "Crnec", "CGCGGGCCG" : "Azijec"}

for line in infile:
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)
infile.close()
outfile.close()
print("Za razultat poglejte fajl krivec.txt")
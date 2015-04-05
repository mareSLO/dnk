datoteka = open("dna.txt", "r")
dna = datoteka.read()

Crni_lasje = "CCAGCAATCGC"
Rjavi_lasje = "GCCAGTGCCG"
Korencek = "TTAGCTATCGC"

Moski = "TGCAGGAACTTC"
Zenska = "TGAAGGACCTTC"

Belec = "AAAACCTCA"
Crnec = "CGACTACAG"
Azijec = "CGCGGGCCG"

Modre_oci = "TTGTGGTGGC"
Zelene_oci = "GGGAGGTGGC"
Rjave_oci = "AAGTAGTGAC"

Kvadraten_obraz = "GCCACGG"
Okrogel_obraz = "ACCACAA"
Ovalen_obraz = "AGGCCTCA"

if dna.count(Moski) and dna.count(Belec) and dna.count(Korencek)\
        and dna.count(Rjave_oci) and dna.count(Okrogel_obraz) == 1:
    print("Ziga je ukradel sladoled!")

elif dna.count(Moski) and dna.count(Belec) and dna.count(Crni_lasje)\
        and dna.count(Modre_oci)and dna.count(Ovalen_obraz) == 1:
    print("Matej je ukradel sladoled!")

elif dna.count(Moski)and dna.count(Belec) and dna.count(Rjavi_lasje)\
        and dna.count(Zelene_oci)and dna.count(Kvadraten_obraz) == 1:
    print("Miha je ukradel sladoled!")
else:
    print("Tat se spretno izogiba rokam pravice!")

print("Kaj sem v posodi pustil zlico, opica ena!!!")
print("Roke prekriza za hrbet, ter se pusti odvesti v kiblo.")

datoteka.close()
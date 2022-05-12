from propy import PyPro
from propy import AAComposition

# dosyanın içeriğinde değişiklik gerekecek :))
dosya = open("ACC.txt", "r", encoding="utf-8")
dosya2 = open("noneff.txt", "a", encoding="utf-8")

for line in dosya:
    if ('>') in line:
        continue
    else:
        DesObject = line  # construct a GetProDes object
        print(DesObject)
        protein = line
        result = AAComposition.CalculateAAComposition(protein) #AAC İÇİN
        #result = AAComposition.CalculateDipeptideComposition(protein)  # DPC İÇİN
        dosya2.writelines(str(result.values()))
        #print(result.values())
        dosya2.write(",noneff")
        dosya2.write("\n")
dosya.close()
#Program to know how much solvent to put in fractions for tests (bioassay, LCMS, etc.)

#a- the general idea
print("""-------------- Alliquot Calculator --------------
""")
# sampleMass = input("What is the mass of your sample in grams? ")
fractionNumber = input("How many fractions do you have?")
# sampleConcentration = input("What concentration do you need to dilute your sample in? (mg/ml) ")

# sampleMassmg = int(sampleMass)*1000

# print("Sample mass in mg: ", int(sampleMassmg), "mg")
# print("Amount of solvent needed in uL: ", (int(sampleMassmg)/int(sampleConcentration))*1000, "uL")

#notes- b- multiple inputs

a,b,c,d,e,f,g,h,i,j,k,l= input("What is the mass of your 12 samples in grams? ").split()


AsampleMassmg = int(a)*1000
BsampleMassmg = int(b)*1000
CsampleMassmg = int(c)*1000
DsampleMassmg = int(d)*1000
EsampleMassmg = int(e)*1000
FsampleMassmg = int(f)*1000
GsampleMassmg = int(g)*1000
HsampleMassmg = int(h)*1000
IsampleMassmg = int(i)*1000
JsampleMassmg = int(j)*1000
KsampleMassmg = int(k)*1000





print("The masses of your",fractionNumber, "samples in mg are below:")
print("""
| Fraction | Mass (mg) | Solvent Needed (uL) | """)

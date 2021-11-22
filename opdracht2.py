pemmican = float(input('hoeveel kosten de pemmican repen? '))
pAantal = 6
vijgen = float(input('hoeveel kosten de vijgen repen? '))
vAantal = 3
biscuit = float(input('hoeveel kosten de biscuits? '))
bAantal = 2
vuurmakers = float(input('hoeveel kosten de  vuurmakers? '))
vuurmakerAantal = 2
lucifers = float(input('hoeveel kosten de lucifers? '))
lAantal = 5
vuursteen = float(input('hoeveel kosten de vuurstenen? '))
vuursteenAantal = 4
sisaltouw = float(input('hoeveel kost het sisaltouw? '))
sAantal = 20

berekening = (pemmican / 4) * pAantal * 5 + (vijgen * vAantal * 5) + (biscuit * bAantal) + (vuurmakers * vuurmakerAantal) + (lucifers * lAantal) + (vuursteen * vuursteenAantal) + (sisaltouw / 2) * sAantal

print(round(berekening, 2))

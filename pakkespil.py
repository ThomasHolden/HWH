import random


antal_6 = 0
antal_66 = 0
sidst_6 = False

print('Pakkespilsberegner v. 1.0')
print('(C) HWH Productions')
print('Beregneren simulerer et pakkespil ')

antal = int(input('Antal slag:'))


for i in range(antal):
	slag = random.randint(1,7)
	print (slag)
	if slag == 6:
		antal_6 = antal_6 + 1
		if sidst_6 == True:
			antal_66 = antal_66 +1
			print('Du har slået 2 seksere i træk!')
		sidst_6 = True
		print('Du har slået en sekser!')
	else:
		sidst_6 = False
print('<< Resultater >>')
print('Du har slået ' + str(antal_6) + " seksere ud af " + str(antal) + ' slag')
print('Sandsynlighed: ' + str((antal_6/antal)*100) + '%')
print('Du har fået 2 seksere i træk ' + str(antal_66) + ' gange')
print('Tak fordi du brugte HWH Productions som din IT-leverandør')

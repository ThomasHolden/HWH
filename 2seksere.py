import random
print('[HWH Pakkespilssimulator v. 1.1]')
def menuvalg():
    valg = input('''-=Menu=-
1: Lav simulering
2: afslut
Valg: ''')
    if int(valg) == 1:
        side = int(input('Vælg en side (1-6): '))
        dd_total = int(input('Hvor mange gange vil du slå en ' + str(side) + "'er 2 gange i træk? "))
        simulering(side,dd_total)
        menuvalg()    
    elif int(valg) == 2:
        print('Tak fordi at du valgte HWH!')
    else:
        print('Ugyldigt valg')
        menuvalg()

def simulering(side,dd_total):
    print('Starter simulering... ')
    dd_antal = 0
    side_antal = 0
    kast = 0
    sidste_side = False
    
    while dd_antal < dd_total:
        kast = kast + 1
        slag = random.randint(1,7)
        
        if slag == side:
            print('[' + str(slag) + ']', end=' ')
            side_antal = side_antal + 1
            if sidste_side == True:
                dd_antal = dd_antal +1
                sidste_side = False
            else:
                sidste_side = True
        else:
            sidste_side = False
            print(str(slag), end=' ')
    print('\nTotal antal kast: ' + str(kast))
    print('Total antal ' + str(side) + "'ere: " + str(side_antal))
    print('Antal ' + str(side) + "'ere 2 gange i træk: " + str(dd_antal))
    input('Tryk på en tast for at fortsætte...')

menuvalg()

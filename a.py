#Programma, kura varētu palīdzēt gatavošanai čempionātam
# 30.11.2021
#Aeksisis Pocs 10.a

#kā strādā programma?
#1 ievada dotos trenera datus
#2 lietotājs aktivizē programmu
#3 lietotājs dara visu sekojot programmas norādījumiem
#4 lietotājs saņem atskaiti, kuru viņš var nodot trenerim/tiesnesim

import time

def trenins(veids,daudzums,ilgums,maksa):
    print('Labdien, Veiksmi trenina! ')
    veidss = input('Ievadiet trenina veidu ')
    daudzumss = input('Ievadiet cik reizes jaaizdara? ')
    ilgumsss = input('Ievadiet cik ilgu laiku jus trenesieties? (minutes) ')
    maksaa = input('Cik maksas trenins par vienu treninu (centi) ')

    veids = veidss
    daudzums = int(daudzumss)
    ilgums = int(ilgumsss)
    maksa = int(maksaa)

    maksa = ilgums * maksa / 100
    #print(f'{veids} trenins jaaizdara {daudzums} reizes,{ilgums} minutes, kopsumma ir {maksa} eiro')
    ilgums = ilgums * 60
    print('')
    print('ja atbilde ir ja - rakstiet ja, ja ne, tad ne')
    sakums = input('Sakt? ')
    sakums = sakums.lower()
    if sakums == 'ja':
        for i in range(ilgums):
            ilgumss = ilgums - i
            print(f'atlika: {ilgumss} sek')
            time.sleep(1)

        
        ilgums = ilgumsss
        print(f'jus izdarijat {veids} treninu {daudzums} reizes,{ilgums} minutes, kopsumma ir {maksa} eiro')
    else:
        print('')



#ilgums jaaievada minutes, maksa centos
trenins('a',1,1,1)
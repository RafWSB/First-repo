import string, matplotlib as mpl;


#Jeden akapit lorem
txt1 = open("text1.txt", "r").read()
#Ten sam akapit lorem + dodatkowe znaki białe, cyfry, znaki specjalne, słowa w zdaniach mają zamienioną kolejność.
# txt2 = open("text2.txt", "r").read()
# Drugi plik którym można zastąpić txt2. Akapit lorem wygenerowany na nowo. całkiem inny.
txt2 = open("text3.txt", "r").read()

#---------- Funkcje usuwające z tekstu zbędne znaki białe, cyfry i znaki specjalne w tym kropki ------------
def usun_znaki_biale(content):
    content = content.replace("\t", " ")
    content = content.replace("\n", " ")
    while "  " in content:
        content = content.replace("  ", " ")
    return content







def usun_znaki_specjalne(content):
    for special in string.punctuation:
        content = content.replace(special, "")
    return content








def usun_cyfry(content):
    for i in range(ord("0"), ord("9") + 1):
        content = content.replace(chr(i), "")
    return content






#-------- Funkcje dzielące teksty na słowa i zdania -------------------------------------------
def podzial_na_slowa(content):
    content = usun_znaki_biale(content)
    content = usun_znaki_specjalne(content)
    content = usun_cyfry(content)
    lista = content.split(" ")
    return lista






def podzial_na_zdania(content):
    content = usun_znaki_biale(content)
    content = usun_cyfry(content)
    lista = content.split(".")
    return lista







#------- Funkcja dzieląca teksty na pojedyncze słowa i sprawdzająca ile słów sie powtarza ------
def skanuj_pojedyncze_slowa(txt1, txt2):
    txt1_slowa = podzial_na_slowa(txt1)
    txt2_slowa = podzial_na_slowa(txt2)
    # print(txt1_slowa)
    # print(txt2_slowa)
    kopia_slowo = 0
    for i in txt1_slowa:
        for j in txt2_slowa:
            if i == j:
                kopia_slowo = kopia_slowo + 1
                break

    print('Ilość słow w tekście nr 1: '+str(len(txt1_slowa)))
    print('Ilość słow w tekście nr 2: ' + str(len(txt2_slowa)))
    print('Ilość słow które sie powtarzają: '+ str(kopia_slowo))
    return ''

# skanuj_pojedyncze_slowa(txt1, txt2)

#------ Funkcja dzialąca teksty na zdania i sprawdzająca słowa w pojedynczych zdaniach --------
def skanuj_pojedyncze_zdania(txt1, txt2):
    txt1_zdania = podzial_na_zdania(txt1)
    txt2_zdania = podzial_na_zdania(txt2)
    for i in range(0, len(txt1_zdania)):
        print('Zdanie nr: ' + str(i + 1))
        skanuj_pojedyncze_slowa(txt1_zdania[i], txt2_zdania[i])

skanuj_pojedyncze_zdania(txt1, txt2)
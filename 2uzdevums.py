import csv

def lasit_un_drukāt_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r') as fails:
            csvlasītājs = csv.reader(fails)
            
            #izdrukā tikai otro kolonnu
            for rinda in csvlasītājs:
                if len(rinda) >= 2:
                    print(rinda[2])
    except FileNotFoundError:
        print(f"Kļūda: Faila '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Radusies kļūda: {e}")

# Aizstājiet 'piemers.csv' ar vēlamo CSV faila nosaukumu
lasit_un_drukāt_otro_kolonnu('piemers.csv')

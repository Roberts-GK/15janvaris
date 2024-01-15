def ievadīt_un_ierakstīt_failā(faila_nosaukums):
    try:
        # Lietotāja vārda ievade
        lietotāja_vārds = input("Ievadiet savu vārdu: ")

        # Faila rakstīšana
        with open(faila_nosaukums, 'Vārds') as fails:
            fails.write(lietotāja_vārds)

        print(f"Vārds '{lietotāja_vārds}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
    except FileNotFoundError:
        print(f"Kļūda: Faila '{faila_nosaukums}' nav atrasts.")
    except PermissionError:
        print(f"Kļūda: Nav atļaujas rakstīt failā '{faila_nosaukums}'.")
    except Exception as e:
        print(f"Radusies kļūda: {e}")

# Aizstājiet 'lietotajs.txt' ar vēlamo faila nosaukumu
ievadīt_un_ierakstīt_failā('lietotajs.txt')

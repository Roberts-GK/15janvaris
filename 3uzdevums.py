def lasit_un_drukāt_trešo_rindu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            # Nolasīt visas rindas
            visas_rindas = fails.readlines()
            
            # Pārbaudīt, vai ir pietiekami daudz rindu
            if len(visas_rindas) >= 3:
                # Izdrukāt trešo rindu (indekss 2, jo indeksācija sākas no 0)
                print("Trešās rindas saturs:")
                print(visas_rindas[2])
            else:
                print(f"Failā '{faila_nosaukums}' ir mazāk par 3 rindām.")
    except FileNotFoundError:
        print(f"Kļūda: Faila '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Radusies kļūda: {e}")

# Aizstājiet 'piemers.txt' ar vēlamo faila nosaukumu
lasit_un_drukāt_trešo_rindu('piemers.txt')

def lasit_un_drukāt_failu(faila_nosaukums):
    try:
        # Atver failu teksta lasīšanai
        with open(faila_nosaukums, 'r') as fails:
            # Nolasa faila saturu
            saturs = fails.read()
            
            # Izdrukā faila saturu
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Faila '{faila_nosaukums}' nav atrasts.")
    except Exception as f:
        print(f"Radusies kļūda: {f}")

# vēlamais faila nosaukums
lasit_un_drukāt_failu('piemers')

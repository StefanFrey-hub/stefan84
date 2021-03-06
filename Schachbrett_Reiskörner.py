import matplotlib.pyplot as plt
summe = 0
feldListe = []


for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damit insgesamt \
            {summe:>30,} Reiskörner") 
        
gewicht = summe * 0.02 / 1000000
print()
print(f"Wenn ein Reiskorn 0,02 Gramm wieg, wiegen die gesamten"\
    f"Reiskörner {gewicht:,.0f} Tonnen")


plt.plot(feldListe)
plt.show()
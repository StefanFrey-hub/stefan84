summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("Feld {}. = {:>30,} Reiskörner und damit insgesamt \
            {:>30,} Reiskörner" \
        .format(feld+1,reiskorn,summe))

gewicht = summe * 0.02 / 1000000
print()
print("Wenn ein Reiskorn 0,02 Gramm wieg, wiegen die gesamten"\
    "Reiskörner {:,.0f} Tonnen".format(gewicht))
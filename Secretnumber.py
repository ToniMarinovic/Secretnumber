secret=5



guess=int (raw_input ("Unesi neki broj:"))
if guess !=  secret:
    print ("Odabrali ste krivi broj!")
elif guess == secret:
    print ("Pogodili ste skriveni broj!")

from time import sleep

txt = input("Please enter the name of the file! (without '.txt') ")
txt = txt + ".txt"

while True:
    try:
        open(txt, 'r')
        print("(File was found!)")
        break
    except FileNotFoundError:
        print("\t|| Oh no!")
        print("\t|| The file you gave me doesn't exist or the folder in which the ascii-to-badusb.py file is doesn't contains the file!")
        print("\t|| Please try again!")
        txt = input("Please enter the name of the file again! (without '.txt') ") + '.txt'

while True:
    save = input("Do you want to have a save at the end of the scipt? (Y/N) ")
    if save == "Y" or save == "y" or save == "Yes" or save == "yes" or save == "YES":
        save = True
        break
    elif save == "N" or save == "n" or save == "No" or save == "no" or save == "NO":
        save = False
        break
    else:
        print("Sorry I couldn't read that. Please try again")

cuts = []

with open(txt, 'r') as file:
    for i in file:
        i.split()
        cuts.append(i)

output = txt[slice(-4)] + "-ascii.txt"

print('Working...')
sleep(0.1)
print('       ?000000000?       ')
sleep(0.1)
print('    ?0?           ?0?    ')
sleep(0.1)
print('   %=               =%   ')
sleep(0.1)
print(' =%                   %= ')
sleep(0.1)
print(' %   0     =%      %   % ')
sleep(0.1)
print('%    0    ?0&      %    %')
sleep(0.1)
print('&    0   %? &      %    &')
sleep(0.1)
print('&    0  %   &      %    &')
sleep(0.1)
print('&    0      &      %    &')
sleep(0.1)
print('%    &      &      &    %')
sleep(0.1)
print(' %   ?0     &     %=   % ')
sleep(0.1)
print(' =%   =%?   &   ?%=   %= ')
sleep(0.1)
print('   %=   =000%000=   =%   ')
sleep(0.1)
print('    ?0?           ?0?    ')
sleep(0.1)
print('       ?000000000?       ')
sleep(0.1)

with open(output, 'w', encoding="utf-8") as out:
    print(f"REM Let's print a little {txt[slice(-4)]} to the screen!", file=out)
    print("DELAY 500", file=out)
    print("GUI R", file=out)
    print("DELAY 200", file=out)
    print("STRING notepad", file=out)
    print("ENTER", file=out)
    print("DELAY 300", file=out)
    for i in cuts:
        print("ENTER", file=out)
        print("STRING", end=" ", file=out)
        print(i, end="", file=out)
    print("", file=out)
    print("ENTER", file=out)
    if save:
        print("CONTROL S", file=out)
        print(f"STRING {txt[slice(-4)]}-hello", file=out)
        print("ENTER", file=out)
        print("ENTER", file=out)
        print("CONTROL S", file=out)

print(f"The ascii art was successfully written to the {output} file.")
print("")
input("Press any key on your keyboard to exit")
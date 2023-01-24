from pick import pick
import tkinter as tk
import tkinter.font as font

#Płeć

title = 'Wybierz płeć'
options = ['Kobieta', 'Mężczyzna']
option, index = pick(options, title)

#Wzrost

title1 = 'Napisz swój wzrost'
wzrost = int(input('Twój wzrost w cm : '))

#Wiek

title2 = 'Ile masz lat '
wiek = int(input("Twój wiek : "))

#Waga

title3 = 'Ile masz wagi'
waga = int(input('Twoja waga w kg : '))

#PAL

title4 = 'Wybierz swoje PAL'
options1 = ['Brak aktywności fizycznej','Niska aktywność fizyczna','Umiarkowana aktywność fizyczna','Wysoka aktywność fizyczna','Bardzo wysoka aktywność fizyczna']
option1,index1 = pick(options1, title4)
if option1 == 'Brak aktywności fizycznej':
    przelicznik=1.2
elif option1=='Niska aktywność fizyczna':
    przelicznik=1.55
elif option1=='Umiarkowana aktywność fizyczna':
    przelicznik=1.86
elif option1=='Wysoka aktywność fizyczna':
    przelicznik=2.2
elif option1=='Bardzo wysoka aktywność fizyczna':
    przelicznik=2.5

#BMR

if option==('Kobieta'):
    płeć='Kobieta'
    bmr=655+(9.6*waga)+(1.8*wzrost)-(4.7*wiek)
    bmr=bmr*przelicznik
    print(f'Twoje zapotrzebowanie kaloryczne wynosi: {bmr}')
elif():
    płeć='Mężczyzna'
    bmr=66+(13.7*waga)+(5*wzrost)-(6.8*wiek)
    bmr=bmr*przelicznik
    print(f'Twoje zapotrzebowanie kaloryczne wynosi: {bmr}')

#GUI

window =tk.Tk()
window.geometry('500x550')
window.title('Przelicznik kalorii')
window.configure(bg = 'azure3')

font1 = font.Font(family = 'helvetica', size = '23')
font2 = font.Font(family = 'helvetica', size = '15')

#Napis

main = tk.Label(window,text = 'Przelicznik kalorii',bg = 'azure3', fg = 'black')
main['font'] = font1
main.place(relx = '0.5', rely = '0.15', anchor = 'center')

#Płeć

a = tk.Label(window,text = 'Płeć : ', bg = 'azure3')
a['font'] = font2
a.place(relx = '0.28', rely = '0.28')

a2 = tk.Label(window,text = (płeć), bg = 'azure3')
a2['font'] = font2
a2.place(relx = '0.45', rely= '0.28')

#Wzrost

b = tk.Label(window,text = 'Wzrost : ', bg = 'azure3')
b['font'] = font2
b.place(relx = '0.28', rely = '0.36')

b2 = tk.Label(window,text = (wzrost), bg = 'azure3')
b2['font'] = font2
b2.place(relx = '0.45', rely= '0.36')

#Wiek

c = tk.Label(window,text = 'Wiek : ', bg = 'azure3')
c['font'] = font2
c.place(relx = '0.28', rely = '0.44')

c2 = tk.Label(window,text = (wiek), bg = 'azure3')
c2['font'] = font2
c2.place(relx = '0.45', rely= '0.44')

#Waga

d = tk.Label(window,text = 'Waga : ', bg = 'azure3')
d['font'] = font2
d.place(relx = '0.28', rely = '0.52')

d2 = tk.Label(window,text = (waga), bg = 'azure3')
d2['font'] = font2
d2.place(relx = '0.45', rely= '0.52')

#BMR

e = tk.Label(window,text = 'Twoje dzienne zapotrzebowanie kcal wynosi : ', bg = 'azure3')
e['font'] = font2
e.place(relx = '0.5', rely = '0.62',anchor = 'center')

e2 = tk.Label(window,text = (bmr), bg = 'azure3')
e2['font'] = font1
e2.place(relx = '0.5', rely= '0.70',anchor= 'center')

window.mainloop()


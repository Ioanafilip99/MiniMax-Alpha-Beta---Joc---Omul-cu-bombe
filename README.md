# MiniMax-Alpha-Beta---Joc---Omul-cu-bombe

Se va implementa un joc asemanator cu Atomic Bomberman dar mult simplificat.

- Simbolurile de pe harta
Jucatorii sunt notati cu 1 si 2. Jucatorul este intrebat daca doreste sa joace cu 1 sau cu 2.
Fiecare jucator se poate deplasa doar in spatiile libere marcate cu spatiu sau intr-un loc in care se afla o
"protectie", locul fiind marcat cu "p". Astfel, obstacolele (locatii in care jucatorul nu poate intra) sunt zidurile,
marcate cu "#" si bombele, marcate cu "b".
- Desfasurarea jocului
Jocul este turn based. Fiecare jucator la randul sau este obligat sa faca o deplasare si optional o plasare de bomba.
Fiecare jucator se poate deplasa doar in directiile sus, jos, stanga, dreapta si numai daca nu exista un obstacol
(zid sau bomba) in sensul deplasarii. Protectiile sunt luate automat de jucatori cand acestia ajung intr-o locatie
cu protectie. Dupa ce un jucator a luat protectia, rezista la strict o explozie de bomba. Jucatorul poate aduna mai
multe protectii de pe harta (deci poate avea un numar np>1 de protectii).
In momentul deplasarii un jucator poate plasa si o bomba care va ramane in urma lui (adica in pozitia in care era
inainte de deplasare). Bomba este inactiva pana o activeaza jucatorul. Jucatorul nu poate plasa inca o bomba
daca are deja o bomba inactiva.
Bonus. Daca jocul pare un pic plictisitor - de exemplu, ambii jucatori refuza sa puna bombe (de exemplu pe cazul
calculator vs calculator), puteti considera ca la fiecare k mutari in care nu a pus bomba, jucatorul sa fie obligat sa
puna o bomba (pur si simplu lasa bomba in urma lui). Ca sa reseteze contorul de mutari, poate pune el o bomba,
pana ajunge la k mutari fara bomba.
Jucatorul pierde jocul daca moare.
- Detaliile unei mutari
Cand vine randul jucatorului, va fi intrebat:
1. Directia in care vrea sa se mute (sus/jos/stanga/dreapta) - incercati sa ii cereti un singur caracter, de exemplu:
w,a,s,d.
2. Actiuni posibile (numai atunci cand e cazul): activare bomba(daca exista), plasare bomba(daca e vreo bomba
inactiva de-a jucatorului, se activeaza automat), nimic. Incercati si aici sa faceti optiuni doar de un caracter.
O bomba activa se declanseaza cand un jucator trece prin dreptul ei (pe linie sau pe coloana fara sa existe
obstacole intre ea si jucator). Explozia se intinde pe toata linia si coloana pe care se afla bomba.
O protectie inseamna ca il protejeaza pe jucator de o explozie.

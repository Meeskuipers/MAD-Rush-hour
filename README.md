# MAD's Rush Hour problem :oncoming_automobile:
#### Mees Kuipers, Danny Thie, Axel Huting ####


Probleem:
Rush hour is een spel dat wordt gespeeld op een vierkant bord. Het doel van het spel is om auto’s op het bord slim te verplaatsen om zo een bepaalde auto het bord uit te kunnen rijden.
![het simpelste bord]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/code_2/Knipsel.png)
De moeilijkheid van dit probleem zit hem in de optimale oplossing vinden voor ieder bord. De oplossing is wanneer de auto het bord uit is gereden in het minst mogelijke aantal zetten. Het vinden van de beste oplossing wordt moeilijker naarmate het bord groter wordt. De upperbound van de hoeveelheid configuraties (statespace) is afhankelijk van de hoeveelheid auto’s en vrachtwagens in het bord. De moveset is de maximaal hoeveelheid stappen van bord naar bord totdat het rode auto het bord heeft verlaten. Dit is dus de statespace min 1.
Elke auto heeft een beweeg ruimte van de lengte van het bord min één, omdat de auto op twee plekken staat. Hetzelfde geld voor een vrachtauto, maar dan met min twee, omdat de vrachtwagen op drie plekke staat. Voor elke plek waar de auto staat is een nieuwe configuratie van het bord. Dus om alle mogelijkheden van het bord te vinden moet je de lengte van het bord min één/twee tot de macht van de hoeveelheid auto’s/vrachtwagen op het bord. Dit geeft de formule van de complexiteit van het probleem:
![formule]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/data/formule.png)

Dit geeft de upperbound van alle mogelijke configuraties van het bord. De upperbound neemt dus toe als de auto’s, vrachtwagens en het grootte van het bord groter word.
De lowerbound van dit probleem is veel moeilijker te bepalen, want dat is eigenlijk de snelste oplossing. De manier waarop wij het bepaald hebben is door alle auto’s rechts van de rode auto van het bord te halen. Daarna beweeg je de auto’s tot dat de rode auto uit het bord kan komen. Dit geeft de volgende lower- en upperbound voor de borden die wij hebben verkregen:
![Upper en lowerbound]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/data/upper_lowerbound.png)

De uitdaging is het maken van een algoritme dat de beste oplossing vind voor grote borden zonder dat de space en time complexity van de gebruikte
algoritmes uit de hand lopen.
 Main:
Als de user main aanroept wordt de user gevraagd om eerst de grid size te definieren. Als de gridsize gedifineert is krijgt de user de optie om zelf te spelen off een algortime zoals dumbsolver aan te roepen. De decision making van het gekozen algoritme wordt per keuze geprint om zo het het denkproces te kunnen volgen. Aan het einde van ieder algoritme wordt de hoeveelheid moves geprint.
 scores van algoritmes:
 Dumbsolver: hoge tot infinite time complexity, zeer lage space complexity.

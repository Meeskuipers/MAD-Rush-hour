# MAD's Rush Hour problem :oncoming_automobile:
#### Mees Kuipers, Danny Thie, Axel Huting ####
 probleeem:
Rush hour is een spel dat wordt gespeeld op een vierkant bord. Het doel van het spel is om auto's op het bord slim te verplaatsen
om zo een bepaalde auto het bordt uit te kunnen rijden. 
 ![het simpelste bord]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/code_2/Knipsel.png)

 De moeilijkheid van dit probleem zit hem in de optimale oplossing vinden voor
ieder bord. De optimale oplossing is wanneer de auto het bord uit is gereden in het minst mogelijke aantal zetten. Het vinden van de 
beste oplossing wordt moeilijker naarmate het bordt groter wordt. De mogelijke hoeveelheid configuraties van het bord wordt meer dan exponentieel
groter naarmate het bord groter wordt. Deze toename in mogelijke configuraties leid tot een hoge space complexity in algoritmes die de beste oplossing proberen te vinden.
De uitdaging is het maken van een algoritme dat de beste oplossing vind voor grote borden zonder dat de space en time complexity van de gebruikte
algoritmes uit de hand lopen.
 Main:
Als de user main aanroept wordt de user gevraagd om eerst de grid size te definieren. Als de gridsize gedifineert is krijgt de user de optie om zelf te spelen off een algortime zoals dumbsolver aan te roepen. De decision making van het gekozen algoritme wordt per keuze geprint om zo het het denkproces te kunnen volgen. Aan het einde van ieder algoritme wordt de hoeveelheid moves geprint.
 scores van algoritmes:
 Dumbsolver: hoge tot infinite time complexity, zeer lage space complexity.

results:
![dumbsolver top resultaat]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/code_2/morevictories.png)
 ![dumbsolver laagste resultat]
(https://github.com/Meeskuipers/MAD-Rush-hour/tree/master/code_2/GREATVICTORY!.png)

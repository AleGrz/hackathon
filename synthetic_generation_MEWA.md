Mechanizm:
Dane do wstawiania bierzemy głównie z biblioteki `faker`, która ma polski dataset do losowych, realistycznych danych.
Niektórych (np. tych o szkołach i uczelniach) nie byliśmy w stanie jednak pozyskać w ten sposób, więc tutaj
użyliśmy LLMa do wygenerowania list z których następnie losowaliśmy rekordy

Odmiana:
W klasyfikacji odmian bierzemy pod uwagę dwie charakterystyki: liczbę (pojedynczą lub mnogą) oraz odmianę przez przypadki.
Najpierw klasyfikujemy te parametry przy pomocy biblioteki spaCy, która ma pożądaną właściwość brania pod uwagę kontekstu,
którego często potrzebujemy do określenia przypadku. Jest ona również, w przeciwieństwie do rozwiązań słownikowych, 
względnie mało podatna na błędy w danych wejściowych, jednak często nie była w stanie klasyfikować mniej popularnych 
słów (np. nazw małych miejscowości). Tu z pomocą przychodziła biblioteka Morfeusz2, która działa na zasadzie słownika -
co prawda tracimy informację o kontekście i odporność na pomyłki w danych wejściowych, ale mamy pewność że możemy 
przetwarzać również mniej używane słowa, a mnogość przypadków w zależności od kontekstu i tak jest raczej dość rzadkim 
zjawiskiem. Po zdobyciu informacji o liczbie i odmianie ponownie używamy biblioteki Morfeusz2 do odmiany słów w generowanych
losowo w "podstawowej" formie. Dzięki zaczerpnięciu informacji o fleksji ze źródłowych tekstów mamy wysoką pewność poprawnej
odmiany słów.
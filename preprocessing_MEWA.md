Preprocessing datasetu:
    - alignment tokenów i znaczników do NER
    - grupowanie niepoprawnych znaczników o podobnej semantyce z tymi poprawnymi

Wzbogacanie datasetu:
Jako, że zbiór posiadał dane raczej niskiej jakości, planowaliśmy wzbogacić go używając `ai4privacy/pii-masking-400k`,
tłumacząc i wzbogacając zbiór o własne znaczniki za pomocą LLM. Jedyne co nam to przyniosło to zmarnowany czas,
gdyż aby osiągnąć dobre wyniki w generowaniu danych w takiej postaci LLMem potrzeba bardzo dużo czasu i pieniędzy, a 
modele z darmowym API okazały się niewystarczające i tworzyły dane nie odbiegające bardzo od tych które dostaliśmy.



Spotkałem się z [name] w [city]
Spotkałem się z [Borysem] w [Szczecinku]


Jadę do mojej [relative], która ma [health]
Jadę do mojej [mamy], która ma [niedosłuch]


Kupiłem mojemu [relative] w [city] nowy zegarek.
Kupiłem mojemu [bratu] w [Wrocławiu] nowy zegarek .


Redaktor rozmawiał z prezydentem miasta [name] [surname] o planach dla [city] .
Redaktor rozmawiał z prezydentem miasta [name] [surname] o planach dla [city] .


Kuzynka [name] ma poważny problem z [health] i szuka pomocy w [city]
Kuzynka [Ewa] ma poważny problem z [nadciśnieniem] i szuka pomocy w [Inowrocławiu] .

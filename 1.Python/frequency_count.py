def most_frequent_chars(s):
    """ Returns a list of all characters in a string ordered on the frequency of occurence
    """
    frequencies = dict()
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    frequencies_inverted = {}
    for char, freq in frequencies.items():
        if freq in frequencies_inverted:
            frequencies_inverted[freq] += [char]
        else:
            frequencies_inverted[freq] = [char]
    freq_list = list(frequencies_inverted.keys())
    freq_list.sort(reverse=True)
    char_list_ordered = []
    for freq in freq_list:
        char_list_ordered += frequencies_inverted[freq]
    return char_list_ordered


s = "aaabbccccccddr"
print(most_frequent_chars(s))

def most_frequent_words(s):
    """ Returns a list of all characters in a string ordered on the frequency of occurence
    """
    frequencies = dict()
    for word in s.split(" "):
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    frequencies_inverted = {}
    for char, word in frequencies.items():
        if freq in frequencies_inverted:
            frequencies_inverted[freq] += [word]
        else:
            frequencies_inverted[freq] = [word]
    freq_list = list(frequencies_inverted.keys())
    freq_list.sort(reverse=True)
    word_list_ordered = []
    for freq in freq_list:
        word_list_ordered += frequencies_inverted[freq]
    return word_list_ordered


s = u"""Wikipedia
    Naar navigatie springenNaar zoeken springen
    Wikipedia
    Wikipedia
    WikiPedia.png
    Type	encyclopedie
    Taal	meertalig
    Registratie	optioneel
    Eigenaar	Wikimedia Foundation
    Auteur(s)	Wikipediagemeenschap
    Opgericht	15 januari 2001
    Status	actief
    Link	wikipedia.org
    Portaal  Portaalicoon  	Media
    Wikipedia is een internetencyclopedie, die wereldwijd door auteurs op vrijwillige basis wordt geschreven. De inhoud moet te controleren zijn en mag geen onrecht doen aan derden. Wikipedia wordt gepubliceerd onder een vrije licentie, zodat de inhoud elders opnieuw te gebruiken is. De website is eigendom van de Wikimedia Foundation, een in de Verenigde Staten gevestigde organisatie zonder winstoogmerk. Onder de paraplu van de Wikimedia Foundation bevinden zich diverse meertalige projecten waarvan Wikipedia het oudste en bekendste is. In alle veelvoorkomende talen is er een Wikipedia.

    Wikipedia is in de basis opgezet in de vorm van een wiki, hetgeen betekent dat elke inhoudelijke pagina door iedere willekeurige bezoeker bewerkt kan worden. Voor Wikipedia is een apart programma ontworpen. De software, MediaWiki, is opensourcesoftware die ook gebruikt wordt door de andere projecten van de Wikimedia Foundation en door talloze andere projecten en bedrijven.


    Inhoud
    1	Vijf zuilen
    2	De naam Wikipedia
    3	Geschiedenis
    3.1	Kenmerken van het project
    3.2	Voorgeschiedenis
    3.3	Oprichting
    3.4	Eerste opzet
    3.5	Groei
    3.6	Verdere ontwikkeling
    3.6.1	Logo
    3.6.2	Culturele samenwerking
    3.6.2.1	Wikipedian in Residence
    3.6.3	Langere termijn
    3.7	Erkenningen
    3.7.1	Erasmusprijs
    3.7.2	Prinses van Asturiëprijs
    4	Knelpunten
    4.1	Vandalisme
    4.2	Snelle verspreiding van verkeerde informatie
    4.3	Vertekening
    4.3.1	Gendergap
    4.4	Reclame en eigen voordeel
    4.5	Sokpoppen
    4.6	Presentatie
    4.7	Negatieve economische waarde en gevolgen voor traditionele encyclopedieën
    4.8	Inhoudelijke censuur
    5	Kwaliteit
    5.1	Duitstalige Wikipedia
    5.2	Engelstalige Wikipedia
    6	Afgeleide sites
    6.1	Spiegelsites
    7	Film
    8	Literatuur
    9	Externe link
    9.1	Referenties
    9.2	Noten
    Vijf zuilen
    Op Wikipedia gelden vijf principes, zuilen genoemd:[1]
    """
print(most_frequent_words(s))
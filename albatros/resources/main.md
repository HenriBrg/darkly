# User Agent HTTP Header

1. Rendons nous sur une des routes indiquées par le bouton Copyrigth en bas de page

Il nous envoie sur la page : http://192.168.1.16/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
À priori, RAS.

2. Fouiner dans l'inspecteur

On observe, entre du blabla sur Epitech :

<!-- You must coming from : "https://www.nsa.gov/" to go to the next step -->

Puis plus bas :

<!-- Let's use this browser : "ft_bornToSec". It will help you a lot. -->

Comment interpréter cela ?
Il faut connaitre un peu les headers HTTP

Le "https://www.nsa.gov/" fait référence à la valeur que doit prendre le header REFERER
Le "ft_bornToSec" fait référence à la valeur que doit prendre le header USER-AGENT

On peut donc CURL la page de en définissant les headers soi-même :

    curl -v -H "User-Agent: ft_bornToSec" -H "Referer: https://www.nsa.gov/" http://192.168.1.16/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c

Puis on re-fouine dans le retour de curl, pour tomber sur un beau flag en début de page, et voilà !

# BONUS

* REFERER :

L'en-tête de requête Referer contient l'adresse de la page web précédente à partir de laquelle un lien a été suivi pour demander la page courante. L'en-tête Referer permet aux serveurs d'identifier la provenance des visiteurs d'une page et cette information peut être utilisée à des fins d'analyse, de journalisation ou pour améliorer la politique de cache par exemple.
Header assez controversé ! Surtout qu'il implique des enjeux de sécurité au-delà de ce que l'on pourrait penser à première vue
Notamment via la fuite de données sensible si le site est mal codé

* USER-AGENT:

The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

Exemple : si nous allons sur n'importe quel site avec Chrome, celui-ci injectera un header de requête tel que :

    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

# PROTECTION


L’en-tête Referrer-Policy peut contrôler quelle information est envoyée par l’en-tête Referer.
Par exemple, une directive no-referrer omettrait intégralement l’en-tête Referer
+ d'infos : https://openweb.eu.org/articles/referrer-policy

# Approfondissement des failles de sécurité liées au REFERER

Un référent est une information transmise à un serveur HTTP lorsqu’un visiteur suit un lien pour accéder à l’une de ses ressources,
lui indiquant l’URL de la page où se situe ce lien qu’il a suivi.

Pourquoi s'inquieter de ce header ?

Ex 1 : Peut-être votre site a une interface d’administration, et vous n’avez sûrement pas envie que l’adresse de cette dernière soit transmise en referrer.
Ex 2 : Imaginons un intranet sur lequel vous pouvez partager des liens. Souhaitez-vous que l’adresse de ce dernier soit transmise vers l’extérieur ?
# HIDDEN LOCATION

En brute forçant les URLs du site, nous remarquons l'existence d'un dossier robots.txt

1. Nous allons http://192.168.1.16/robots.txt

Nous en déduisons l'existence d'une ressource nommée ".hidden"

2. Nous allons http://192.168.1.16/.hidden

Nous y trouvons une liste de fichiers bien trop longue pour les ouvrir un par un,
donc en écrivant un script pour print le contenu du fichier, nous devrions trouver quelquechose !

3. CF. readmeOpener.py et obtient le précieux flag !

# PROTECTION

Dans la mesure où c'est une faille "volontaire", contrairement à une injection SQL par exemple, il n'y a pas vraiment de protection cohérente.

Néanmoins, en plaçant le répertoire .hidden dans .htaccess, on restreindra l'accès aux utilisateurs définit, ce qui pourrait être utile dans ce cas présent.
Il faut veiller à ne pas oublier de modifier le htpasswd pour ajouter l'utilisateur souhaité.
Autrement, les utilisateurs peuvent être définit dans la configuration du serveur nGinx (+ d'infos ici : https://www.tecmint.com/password-protect-web-directories-in-nginx/)

Il aurait fallu que ça soit un honeypot, ça aurait été à la fois frustrant et amusant ... :D, mais avec une belle leçon à la clé 
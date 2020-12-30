# File Upload

1. On note un formulaire d'upload sur la page : http://192.168.1.16/?page=upload#

<!-- <form enctype="multipart/form-data" action="#" method="POST">

    <input type="hidden" name="MAX_FILE_SIZE" value="100000">
    Choose an image to upload:
    <br>
    <input name="uploaded" type="file"><br>
    <br>
    <input type="submit" name="Upload" value="Upload">

</form> -->

Dedans s'y trouve un input : <input name="uploaded" type="file">

En uploadant une image .jpg, c'est accepté par le serveur, mais dans une optique de sécurité, n'importequi pourrait upload autre chose qu'une image
Donc uploader un fichier .php peut être utile, mais le soucis est que le serveur le détecte et bloque l'upload

On peut contourner ça en rajoutant .jpg au fichier .php (cf. dossier courant) voire en mettant un \0 :

    rhell.php.jpg   --> Lu en tant que .jpg donc ça passe
    rhell.php\0.jpg --> Lu en tant que .jpg donc ça passe, mais à priori, lors de l'ouverture future du fichier, ça sera lu / exécuter en tant que .php :)
    TODO : on pourrait aussi hexediter le magic number du fichier : https://gobiasinfosec.blog/2019/12/24/file-upload-attacks-php-reverse-shell/

Et si on parvient ensuite à exécuter, donc simplement "aller" sur la page où se trouve la ressource uploadé, et bien on peut faire PLEINNN de choses, comme un reverse shell
Le soucis, c'est que la ressource semble introuvable, bien qu'uploadée
En théorie le serveur devrait répondre 201 avec le header Location qui situe (dans un contexte choisi) le path de la ressource nouvellement créée

2. Il faut trouver un moyen de bypass, passons par curl pour ça

https://ec.haxx.se/http/http-multipart

Depuis le dossier resources, on peut run le CURL suivant :

    curl -v -X POST "http://192.168.1.16/?page=upload"  -F "uploaded=@rshell.php.jpg" -F "Upload=Upload" -H "Content-Type: image/jpg" 
   
    Le : -H "Content-Type: image/jpg" ne semble pas fonctionner, car le submit bouton en lui-même est un input texte, donc tout n'est pas jpg, donc ça ne passe pas
    Du coup, on peut préciser le type d'un l'input précis comme ceci :

**SOLUTION** : curl -v -X POST "http://192.168.1.16/?page=upload" -F "uploaded=@rshell.php;type=image/jpg" -F "Upload=Upload"

On peut s'intéresser au header envoyé par CURL, c'est utile
On récupère ainsi une réponse HTML avec dedans un flag :) et voila !
Malheureusement, l'upload reste introubable

# Protection

Comme toujours, tous les inputs du client doivent être "sanitize" et ne jamais se fier à l'extension d'un fichier uploadé, qui n'est au fond qu'un nom, rien de plus

# Bonus

* mulltiplart/form-data (+ enctype)

https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean

3 formes d'encoding pour les forms en HTML :

- application/x-www-form-urlencoded (the default)
- multipart/form-data
- text/plain (à éviter)

Lorsqu'un input de type file est présent dans le form, il vaut mieux utiliser multipart/form-data puis l'encoding sera + adapté à un fichier, potentiellement volumineux
De plus, l'upload de fichier fait transiter beaucoup de "non-printable characters", surtout pour les images, contrairement aux inputs texte


Un peu d'anglais: when you make a POST request, you have to encode the data that forms the body of the request in some way.

    Enctype "encode type" attribute specifies how the form-data should be encoded when submitting it to the server
    multipart/form-data is one of the value of enctype attribute, which is used in form element that have a file upload.
    multi-part means form data divides into multiple parts and send to server.

Exemple d'usage du enctype :  <form enctype="multipart/form-data" action="#" method="POST">

Si le formulaire n'a aucun intermédiaire (validation notamment) côté client, alors inutile de s'embêter avec tout cela, et utiliser les forms fournit par le framework (ex: RoR : form_for)


* Le code HTTP 100

Le code de statut de réponse HTTP 100 Continue indique que, jusqu'à présent, tout est normal (OK) et que le client doit poursuivre avec la requête ou l'ignorer si celle-ci est déjà finie.

Afin que le serveur vérifie les en-têtes des requêtes, un client doit envoyer Expect : 100-continue comme en-tête dans la requête initiale
et recevoir le code de statut 100 Continue comme réponse avant d'envoyer le corps de la requête.
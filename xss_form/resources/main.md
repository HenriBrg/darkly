# XSS (Stored)

1. On a un ormulaire qui affiche sur la page le contenu envoyé au formulaire
Ce dernier point est intéressant car on peut se demander si l'input est "sanitize" à l'affichage

Le formulaire en question se trouve ici : http://192.168.1.16/index.php?page=feedback

2. Pour commencer testons une injection de javascript :

   <script>alert("Hello")</script>
   <script><script>alert("42")</script></script>
   javascript:alert(document.cookie)
   script

En théorie, si l'input n'est pas sanitize, alors lors du rendu du DOM, l'affiche du commentaire devrait faire appel à la fonction alert() du DOM.

Mais Wandre a été sympa visiblement, le simple fait d'écrire 'script' en commentaire suffit à générer le flag

NB : assez étrange, il bloque l'alerte ou alors la XSS fail car on a pas l'alert(), ça semble full random

# PROTECTION

Il ne faut pas laisser la possibilité d'injecter du JS qui serait ensuite évaluer par le navigateur

* Pour contrer cela, il faut "sanitizer" ou nettoyer tous les inputs des forms vers le serveur, mais cela est faisable aussi (en + bien sûr) lors du rendu de la page

Pour cela, il faut escape les caractères spéciaux, une petite liste :

    "	&#34
    #	&#35
    &	&#38
    '	&#39
    (	&#40
    )	&#41
    /	&#47
    ;	&#59
    <	&#60
    >	&#62

Les frameworks moderne faut cette esquive par défaut

* Whitelister

On peut whitelist certaines valeurs pour s'assurer qu'elles ne soient jamais présente, en interdisant tout simplement la présence d'un contenu donné, phrases, caractères ...

* Content-Security Policy

Les navigateurs récents propose un header HTTP de réponse empêchant ou restreignant l'usage du JS sur la page web.
Il faut donc configurer notre serveur afin qu'il inclus le header Content-Security-Policy, par exemple :

    Content-Security-Policy: script-src 'self' https://apis.google.com

Grâce à ça, on peut interdire l'exécution du JS et/ou choisir d'où vient (autrement dit qui peut) le JS à exécuter

On voit parfois en HTML :

    <meta http-equiv="Content-Security-Policy" content="script-src 'self' https://apis.google.com">

La finalite est la même que le header


# XSS via GET parameters

Tout est là : https://owasp.org/www-community/xss-filter-evasion-cheatsheet

1. Sur la page http://192.168.1.16/?page=media&src=nsa

On constate que l'image affichée dépend du paramètre src, donc potentiellement un XSS car le navigateur va executer ce que contient 'src'
Donc tout et nimportequoi, surtout nimportequoi puisque l'user peut s'en servir

2. Dans le tutoriel XSS de OWASP : https://owasp.org/www-community/xss-filter-evasion-cheatsheet pour bypasser un WAF

NB : Un Web Application Firewall (WAF) est un type de pare-feu qui protège le serveur d'applications Web dans le backend contre diverses attaques. Le WAF garantit que la sécurité du serveur Web n'est pas compromise en examinant les paquets de requête HTTP / HTTPS et les modèles de trafic Web.

Parmi toutes les XSS, certaines se place justement dans la querie string de l'url

OWASP donne un exemple : /?param=<data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=

On peut tester avec le payload suivant : <script>alert(document.cookie)</script>

    Souvent, ce genre de faille sans le base64, ça ne passe pas

  <script>alert(document.cookie)</script> = PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpPC9zY3JpcHQ+
    
Donc : http://192.168.1.16/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpPC9zY3JpcHQ+


# Protection

Ne jamais insérer dans la page un donnée venant d'un paramètre de la query string
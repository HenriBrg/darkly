# Edition du DOM

Au fond sur tous les liens ayant des paramètres dans la query string, il y a potentiellement une faille car on envoie une donnée au serveur
Donc vu la robustesse du site, même une simple de modification d'un href se tente

1. Aller sur la home http://192.168.1.16/index.php

2. Il y a 3 boutons en bas comme celui ci pour Facebook : http://192.168.1.16/index.php?page=redirect&site=facebook

Modifions le paramètre "site" et hop un flag pop ...
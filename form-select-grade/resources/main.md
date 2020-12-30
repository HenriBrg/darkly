# FORM SELECT GRADE

http://192.168.1.26/?page=survey#

En éditant le select pour le grade des survey (une value incohérent, sur un autre grade que 1 car c'est celui load pardéfaut), on obtient un flag

<select name="valeur" onchange="javascript:this.form.submit();">
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
    <option value="6">6</option>
    <option value="7">7</option>
    <option value="8">8</option>
    <option value="9">9</option>
    <option value="10">10</option>
</select>

Les formulaires avec des choix imposés doivent être protégés de l'édition dans le DOM.
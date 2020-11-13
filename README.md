# Air-traffic

## Structure

Les dossier se découpe en 3 projets plus les notbooks.

Les projets airtraffic_dataclean/ et restful_app/ ont chacun leur propre venv. (sinon bug de dépendense circulaire)<br/>
Il faut donc ouvrir leurs dossiers séparemment, leur créer un venv chacun. Voir la section **venv**.

## Disclaimer

Les imports des .py comme env.py peuvent poser soucis d'une machine a l'autre ou selon l'IDE. On selon les machines de notre groupe certains qui doivent importer `from env` et d'autres `from database.env` depuis app.py de restfull_app/. Il est donc possible que vous aillez ce genre d'erreur et donc qu'il faille ajouter ou retirer le nom d'un dossier lors d'un import.

## CSV

Extraire l'archive des csv vers data-csv

Pour importer les csv : 

    cd airtraffic_dataclean/
    # lancer le venv voir **venv**
    py database_init.py

## React
Aller dans le dossier react/ :

Installer les dépendances :

    cd react/
    npm install

Lancer le server de rendu du front : 

    npm start

## venv

Créer le venv : <br/>
    
    python3 -m venv venv

Lancer le venv :<br/>

Widows : 

    venv\Scripts\activate

Unix : 

    venv/bin/activate

Installer les packages requis : <br/>

    pip install -r requirements.txt

Mettre à jour la liste des package : <br/>


    pip freeze > requirements.txt


## flask

Lancer l'API python: <br/>

    cd restfull_app
    flask run


## env
Créer 2 env.py a partir des env.py.sample dans airtraffic_dataclean/ et restful_app/database/ pour la connexion a la BDD.
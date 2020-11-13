# Air-traffic

Extraire l'archive des csv dans data-csv

## Structure

Les dossier se découpe en 3 projets plus les notbooks.

Les projets airtraffic_dataclean/ et restful_app/ ont chacun leur propre venv. (sinon bug de dépendense circulaire)

Le 3eme projet est le projet React : react/. Pour le lancer :<br/>
`npm install` puis `npm start`

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

Créer et remplir la BDD : <br/>

    python database_init.py

Lancer l'application : <br/>

    flask run


## env
Créer 2 env.py a partir des env.py.sample depuis airtraffic_dataclean/ et restful_app/database/ pour la connexion a la BDD.


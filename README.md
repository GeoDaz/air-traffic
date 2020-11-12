# Air-traffic

Extraire l'archive des csv dans data-csv


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
Créer un env.py a partir du env.sample.py pour la connexion a la BDD.


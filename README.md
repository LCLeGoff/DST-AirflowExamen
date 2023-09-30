# DST-AirflowExamen
Pour organiser mon code, je n'ai pas tout mis dans le fichier `dags/openweather_dag.py`.
Dans `scripts` se trouvent les fichiers contenant les fonctions à exécuter pendant les tâches.
Dans `utils` se trouve une classe pour manipuler plus facilement les json.

J'ai modifié le fichier `docker-compose.yaml` pour rendre accessible `scripts` et `utils` depuis airflow.

J'ai aussi ajouté le module `python-dotenv` dans `docker-compose.yaml` pour importer la clé de l'api openweather avec le fichier `.env`.

Les fichiers `run.py` et `requirements.txt` étaient pour tester les fonctions avant de coder le dag.

J'ai laissé les données générées par le dag 
dans les repertoires ``clean_data`` et ``raw_files`` pour montrer le bon fonctionnement du dag. 
Si vous avez décompressé l'archive sous MacOs, 
les ``:`` dans les noms de fichiers de ``raw_files`` peuvent être remplacé par ``/``.
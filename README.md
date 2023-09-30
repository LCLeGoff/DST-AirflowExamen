# DST-AirflowExamen
Pour organiser mon code, je n'ai pas tout mis dans mon fichier `openweather_dag.py`.
Dans `scripts` se trouvent les fichiers contenant les fonctions à éxécuter pendant les taches.
Dans `utils` se trouvent une classe pour manipuler plus facilement les json.

J'ai modifié le fichier docker-compose pour rendre accessible `scripts` et `utils` depuis airflow.

J'ai aussi ajouté le module `python-dotenv` dans `docker-compose.yaml` pour importer la clé de l'api openweather avec le fichier `.env`
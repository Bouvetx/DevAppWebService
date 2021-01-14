# DevAppWebService
Developpement of a application/webservice

## ATTENTION LES FICHIERS SUIVANTS SONT SOUS LEUR FORME POUR FONCTIONNER SUR MON SYSTÈME 

## TOUTES LES RÉFÉRENCES À LOCALHOST ONT ÉTÉ REMPLACÉES PAR MON ADRESSE IP (MERCI WINDOWS)

### Pour mettre en place le service RabbitMQ\
  - Lancer le docker-compose.yml présent dans le dossier RabbitMQ (docker-compose up)


### Pour créer vos queues\
  - éditez la ligne
    - cl = Client('192.168.99.100:15672','xavier','bouvet')
  - et remplacez la par
    - cl = Client('localhost:15672','xavier','bouvet')
  - lancer le script python\
  - Il faut alors indiquer le nom de la queue que vous voulez créer\
  - Si vous entrez un nom déjà utilisé il vous seras demandé d'entrer un nouveau nom
  

### Pour lancer l'ingestion 
- Lancer le docker-compose.yml présent dans le dossier NiFi (docker-compose up)\
-  Pour accéder à l'interface de Nifi suivez le lien suivant http://localhost:8083/nifi/ \
    - Importer le template Nifi2InfluxDB.xml présent dans le dossier NiFi\
  - Changez les paramètres dans le processus ConsumeAMQP\
    - Queue : "le nom de la queue que vous avez créé"\
    - Host name : Poc\
    - User name : xavier\
    - Password : bouvet\
  - Changez les paramètres dans le processus ExecuteScript\
    - dans le paramètre Script Body\
      - changer la ligne\
        - var measure = "client1"\
      - par\
        - var measure = "le nom de la queue que vous avez créé"
    

### Pour lancer la base de données\
  - éditez la ligne\
    - command: "--influxdb-url=http://192.168.99.100:8086" \
  - et remplacez la par \
    - command: "--influxdb-url=http://localhost:8086" \
  - Lancer le docker-compose.yml présent dans le dossier influxdb (docker-compose up)
  
  
### Pour lancer la visualisation\
  - Lancer le docker-compose.yml présent dans le dossier Grafana (docker-compose up)\
  - Pour accéder à l'interface de Grafana suivez le lien suivant http://localhost:8084 \
    - Email or username : admin\
    - Password : secret
  - Importer les différents dashboards
  
### Pour générer des données
  - Lancer le docker-compose présent dans l'un des sous-dossiers présent dans FakeMessage

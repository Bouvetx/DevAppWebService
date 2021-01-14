# DevAppWebService
Developpement of a application/webservice

#ATTENTION LES FICHIER SUIVANT SONT SOUS LEUR FORME POUR FONCTIONER SUR MON SYSTEME
#TOUTES LES REFERENCE A LOCALHOST ON ETE REMPLACE PAR MON ADDRESSE IP (MERCI WINDOWS)

Pour mettre en place le service RabbitMQ\
  Lancer le docker-compose.yml présent dans le dossier RabbitMQ (docker-compose up)

Pour créer vos queue lancer le scripte python
  Il faut alors indiquer le nom de la queue que vous voullez créer
  Si vous entré un nom deja utilisé vous demenderas d'entréer un nouveau nom
  
Pour lancer l'ingestion 
  Lancer le docker-compose.yml présent dans le dossier NiFi (docker-compose up)
  Pour acceder a l'interface de Nifi suivez le lien suivant http://localhost:8083/nifi/
  Importer le template Nifi2InfluxDB.xml présent dans le dossier NiFi
  Changer les parametre dans le processus ConsumeAMQP
    Queue : "le nom de la queue que vous avez créer"
    Host name : Poc
    User name : xavier
    Password : bouvet
  Changer les parametre dans le processus 
    dans le paramètres Script Body
      changer la ligne
        var measure = "client1"
      par
        var measure = "le nom de la queue que vous avez créer"
    
    
Pour lancer la base de donnée
  editer la ligne
    command: "--influxdb-url=http://192.168.99.100:8086"
  et remplacer la par 
    command: "--influxdb-url=http://localhost:8086"
  Lancer le docker-compose.yml présent dans le dossier influxdb (docker-compose up)
  
  
Pour lancer la visualisation
  Lancer le docker-compose.yml présent dans le dossier grafana (docker-compose up)
  Pour acceder a l'interface de Grafana suivez le lien suivant http://localhost:8084
    Email or username : admin
    Password : secret

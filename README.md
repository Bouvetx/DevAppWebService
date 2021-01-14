# DevAppWebService
Developpement of a application/webservice

#ATTENTION LES FICHIER SUIVANT SONT SOUS LEUR FORME POUR FONCTIONER SUR MON SYSTEME
#TOUTES LES REFERENCE A LOCALHOST ON ETE REMPLACE PAR MON ADDRESSE IP (MERCI WINDOWS)

Pour mettre en place le service RabbitMQ\
\tLancer le docker-compose.yml présent dans le dossier RabbitMQ (docker-compose up)


Pour créer vos queue lancer le scripte python\
\tIl faut alors indiquer le nom de la queue que vous voullez créer\
\tSi vous entré un nom deja utilisé vous demenderas d'entréer un nouveau nom
\t

Pour lancer l'ingestion 
Lancer le docker-compose.yml présent dans le dossier NiFi (docker-compose up)\
\tPour acceder a l'interface de Nifi suivez le lien suivant http://localhost:8083/nifi/ \
\tImporter le template Nifi2InfluxDB.xml présent dans le dossier NiFi\
\tChanger les parametre dans le processus ConsumeAMQP\
\t\tQueue : "le nom de la queue que vous avez créer"\
\t\tHost name : Poc\
\t\tUser name : xavier\
\t\tPassword : bouvet\
\tChanger les parametre dans le processus \
\t\tdans le paramètres Script Body\
\t\t\tchanger la ligne\
\t\t\t\tvar measure = "client1"\
\t\t\tpar\
\t\t\t\tvar measure = "le nom de la queue que vous avez créer"
\t\t

Pour lancer la base de donnée\
\tediter la ligne\
\t\tcommand: "--influxdb-url=http://192.168.99.100:8086" \
\tet remplacer la par \
\t\tcommand: "--influxdb-url=http://localhost:8086" \
\tLancer le docker-compose.yml présent dans le dossier influxdb (docker-compose up)
\t
\t
Pour lancer la visualisation\
\tLancer le docker-compose.yml présent dans le dossier grafana (docker-compose up)\
\tPour acceder a l'interface de Grafana suivez le lien suivant http://localhost:8084 \
\t\tEmail or username : admin\
\t\tPassword : secret

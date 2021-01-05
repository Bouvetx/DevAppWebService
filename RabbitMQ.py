from pyrabbit.api import Client
#https://github.com/bkjones/pyrabbit
#https://rawcdn.githack.com/rabbitmq/rabbitmq-management/v3.8.9/priv/www/api/index.html
#pip3 install pyrabbit
#https://pyrabbit.readthedocs.io/en/latest/
#https://pyrabbit.readthedocs.io/en/latest/api.html
#https://github.com/bkjones/pyrabbit/blob/master/pyrabbit/api.py

new_enclos =""

#global variable
cl = Client('192.168.99.100:15672','xavier','bouvet')
cl.is_alive()

def main():
    #Pyrabbit api



    dic_queue = cl.get_queues()

    confirm = False


    while(confirm == False):
        print("Enter le nom du nouvel enclos")
        new_enclos = input()
        if(new_enclos==""):
            print("/!\ Nom non valide")
        else:
            confirm=True
    return new_enclos

def check_queue(new_name,dic_queue):
    """
    Check if a name is in a dic
    """
    for _ in dic_queue:
        if (_ == new_name):
            print("/!\ Un virtual host poss�de d�j� ce nom")
            return False
    return True

def deploy_new_enclos(new_enclos):

    cl.create_queue(vhost="/",name=new_enclos)
    cl.create_binding(vhost="/",exchange="Topic",queue=new_enclos,rt_key=new_enclos+"_data")

if __name__ == '__main__' :
    try :
        new_enclos = main()
        cl.create_vhost("/")
        cl.create_exchange(vhost="/", name="Topic", xtype="topic")
        deploy_new_enclos(new_enclos)
    except KeyboardInterrupt :
        print('INterrupted')
        try:
            sys.exit(0)
        except SystemExit :
            OS._exit(0)


#client_global = input("Enter le nom du nouveau client")

#cl.create_vhost('example_vhost')
#cl.delete_vhost('example_vhost')
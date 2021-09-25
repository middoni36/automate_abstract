import random
import string
from datetime import datetime
from transactionsndlogin import Logging
class place:
    def __init__(self,*args):
        self.place=args[0],args[1],args[2]
    def get_place(self):
        return self.place

class automate:
    registred_clients=[]
    def __init__(self,pos:place):
        self.pos=pos
        self.numbofclient=0
        self.aut_transactions={}
        self.functions_dict={"1":self.check_transaction,"2":self.get_deposit,"3":self.make_deposit,"4":self.transfer_money}
        self.current_client=None
        self.logg_manager=Logging.create_log()



    def set_auttransactions(self,type):
        self.aut_transactions[(type,self.current_client.get_id())]=f"{datetime.time().now()}"

    def make_deposit(self,amount):   #setdeposit
        self.current_client.set_deposit(amount)

    def get_deposit(self):
        print(f"{self.current_client.get_deposit()} $")

    def check_transaction(self):
        pass

    def transfer_money(self, amount):
        pass


    def register(self,client):

        #register the client store his objext in self.current_client and in registred_clients
        while client_pass1 != client_pass2 :
            client_pass1=input("please insert your own password = ")
            client_pass2=input("please Repeat your own password = ")

        self.current_client=client
        automate.registred_clients.append(self.current_client)
        self.check_client(client)
        # call the menu




    def print_mainmenu(self):
        global h_choice
        h_choice=input("choose a Function : \n 1)check-transaction  2) get_deposit  3)set_deposit  4)Transfer_money ")
        self.functions_dict[h_choice]()


    def check_client(self,client):
        global choice
        self.logg_manager.setuser_id(client.get_id())
        if client.get_id() in automate.registred_clients:
            self.current_client=client
            print("client Already registred.....")
            self.give_credentials()
            return None

        else :
            self.print_register_menus()
            if choice=="2":
                client.log_out()
                return None
            self.register(client)

    def print_register_menus(self):
        global choice
        choice = input("1: register , 2: log-out  ")

    def give_credentials(self):
        truth=self.logg_manager.check_validitiy(self.current_client.get_id())
        if not truth:
            self.give_credentials()
        self.print_mainmenu()









class client:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.id=self.choose_rand_id()
        self.transactions={}
        self.deposit=0
        self.password=""



    def set_password(self,mypass):
        self.password=mypass

    def choose_rand_id(self):
        myid=""
        for a in range(1,17):
            myid+=random.choice(string.ascii_letters)
            if a%4==0:
                myid+="-"
        print(myid)

    def set_transaction(self,type:str):
        self.transactions[type]=str(datetime.now().date())
    def get_id(self):
        return self.id
    def log_in(self,aut:automate):
        aut.check_client(self)
        #print menu aut.menu

        pass
    def set_deposit(self,amount):
        self.deposit=amount
    def get_deposit(self):
        return self.deposit
    def log_out(self):
        print("Logging out .......")

if __name__=="__main__":
    pass







class Logging: # create object of logginf and insert it in automate he will use it to create user and log-in and register it
    __log_check=None
    def __init__(self): #we use one logging object to chekc validity of user and also to store the time of logging
     self.history_log={} #user id and history logs
     self.__user_password={} # user id >> user password



    @staticmethod
    def create_log():
        if Logging.__log_check==None:
            Logging.__log_check=Logging()
            return Logging.__log_check
        else :
            return Logging.__log_check
    def reg_loghistory(self,id ,succed):
        self.history[id].append("client : id {},time log-in = {} , succed = {} ".format(id,succed))
    def check_validitiy(self,id):
        password=input("Please give your password = ")
        if self.__user_password[id]==password :
            self.reg_loghistory(id,True)
            return True
        else :
            self.reg_loghistory(id, False)
            return False



    def setuser_id(self,id):
        self.history_log[id]=[]
    def setuser_pass(self,userid,password):
        self.__user_password[userid]=password



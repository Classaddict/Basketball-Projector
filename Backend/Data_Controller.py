from server import *;

class Data_Controller:
    """
        Class to help perfrom basic CRUD operations on the databases
    """
    def getFakePlayerData():
        """
            Returns all data from Fake_Player_Data table
        """
        sql='''SELECT * FROM FAKE_PLAYER_DATA;''' 
        exec_commit(sql)
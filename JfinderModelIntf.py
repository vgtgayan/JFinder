
"""
/************************************************************************
|       ======================RUBICTRON=====================           |
|                   Oooo                                               |
+============oooO--(   )===============================================+
|           (   )   ) /                                                |
|            \ (   (_/                   .--.......--.                 |
|             \_)                     .-(   |||| ||    )-.             |
|____________________________________/   '--'''''''--''   \____________|
Created By    : Asitha Sandakalum(asitha@synopsys.com) 
Creation Date :
Last Modified :

-----------------------------------------------------------------------*/
"""

import pickle

class JfinderModelIntf:

    def save_model(self, model, model_name):
        pickle.dump(model, open(model_name, "wb"))
 
    def load_model(self, model_file_path):
        with open(model_file_path, 'rb') as pickled_file:
            loaded_model_data = pickle.load(pickled_file)
        return loaded_model_data
 
    def getresult(self, num: int, search_string: str)-> list:
        pass

    def setmodels(self, model_name: str):
        pass

    def train_and_save_model(self, model_name: str):
        pass


class CheckFiles:
    def __init__(self):
        self.isFileempty = False
    def checkFileisEmpty(self,file_name:str):
        with open(file_name,"r") as f:
            line = f.readline()
            if not line:
                self.isFileempty = True
        
        return self.isFileempty           

    def AfterEmpty(self,file_name,b:object):
        b.Fileno += 1   
        print(b.Fileno)      
        

import json, random


def load(filename="hello.db",autoDumping=False):

    ''''''

    meradb=MeraDb(filename,autoDumping)
    meradb.load_file()

    return meradb


class MeraDb:
    filename =""
    jobject={}
    autoDumping=False

    def __init__(self,filename,autoDumping):
        self.filename= filename
        self.autoDumping = autoDumping
    def load_file(self):
        print ("loading")
        try:
            files= open(self.filename, 'r+')
        except:
            files= open(self.filename, 'w+')    
        content= files.read()
        if content == "": 
           content= json.dumps({})
        
        self.jobject= json.loads(content)
        

        print ("loading success")

        return self.jobject


    def dump(self):
        
    
        file1=open(self.filename, "w")
        data=json.dumps(self.jobject)
        file1.write(data)
        return self.jobject




    def get(self,key):
        try:
            print (self.jobject[key])
            return self.jobject[key]
        except:
            print("This key doesn't exist")
            return "This key doesn't exist"


    def set(self,key,value):

        self.jobject[key]= value
        if self.autoDumping== True:
            self.dump()

        return "ok"



    def get_all(self):
        object_list=[]
        
        for keys in self.jobject:
            object_list.append(keys)
        if object_list ==[]:
            print ("There is no key present in the DB.") 
            return "ok"   
        print (object_list)    
        return "ok"
        
            

    def rem(self, key):
        
        try:
            self.jobject.pop(key)
            if self.autoDumping==True:
                self.dump()

        except:
            print("This key doesn't exist.")
            return "This key doesn't exist."
        return "Done"
        


    def exists(self, key):
        
        if key in self.jobject:
            print(True)
            return True
        print(False)
        return False 



    def total_keys(self):
        
        print(len(self.jobject))
        return "Done"



    def del_db(self):
        
        for i in list(self.jobject):
            del self.jobject[i]
        if self.autoDumping==True:
            self.dump()
        return "Done"



    def random_insert(self, number):
        
        i=0
        while i<number:
            key= random.randint(0,1000)
            value= random.randint(0,1000)
            self.jobject[key]=value

            i+=1 
        if self.autoDumping==True:
            self.dump()     
        return self.jobject


    def dmerge(self,filename):
        # open_file= open(filename,"r+")
        # data= open_file.read()
        # self.jobject= json.loads(data)
        # self.dump()
        second = MeraDb(filename,True)
               
        self.jobject=second.load_file()
        if self.autoDumping==True:
            self.dump()

        return second

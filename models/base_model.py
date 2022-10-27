import json
import uuid
import datetime
import mysql.connector

class BaseModel():
    def __init__(self) -> None:
        self.object = self.fileSystem()

    def fileSystem(self):
        return {}

    def create(self, **kwargs):
        """A model method that creates objects using **kwargs"""
        for key, item in kwargs.items():
            object = {}
            dt = datetime.datetime.today()
            obj_id = str(uuid.uuid4())
            object["id"] = obj_id
            object[key] = item
            object["created"] = str(dt)
            self.object[obj_id] = object
    
    def delete(self, *args):
        """A model method that deletes a record using *args"""
        data = self.read(state='r')

        if type(args).__name__ != 'tuple':
            args = list(args)
        
        for arg in args:
            if arg in data.keys():
                del data[arg]
                print(f"{arg} successfully deleted")
            else:
                print(f"{arg} record not found")

        file = self.read(state='w')
        json.dump(data, file, ensure_ascii=False, indent=4)    
        
    def update(self, **kwargs):
        """A model method that updates the data in a record"""
        data = self.read(state='r')
        
        for key, item in kwargs.items():
            for k, v in data.items():
                if key == k:
                    data[k]['name'] = item
        
        self.object = data
        self.save()

    def read(self, state):
        """A model method that loads the records saved in json or database format, and if no record found, returns an empty dictionary"""

        #file system
        try:
            if state == 'r':
                with open("../file storage/hnbn.json", ) as file:
                    record = json.load(file)
            else:
                file = open("../file storage/hnbn.json", state, encoding="utf8")
                record = file
        except Exception as e:
            record = self.fileSystem()
        
        return record
        
        #database
        # self.dataBase = mysql.connector.connect(
        #     host = 'localhost'
        # )

    def save(self):
        """A model method that saves the records in json or database format"""

        #Read the file system if it exists, else create the first copy
        try:
            data = self.read(state='r')
            for key, item in self.object.items():
                if not key in data.keys():
                    data[key] = item
        except FileNotFoundError:
            file = self.read(state='w')
            json.dump(self.object, file, ensure_ascii=False, indent=4)
            file.close()
        else:
            file = self.read(state='w')
            #print(data)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.close()

# b = BaseModel()
# b.create(name="Good")
# b.save()
# #id = {'f4cb1f18-e2ff-45ae-bab5-643b675fbd68':"Great"}
# id = ["1e519e62-5fbd-4778-8499-bce974880526",
#       "b706b2b4-3fec-4045-9e96-6d7a338ad84e", "ed463884-4278-4d70-9678-6599debccd81"]
# b.delete(*id)


# import mysql.connector
# from mysql.connector import errorcode

# try:
#   cnx = mysql.connector.connect(user='scott',
#                                 database='employ')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()
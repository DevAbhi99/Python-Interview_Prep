from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any


api=FastAPI()

data:List[Dict[str, Any]]=[{
    "name":"Subhayan",
    "age":21
}]

print(data)

class dataModel(BaseModel):
    name:str
    age:int


#getmethod to fetch data
@api.get('/getData')
def getData():
    return data

#Post method to send data to the server or the api
@api.post('/sendData')
def sendData(new_data:dataModel):
    data.append(new_data)
    return {"message": "successfully data inserted"}

#Put method to update data in the api
@api.put('/updateData/{index}')
def updateData(new_data:dataModel, index):
    data[int(index)]=new_data
    return {"message": "Data Updated"}

#Delete method to delete data in the api
@api.delete('/deleteData')
def deleteData(new_data:dataModel):
    data.remove(new_data)
    return {"message": "Data Deleted"}

#Delete all data 
@api.delete('/deleteAll')
def deleteAll():
    data.clear()
    return {"message":"Data cleared"}




    
    


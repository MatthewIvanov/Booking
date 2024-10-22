from fastapi import FastAPI

app=FastAPI()



@app.get('/hotels/{id}')
def get_hotels(id:int,date_from,date_to):
    return id,date_from,date_to
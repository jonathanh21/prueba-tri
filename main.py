

from fastapi import FastAPI
from database import get_jsonparsed_data
import compress_json
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/characters")
async def index(name: str = None, status: str = None, species:str = None, download:bool = False):
    query_params = '?'
    if name:
        query_params += f"name={name}&" 
    if status:
        query_params += f"status={status}&" 
    if species:
        query_params += f"name={species}" 
    if query_params == '?':
        characters_list = get_jsonparsed_data()
    else:
        characters_list = get_jsonparsed_data(query_params)
    if download:
        file_path = "characters.json.gz"
        compress_json.dump(characters_list, "characters.json.gz")
        return FileResponse(path=file_path, filename=file_path, media_type='text/mp4')
    return {"list": characters_list['results']}



    
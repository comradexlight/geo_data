from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from utils import draw_map


app = FastAPI()
 
@app.get("/")
def root() -> FileResponse:
    return FileResponse("templates/index.html")
 
 
@app.post("/cadastre_number")
def postdata(cadastre_number = Form()) -> FileResponse:
     draw_map(cadastre_number)
     return FileResponse(f"templates/map.html")


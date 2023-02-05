'''The simple server for drawing plot boundaries by cadastre number'''
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from utils import draw_map


app = FastAPI()

@app.get("/")
async def index() -> FileResponse:
    '''This function gives index.html by get request'''
    return FileResponse("templates/index.html")


@app.post("/cadastre_number")
async def post_cadastre_number(cadastre_number = Form()) -> HTMLResponse:
    '''This fucntion gives the page with the map and the boundary'''
    content = draw_map(cadastre_number)
    return HTMLResponse(content=content, status_code=200)

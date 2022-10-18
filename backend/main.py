from typing import Union
from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

# current_file = Path(__file__)
# current_file_dir = current_file.parent
# project_root = current_file_dir.parent
# project_root_absolute = project_root.resolve()
# static_root_absolute = project_root_absolute / "frontend"


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory='templates')

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

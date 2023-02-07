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
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get("/history", response_class=HTMLResponse)
def service(request: Request):
    return templates.TemplateResponse("about/about.html", context={"request": request, "name": 'о нас'})

@app.get("/service", response_class=HTMLResponse)
def service(request: Request):
    return templates.TemplateResponse("about/service.html", context={"request": request, "name": 'сервис'})

@app.get("/product", response_class=HTMLResponse)
def service(request: Request):
    return templates.TemplateResponse("about/product.html", context={"request": request, "name": 'продукты'})

@app.get("/contact", response_class=HTMLResponse)
def service(request: Request):
    return templates.TemplateResponse("about/contact.html", context={"request": request, "name": 'контакт'})

@app.get("/team", response_class=HTMLResponse)
def service(request: Request):
    return templates.TemplateResponse("about/teams.html", context={"request": request, "name": 'команда'})


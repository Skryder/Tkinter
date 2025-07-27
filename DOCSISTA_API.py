from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates  
import CMTS_STATS_MODEL

md = CMTS_STATS_MODEL.CMTS_STATS_MODEL()

class CMTSModel(BaseModel):
    Message: str

app = FastAPI()
template = Jinja2Templates(directory="templates")

@app.post("/static/post-cmts-output/")
async def post_cmts_output(output: CMTSModel):
    print("Posting CMTS Output: " + output.Message + "\n")
    md.parse_from_clipboard(output.Message)
    #print("parsed: " + md.model_string)

@app.get("/static/get-model")
async def get_model():
    return md.model


@app.get("/static/get-readable", response_class=HTMLResponse)
async def get_readable_stats(request: Request):
    return template.TemplateResponse(
        request=request, name="model.html", context={"cmIdx": "1"}
    )




app.mount("/static", StaticFiles(directory="static", html = True), name="static")













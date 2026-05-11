from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Catering Menu")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    items = [
        {
            "name": "Smoky Tandoori Paneer Skewers",
            "description": "Charred paneer cubes with peppers, onions, and mint chutney.",
            "price": "$9 / plate",
        },
        {
            "name": "Butter Chicken Bites",
            "description": "Tender chicken in a rich tomato-cream sauce with mini naan.",
            "price": "$12 / plate",
        },
        {
            "name": "Masala Veg Pulao",
            "description": "Fragrant basmati rice with seasonal vegetables and mild spice.",
            "price": "$8 / plate",
        },
        {
            "name": "Chaat Party Cups",
            "description": "Crunchy, tangy, and sweet street-style chaat served in cups.",
            "price": "$7 / cup",
        },
        {
            "name": "Gulab Jamun Duo",
            "description": "Two warm gulab jamuns finished with pistachio crumbs.",
            "price": "$5 / serving",
        },
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"items": items},
    )


@app.get("/our-story", response_class=HTMLResponse)
async def our_story(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="our_story.html",
        context={},
    )

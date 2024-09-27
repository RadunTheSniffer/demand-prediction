from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from  fastapi.templating import Jinja2Templates
from data_extractor import*


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def query_sites(request: Request):
    return templates.TemplateResponse(
    "query.html", {"request": request}
    )

@app.post("/results")
async def query_results(request: Request, query: str = Form(...)):
    try:
        print(f"Received query: {query}")
        
        if not query:
            raise ValueError("Invalid input: query cannot be empty and count must be positive.")
        
        # Call the scraper function with query and count
        scraped_data = scrape_data(query)
        
        if not scraped_data:
            raise ValueError("No data retrieved.")
        
        return HTMLResponse(content=scraped_data)
    except ValueError as e:
        print(f"ValueError: {e}")
        return HTMLResponse(content=f"<h1>Error: {str(e)}</h1>", status_code=400)
    
    except Exception as e:
            print(f"Exception: {e}")
            return HTMLResponse(content=f"<h1>An unexpected error occurred: {str(e)}</h1>", status_code=500)
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000
    )

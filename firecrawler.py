from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
from typing import List
from smolagents import Tool
import os


#Fetch API key fior firecrawl
api_key = os.getenv("FIRECRAWL_API_KEY")


class FireCrawlTool(Tool):
    name = "firecrawl_website_qa"
    description = """
    This tool scrapes websites using an API call"""
    
    inputs = {
        "website": {
            "type": "string",
            "description": "A singlular website address",
        }
    }
    
    output_type = "string"


    def forward(self, website: str):
    
        # Initialize the FirecrawlApp with the API key
        app = FirecrawlApp(api_key = api_key)


        # Scrape a website:
        scrape_result = app.scrape_url(website, 
            params={
                'location': {
                    'country': 'AU'
                }
            }
        )

        scrape_result =  scrape_result['markdown'][:7000]
    
    
        return scrape_result 
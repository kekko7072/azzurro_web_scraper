from scrapegraphai.graphs import SmartScraperGraph

# THIS IT'S MY PERSONAL API KEY, PLEASE DON'T USE IT IN PRODUCTION
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4",
    },
}


def scrape_from_link(link):
    smart_scraper_graph = SmartScraperGraph(
        prompt="Utilizza questo sito trovare le informazioni sui bandi pubblici.",
        source=link,
        config=graph_config
    )

    return smart_scraper_graph.run()

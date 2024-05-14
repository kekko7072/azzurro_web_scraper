from scrapegraphai.graphs import SmartScraperGraph


def scrape_from_link(OPENAI_API_KEY: str, link: str):
    smart_scraper_graph = SmartScraperGraph(
        prompt="Utilizza questo sito trovare le informazioni sui bandi pubblici.",
        source=link,
        config={
            "llm": {
                "api_key": OPENAI_API_KEY,
                "model": "gpt-4o",
            },
        }
    )

    return smart_scraper_graph.run()

import json

from ingestion import process_news_files

news_data = process_news_files("./data")
print(json.dumps(news_data, indent=2))

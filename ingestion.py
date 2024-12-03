import os


def process_news_files(folder_path):
    news_data = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r') as f:
            file_contents = f.read()

        lines = file_contents.splitlines()
        current_article = {}
        is_content = False
        for line in lines:
            line = line.strip()
            if not line:
                if current_article:  # End of an article
                    news_data.append(current_article)
                    current_article = {}
                is_content = False  # Reset content flag
                continue

            if not current_article.get('title'):
                current_article['title'] = line
            elif '/' in line and len(line) == 10:
                current_article['publication_date'] = line
            elif ',' in line and not is_content:  # Author line
                current_article['author'], current_article['source'] = line.rsplit(',', 1)
                current_article['author'] = current_article['author'].strip()
                current_article['source'] = current_article['source'].strip()
            elif line.startswith('http'):
                current_article['source'] = line
            else:
                is_content = True
                current_article['content'] = (current_article.get('content') or '') + line + '\n'

            if current_article:  # Add the last article if any
                news_data.append(current_article)

    return news_data

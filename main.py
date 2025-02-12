import requests
from flask import Flask, render_template
from googletrans import Translator


app: Flask = Flask(__name__)
translator: Translator = Translator()


@app.route('/', methods=['GET'])
def get_quote() -> str:
    quote_url: str = 'https://api.quotable.io/random'
    response: requests = requests.get(url=quote_url, verify=False)  # Сервер не поддерживает верификацию

    if response.status_code == 200:
        quote_data: dict[str: str] = response.json()
        quote_text: str = quote_data.get('content', 'No quote found')
        author: str = quote_data.get('author', 'Unknown')

        ru_text: str = translator.translate(quote_text, dest='ru').text
        ru_author: str = translator.translate(author, dest='ru').text

    else:
        ru_text: str = 'Ошибка при извлечении цитаты'
        ru_author: str = ''

    return render_template('index.html', quote=ru_text, author=ru_author)


if __name__ == "__main__":
    app.run(debug=False)
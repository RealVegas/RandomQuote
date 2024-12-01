import requests
from flask import Flask, render_template
from googletrans import Translator


app = Flask(__name__)
translator = Translator()


@app.route('/', methods=['GET', 'POST'])
def get_quote():
    quote_url = 'https://api.quotable.io/random'
    response = requests.get(url=quote_url, verify=False)

    if response.status_code == 200:
        quote_data = response.json()
        quote_text = quote_data.get('content', 'No quote found')
        author = quote_data.get('author', 'Unknown')

        trans_text = translator.translate(quote_text, dest='ru').text
        trans_author = translator.translate(author, dest='ru').text

    else:
        trans_text = 'Ошибка при извлечении цитаты'
        trans_author = ''

    return render_template('index.html', quote=trans_text, author=trans_author)



if __name__ == "__main__":
    app.run(debug=True)
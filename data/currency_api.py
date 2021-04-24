from flask import jsonify, Blueprint, request
import bs4
import requests

blueprint = Blueprint('currency_api',
                      __name__)


@blueprint.route('/currency', methods=['GET'])
def get_exchange_rate():
    try:
        currency_from = request.args.get('from')
        currency_to = request.args.get('to')
    except ValueError:
        return jsonify(error='parameters error'), 404
    url = 'https://www.google.com/search?q=курс+{0}+к+{1}&oq=курс+{0}+к+{1}' \
          '&aqs=chrome.0.0i131i433j69i57j0i131i433j0l7.3822j1j7&sourceid=chrome&ie=UTF-8'. \
        format(currency_from, currency_to)
    headers = {"Content-Language": "en-US"}
    response = requests.get(url, headers=headers)
    html_page = response.content
    s = bs4.BeautifulSoup(html_page, 'html.parser')
    convert = s.find_all(class_='BNeawe iBp4i AP7Wnd')
    if not convert:
        return jsonify(error='parameters error'), 404
    full_text = convert[-1].text
    n, *words = full_text.split()
    n, text = n.replace(',', '.'), ' '.join(words)
    return jsonify(exchange=n, text=text)

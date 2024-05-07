from waybackpy import WaybackMachineCDXServerAPI
from waybackpy.exceptions import NoCDXRecordFound

from flask import Flask, request, Response, render_template
import os

app = Flask(__name__)

YEAR_RANGE = (1996, 2023)
YEAR = 2001

def wayback_api(url):
    try:
        cdx_api = WaybackMachineCDXServerAPI(url, "")
        new_url = cdx_api.near(year=YEAR).archive_url
        return new_url
    except NoCDXRecordFound:
        return 'False'

@app.route('/web')
def get_page():
    url = request.args.get('url')
    if(len(url) > 0):
        print(f'Requested: {url}')
        result = wayback_api(url)
    else: result = ''
    return Response(result)

@app.route('/set')
def set_year():
    global YEAR
    new_year = int(request.args.get('year'))
    if new_year < YEAR_RANGE[0] or new_year > YEAR_RANGE[1]: return Response('False', 200)
    YEAR = new_year
    print(f'Changed year to: {YEAR}')
    return Response('True', 200)

@app.route('/')
def index():
    return render_template('whitespace.html', data={'year': YEAR})

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    app.run()
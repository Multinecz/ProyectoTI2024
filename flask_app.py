import webbrowser
import joblib # type: ignore
from flask import Flask, render_template, request # type: ignore


app = Flask(__name__)

def detection(model, x):
    x = str(x)
    language = model.predict([x])[0]
    if len(x) <= 20:
        language = 'frase demasiado corta (<25 chars.)'
    elif language == 'fr':
        language = 'francés'
    elif language == 'pt':
        language = 'portugués'
    elif language == 'it':
        language = 'italiano'
    elif language == 'en':
        language = 'inglés'
    elif language == 'es':
        language = 'español'
    return language


@app.route('/', methods=['POST', 'GET'])
def main_app():
    try:
        result = request.form
        if request.method == 'POST':
            dict_result = dict(result)
            text = dict_result['text_to_language']
            lang = detection(model, text)
        else:
            lang = None
        return render_template('index.html', result={'language': lang.upper()})
    except:
        return render_template('index.html', result={'language': None})


if __name__ == '__main__':
    model = joblib.load('models/model.pkl')
    url = "http://localhost:5000"
    webbrowser.open_new(url)
    app.run()
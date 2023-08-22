from flask import Flask, render_template, request
import redis

app = Flask(__name__, static_folder='static', template_folder='templates')
redis_client = redis.Redis(host='192.168.122.45', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        word_freq = redis_client.zscore('word_freq', search_term.lower())
        return render_template('index.html', search_result=(search_term, word_freq))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, render_template, json
import redis

app = Flask(__name__)
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/top-scores')
def get_top_scores():
    top_scores = redis_conn.zrevrange('word_freq', 0, 9, withscores=True)
    top_scores_dict = {key.decode(): value for key, value in top_scores}
    top_scores_json = json.dumps(top_scores_dict)
    return jsonify(top_scores_dict)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


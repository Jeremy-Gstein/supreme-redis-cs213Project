from flask import Flask, jsonify
import redis
import json

app = Flask(__name__)
redis_conn = redis.Redis(host='10.0.0.22', port=6379, db=0)

@app.route('/top-scores')
def get_top_scores():
    top_scores = redis_conn.zrevrange('word_freq', 0, 9, withscores=True)
    top_scores_dict = dict(top_scores)
    top_scores_json = json.dumps(top_scores_dict)
    return jsonify(top_scores_json)

if __name__ == '__main__':
    app.run()


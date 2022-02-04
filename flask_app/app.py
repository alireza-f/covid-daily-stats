import imp
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('../daily-stats.json') as stats:
        stats_list = json.loads(stats.read())

    today_stats = stats_list[-1]
    return today_stats


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
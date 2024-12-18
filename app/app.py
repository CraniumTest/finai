from flask import Flask, render_template
from data_collection.collect_data import get_stock_data
from analysis.market_trend import analyze_trends
from analysis.sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    stock_data = get_stock_data()
    trend_predictions = analyze_trends(stock_data)
    sentiment = analyze_sentiment("Apple stocks are soaring today, great time to buy!")
    
    return render_template('index.html', trend_predictions=trend_predictions[:5], sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV Data
df = pd.read_csv("ADANIPORTS.csv")

# Convert 'Date' to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    # Prepare data for the chart
    stock_data = {
        "dates": df["Date"].astype(str).tolist(),
        "open": df["Open"].tolist(),
        "high": df["High"].tolist(),
        "low": df["Low"].tolist(),
        "close": df["Close"].tolist(),
        "volume": df["Volume"].tolist()
    }
    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(debug=True)

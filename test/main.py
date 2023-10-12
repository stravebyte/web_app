from flask import Flask, render_template, request
import yfinance as yf
app = Flask(__name__)

@app.route('/')

def index():
 data = "&_&_&_"
 return render_template('index.html', data=data)

@app.route("/submit", methods=['POST'])
def submit():
 start_date = request.form.get("start-date")
 end_date = request.form.get("end-date")
 symbol = request.form.get("symbol")
 data = yf.download(symbol, start=start_date, end=end_date)
 closed_price = data["Close"]
 five_days = closed_price[-5:]
 ten_days = closed_price[-10:]
 five = 0
 ten = 0
 for i in five_days:
  five += i
 for i in ten_days:
  ten += i
 indicate = ""
 if five > ten:
  indicate = "Buy"
 else:
  indicate = "Sell"
 return render_template('index.html', five=five, ten=ten, indicate=indicate)

if __name__ == "__main__":
 app.run(debug=True)

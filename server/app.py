import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def read_csv():
    """Read the CSV file and return as DataFrame"""
    try:
        print("Trying to read CSV...")  # Debug
        # Use absolute path to be sure
        import os
        csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "logs.csv")
        print(f"Looking for CSV at: {csv_path}")  # Debug
        df = pd.read_csv(csv_path)
        print(f"Read {len(df)} rows")  # Debug
        # Remove duplicate headers that got mixed in with data
        df = df[df['ts'] != 'ts']  # Remove header rows
        df['ts'] = pd.to_datetime(df['ts'])
        df['tempC'] = pd.to_numeric(df['tempC'])
        df['humidity'] = pd.to_numeric(df['humidity'])
        print(f"After cleaning: {len(df)} rows")  # Debug
        return df.sort_values('ts')
    except Exception as e:
        print(f"Error reading CSV: {e}")  # Debug
        # If file doesn't exist or is empty, return empty DataFrame
        return pd.DataFrame(columns=['ts', 'tempC', 'humidity'])

@app.route('/')
def dashboard():
    """Show the main page"""
    return render_template('index.html')

@app.route('/api/latest')
def latest_reading():
    """Get the most recent sensor reading"""
    df = read_csv()
    
    if df.empty:
        return jsonify({"data": None})
    
    # Get the last row
    latest = df.iloc[-1]
    
    data = {
        "ts": latest['ts'].isoformat(),
        "tempC": float(latest['tempC']),
        "humidity": float(latest['humidity'])
    }
    
    return jsonify({"data": data})

@app.route('/api/series')
def time_series():
    """Get all the data for charts"""
    df = read_csv()
    
    if df.empty:
        return jsonify({"data": {"ts": [], "tempC": [], "humidity": []}})
    
    # Convert to lists for the charts
    data = {
        "ts": [ts.isoformat() for ts in df['ts']],
        "tempC": df['tempC'].tolist(),
        "humidity": df['humidity'].tolist()
    }
    
    return jsonify({"data": data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
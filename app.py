from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for daily logs (in-memory, no database)
daily_logs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analysis', methods=['GET', 'POST'])
def analysis_result():
    if request.method == 'POST':
        # Mock food analysis result (no real ML model)
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        # Simulate food detection
        result = {
            'foods': [
                {'name': 'Apple', 'portion': 1, 'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2},
                {'name': 'Bread', 'portion': 2, 'calories': 160, 'protein': 6, 'carbs': 30, 'fat': 2}
            ],
            'total': {'calories': 212, 'protein': 6.3, 'carbs': 44, 'fat': 2.2}
        }
        
        # Store in daily logs
        daily_logs.append({
            'timestamp': datetime.now(),
            'foods': result['foods'],
            'total': result['total']
        })
        
        return render_template('analysis_result.html', result=result)
    return render_template('analysis_result.html', result=None)

@app.route('/daily-log')
def daily_log():
    return render_template('daily_log.html', logs=daily_logs)

@app.route('/api/track-food', methods=['POST'])
def track_food():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    # Mock API response
    result = {
        'foods': [
            {'name': 'Apple', 'portion': 1, 'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2},
            {'name': 'Bread', 'portion': 2, 'calories': 160, 'protein': 6, 'carbs': 30, 'fat': 2}
        ],
        'total': {'calories': 212, 'protein': 6.3, 'carbs': 44, 'fat': 2.2}
    }
    
    # Store in daily logs
    daily_logs.append({
        'timestamp': datetime.now(),
        'foods': result['foods'],
        'total': result['total']
    })
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
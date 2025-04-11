# Food Tracker (Simplified)

A minimal Flask-based food tracking module built for a hackathon challenge. Users can upload an image of their meal, view a mock nutritional breakdown (calories, protein, carbs, fats), and track daily logs using a simple web interface. This version uses hardcoded data and does not include machine learning or database integration.

## Features
- **Image Upload**: Upload or capture a meal image via a web interface.
- **Mock Nutritional Analysis**: Displays a hardcoded breakdown for Apple and Bread.
- **Daily Log**: Tracks uploaded meals with timestamps (stored in-memory).
- **Responsive UI**: Clean, user-friendly design with CSS styling.

## Project Structure
bash '''
food_tracker/
├── /static/
│   ├── /css/
│   │   └── style.css
├── /templates/
│   ├── base.html
│   ├── index.html
│   ├── analysis_result.html
│   ├── daily_log.html
├── app.py
├── requirements.txt
└── README.md
'''


## Prerequisites
- Python 3.6 or higher
- A web browser (Chrome, Firefox, Edge recommended)
bash '''
python app.py
'''

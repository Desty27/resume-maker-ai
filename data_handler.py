import json
import os
from datetime import datetime

def save_user_data(data):
    """Save user data to JSON file with timestamp"""
    os.makedirs('user_data', exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"user_data/{data['personal']['name'].replace(' ', '_')}_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    return filename
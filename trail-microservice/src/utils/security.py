from flask import request, jsonify
import re

def validate_trail_data(data):
    if not isinstance(data, dict):
        return False, "Invalid data format"
    
    required_fields = ['TrailID', 'Trail_name', 'Trail_Summary', 'Trail_Description', 'Difficulty', 'Location', 'Length', 'Elevation_gain', 'Route_type', 'OwnerID']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    if not isinstance(data['Trail_name'], str) or len(data['Trail_name']) > 255:
        return False, "Trail_name must be a string with a maximum length of 255 characters"
    
    if not isinstance(data['Trail_Summary'], str) or len(data['Trail_Summary']) > 255:
        return False, "Trail_Summary must be a string with a maximum length of 255 characters"
    
    if not isinstance(data['Trail_Description'], str):
        return False, "Trail_Description must be a string"
    
    if not isinstance(data['Difficulty'], str) or len(data['Difficulty']) > 50:
        return False, "Difficulty must be a string with a maximum length of 50 characters"
    
    if not isinstance(data['Location'], str) or len(data['Location']) > 255:
        return False, "Location must be a string with a maximum length of 255 characters"
    
    if not isinstance(data['Length'], (int, float)):
        return False, "Length must be a number"
    
    if not isinstance(data['Elevation_gain'], int):
        return False, "Elevation_gain must be an integer"
    
    if not isinstance(data['Route_type'], str) or len(data['Route_type']) > 50:
        return False, "Route_type must be a string with a maximum length of 50 characters"
    
    if not isinstance(data['OwnerID'], int):
        return False, "OwnerID must be an integer"
    
    return True, "Validation successful"

def sanitize_input(input_string):
    return re.sub(r'[<>]', '', input_string)  # Remove potential HTML tags

def handle_error(error_message):
    response = jsonify({"error": error_message})
    response.status_code = 400
    return response
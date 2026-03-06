import sys
import os
import random

# Mock request context
class MockRequest:
    args = {}
    
sys.modules['flask.request'] = MockRequest()

sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    from backend.app import rankings_db, get_country_profile_detail, app
    
    # Needs a context
    with app.app_context():
        # Test valid country
        response = get_country_profile_detail('IND')
        data = response.json
        print(f"Country: {data['name']}")
        print(f"Rank: {data['rank']}")
        print(f"Total Countries: {data.get('total_countries')}")
        
        if data['rank'] > 0 and data.get('total_countries') >= 190:
            print("SUCCESS: Dynamic rank and total count present.")
        else:
            print("FAILURE: Invalid rank or missing total count.")

except Exception as e:
    print(f"Error: {e}")

import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    from backend.app import rankings_db, global_sustainability_data
    from backend.country_data_names import country_names
    
    print(f"Global Data Count: {len(global_sustainability_data)}")
    print(f"Rankings DB Count: {len(rankings_db)}")
    
    expected_min = 190
    if len(rankings_db) >= expected_min:
        print("SUCCESS: Rankings DB populated with all countries.")
    else:
        print(f"FAILURE: Rankings DB has only {len(rankings_db)} entries. Expected > {expected_min}")
        
    # Check a specific new country
    burundi = next((r for r in rankings_db if r["id"] == "BDI"), None)
    if burundi:
        print(f"Found new country: {burundi['name']} - Score: {burundi['overall_score']}")
    else:
        print("FAILURE: Could not find new country 'Burundi' (BDI)")
        
except Exception as e:
    print(f"Error during verification: {e}")

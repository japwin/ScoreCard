from flask import Flask, request, jsonify, session
from flask_cors import CORS
from airtable import Airtable
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'try'  # Replace with a real secret key

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
)

# Initialize Airtable
AIRTABLE_API_KEY = 'your_api_key'
AIRTABLE_BASE_ID = 'your_base_id'
AIRTABLE_TABLE_NAME = 'Fights'
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)

# Helper decorator to initialize user session data if not present
def ensure_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({'error': 'User not logged in'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.json['username']
    return jsonify({'message': 'Logged in successfully'})

@app.route('/start_fight', methods=['POST'])
@ensure_user
def start_fight():
    record = {
        'Username': session['username'],
        'Fighter1': request.json['fighter1'],
        'Fighter2': request.json['fighter2'],
        'Round Number': 1,
        'SCard1': json.dumps([]),
        'SCard2': json.dumps([]),
        'Pick Counts': json.dumps({'fighter1': 0, 'fighter2': 0, 'draw': 0}),
    }
    try:
        airtable.insert(record)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'message': 'Fight started successfully'})

@app.route('/round', methods=['POST'])
@ensure_user
def round():
    round_number = request.json['round_number']
    username = session['username']
    try:
        fight_record = airtable.search('Username', username)
        if not fight_record:
            return jsonify({'error': 'Fight record not found'}), 404
        fight = fight_record[0]['fields']
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Process the round
    SCard1 = json.loads(fight['SCard1'])
    SCard2 = json.loads(fight['SCard2'])
    pick_counts = json.loads(fight['Pick Counts'])

    # Handle different actions
    if 'ko' in request.json:
        fight['Winner'] = f"KO - {request.json['winner']}"
        pick_counts[request.json['winner']] += 1
        fight['Pick Counts'] = json.dumps(pick_counts)
        airtable.update(fight_record[0]['id'], fight)
        return jsonify({'message': 'Fight ended with KO'})

    # Handle other actions similarly...
    
    return jsonify({'message': 'Round processed successfully'})

@app.route('/results', methods=['GET'])
@ensure_user
def results():
    username = session['username']
    try:
        fight_record = airtable.search('Username', username)
        if not fight_record:
            return jsonify({'error': 'Fight record not found'}), 404
        fight = fight_record[0]['fields']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    total1 = sum(json.loads(fight['SCard1']))
    total2 = sum(json.loads(fight['SCard2']))
    pick_counts = json.loads(fight['Pick Counts'])

    if fight['Winner'] is None:
        if total1 > total2:
            winner = fight['Fighter1']
            pick_counts['fighter1'] += 1
        elif total2 > total1:
            winner = fight['Fighter2']
            pick_counts['fighter2'] += 1
        else:
            winner = "Draw"
            pick_counts['draw'] += 1
        fight['Winner'] = winner
        fight['Pick Counts'] = json.dumps(pick_counts)
        airtable.update(fight_record[0]['id'], fight)
    else:
        winner = fight['Winner']
    
    return jsonify({
        'username': username,
        'fighter1': fight['Fighter1'],
        'fighter2': fight['Fighter2'],
        'SCard1': json.loads(fight['SCard1']),
        'SCard2': json.loads(fight['SCard2']),
        'winner': winner,
        'pick_counts': pick_counts
    })

@app.route('/reset', methods=['POST'])
@ensure_user
def reset():
    username = session['username']
    try:
        fight_record = airtable.search('Username', username)
        if not fight_record:
            return jsonify({'error': 'Fight record not found'}), 404
        airtable.delete(fight_record[0]['id'])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'message': 'Fight reset successfully'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS
app.secret_key = 'try'  # Replace with a real secret key

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
)

# Initialize global variables to store pick counts
pick_counts = {'fighter1': 0, 'fighter2': 0, 'draw': 0}

# Helper decorator to initialize user session data if not present
def ensure_session_data(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'SCard1' not in session:
            session['SCard1'] = []
        if 'SCard2' not in session:
            session['SCard2'] = []
        if 'round_number' not in session:
            session['round_number'] = 1
        if 'winner' not in session:
            session['winner'] = None
        if 'fighter1' not in session:
            session['fighter1'] = "Fighter 1"
        if 'fighter2' not in session:
            session['fighter2'] = "Fighter 2"
        if 'username' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('fighters'))
    return render_template('index.html')

@app.route('/fighters', methods=['GET', 'POST'])
@ensure_session_data
def fighters():
    if request.method == 'POST':
        session['fighter1'] = request.form['fighter1']
        session['fighter2'] = request.form['fighter2']
        return redirect(url_for('round', round_number=1))
    return render_template('fighters.html')

@app.route('/round/<int:round_number>', methods=['GET', 'POST'])
@ensure_session_data
def round(round_number):
    if request.method == 'POST':
        if 'ko' in request.form:
            session['winner'] = f"KO - {request.form['winner']}"
            if request.form['winner'] == 'fighter1':
                pick_counts['fighter1'] += 1
            else:
                pick_counts['fighter2'] += 1
            return redirect(url_for('results'))
        if 'no_contest' in request.form:
            session['winner'] = "No Contest"
            return redirect(url_for('results'))
        if 'points' in request.form:
            session['SCard1'].append(int(request.form['score1']))
            session['SCard2'].append(int(request.form['score2']))
            return redirect(url_for('results'))
        if 'finish' in request.form:
            session['SCard1'].append(int(request.form['score1']))
            session['SCard2'].append(int(request.form['score2']))
            return redirect(url_for('results'))

        session['SCard1'].append(int(request.form['score1']))
        session['SCard2'].append(int(request.form['score2']))
        if round_number >= 15:
            return redirect(url_for('results'))
        session['round_number'] = round_number + 1
        return redirect(url_for('round', round_number=round_number + 1))
    return render_template('round.html', round_number=round_number, fighter1=session['fighter1'], fighter2=session['fighter2'])

@app.route('/results')
@ensure_session_data
def results():
    total1 = sum(session['SCard1'])
    total2 = sum(session['SCard2'])
    if session['winner'] is None:
        if total1 > total2:
            winner = session['fighter1']
            pick_counts['fighter1'] += 1
        elif total2 > total1:
            winner = session['fighter2']
            pick_counts['fighter2'] += 1
        else:
            winner = "Draw"
            pick_counts['draw'] += 1
    else:
        winner = session['winner']
    return render_template('results.html', username=session['username'], fighter1=session['fighter1'], fighter2=session['fighter2'], SCard1=session['SCard1'], SCard2=session['SCard2'], winner=winner, pick_counts=pick_counts)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

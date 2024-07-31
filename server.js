const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const cors = require('cors');

const app = express();
const port = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true
}));

// Routes
app.get('/', (req, res) => {
    if (req.method === 'POST') {
        req.session.username = req.body.username;
        res.redirect('/fighters');
    } else {
        res.send('<form method="post"><input name="username" /><button type="submit">Submit</button></form>');
    }
});

app.get('/fighters', (req, res) => {
    if (req.method === 'POST') {
        req.session.fighter1 = req.body.fighter1;
        req.session.fighter2 = req.body.fighter2;
        res.redirect('/round/1');
    } else {
        res.send('<form method="post"><input name="fighter1" /><input name="fighter2" /><button type="submit">Submit</button></form>');
    }
});

app.get('/round/:round_number', (req, res) => {
    const roundNumber = req.params.round_number;
    if (req.method === 'POST') {
        // Handle POST request here
        res.redirect(`/round/${parseInt(roundNumber) + 1}`);
    } else {
        res.send(`<h1>Round ${roundNumber}</h1><form method="post"><button type="submit">Next Round</button></form>`);
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

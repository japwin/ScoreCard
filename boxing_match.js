let SCard1 = [];
let SCard2 = [];
let fighter1, fighter2;

function submitFighters() {
    fighter1 = document.getElementById('fighter1').value;
    fighter2 = document.getElementById('fighter2').value;
    
    if (!fighter1 || !fighter2) {
        alert('Please enter names for both fighters.');
        return;
    }

    alert('Hello ' + fighter1 + ' and ' + fighter2);
    startRounds();
}

function startRounds() {
    document.getElementById('rounds').innerHTML = `
        <button onclick="handleRound(1)">Start Round 1</button>
    `;
}

function handleRound(roundNumber) {
    let roundContent = `
        <h2>Round ${roundNumber}</h2>
        <label>${fighter1} Score: <input type="number" id="Round${roundNumber}F1" min="7" max="10"></label>
        <label>${fighter2} Score: <input type="number" id="Round${roundNumber}F2" min="7" max="10"></label>
        <button onclick="submitRound(${roundNumber})">Submit Round ${roundNumber}</button>
    `;
    document.getElementById('rounds').innerHTML = roundContent;
}

function submitRound(roundNumber) {
    let RoundF1 = parseInt(document.getElementById(`Round${roundNumber}F1`).value);
    let RoundF2 = parseInt(document.getElementById(`Round${roundNumber}F2`).value);

    // Validate scores
    if (isNaN(RoundF1) || isNaN(RoundF2) || RoundF1 < 7 || RoundF1 > 10 || RoundF2 < 7 || RoundF2 > 10) {
        alert('Scores must be between 7 and 10.');
        return;
    }

    // Store scores
    SCard1.push(RoundF1);
    SCard2.push(RoundF2);
    
    // Calculate totals
    let overall1 = SCard1.reduce((a, b) => a + b, 0);
    let overall2 = SCard2.reduce((a, b) => a + b, 0);
    
    // Show scores
    alert(`${fighter1} Scores: ${SCard1.join(", ")} Total: ${overall1}`);
    alert(`${fighter2} Scores: ${SCard2.join(", ")} Total: ${overall2}`);
    
    // Decide whether to continue
    if (roundNumber < 15) {
        let continueMatch = confirm('Continue to next round?');
        if (continueMatch) {
            handleRound(roundNumber + 1);
        } else {
            Results();
        }
    } else {
        alert('Fight goes to Scorecards');
        ScoreCards();
    }
}

function Results() {
    let ending = prompt('How did it end? 1=KO, 2=No Contest, 3=Scorecards, 4=DQ');
    if (ending === '1') {
        KnockOut();
    } else if (ending === '2') {
        alert('No Contest');
        alertResults();
    } else if (ending === '3') {
        ScoreCards();
    } else if (ending === '4') {
        alert('Under Construction');
        alert('Bye');
    }
}

function KnockOut() {
    let overall1 = SCard1.reduce((a, b) => a + b, 0);
    let overall2 = SCard2.reduce((a, b) => a + b, 0);
    
    let KOWinner = prompt(`Who Won? 1=${fighter1} 2=${fighter2}`);
    if (KOWinner === '1') {
        alert(`Winner by KO ${fighter1}`);
    } else if (KOWinner === '2') {
        alert(`Winner by KO ${fighter2}`);
    } else {
        alert('You Drunk?!');
    }
    alertResults();
}

function ScoreCards() {
    let Scorecard1 = SCard1.reduce((a, b) => a + b, 0);
    let Scorecard2 = SCard2.reduce((a, b) => a + b, 0);
    
    if (Scorecard1 > Scorecard2) {
        alert(`Winner by Decision ${fighter1}`);
    } else if (Scorecard2 > Scorecard1) {
        alert(`Winner by Decision ${fighter2}`);
    } else {
        alert('Draw');
    }
    alertResults();
}

function alertResults() {
    let overall1 = SCard1.reduce((a, b) => a + b, 0);
    let overall2 = SCard2.reduce((a, b) => a + b, 0);
    alert(`${fighter1} Scores: ${SCard1.join(", ")} Total: ${overall1}`);
    alert(`${fighter2} Scores: ${SCard2.join(", ")} Total: ${overall2}`);
    alert('Bye');
}

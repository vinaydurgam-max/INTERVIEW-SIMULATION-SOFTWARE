const express = require('express');
const mysql = require('mysql2');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// MySQL Database Connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root', 
    password: 'mysql', 
    database: 'interview_simulation' 
});

// Connect to the MySQL database
db.connect((err) => {
    if (err) {
        console.error('Database connection error: ', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// Route: Serve the home page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route: Serve the candidate page
app.get('/candidate.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'candidate.html'));
});

// Route: Serve the expert page
app.get('/expert.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'expert.html'));
});

// Route: Serve the demo page
app.get('/demo.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'demo.html'));
});

// Route: Serve the terms and conditions page
app.get('/terms.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'terms.html'));
});

// Route: Serve the about page
app.get('/about.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'about.html'));
});

// API Routes: CRUD operations for candidates

// Get all candidates
app.get('/api/candidates', (req, res) => {
    db.query('SELECT * FROM candidates', (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// Add a new candidate
app.post('/api/candidates', (req, res) => {
    const { name, email, phone } = req.body;
    const query = 'INSERT INTO candidates (name, email, phone) VALUES (?, ?, ?)';
    db.query(query, [name, email, phone], (err, result) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ id: result.insertId });
    });
});

// API Routes: CRUD operations for experts

// Get all experts
app.get('/api/experts', (req, res) => {
    db.query('SELECT * FROM experts', (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// Add a new expert
app.post('/api/experts', (req, res) => {
    const { name, email, expertise } = req.body;
    const query = 'INSERT INTO experts (name, email, expertise) VALUES (?, ?, ?)';
    db.query(query, [name, email, expertise], (err, result) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ id: result.insertId });
    });
});

// API Routes: Interview management

// Start a new interview
app.post('/api/interviews/start', (req, res) => {
    const { candidate_id, expert_id } = req.body;
    const query = 'INSERT INTO interviews (candidate_id, expert_id, start_time) VALUES (?, ?, NOW())';
    db.query(query, [candidate_id, expert_id], (err, result) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Interview started', interviewId: result.insertId });
    });
});

// End an interview
app.post('/api/interviews/end/:id', (req, res) => {
    const interviewId = req.params.id;
    const query = 'UPDATE interviews SET end_time = NOW() WHERE id = ?';
    db.query(query, [interviewId], (err) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Interview ended' });
    });
});

// Get all interviews
app.get('/api/interviews', (req, res) => {
    const query = `SELECT interviews.id, candidates.name AS candidate_name, experts.name AS expert_name, 
                   interviews.start_time, interviews.end_time, interviews.total_score 
                   FROM interviews 
                   JOIN candidates ON interviews.candidate_id = candidates.id 
                   JOIN experts ON interviews.expert_id = experts.id`;
    db.query(query, (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// API Routes: Questions and Responses

// Get all questions for a given level
app.get('/api/questions/:level', (req, res) => {
    const level = req.params.level;
    const query = 'SELECT * FROM questions WHERE level = ?';
    db.query(query, [level], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// Add a candidate response
app.post('/api/responses', (req, res) => {
    const { interview_id, question_id, response_text, score } = req.body;
    const query = 'INSERT INTO responses (interview_id, question_id, response_text, score) VALUES (?, ?, ?, ?)';
    db.query(query, [interview_id, question_id, response_text, score], (err, result) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ id: result.insertId });
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

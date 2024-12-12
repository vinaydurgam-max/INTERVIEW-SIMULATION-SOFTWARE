# Web-Based Selector-Applicant Simulation Software

This project is a **Selector-Applicant Simulation Software** designed to assist in recruitment and assessment by providing an immersive, boardroom-like interview experience. The software is developed for the Recruitment and Assessment Centre (RAC) under DRDO, Ministry of Defence, to ensure an unbiased and objective interviewing process.

## **Features**

- **Dynamic Questioning**: Experts can create and manage interview questions relevant to the candidate's expertise.
- **Real-Time Response Analysis**: The system evaluates candidate responses using NLP to score relevancy and quality.
- **Integrated Scoring**: Automated scoring for both questions and responses ensures an objective evaluation.
- **Database Storage**: All interview data is securely stored in a MySQL database for future reference and analysis.

## **Technology Stack**

- **Front-End**: React.js for an intuitive user interface.
- **Back-End**: Node.js with Express for handling server-side logic and API endpoints.
- **NLP Service**: Python with Flask for evaluating questions and responses using pre-trained transformer models.
- **Database**: MySQL for persistent data storage.

## **Setup Instructions**

### Prerequisites

Ensure the following are installed on your system:

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [MySQL](https://dev.mysql.com/downloads/installer/)
- [VS Code](https://code.visualstudio.com/)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/yourusername/interview-simulation.git
cd interview-simulation
```

### **Step 2: Set Up the Database**

1. Open MySQL Workbench or connect via the command line.
2. Create a database and table:

```sql
CREATE DATABASE rac_simulation;

USE rac_simulation;

CREATE TABLE interviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    questions TEXT,
    responses TEXT,
    question_scores TEXT,
    response_scores TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Step 3: Set Up the Back-End**

1. Navigate to the `backend` directory:

```bash
cd backend
```

2. Install dependencies:

```bash
npm install
```

3. Start the server:

```bash
node server.js
```

### **Step 4: Set Up the Front-End**

1. Navigate to the `frontend` directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React application:

```bash
npm start
```

### **Step 5: Set Up the NLP Service**

1. Navigate to the `nlp-service` directory:

```bash
cd nlp-service
```

2. Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask nltk transformers
```

3. Start the Flask application:

```bash
python app.py
```

### **Step 6: Test the Application**

- Open the React application in your browser (usually at `http://localhost:3000`).
- Add interview questions and responses.
- Submit the interview and verify scores in the console and MySQL database.

## **Project Structure**

```
interview-simulation/
├── backend/                     # Server-side logic and API
│   ├── server.js                # Main Node.js server file
│   ├── package.json             # Backend dependencies
│   └── config/                  # Configuration files
│       └── db.js                # MySQL database connection logic
├── frontend/                    # Client-side application
│   ├── public/                  # Static files (HTML, CSS, JS)
│   │   ├── index.html           # Entry point HTML file
│   │   └── favicon.ico          # Favicon
│   ├── src/                     # React components
│   │   ├── App.js               # Main React component
│   │   ├── index.js             # Entry point for React app
│   │   ├── components/          # Reusable components
│   │   │   ├── QuestionForm.js  # Component for adding questions
│   │   │   ├── ResponseForm.js  # Component for candidate responses
│   │   │   └── ScoreCard.js     # Component to display scores
│   └── package.json             # Frontend dependencies
├── nlp-service/                 # Natural Language Processing service
│   ├── app.py                   # Flask application for NLP logic
│   ├── requirements.txt         # Python dependencies
│   └── models/                  # Pre-trained NLP models
│       └── transformer_model/   # Directory for model files
├── database/                    # Database scripts and backups
│   ├── create_tables.sql        # SQL script to create database schema
│   └── seed_data.sql            # Script to populate initial data
├── tests/                       # Test cases for each module
│   ├── backend.test.js          # Test cases for backend API
│   ├── frontend.test.js         # Test cases for React components
│   └── nlp-service.test.py      # Test cases for Flask NLP service
├── README.md                    # Project documentation
├── LICENSE                      # Project license
└── .gitignore                   # Files and directories to ignore in Git
```

## **Future Enhancements**

- Advanced NLP models for more nuanced response analysis.
- Real-time audio and video interviewing capabilities.
- Role-specific question generation.
- Enhanced reporting and analytics for interview outcomes.

## **Contributors**

- [Your Name](https://github.com/yourusername) - Developer
  

## **License**

This project is licensed for DURGAM VINAY KUMAR. See the `LICENSE` file for details.


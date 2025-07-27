# Conversational AI for Banking

This project is a proof-of-concept for a conversational AI system designed to handle dynamic banking interactions, as described in the second problem statement.

## Project Overview

The goal is to build an intelligent assistant that can manage multi-turn conversations for tasks like:
- Applying for loans
- Blocking a lost or stolen card
- Requesting account statements
- Checking balances

## Features

- **Multi-Turn Conversation:** Manages context across multiple user messages.
- **Task-Oriented:** Guides users through specific banking workflows.
- **API Integration:** Interacts with mock banking APIs to perform actions.
- **Context Switching:** (Future Goal) Will handle shifts in user intent.

## Getting Started

To get started with this project, you'll need to have Python and `pip` installed.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

This project consists of two main components: the mock API server and the conversational AI application. You'll need to run them in separate terminals.

**1. Run the Mock API Server:**

In your first terminal, start the Flask server:
```bash
python api/mock_server.py
```
You should see output indicating that the server is running on `http://127.0.0.1:5000`.

**2. Run the Backend Server:**

In your second terminal, start the Python backend server:
```bash
python src/server.py
```
You should see output indicating that the server is running on `http://127.0.0.1:5001`.

**3. Run the React Frontend:**

In a third terminal, navigate to the `frontend` directory and start the React development server:
```bash
cd frontend
npm start
```
This will open a new browser tab with the chat application.

## Use Cases

1.  **Block a Card:** A user can request to block their debit or credit card.
2.  **Check Balance:** A user can ask for their account balance.

# Appui Pro : Analyste Financier IA Gen

This repository contains the backend and frontend of the AI Generative financial analysis for BPGO "Conseillers Pros"

## Setup Local

```bash
# Install the prerequisite software 
bash bin/setup.sh

# Exit the shell and start a new one for the Python virtual environment to be activated.
exit
```


## Running Services

```bash
# Run the services
make run_locally

# Stop the services
make stop_locally
```

Streamlit Web Service: Accessible at http://localhost:8501
Swagger API Documentation: Available at http://localhost:8001/docs

## Tests

```bash
# Unit Tests
make run_unit_tests

# Integration Tests
make run_integration_tests   # Ensure services are running before executing

# Acceptance Tests
make run_bdd   # Ensure services are running before executing

# Code Quality Tests
make lint
```

## Repository Structure

### Backend Structure
- 📂`backend`: Contains the scripts for the Flask backend API.
  - 🐳 `Dockerfile`: Script to build the backend image.
  - 📄 `requirements.txt`: Lists backend dependencies.
  - 🐍 `app.py`: Defines the Flask API.
  - 📂`src`: Source directory for backend components:
    - 📂`models`: API models for `flask_restx`.
    - 📂`routes`: API routes for Flask.
    - 📂`services`: Services utilized by the routes.
    - 📂`utils`: Utility functions used by the services.

### Frontend Structure
- 📂`frontend`: Contains the scripts for the Streamlit frontend.
  - 🐳 `Dockerfile`: Script to build the frontend image.
  - 📄 `requirements.txt`: Lists frontend dependencies.
  - 🐍 `app.py`: Defines the Streamlit app.
  - 📂`src`: Source directory for frontend components:
    - 📂`components`: Defines reusable components.
    - 📂`pages`: Scripts for rendering pages.
    - 📂`utils`: Functions used by pages and components.

### Testing & Utilities
- 📂`features`: Acceptance tests written in Gherkin format, runnable via "behave" or "make run_bdd".
- 📂`tests`: Contains unit and integration tests:
  - 📂`unittests`: Unit tests categorized by:
    - 📂`backend`: Backend unit tests.
    - 📂`frontend`: Frontend unit tests.
    - 📂`utils`: Utility function unit tests.
  - 🧪 `test_integration.py`: Integration tests.
- 📂`utils`: Utility scripts:
  - `fill_database.py`: Fills the PostgreSQL database with BPGO data.

### Deployment
- 📂`deploy`:
  - 🐳 `compose.yml`: Script to launch containers.

### Additional Configuration
- 🛠️ `Makefile`: Provides commands for run, build, test, and more.
- 📄 `requirements.txt`: Lists all dependencies.
- 🛠️ `setup.cfg`: Enhances testing and code quality commands.
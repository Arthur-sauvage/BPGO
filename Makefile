help:  ## 📜 Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-30s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

VERSION = ":latest"
GROUPE =""
ARGUMENT=""

# Function to build Docker image
build_image:
	@echo "Building container image $(tag)..."
	@docker build -t $(tag) $(dir)

.PHONY: build_images

build_images:  ## 🔨 Build container images from Dockerfiles
	@echo "Building container images..."
	@$(MAKE) build_image dir=backend tag=$(GROUPE)back_Appui_Pro$(VERSION) &
	@$(MAKE) build_image dir=frontend tag=$(GROUPE)front_Appui_Pro$(VERSION) &

create_venv_locally:  ## 🐍 Create a virtual environment locally
	@echo "Creating virtual environment..."
	@python3 -m venv .venv

install_dependancies:  ## 📦 Install the dependencies
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

run_postgres:  ## 🐘 Run the PostgreSQL database
	@echo "Running the PostgreSQL database..."
	@docker run --name postgres -e POSTGRES_DB=$(POSTGRES_DB) -e POSTGRES_USER=$(POSTGRES_USER) -e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) -d -p $(POSTGRES_PORT):5432 postgres:latest

fill_db:  ## 📚 Fill the database with data
	@echo "Filling the database with data..."
	@python utils/fill_database.py

run_locally:  ## 🚀 Run the application locally
	@echo "Running the application locally..."
	@streamlit run frontend/app.py --server.port 8501 & echo $$! > streamlit.pid
	@export FLASK_ENV=development
	@python backend/app.py & echo $$! > flask.pid

stop_locally:  ## 🔴 Stop the application
	@echo "Stopping the application..."
	@[ -f streamlit.pid ] && kill `cat streamlit.pid` && rm streamlit.pid || echo "Streamlit not running"
	@[ -f flask.pid ] && kill `cat flask.pid` && rm flask.pid || echo "Flask not running"

run_unit_tests:  ## 🧪 Run the unit tests
	@echo "Running the unit tests..."
	@nosetests tests/unittests

run_integration_tests:  ## 🧪 Run the integration tests
	@echo "Running the integration tests..."
	@nosetests tests/integrations/

run_all_tests:  ## 🧪 Run all the tests (unit & integration)
	@echo "Running all the tests..."
	@nosetests

run_tests:  ## 🧪 Run test with potential argument
	@echo "Running the tests on $(ARGUMENT)..."
	@nosetests $(ARGUMENT)

run_bdd:  ## 🧪 Run the BDD tests
	@echo "Running the BDD tests..."
	@behave

lint:  ## 🧹 Lint the code
	@echo "Linting the code..."
	flake8 backend frontend tests features --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 backend frontend tests features --count --max-complexity=10 --max-line-length=127 --statistics
	pylint backend frontend tests features --max-line-length=127
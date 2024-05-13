#!/bin/bash
echo "**************************************************"
echo " Setting up Appui Pro Project Environment"
echo "**************************************************"

# Function to check if the file exists
check_document_exists() {
    if [ ! -f "documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx" ]; then
        echo "Error: The required file 'documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx' does not exist."
        echo "Please ensure the file is present and re-run the setup script."
        exit 1
    fi
}
# Function to check if the file exists
check_env_exists() {
    if [ ! -f ".env" ]; then
        echo "Creating .env file..."
        touch .env
    fi
}

add_env_variables() {
    local env_file=".env"
    local postgres_name="POSTGRES_NAME=postgres"
    local postgres_db="POSTGRES_DB=my_db"
    local postgres_user="POSTGRES_USER=my_user"
    local postgres_password="POSTGRES_PASSWORD=my_password"
    local postgres_port="POSTGRES_PORT=5432"
    local postgres_host="POSTGRES_HOST=localhost"

    # Check if each environment variable exists in the .env file
    if ! grep -q "^$postgres_name" "$env_file"; then
        echo "Adding '$postgres_name' to $env_file"
        echo "$postgres_name" >> "$env_file"
    fi

    if ! grep -q "^$postgres_db" "$env_file"; then
        echo "Adding '$postgres_db' to $env_file"
        echo "$postgres_db" >> "$env_file"
    fi

    if ! grep -q "^$postgres_user" "$env_file"; then
        echo "Adding '$postgres_user' to $env_file"
        echo "$postgres_user" >> "$env_file"
    fi

    if ! grep -q "^$postgres_password" "$env_file"; then
        echo "Adding '$postgres_password' to $env_file"
        echo "$postgres_password" >> "$env_file"
    fi

    if ! grep -q "^$postgres_port" "$env_file"; then
        echo "Adding '$postgres_port' to $env_file"
        echo "$postgres_port" >> "$env_file"
    fi

    if ! grep -q "^$postgres_host" "$env_file"; then
        echo "Adding '$postgres_host' to $env_file"
        echo "$postgres_host" >> "$env_file"
    fi
}

# Function to check if the current user is in the docker group
check_docker_group() {
    if groups "$USER" | grep &>/dev/null '\bdocker\b'; then
        return 0  # User is in the docker group
    else
        return 1  # User is not in the docker group
    fi
}

# Function to wait for the PostgreSQL container to start
wait_for_postgres() {
    local max_retries=5
    local wait_seconds=5
    local retry_count=0

    echo "Waiting for PostgreSQL container to start..."

    until docker exec postgres pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" &>/dev/null; do
        if [ $retry_count -eq $max_retries ]; then
            echo "Error: PostgreSQL container did not start within the expected time."
            exit 1
        fi

        retry_count=$((retry_count + 1))
        sleep "$wait_seconds"
    done

    echo "PostgreSQL container is ready."
}

# Check if the file exists before proceeding
echo "*** Checking if the required file exists..."
check_document_exists

# Check if the .env file exists
echo "*** Checking if the .env file exists..."
check_env_exists

# Add or update environment variables in .env file
echo "*** Adding environment variables to .env file..."
add_env_variables

# Source the .env file to load environment variables
if [ -f .env ]; then
    source .env
fi

echo "*** Installing Docker & Make"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker.io make

# Check if the user is in the docker group
if ! check_docker_group; then
    echo "Error: User is not in the docker group."
    echo "Please add the user to the docker group or run this script with sudo."
    exit 1
fi

echo "*** Creating a Python virtual environment"
python3 -m venv .venv

echo "*** Configuring the developer environment..."
echo "# Appui Pro Project additions" >> ~/.bashrc
echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc
echo "source .venv/bin/activate" >> ~/.bashrc

echo "*** Installing Selenium and Chrome for BDD"
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 ca-certificates chromium-browser python3-selenium

echo "*** Installing Python depenencies..."
. .venv/bin/activate && python3 -m pip install --upgrade pip wheel
source .venv/bin/activate && pip install -r requirements.txt

echo "*** Starting the Postgres Docker container..."
make run_postgres

echo "*** Checking the Postgres Docker container..."
docker ps

# Wait for PostgreSQL container to start
wait_for_postgres

echo "*** Setting up the Postgres database..."
source .venv/bin/activate && python utils/fill_database.py

echo "**************************************************"
echo " Appui Pro Project Environment Setup Complete"
echo "**************************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""
echo "Then use make run_locally to start the application !"
echo "Your application will be available at http://localhost:8501/" 
echo ""
# Flask CRUD Application with SQLite  

This is a simple **Flask CRUD (Create, Read, Update, Delete) application** that uses **SQLite3** as the database. It allows users to add, edit, delete, and view user records.  

It has been modified by us for the purposes of the course. The original repo can be found [here](https://github.com/iamsamimsarkar/flask-crud-sqlite)

## Technologies

| Technology | How we use it |
| --- | --- |
| Flask application | Provides the web app's CRUD interface for adding, viewing, editing, and deleting user records. |
| SQLite3 | Stores the application's user records in a lightweight database. |
| Pytest | Runs the automated tests for the application. |
| Ruff | Lints the Python code to catch style and common code issues. |
| Docker | Packages the application and its dependencies into an image that can be run locally or deployed. |
| GitHub Actions | Automates code-quality checks, tests, Docker image builds, and deployment workflows. |
| Terraform | Defines and manages the Google Cloud resources used by the application as code. |
| Google Cloud Run | Hosts the deployed containerized application. |

## Local installation instructions  

1. **Clone the Repository**  

2. **Create a Virtual Environment (Optional but Recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   ```bash
   python app.py
   ```

5. **Open in Browser**  
   Open `http://127.0.0.1:5000/` in your browser.  

## If you'd rather run it with Docker

From the repository root, build a local image:

```bash
docker build -t flask-crud-app .
```

Start a container from that image:

```bash
docker run --rm -p 8000:8000 -v app_data:/app/instance flask-crud-app
```

Open `http://localhost:8000/` in your browser. Press `Ctrl+C` to stop the container. The named `app_data` volume keeps the SQLite database when the container is removed.

Alternatively, use Docker Compose to build and start the application:

```bash
docker compose up --build
```

Then open `http://localhost:8000/`. Stop the application with `Ctrl+C`; run `docker compose down` to remove the container while keeping the database volume.

## Information for teaching staff

The report for our project can be found here in the root folder of the repo as "Report.pdf". It contains a more detailed description of our architecture, how the various components interact, discussion of our design decisions, limitations and trade-offs as well as the required note on how we used AI in this project.

The webpage hosting our deployed version of the application can be found [here](https://devops-app-2ldrlwtrxq-lz.a.run.app/)

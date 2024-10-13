Here’s a complete `README.md` file for the Flask Docker Demo project:

---

# Flask Docker Demo

This project demonstrates how to build a simple Flask application and run it in a Docker container using Docker Compose. The application includes basic routes and can be easily extended to add more functionality.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [Building and Running with Docker Compose](#building-and-running-with-docker-compose)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up the Flask Docker Demo project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your system:
- [Python 3.9+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HamzehSayeh/capstone-project.git
   cd flask_docker_demo
   ```

2. **Set Up a Virtual Environment** (for local development):
   ```bash
   python -m venv venv
   source venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**:
   ```bash
   python run.py
   ```

   Open your browser and go to `http://localhost:5000`.

## Project Structure

```
flask_docker_demo/
├── app/                # Application folder
│   ├── __init__.py     # Flask app initialization
│   └── routes.py       # Application routes
├── Dockerfile          # Docker configuration file
├── docker-compose.yml  # Docker Compose configuration file
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── run.py              # Flask application entry point
└── .gitignore          # Git ignore file
```

### Key Files

- **`app/__init__.py`**: Initializes the Flask application.
- **`app/routes.py`**: Defines the routes (endpoints) for the application.
- **`run.py`**: Main script to run the Flask application.
- **`Dockerfile`**: Used to build the Docker image for the Flask application.
- **`docker-compose.yml`**: Docker Compose configuration to manage the Flask application container.

## Running the Application

### Running Locally

If you want to run the application locally (outside of Docker):

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python run.py
   ```

3. Open your browser and go to:
   ```
   http://localhost:5000
   ```

### Building and Running with Docker Compose

To build and run the application inside a Docker container, follow these steps:

1. **Build and Run the Application**:
   ```bash
   docker-compose up --build
   ```

2. Open your browser and go to:
   ```
   http://localhost:5000
   ```

Docker Compose will handle building the image and running the container. If you make changes to the code, you will need to rebuild the container using the `--build` flag.

## Technologies Used

- **[Flask](https://flask.palletsprojects.com/)**: A lightweight WSGI web application framework.
- **[Docker](https://www.docker.com/)**: A platform to develop, ship, and run applications inside containers.
- **[Docker Compose](https://docs.docker.com/compose/)**: A tool for defining and running multi-container Docker applications.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push the changes to your branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
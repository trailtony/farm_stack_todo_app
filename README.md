
# 🌾 FARM Stack To-Do App

A full-stack To-Do application built using the FARM stack: FastAPI, React, and MongoDB. This project demonstrates how to develop a modern web application with a Python backend, a React frontend, and MongoDB as the database.

## 🚀 Features

- **FastAPI** for building high-performance APIs
- **React** for a dynamic and responsive user interface
- **MongoDB** for flexible and scalable data storage
- **Docker Compose** for easy setup and deployment
- Interactive API documentation with Swagger UI

## 🛠️ Technologies Used

- Backend: FastAPI, Uvicorn, Motor (async MongoDB driver)
- Frontend: React, Axios
- Database: MongoDB
- Containerization: Docker, Docker Compose

## 📦 Installation

### Prerequisites

- Docker and Docker Compose installed on your machine
- A MongoDB URI (e.g., from MongoDB Atlas)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/trailtony/farm_stack_todo_app.git
   cd farm-stack-todo-app
   ```

2. **Set up environment variables**:

   Create a `.env` file in the root directory and add your MongoDB URI:

   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/todoapp?retryWrites=true&w=majority
   ```

3. **Build and run the containers**:

   ```bash
   docker-compose up --build
   ```

4. **Access the application**:

   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000](http://localhost:8000)
   - API Docs (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Running Tests

To run backend tests using Pytest:

```bash
docker-compose exec backend pytest
```

## 📁 Project Structure

```
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── database.py
│   └── tests
├── frontend
│   ├── public
│   └── src
│       ├── components
│       ├── App.js
│       └── index.js
├── .env
├── docker-compose.yml
└── README.md
```

## 📚 Resources

- [Use the FARM Stack to Develop Full Stack Apps](https://www.freecodecamp.org/news/use-the-farm-stack-to-develop-full-stack-apps/)
- [FARM Stack Course - FastAPI, React, MongoDB](https://www.youtube.com/watch?v=PWG7NlUDVaA)
- [MongoDB Developer FARM Stack To-Do App](https://github.com/mongodb-developer/farm-stack-to-do-app)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

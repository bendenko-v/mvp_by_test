# MVP / Задание для Back-end разработчиков

**Задание:**

- Создать сервер на Django/Flask (для Python)
- Подключить базу данных (MongoDB)
- Создать пользователя в базе данных
- Проверить, как работает, через Postman

Подключаться к API не требуется, мокайте данные.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [API Endpoints](#api-endpoints)
- [Configuration](#configuration)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11+
- Docker
- Docker Compose

### Installation

Clone the repository and install the dependencies:

```bash
git clone git@github.com:bendenko-v/mvp_by_test.git
cd mvp_by_test
pip install -r requirements.txt
```

Copy the .env-example file:

```bash
cp .env-example .env
```

Edit the .env file with your configuration details.

Set up your MongoDB database using Docker Compose:

```bash
docker-compose up -d
```

### Usage

Run the application:

```bash
python src/manage.py runserver
```

### API Endpoints

#### Users

- **Create User:** `/users/create/` (POST)
- **User Detail:** `/users/<id>/` (GET)
- **User Posts:** `/users/<id>/posts/` (GET)
- **User List:** `/users/` (GET)

#### Posts

- **Post List:** `/posts/` (GET, POST, PUT, DELETE)

### Configuration

Configure the application by updating the settings in .env. Make sure to set up your database connection and other
relevant options.

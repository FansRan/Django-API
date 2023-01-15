<div align="center">
  <h1>Django API</h1>
  
  <p>
    This a simple api build with Django and Django REST Framework of Python programming language.
    It aims to fetch and store info about lodging in a database backend.
  </p>

</div>

<br />

<!-- Table of Contents -->

# Table of Contents

- [About the Project](#about-the-project)
  - [Tech Stack](#tech-stack)
  - [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run Locally](#run-locally)
- [Contact](#contact)

<!-- About the Project -->

## About the Project

<!-- TechStack -->

### Tech Stack

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.django-rest-framework.org/">Django REST framework</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.sqlite.org/">SQLite</a></li>
    <li><a href="https://www.oracle.com/">Oracle</a></li>
  </ul>
</details>

<!-- Features -->

### Features

- Store ad fetch data about:
    - Lodging
    - Commune
    - Piece (Quartier)
    - Individual

<!-- Getting Started -->

## Getting Started

<!-- Prerequisites -->

### Prerequisites

This project uses python3 and venv module

Run these commands

```bash
 sudo apt install python3

 python3 -m pip install venv
```

<!-- Installation -->

### Installation

Install the project by creating virtual environment

```bash
  python3 -m venv your/env/path

  source your/env/path/bin/activate
```

<!-- Run Locally -->

### Run Locally

Clone the project

```bash
  git clone https://gitlab.com/FansRan/Django-API
```

Go to the project directory

```bash
  cd Django-API
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Run the migration process

```bash
  python3 manage.py migrate
```

Start the development server

```bash
  python3 manage.py runserver
```

The server listen on port 8000

<!-- Contact -->

## Contact

Project Link: [https://gitlab.com/FansRan/Django-API](https://gitlab.com/FansRan/Django-API)

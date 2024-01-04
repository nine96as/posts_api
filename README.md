# Posts API

The Posts API is a back-end server built using Python and Flask that allows for CRUD operations on both posts and users.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)

## Technologies Used

- [Python](https://www.python.org/) - version 3.12.1

## Setup

Clone the repository and `cd` into the root repository directory:

```sh
git clone git@github.com:nine96as/posts_api.git && cd posts_api
```

Start up the virtual environment using `pipenv`:

```sh
pipenv shell
```

Install required dependencies:

```sh
pipenv install
```

> [!important]
> Please ensure you are using the Python version listed in the [Technologies Used](#technologies-used) section.

## Configuration

1. Fetch the `DB_URL` by creating a database instance, [using this guide](https://www.elephantsql.com/docs/index.html), where [ElephantSQL](https://www.elephantsql.com/) is used as the database provider

2. Create a `.env` file within the root repository directory, and fill it in as shown below:

```env
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=postgresql://...
```

> [!warning]
> When running the API in production, make sure to remove the `FLASK_DEBUG` environment variable to prevent the accidental exposure of data.

## Usage

Seed the database data with:

```sh
python seed.py
```

Run the back-end API with:

```sh
pipenv run start
```

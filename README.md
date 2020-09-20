<h1 align="center">
  Volunteering
  <br />
  <img alt="Volunteering CI" src="https://github.com/WesGtoX/volunteering/workflows/volunteering%20CI/badge.svg" />
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#usage">Usage</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/volunteering?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/volunteering?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/volunteering?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/volunteering?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/volunteering?style=plastic" />
</p>


# Volunteering

Volunteers is an API to manage the inclusion of volunteers and actions being possible to carry out the entire process of insertion, listing, viewing details, updating and removal.


## Technology 

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


### Install and Run

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/volunteering.git
```
2. Set a `SECRET_KEY` in `.env`:
```bash
cp .env.sample .env
```
3. Run:
```bash
make run
```
4. Run tests:
```bash
make test
```


## Usage

### Endpoints

#### Volunteers

|  Method  | Endpoint          | Description                               |
| :------: | ----------------- | ----------------------------------------- |
|  `POST`  | `/volunteers/`    | Register a volunteer.                     |
|  `GET`   | `/volunteers/`    | List all registered volunteers.           |
|  `GET`   | `/volunteers/:id` | Show the detail of a specific volunteer.  |
|  `PUT`   | `/volunteers/:id` | Change the data for a specific volunteer. |
| `DELETE` | `/volunteers/:id` | Remove a specific volunteer.              |

#### Actions

|  Method  | Endpoint       | Description                            |
| :------: | -------------- | -------------------------------------- |
|  `POST`  | `/actions/`    | Create an action.                      |
|  `GET`   | `/actions/`    | List all created actions.              |
|  `GET`   | `/actions/:id` | Show the detail of a specific action.  |
|  `PUT`   | `/actions/:id` | Change the data for a specific action. |
| `DELETE` | `/actions/:id` | Remove a specific action.              |

_For more examples, please refer to the [Documentation](https://github.com/WesGtoX/volunteering/wiki)_


## License

Distributed under the MIT License. See [LICENSE](LICENSE.md) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:

# Github API Client

A `Github API Client` that pulls data from github api

## Installation

Create a [virtual environment](https://virtualenv.pypa.io/en/stable/) first.

```bash
virtualenv -p python3.6 <name_of_env> --always-copy --no-site-packages
source <name_of_env>/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
(env) pip install -r requirements.pip
```

## Basic Usage

```python
(env) import github

(env) gh = github.Github(owner='ioliveros')
(env) gh.read()

>> {
    'owner': 'ioliveros',
    'repo': 'gosuapi',
    'page': 1,
    'per_page': 10,
    'resource': {
        'commits': [{.. }],
        'pulls': [{.. }],
        'issues': [{.. }]
  }
}

```

## Passing Proxy
to avoid rate limit `API rate limit exceeded` error

```python
(env) import github

(env) gh = github.Github(owner='ioliveros', proxies={'http':'<ip>:<port>', 'https':'<ip>:<port>'})
(env) gh.read()

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Concerns, feedback or just want to get in touch? Email me: ioliveros.dev@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
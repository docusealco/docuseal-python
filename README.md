# DocuSeal Python

The DocuSeal Python library provides seamless integration with the DocuSeal API, allowing developers to interact with DocuSeal's electronic signature and document management features directly within Python applications. This library is designed to simplify API interactions and provide tools for efficient implementation.

## Documentation

Detailed documentation is available at [DocuSeal API Docs](https://www.docuseal.com/docs/api?lang=python).

## Requirements

Python 3.5 and later.

## Installation

```sh
pip install --upgrade docuseal
```

Install from source with:

```sh
python setup.py install
```

## Usage

### Configuration

Set up the library with your DocuSeal API key based on your deployment. Retrieve your API key from the appropriate location:

#### Global Cloud

API keys for the global cloud can be obtained from your [Global DocuSeal Console](https://console.docuseal.com/api).

```python
from docuseal import docuseal

docuseal.key = 'API_KEY'
```

#### EU Cloud

API keys for the EU cloud can be obtained from your [EU DocuSeal Console](https://console.docuseal.eu/api).

```python
from docuseal import docuseal

docuseal.key = 'API_KEY'
docuseal.url = 'https://api.docuseal.eu'
```

#### On-Premises

For on-premises installations, API keys can be retrieved from the API settings page of your deployed application, e.g., https://yourdocusealapp.com/settings/api.

```python
from docuseal import docuseal

docuseal.key = 'API_KEY'
docuseal.url = 'https://yourdocusealapp.com/api'
```

## API Methods

## Support

For feature requests or bug reports, visit our [GitHub Issues page](https://github.com/docusealco/docuseal-php/issues).


## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

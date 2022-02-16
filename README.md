# traq.py

[![PyPI version](https://badge.fury.io/py/traq.svg)](https://badge.fury.io/py/traq)

traQ v3 API library for Python >= 3.6.

## Generation

```shell
./generate.sh 3.0.0-0
# Configure PyPI account and ~/.pypirc
./upload.sh
```

## Usage

A quick example of posting message to a channel:
```python
from traq import ApiClient, Configuration
from traq.api.message_api import MessageApi
from traq.model.post_message_request import PostMessageRequest

if __name__ == '__main__':
    client = ApiClient(Configuration(access_token="your-access-token"))
    m_api = MessageApi(client)
    message = m_api.post_message("channel-id", post_message_request=PostMessageRequest("おいす〜"))
    print(message)
```

For more, see [./out/README.md](./out/README.md)

## References

- https://openapi-generator.tech/docs/generators/python
- https://packaging.python.org/en/latest/tutorials/packaging-projects/

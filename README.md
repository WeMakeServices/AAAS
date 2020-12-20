# AAAS (Addition as a Service)

Have you ever wanted a simple REST API that enabled you to add two single digit positive integers?

Look no further.

Addition as a Service (AAAS) provides users with an easy, robust, reliable, and atomic REST API for most addition needs. If your requirements for addition fall under the following:

1. You wish to add exactly `2` positive integers together
2. All `2` of these positive integers are within the range `1-9` inclusive
3. You require the ability to call this api once a day or less frequently

Then you are welcome to use AAAS for your addition needs!

AAAS can be reached at https://add.woohoojin.dev/

# Usage Example

```python
import time
import requests
from typing import Iterator, List

class Addition:
    """
    Addition represents an algebraic expression in the
    form of `x + y`. For this class, `x` and `y` must both
    be contained within the bounds 1-9, inclusive.

    Additionally (ha!), they (x and y) must both be integers.
    """
    def __init__(self, x: int, y: int):
        if x >= 10 or y >= 10 or x <= 0 or y <= 0:
            raise ValueError("Invalid Addition")

        self.x = x
        self.y = y

def perform_multiple_additions(additions: List[Addition]) -> Iterator[int]:
    """
    Given a list of Additions, `perform_multiple_additions`
    will iterate over them and call out to AAAS (Addition as
    a Service). Results from AAAS are returned synchronously.
    """
    to_return = []
    for addition in additions:
        result = aaas(addition.x, addition.y)
        yield result
        # AAAS supports one query a day
        time.sleep(86400)

def aaas(x: int, y: int) -> int:
    """
    Calls out to AAAS API and returns the result.
    """
    result = requests.get(f"https://add.woohoojin.dev/{x}/{y}")
    return int(result.text)
```

# API Documentation

**URL** : `/x/y`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 1 request per day

**Description** : Returns the summation of x and y.

## Success Response

**Code** : `200 OK`

**Content examples**

For a request with `x = 5` and `y = 9`

```json
14
```

For a request with `x = 2` and `y = 4`

```json
6
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `x = 10` and `y = 4` (10 is out of bounds)

```json
Bad request
```

For a request with `x = 0` and `y = 4` (0 is out of bounds)

```json
Bad request
```

**Code** : `429 Too Many Requests`

**Content examples**

For a request made less than 24 hours before the previous request

```json
Too Many Requests
1 per 1 day
```

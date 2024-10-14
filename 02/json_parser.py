import json
from collections.abc import Callable


def parse(
    json_str: str,
    required_keys: list[str] | None = None,
    tokens: list[str] | None = None,
    callback: Callable[[str, str], None] | None = None,
) -> None:
    try:
        obj = json.loads(json_str)
        for key in required_keys:
            if key in list(obj.keys()):
                for token in tokens:
                    if isinstance(obj[key], str):
                        value = obj[key].lower()
                    else:
                        value = [x.lower() for x in obj[key]]
                    if token.lower() in value:
                        callback(key, token)
    except TypeError:
        print("Wrong input type!")

from .. import types


def clean_dict(data: types.IDict):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            clean_dict(value)  # type: ignore
        elif isinstance(value, list):
            for item in value:  # type: ignore
                if isinstance(item, dict):
                    clean_dict(item)  # type: ignore
        if value is None or value == [] or value == {}:
            data.pop(key)
        elif isinstance(value, list) and not any(value):  # type: ignore
            data.pop(key)

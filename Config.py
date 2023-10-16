from types import SimpleNamespace
import yaml


def dict_to_obj(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_obj(v) for k, v in d.items()})
    return d


def obj_to_dict(obj):
    if isinstance(obj, SimpleNamespace):
        return {k: obj_to_dict(v) for k, v in vars(obj).items()}
    return obj


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)

            with open('config.yaml', 'r') as f:
                data = yaml.safe_load(f)
                simple_namespace_obj = dict_to_obj(data)
                cls._instance.__dict__.update(vars(simple_namespace_obj))

        return cls._instance

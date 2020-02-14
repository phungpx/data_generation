import cv2
from pathlib import Path 
from importlib import import_module

def load_yaml(yaml_file):
	import yaml
	with open(yaml_file) as f:
		settings = yaml.safe_load(f)
	return settings

def create_instance(config, *args, **kwargs):
    from importlib import import_module
    module = config['module']
    name = config['name']
    config_kwargs = config.get(name, {})
    for key, value in config_kwargs.items():
        if isinstance(value, str):
            config_kwargs[key] = eval(value)
    return getattr(import_module(module), name)(*args, **config_kwargs, **kwargs)
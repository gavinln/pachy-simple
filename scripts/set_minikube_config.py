#!/usr/bin/env python3

from pathlib import Path

minikube_config_dir = Path('/minikube-config')
default_config = minikube_config_dir / 'profiles' / 'minikube' / 'config.json'
with default_config.open() as f:
    for line in f.readlines():
        print(line)

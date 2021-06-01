import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'tp=_sbawuvbairbnainbiar4kf6q@)6d)0$g^qu2-cd78i_(_0dx'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

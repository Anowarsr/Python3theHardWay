try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47',
    'author': 'Anowar Hossain Sardar',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'anowarsardarhossain@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Exercise47'],
    'scripts': [],
    'name': 'MyProjects'
}

setup(**config)
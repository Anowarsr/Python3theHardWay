try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project 01',
    'author': 'Anowar Hossain Sardar',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'anowarsardarhossain@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Projects1'],
    'scripts': [],
    'name': 'MyProjects1'
}

setup(**config)
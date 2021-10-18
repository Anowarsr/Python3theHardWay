try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Advance User Input',
    'author': 'Anowar Hossain Sardar',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'anowarsardarhossain@gmail.com',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages': ['Exercise49'],
    'scripts': [],
    'name': 'MyProject_v2'
}

setup(**config)
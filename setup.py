from setuptools import setup
from io import open
from catalyst_sphinx_theme import __version__

setup(
    name = 'catalyst_sphinx_theme',
    version =__version__,
    author = 'Artem Zolkin',
    author_email= 'arquestro93@gmail.com',
    url="https://github.com/catalyst-team/catalyst_sphinx_theme",
    docs_url="https://github.com/catalyst-team/catalyst_sphinx_theme",
    description='Catalyst Sphinx Theme',
    py_modules = ['catalyst_sphinx_theme'],
    packages = ['catalyst_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'catalyst_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/**/*.js',
        'static/fonts/**/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'catalyst_sphinx_theme = catalyst_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ],
    python_requires='>=3.6',
)

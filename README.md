# Catalyst Sphinx Theme

Sphinx theme for [Catalyst Docs](https://catalyst-team.github.io/catalyst/index.html) based on the [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/latest).

## Local Development

Run python setup:

```
python setup.py install
```

and install the dependencies using `pip install -r docs/requirements.txt`

In the root directory install the `package.json`:

```
# node version 8.4.0
yarn install

```

If you have `npm` installed then run:

```
npm install
```

- If you want to see generated documentation for `docs/demo` then create
`.env.json` file and make it empty json file. Means `.env.json file` will
contain

```
{}
```

Run grunt to build the html site and enable live reloading of the demo app at `localhost:1919`:

```
grunt
```

The resulting site is a demo.

#### Docs

```
# in ./docs
make html
```

Once these are successful, navigate to the `conf.py` file in each project. In the Docs these are at `./docs/source`. The Tutorials one can be found in the root directory.

In `conf.py` change the html theme to `catalyst_sphinx_theme` and point the html theme path to this repo's local folder, which will end up looking something like:

```
html_theme = 'catalyst_sphinx_theme'
html_theme_path = ["../../../catalyst_sphinx_theme"]
```

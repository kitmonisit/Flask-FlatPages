"""
Flask-FlatPages
---------------

Provides flat static pages to a Flask application, based on text files
as opposed to a relationnal database.

Links
`````

* `documentation <http://packages.python.org/Flask-FlatPages>`_
* `development version
  <http://github.com/SimonSapin/Flask-FlatPages/zipball/master#egg=Flask-FlatPages-dev>`_
"""

from setuptools import setup, find_packages

setup(
    name='Flask-FlatPages',
    version='0.2', # also change this in docs/conf.py
    url='https://github.com/SimonSapin/Flask-FlatPages',
    license='BSD',
    author='Simon Sapin',
    author_email='simon.sapin@exyr.org',
    description='Provides flat static pages to a Flask application',
    long_description=__doc__,
    packages=find_packages(),
    namespace_packages=['flaskext'],
    # test pages
    package_data={'': ['pages*/*.*', 'pages/*/*.*', 'pages/*/*/*.*']},
    test_suite='flaskext.flatpages.tests',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'PyYAML',
        'Markdown',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)


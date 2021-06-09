# -*- coding: utf-8 -*-
"""Setup module for flask taxonomy."""
import os

from setuptools import setup

readme = open('README.md').read()
history = open('CHANGES.md').read()
OAREPO_VERSION = os.environ.get('OAREPO_VERSION', '3.3.40')


install_requires = [
    'oarepo-mapping-includes',
    'oarepo-records-draft',
    'oarepo-communities',
    'oarepo-invenio-model',
]

tests_require = [
    'oarepo-records-draft',
    'oarepo-actions',
    'oarepo-validate',
    'coverage',
    'oarepo-mapping-includes',
    # 'werkzeug==1.0.1',
    # 'flask==1.1.4',
    'werkzeug',
    'flask',
    'invenio-app==1.2.7',
    'celery==5.0.5',
    # 'flask-sqlalchemy==2.4.4',
    # 'invenio-search==1.3.1'
    'sqlalchemy==1.3.24'
]

extras_require = {
    'tests': [
        'oarepo[tests]~={version}'.format(version=OAREPO_VERSION),
        *tests_require
    ]
}

setup_requires = [
    'pytest-runner>=2.7',
]

g = {}
with open(os.path.join('oarepo_doi_generator', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="oarepo_doi_generator",
    version=version,
    url="https://github.com/oarepo/oarepo-doi-generator",
    license="MIT",
    author="Alzbeta Pokorna",
    author_email="alzbeta.pokorna@cesnet.cz",
    description="OARepo doi generator",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=['oarepo_doi_generator'],
    entry_points={

        #'invenio_search.mappings': [
        #    'documents= oarepo_doi_generator.mappings',
        #],
        # 'invenio_search.mappings': [
        #     'test_mapping = test_mapping.mappings'
        # ],
        'invenio_jsonschemas.schemas': [
            'oarepo_doi_generator = oarepo_doi_generator.jsonschemas',
        ],

        'invenio_base.apps': [
            #'document = oarepo_doi_generator.DocumentRecordMixin',
          #  'oarepo_actions = oarepo_actions:Actions'
        ],
    },
    include_package_data=True,
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)

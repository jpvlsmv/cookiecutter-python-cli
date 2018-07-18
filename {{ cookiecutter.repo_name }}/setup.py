"""
{{ cookiecutter.project_short_description }}

For dev/build environment, pip install -e .[dev]
Testing is done in the qa environment pip install -e .[qa]
"""
from setuptools import find_packages, setup

runtime_dependencies = ['click']
dev_dependencies  = [
            'bump2version',
        ]
qa_dependencies = [
            'pylint',    
            'flake8',
            'tox',
        ]

setup(
    name='{{ cookiecutter.pypi_name }}',
    version='{{ cookiecutter.version }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    license='BSD',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=runtime_dependencies,
    extras_require={
        'dev': dev_dependencies,
        'qa': dev_dependencies + qa_dependencies
    },
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.script_name }} = {{ cookiecutter.package_name }}.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

"""
Cheater is a cheetsheet display app
"""
from setuptools import find_packages, setup

dependencies = ['click', 'Jinja2>=2.7.3', 'Markdown>=2.5.2']

setup(
    name='cheater',
    version='0.1.2',
    url='https://github.com/skalanux/cheater',
    license='GPLV3',
    author='Juan Manuel Schillaci',
    author_email='jmschillaci@gmail.com',
    description='Cheater is a cheetsheet display app',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'cheater = cheater.cli:main',
        ],
    },
     data_files=[
             ('', [
                         'cheater/cheatsheets/stylesheet.css',
                         'cheater/cheatsheets/template.html',
                     ]),],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
         'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

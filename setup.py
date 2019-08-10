import os
import re
import setuptools

NAME = 'belter'
HERE = os.path.abspath(os.path.dirname(__file__))

def read_file(name):
    with open(name, encoding='utf-8') as handle:
        return handle.read()

def find_value(source, identifier):
    '''
    Manually parse the given source, looking for lines of the form:
        <identifier> = '<value>'
    Returns the value. We do this rather than import the file directly because
    its dependencies will not be present when setuptools runs this setup.py
    before installing our dependencies, to find out what they are.
    '''
    regex =r"^%s\s*=\s*['\"]([^'\"]*)['\"]$" % (identifier,)
    match = re.search(regex, source, re.M)
    if not match:
        raise RuntimeError(
            "Can't find '%s' in source:\n%s" % (identifier, source)
        )
    return match.group(1)

def get_version():
    return find_value(
        read_file(os.path.join(HERE, NAME, '__init__.py')),
        '__version__',
    )

def main():

    setuptools.setup(

        # Required
        name=NAME,
        version=get_version(),
        packages=setuptools.find_packages(
            exclude=['docs', 'tests'],
        ),

        ## Description
        description='A game, like Asteroids, with 2D vector graphics.',
        long_description=read_file(os.path.join(HERE, 'README.md')),
        long_description_content_type='text/markdown',
        url='https://github.com/tartley/belter',
        author='Jonathan Hartley',
        author_email='tartley@tartley.com',
        keywords='game 2d vector simulation asteroids',

        ## Dependencies
        python_requires='>=3.7, <4',
        # See https://packaging.python.org/en/latest/requirements.html
        install_requires=[
            'colortuple >=1.0.2, <2',
            'moderngl >=5.5.2, <6',
            'pyglet >=1.4.1, <2',
            'py2d-fixed >=0.1, <2',
        ],
        # Install these with eg. `pip install NAME[dev]`
        # (I can't figure out how to get pip-compile to use this though,
        # so these go into requirements/dev.in for now)
        # extras_require={
        #     'dev': [],
        # },

        ## Data files
        # Preferred approach:
        # package_data={
        #     'sample': ['package_data.dat'],
        # },
        # Fallback for data that has to live outside of packages
        # data_files=[
        #     ('my_data', ['data/data_file']),
        # ],

        # (These can be conditional on extras_require)
        entry_points={
            'console_scripts': [
                'belter = belter.main:main',
            ],
            # 'gui_scripts': [],
        },

        # Keys are rendered as text on PyPI.
        project_urls={
            'Github': f'https://github.com/tartley/{NAME}',
        },

        # See https://pypi.org/classifiers/
        classifiers=[
            #'Development Status :: 1 - Planning',
            'Development Status :: 2 - Pre-Alpha',
            #'Development Status :: 3 - Alpha',
            #'Development Status :: 4 - Beta',
            #'Development Status :: 5 - Production/Stable',
            #'Development Status :: 6 - Mature',
            #'Development Status :: 7 - Inactive',

            #'Environment :: Console',
            #'Environment :: MacOS X',
            #'Environment :: No Input/Output (Daemon)',
            #'Environment :: Web Environment',
            #'Environment :: Win32 (MS Windows)',
            'Environment :: X11 Applications',

            #'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            #'Intended Audience :: System Administrators',

            #'License :: OSI Approved :: BSD License',
            'License :: OSI Approved :: MIT License',
            #'License :: Other/Proprietary License',

            'Natural Language :: English',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: Implementation :: CPython',

            #'Operating System :: Microsoft :: Windows :: Windows 7',
            #'Operating System :: MacOS :: MacOS X',
            #'Operating System :: OS Independent',
            #'Operating System :: POSIX',
            'Operating System :: POSIX :: Linux',

            'Topic :: Games/Entertainment',
        ],
    )

if __name__ in ['__main__', 'builtins']:
    main()


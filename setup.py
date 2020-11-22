import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'wbuilder2',
    packages = ["wbuilder2"],
    version = '2.0.0',
    license='MIT',
    description = 'HTML template generator for Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/wbuilder2',
    download_url = 'https://github.com/rmaniego/wbuilder2/archive/v1.0.tar.gz',
    keywords = ['HTML', 'GENERATOR', 'PYTHONIC'],
    install_requires=[ 'beautifulsoup4', 'html5lib' ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)
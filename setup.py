from setuptools import setup, find_packages

setup(
    name = 'vergeai',
    url = "https://master.d23pjv5h2c4648.amplifyapp.com/",
    author = "Vale Tolpegin",
    author_email = "valetolpegin@gmail.com",
    version = "1.0",
    maintainer = "Vale Tolpegin",
    maintainer_email = "valetolpegin@gmail.com",
    packages = find_packages(exclude = ('tests', 'doc')),
    install_requires = [
        'requests==2.31.0',
        'numpy==1.18.0',
        'loguru==0.4.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

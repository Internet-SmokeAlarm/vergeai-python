from setuptools import setup, find_packages

setup(
    name = 'fedlearn-sdk',
    url = "https://internetsmokealarm.com",
    author = "ISA Systems, LLC",
    author_email = "valetolpegin@internetsmokealarm.com",
    version = "0.0.1",
    maintainer = "ISA Systems, LLC",
    maintainer_email = "valetolpegin@internetsmokealarm.com",
    packages = find_packages(exclude = ('tests', 'doc')),
    install_requires = [
        'requests==2.22.0'],
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

from setuptools import setup, find_packages
DESCRIPTION = '''
This is Abubakar Hafeez  Package
It contains two modules:
 1. Check Email Security.
 2.Check Password Security.
'''


setup(
    name='bakarSecure',
    version='0.2',
    description=DESCRIPTION, 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abubakar Hafeez',
    author_email='<abubakarhafeez66@gmail.com>',
    url='https://github.com/AbubakarS989/Bakar-Module',
    packages=['bakarSecure'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

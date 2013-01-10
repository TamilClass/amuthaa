from distutils.core import setup

setup(
    name='amuthaa',
    description='Useful Tamil Language tools, by the people who brought you TamilClass.org',
    long_description=open('README.rst').read(),
    
    url='https://github.com/TamilClass/amuthaa',
    
    version='0.1dev',    
    license='LICENSE.txt',    
    
    author='TamilClass.org',
    author_email='info@tamilclass.org',
    
    packages=['amuthaa', 'amuthaa.test'],
    
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Natural Language :: Tamil',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Education'
    ],
    
    keywords = "amuthaa tamil unicode language text processing",
    
    test_suite='nose.collector',   
    tests_require=['nose'],

)
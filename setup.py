from setuptools import setup, find_packages


setup(
    name='wl_mg',
    version='0.6',
    license='MIT',
    author="MaGiXx",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/MaGiXxScripter/wl_mg',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)

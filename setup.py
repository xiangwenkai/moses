from setuptools import setup, find_packages


setup(name='molsets',
      version='1.0',
      python_requires='>=3.5.0',
      packages=find_packages() + ['moses/metrics/SA_Score',
                                  'moses/metrics/NP_Score',
                                  'moses/dataset/data'],
      description=('Molecular Sets (MOSES): '
                   'A Benchmarking Platform for Molecular Generation Models'),
      author='Insilico Medicine',
      author_email='moses@insilico.com',
      license='MIT',
      package_data={
          '': ['*.csv', '*.h5', '*.gz', '*.csv.gz', '*.npz'],
      }
      )

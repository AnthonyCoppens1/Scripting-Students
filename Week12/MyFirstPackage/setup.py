from setuptools import setup, find_packages

setup(name='DSPSPackage',
      version='1.0',
      description='My first package',
      author='Me, myself and I',
      license='MIT',
      packages=find_packages(include=['mypackage']),
      install_requires=['playsound', 'requests']
      )
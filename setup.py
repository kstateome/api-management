from setuptools import setup

version = '0.1'

setup(name='api-management',
      version=version,
      description="Utilities for K-State APIs",
      long_description=open("./README.txt", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: Private",
          ],
      keywords='kstate-utils',
      author='Derek Stegelman',
      author_email='derekst@k-state.edu',
      url='http://github.com/kstateome/api-management',
      license='',
      packages=['api_manager', 'api_manager.migrations'],
      install_requires = ['django-piston', 'django==1.3'],
      include_package_data=True,
      zip_safe=True,
      )
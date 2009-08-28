from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.geo.geographer',
      version=version,
      description="Geographic annotation for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='gis geography geospatial plone',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url="'https://svn.plone.org/svn/collective/collective.geo.geographer",
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zgeo.geographer',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

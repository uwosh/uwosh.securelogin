from setuptools import setup, find_packages
import os

version = '0.1.5'

setup(name='uwosh.securelogin',
      version=version,
      description="Theme that makes login_form post to SSL URLs, based on Sunburst Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='login secure SSL HTTPS theme skin', # portlet form
      author='T. Kim Nguyen',
      author_email='nguyen@uwosh.edu',
      url='https://svn.it.uwosh.edu/svn/plone/Projects/uwosh.securelogin/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

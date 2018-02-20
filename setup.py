from setuptools import setup

setup(name='geo_street_talk',
      version='0.1.2',
      description='Geo-street-talk',
      url='https://github.com/Streets-Data-Collaborative/geo-street-talk-global',
      author='Yukun Wan',
      author_email='yw3447@nyu.edu',
      license='MIT',
      packages=['geo_street_talk'],
      install_requires=['osmnx','geopandas','shapely'],
      zip_safe=False)

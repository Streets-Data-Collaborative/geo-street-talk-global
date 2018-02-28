.. Geo_street_talk documentation master file, created by
   sphinx-quickstart on Tue Feb 27 15:28:06 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Geo Street Talk!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Description
-----------
Geo Street Talk (GST) enables a slightly more intuitive way of communicating points on a street. We created GST to convert any location coordinate along any cities to a conversational string.

Imagine looking at any non-cartographical data visualization or UI component (tables, graphs, text, etc.) that aims to display, say, characteristics of the worst potholes in the city. To represent the location, we could display a coordinate (e.g. 40.7217267,-73.9870392), but without looking at a map, where is this?

One could imagine instead displaying an address (i.e. 263 E Houston St), but, again, without looking at a map, even to a native New Yorker like myself, I don't know immediately know if this is on the east or west side of the city.

Building on a `solid foundation`_, the deliverable of this project will programmatically output more immediately meaningful descriptions (i.e. "Houston Street between Avenue B and Avenue C").

As folks who are in the data weeds day-to-day, it's important to not lose sight of higher-level user experience.


Project lead: David Marulli (`@dmarulli`_ | `david@argolabs.org`_)

Primary developer: `@YukunVVan`_

Orgs: `Streets Data Collaborative`_ | `ARGO`_

.. _@dmarulli: https://github.com/dmarulli

.. _david@argolabs.org: david@argolabs.org

.. _@YukunVVan: https://github.com/YukunVVan

.. _Streets Data Collaborative: https://www.streetsdatacollaborative.org

.. _ARGO: http://www.argolabs.org

.. _solid foundation: https://medium.com/a-r-g-o/introducing-geo-street-talk-c11bd2306ff1

Installation
-------------
To install the released version, you can use pip::

    pip install geo_street_talk


Dependencies
--------------

Installation should also install all dependencies:

- `geopandas`_
- `shapely`_
- `osmnx`_

.. _geopandas: http://geopandas.org/

.. _shapely: http://toblerity.github.io/shapely

.. _osmnx: https://osmnx.readthedocs.io


How to use
--------------

Use function streetTalk to return a translated address.

.. function:: geo_street_talk.street(longitude,latitude,cityname,networkType='drive')

  This function takes a lat/lng pair and a city name as inputs, and returns
  a conversational string stating nearest street as well as enclosing streets.

  longitude: float

  latitude: float

  cityname: string

  networkType: string

      This is used to generate graph from ``OSMnx``. You can also specify several different network types:

        ``drive`` - get drivable public streets (but not service roads)

        ``drive_service`` - get drivable streets, including service roads

        ``walk`` - get all streets and paths that pedestrians can use (this network type ignores
        one-way directionality)

        ``bike`` - get all streets and paths that cyclists can use

        ``all`` - download all non-private OSM streets and paths

        ``all_private`` - download all OSM streets and paths, including private-access ones



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

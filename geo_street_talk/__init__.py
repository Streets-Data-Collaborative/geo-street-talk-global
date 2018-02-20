import osmnx as ox
import geopandas as gpd
from shapely.geometry import Point

def nearestSegment(point,city):
    '''
    This function takes a lat/lon point and a geodataframe of city shapefile
    as inputs and returns a name and unique id for nearest street segment to
    that point as well as unique ids for the segment's enclosing intersections
    point: shapely.geometry.Point (lon/lat)
    city: geodataframe of edges of segments in city
    return: nearest_name, nearest_id, from_id, to_id
    '''
    idx = city.geometry.distance(point).sort_values().index[0]
    nearest_name = city.loc[idx,'name']
    nearest_id = city.loc[idx,'osmid']
    from_id = city.loc[idx,'from']
    to_id = city.loc[idx,'to']
    return nearest_name, nearest_id, from_id, to_id

def intersectingStreets(node_id,city):
    '''
    This function takes a lat/lng pair as an input, and returns the names of
    intersecting streets
    node_id: node id, string
    city: geodataframe of edges of segments in city
    return: street_name, street_name_1
    '''
    return city[(city['from'] == node_id) | (city['to'] == node_id)].name.unique()


def streetTalk(lon,lat,cityname,networkType='drive'):
    '''
    This function takes a lat/lng pair and a city name as inputs, and returns
    a conversational string stating nearest street as well as enclosing streets
    point: shapely.geometry.Point
    cityname: string
    networkType: string
    '''
    if cityname not in globals():
        try:
            #If the map of city is downloaded, use them directly
            globals()[cityname] = gpd.read_file('data/'+cityname+'/edges/edges.shp')
            #print('the map of city is downloaded')
        except:
            #If the map is not downloaded, download the map of city via OpenStreetMap
            G = ox.graph_from_place(cityname + ', USA', network_type=networkType)
            #Save the map in shapefile locally
            ox.save_load.save_graph_shapefile(G, filename=cityname, folder=None, encoding='utf-8')
            #print('Map of ' + cityname + 'is saved in shapefile locally!')
            #citymap_node = gpd.read_file('data/'+cityname+'/nodes/nodes.shp')
            globals()[cityname] = gpd.read_file('data/'+cityname+'/edges/edges.shp')

    citymap_edge = globals()[cityname]
    #print('map loaded')

    point = Point(lon,lat)
    nearest_name, nearest_id, from_id, to_id = nearestSegment(point,citymap_edge)

    enclosing_from = intersectingStreets(from_id,citymap_edge)
    enclosing_to = intersectingStreets(to_id,citymap_edge)

    try:
        street_from  = enclosing_from[1] if enclosing_from[0] == nearest_name else enclosing_from[0]
        street_to  = enclosing_to[1] if enclosing_to[0] == nearest_name else enclosing_to[0]
        conversational = "{} between {} and {}".format(nearest_name,street_from,street_to)
    except:
        conversational = nearest_name

    return conversational

import osmnx as ox
import geopandas as gpd
from shapely.geometry import Point

def inverse_streetTalk(street_name, street_from, street_to, cityname):
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

    on_st = citymap_edge[citymap_edge['name'] == street_name]
    from_st = citymap_edge[citymap_edge['name'] == street_from]
    to_st = citymap_edge[citymap_edge['name'] == street_to]

    for i in on_st.index:
        if ((on_st.loc[i,'from'] in from_st['from'].values) or (on_st.loc[i,'from'] in from_st['to'].values)\
        or (on_st.loc[i,'to'] in from_st['from'].values) or (on_st.loc[i,'to'] in from_st['to'].values)) \
        and ((on_st.loc[i,'from'] in to_st['from'].values) or (on_st.loc[i,'from'] in to_st['to'].values) \
        or (on_st.loc[i,'to'] in to_st['from'].values) or (on_st.loc[i,'to'] in to_st['to'].values)):
            p = on_st[on_st.index==i].centroid.values[0]
            return p.x, p.y

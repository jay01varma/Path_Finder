import osmnx as ox
import networkx as nx
import streamlit as st
import folium
from streamlit_folium import folium_static

def get_map_data(city_name):
    place_name = f"{city_name}, Canada"
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph

def get_node_names(graph):
    return {
        node: f"{graph.nodes[node]['y']:.4f}, {graph.nodes[node]['x']:.4f}"
        for node in graph.nodes()
    }

def a_star_search(graph, source, target):
    path = nx.astar_path(graph, source, target, weight='length')
    return path

def plot_shortest_path(graph, shortest_path):
    m = folium.Map(
        location=(
            graph.nodes[shortest_path[0]]['y'],
            graph.nodes[shortest_path[0]]['x']
        ),
        zoom_start=12
    )
    # Add start and end markers
    folium.Marker(
        location=(
            graph.nodes[shortest_path[0]]['y'],
            graph.nodes[shortest_path[0]]['x']
        ),
        popup="Start",
        icon=folium.Icon(color='green')
    ).add_to(m)
    folium.Marker(
        location=(
            graph.nodes[shortest_path[-1]]['y'],
            graph.nodes[shortest_path[-1]]['x']
        ),
        popup="End",
        icon=folium.Icon(color='red')
    ).add_to(m)
    # Add path lines
    for i in range(len(shortest_path) - 1):
        edge = (shortest_path[i], shortest_path[i + 1])
        folium.PolyLine(
            locations=[
                (graph.nodes[edge[0]]['y'], graph.nodes[edge[0]]['x']),
                (graph.nodes[edge[1]]['y'], graph.nodes[edge[1]]['x'])
            ],
            color='blue'
        ).add_to(m)
    return m

def main():
    st.title("Shortest Path Finder")

    # List of Canadian cities
    cities = sorted(list(set([
        "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton",
        "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener",
        "London", "Victoria", "Halifax", "Oshawa", "Windsor",
        "Saskatoon", "Regina", "St. John's", "Barrie", "Kelowna",
        "Sherbrooke", "Guelph", "Abbotsford", "Kingston", "Kanata",
        "Trois-Rivières", "Moncton", "Chicoutimi", "Milton", "Red Deer",
        "Brantford", "Thunder Bay", "White Rock", "Nanaimo", "Sudbury",
        "Lethbridge", "Saint John", "Peterborough", "Kamloops", "Sarnia",
        "Prince George", "Medicine Hat", "Drummondville", "New Westminster",
        "Chilliwack", "Saint-Jérôme", "Granby", "Fredericton", "North Bay",
        "Belleville", "Charlottetown", "Saint-Hyacinthe", "Cornwall",
        "Brockville", "Timmins", "Orillia", "Moose Jaw", "Lloydminster",
        "Penticton", "Prince Albert", "Grande Prairie", "Wood Buffalo",
        "Stratford", "Welland", "North Vancouver", "Vernon", "Courtenay",
        "Campbell River", "Fort McMurray", "Yellowknife", "Whitehorse",
        "Iqaluit"
    ])))

    selected_city = st.selectbox("Select City:", cities)

    with st.spinner("Downloading map and computing path..."):
        try:
            graph = get_map_data(selected_city)
            node_names = get_node_names(graph)
            node_values = list(node_names.values())
            selected_source = st.selectbox("Source Node:", node_values)
            selected_target = st.selectbox("Destination Node:", node_values)

            if st.button("Find Shortest Path"):
                source_node = next(
                    node for node, name in node_names.items() if name == selected_source)
                target_node = next(
                    node for node, name in node_names.items() if name == selected_target)
                shortest_path = a_star_search(graph, source_node, target_node)
                m = plot_shortest_path(graph, shortest_path)
                folium_static(m)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



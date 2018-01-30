import json
import re
import copy
import sys

# test = json.load(open('nodes1.json'))
# print len(test)
# sys.exit(0)

def node_write(node_elements, nodes_sc, nodes1_f):
	index = 0
	for n_e in node_elements:
		toid = str(n_e['id'])
		point_x = n_e['lon']
		point_y = n_e['lat']
		index += 1
		nodes_sc.append({'toid': toid, "point": [point_x, point_y], "index": index})
	with open(nodes1_f, 'w') as outfile:
		json.dump(nodes_sc, outfile, indent=2)
	print('end of nodes')

def link_write(way_elements, links_sc, node_dictionary, links1_f):
	index = 0
	for w_e in way_elements:
		toid = str(w_e['id'])+'_'+str(w_e['parts'])
		term = 'Motorway'
		restriction = "One Way"
		nature = 'Dual Carriageway'
		negativeNode = str(w_e['nodes'][0])
		positiveNode = str(w_e['nodes'][-1])
		orientation = '-'
		polyline = []
		for way_node in w_e['nodes']:
			for item in node_dictionary[way_node]:
				polyline.append(item)
		links_sc.append({'index': index, 'toid': toid, 'term': term, 'restriction': restriction, 'nature': nature, 'orientation': orientation, 'positiveNode': positiveNode, 'negativeNode': negativeNode, 'polyline': polyline})
		index += 1

	with open(links1_f, 'w') as outfile:
		json.dump(links_sc, outfile, indent=2)
	print('end of links')

# read the overpass data and separate into nodes and links
overpass_f = 'target.osm'
data = json.load(open(overpass_f))
elements = data['elements']
node_elements = []
way_elements = []
for e in elements:
	if e['type']=='node':
		node_elements.append(e)
	if e['type']=='way':
		way_elements.append(e)
print elements[0]
print node_elements[0]
print way_elements[0]
print len(elements), len(node_elements), len(way_elements)

# filter out the drivable links
pattern_drivable = "(motorway|motorway_link|motorway_junction|trunk|trunk_link|primary_link|primary|secondary|tertiary|unclassified|unsurfaced|track|residential|living_street|dservice)"
way_elements = [w_e for w_e in way_elements if re.search(pattern_drivable, w_e['tags']['highway'])]
node_id_set = set() # all nodes
endnode_id_set = set() # end nodes
crossnode_id_set = set() # nodes that appear twice in all selected links
for w_e in way_elements:
	endnode_id_set.add(w_e['nodes'][0])
	endnode_id_set.add(w_e['nodes'][-1])
	for n_w_e in w_e['nodes']:
		if n_w_e in node_id_set:
			crossnode_id_set.add(n_w_e)
		node_id_set.add(n_w_e)
crossandendnode_id_set = crossnode_id_set.union(endnode_id_set)
print len(node_id_set), len(endnode_id_set), len(crossnode_id_set), len(crossandendnode_id_set)
node_elements = [n_e for n_e in node_elements if n_e['id'] in crossandendnode_id_set]

way_elements_break = []
for w_e in way_elements:
	w_e_nodes = [nodes for nodes in w_e['nodes'] if nodes in crossandendnode_id_set]
	parts = 0
	for i_node in range(len(w_e_nodes)-1):
		w_e_break = copy.deepcopy(w_e)
		w_e_break['nodes'] = w_e_nodes[i_node:i_node+2]
		w_e_break['parts'] = parts
		way_elements_break.append(w_e_break)
		parts += 1
print way_elements_break[0:2]
print len(node_elements), len(way_elements), len(way_elements_break)

# TODO: combine nodes, break links
nodes_sc = []
links_sc = []
node_write(node_elements, nodes_sc, 'nodes1_drivable_graph.json')
node_dictionary = {n['id']:[n['lon'], n['lat']] for n in node_elements}
link_write(way_elements_break, links_sc, node_dictionary, 'links1_drivable_graph.json')

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas_rhino

from compas.datastructures import Mesh
from compas.geometry import add_vectors
from compas.geometry import scale_vector


mesh = Mesh.from_json('cablenet.json')

boundary = set(mesh.vertices_on_boundary())

connectors = []

# make a connector for every unconstrained ("normal", "internal" vertices) that is not on the boundary

for key, attr in mesh.vertices(True):
    # skip vertices on the boundary
    if key in boundary:
        continue

    # skip vertices that have a constraint

    # start and end point of the connector
    p1 = mesh.vertex_coordinates(key)

    # connector "pipe" drawing data as a dict
    connectors.append({
        'points' : [p1, p2],     # points along the pipe
        'color'  : (255, 0, 0),  # the pipe color
        'name'   : ,             # name of the pipe indicating the vertex it is connected to
        'radius' : 0.0025        # the pipe radius
    })

compas_rhino.xdraw_pipes(connectors, layer="Connectors", clear=True)

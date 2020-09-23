import gmsh 
import numpy as np

def split_sequence(sequence, size):
    subsequences = []
    for start in range(0, len(sequence), size):
        end = start + size
        subsequence = sequence[start:end]
        subsequences.append(subsequence)
    return subsequences

def mm_to_m(mm):
    return float(mm) / 1000

class Mesher:
    def __init__(self, size=0):
        self.size = size

        self.file = ''

        self.points = dict()
        self.lines = dict()
        self.planes = dict()
        self.entities = dict()

    def load_geometry(self, points, lines):
        a = all([len(p)==3 for p in points.values()])
        b = all([(p in points) and (len(lines)==2) for l in lines.values() for p in l])
        
        self.file = ''

        gmsh.initialize('', False)
        gmsh.option.setNumber('Mesh.CharacteristicLengthMin', self.size)
        gmsh.option.setNumber('Mesh.CharacteristicLengthMax', self.size)
        
        for i, coord in points.items():
            gmsh.model.geo.addPoint(*coord, tag=i)
        
        for i, (p0,p1) in lines.items():
            gmsh.model.geo.addLine(p0, p1, tag=i)

        gmsh.model.geo.addCurveLoop(list(lines.keys()), tag=1)
        gmsh.model.geo.addPlaneSurface([1])
        gmsh.model.geo.synchronize()
        gmsh.model.mesh.generate()

        self.points = self._get_points()
        self.lines = self._get_lines()
        self.planes = self._get_planes()
        self.entities = self._get_entities()
        self.nodal_coordinates = self._get_nodal_coordinates()
        self.connectivity = self._get_connectivity_matrix()
         
        gmsh.fltk.run()
        gmsh.finalize()

    def load_file(self, path):
        gmsh.initialize('', False)
        gmsh.open(path)
        gmsh.option.setNumber('Mesh.CharacteristicLengthMin', self.size)
        gmsh.option.setNumber('Mesh.CharacteristicLengthMax', self.size)
        gmsh.model.mesh.generate()

        self.points  = self._get_points()
        self.lines = self._get_lines()
        self.planes = self._get_planes()
        self.entities = self._get_entities()
        self.nodal_coordinates = self._get_nodal_coordinates()
        self.connectivity = self._get_connectivity_matrix()
        
        gmsh.fltk.run()
        gmsh.finalize()

        file = open(path)
        self.file = file.read()
    
    def _get_points(self):
        indexes, coords, _ = gmsh.model.mesh.getNodes(1, -1, True)

        dict_points = dict()
        for i, (x, y, z) in zip(indexes, split_sequence(coords, 3)):
            dict_points[i] = (mm_to_m(x), mm_to_m(y), mm_to_m(z))

        return dict_points

    def _get_nodal_coordinates(self):
        indexes, coords, _ = gmsh.model.mesh.getNodes(1, -1, True)

        dict_nodes = dict()
        for i, (x, y, z) in zip(indexes, split_sequence(coords, 3)):
            dict_nodes[i] = (mm_to_m(x), mm_to_m(y), mm_to_m(z))

        nodal_coordinates = np.zeros((len(dict_nodes),4), dtype=float)
        for index, (node, coordinates) in enumerate(dict_nodes.items()):
            nodal_coordinates[index, 0] = node
            nodal_coordinates[index, 1:] = coordinates  

        return nodal_coordinates

    def _get_lines(self):
        _, indexes, points = gmsh.model.mesh.getElements(1)
        indexes = list(indexes[0]) if indexes else []
        points = list(points[0]) if points else []

        lines = dict()
        for i, p in zip(indexes, split_sequence(points,2)):
            lines[i] = p 

        return lines
    
    def _get_planes(self):
        _, indexes, points = gmsh.model.mesh.getElements(2)
        indexes = list(indexes[0]) if indexes else []
        points = list(points[0]) if points else []

        dict_planes = dict()
        for i, p in zip(indexes, split_sequence(points,3)):
            dict_planes[i] = p 

        return dict_planes

    def _get_connectivity_matrix(self):
        _, indexes, points = gmsh.model.mesh.getElements(2)
        indexes = list(indexes[0]) if indexes else []
        points = list(points[0]) if points else []

        dict_elements = dict()
        for i, p in zip(indexes, split_sequence(points,3)):
            dict_elements[i] = p 

        connectivity = np.zeros((len(dict_elements), 4), dtype=int)
        for index, nodes in enumerate(dict_elements.values()):
            connectivity[index, 0] = index+1
            connectivity[index, 1:] = nodes  

        return connectivity

    def _get_entities(self):
        entities = dict()
        for dim, tag in gmsh.model.getEntities(1):
            # _, indexes, connectivity = gmsh.model.mesh.getElements(dim,tag)
            # node_indexes = node_indexes[0]
            # connectivity = split_sequence(connectivity[0], 2)
            _, indexes, _ = gmsh.model.mesh.getElements(dim,tag)
            indexes = list(indexes[0]) if indexes else []
            entities[tag] = indexes

        return entities


def test_1():
    nodes = {
        1: (0,0,0),
        2: (3,0,0),
        3: (3,1,0),
        4: (2,1,0),
        5: (2,3,0),
        6: (3,3,0),
        7: (3,4,0),
        8: (0,4,0),
        9: (0,3,0),
        10: (1,3,0),
        11: (1,1,0),
        12: (0,1,0),
        # 13: (1.25, 1.75, 0),
        # 14: (1.75, 1.75, 0),
        # 15: (1.75, 2.25, 0),
        # 16: (1.25, 2.25, 0)
    }

    lines = {
        1: (1,2),
        2: (2,3),
        3: (3,4),
        4: (4,5),
        5: (5,6),
        6: (6,7),
        7: (7,8),
        8: (8,9),
        9: (9,10),
        10: (10,11),
        11: (11,12),
        12: (12,1),
        # 13: (13,14),
        # 14: (14,15),
        # 15: (15,16),
        # 16: (16,13)
    }

    m = Mesher(0.5)
    m.load_geometry(nodes, lines)
    print(m.connectivity)
    print(m.nodal_coordinates)

def test_2():
    m = Mesher(0.2)
    m.load_file('tube_2.iges')

def test_3():
    m = Mesher(10)
    m.load_file('teapot.iges')

if __name__ == '__main__':

    test_1()
    # test_2()
    # test_3()
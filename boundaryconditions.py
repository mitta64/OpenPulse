import numpy as numpy

from node import Node
from tube import TubeCrossSection
from material import Material
from element import Element

class BoundaryConditions 

    # Index to apply boundary conditions

    def __init__(self, del_lines):
        self.del_lines = del_lines

    def count_dofs_fixed(self,delete_line):
        "Number of dofs fixed"
        count_dof_fixed = lambda delete_line: Node.degree_freedom*self.fixed_nodes.shape[0] if delete_line==True else 0
        return count_dof_fixed(delete_line)
    
    def count_index_dofs_fixed(self,delete_line):
        "Number of indexes i and j relative to dofs fixed"
        count_ind_dof_fixed = lambda delete_line: 3*(Node.degree_freedom**2)*self.fixed_nodes.shape[0] if delete_line==True else 0
        return count_ind_dof_fixed(self.delete_line)

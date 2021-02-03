import numpy as np
from time import time
from pulse.preprocessing.node import DOF_PER_NODE_STRUCTURAL

# this is temporary, and will be changed a lot
def get_structural_frf(mesh, solution, node, dof, absolute=False, real=False, imaginary=False):
    position = mesh.nodes[node].global_index * DOF_PER_NODE_STRUCTURAL + dof
    if absolute:
        results = np.abs(solution[position])
    elif real:
        results = np.real(solution[position])
    elif imaginary:
        results = np.imag(solution[position])
    else:
        results = solution[position]
    return results

def get_structural_response(mesh, solution, column, scf=0.2, gain=None, Normalize=True):
       
    data = np.real(solution)
    ind = np.arange( 0, data.shape[0], DOF_PER_NODE_STRUCTURAL )
    rows = int(data.shape[0]/DOF_PER_NODE_STRUCTURAL)

    u_x, u_y, u_z = data[ind+0, column], data[ind+1, column], data[ind+2, column]
    rot_xyz = np.array([data[ind+3, column], data[ind+4, column], data[ind+5, column]]).T
    rot_xyz = rot_xyz.copy()

    u_def = ((u_x)**2 + (u_y)**2 + (u_z)**2)**(1/2) 
    
    if Normalize:
        r_max = max(u_def)
        if r_max==0:
            r_max=1
    else:
        r_max, scf = 1, 1

    coord_def = np.zeros((rows,4))
    coord = mesh.nodal_coordinates_matrix
    connect = mesh.connectivity_matrix

    if gain is None:
        factor = (scf/r_max)
    else:
        factor = gain*(scf/r_max)

    coord_def[:,0] = coord[:,0]
    coord_def[:,1] = coord[:,1] + u_x*factor
    coord_def[:,2] = coord[:,2] + u_y*factor
    coord_def[:,3] = coord[:,3] + u_z*factor

    # t0 = time()
    nodes = mesh.nodes
    for node in nodes.values():
        global_index = node.global_index 
        node.deformed_coordinates = coord_def[global_index, 1:]
        node.deformed_rotations_xyz = rot_xyz[global_index, :]*factor
    
    mesh.process_element_cross_sections_orientation_to_plot()
    # dt = time() - t0
    # print(dt)

    # t0 = time()
    # elements = mesh.structural_elements
    # list_test = []
    # for element in elements.values():
    #     element.get_deformed_local_coordinate_system_info()
    # dt = time() - t0
    # print(dt)
    
    return connect, coord_def, u_def, factor

def get_reactions(mesh, reactions, node, dof, absolute=False, real=False, imaginary=False):
    #reactions: dictionary with all reactions and global dofs are the keys of dictionary
    key = mesh.nodes[node].global_index * DOF_PER_NODE_STRUCTURAL + dof
    # print("Node ID: {} - key: {}".format(node,key))
    if absolute:
        results = np.abs(reactions[key])
    elif real:
        results = np.real(reactions[key])
    elif imaginary:
        results = np.imag(reactions[key])
    else:
        results = reactions[key]
    return results

def get_stress_spectrum_data(stresses, element_id, stress_key, absolute = False, real = False, imaginary = False):
    if absolute:
        return np.abs(np.array(stresses[element_id][stress_key,:]))
    elif real:
        return np.real(np.array(stresses[element_id][stress_key,:]))
    elif imaginary:
        return np.imag(np.array(stresses[element_id][stress_key,:]))
    else:
        return np.array(stresses[element_id][stress_key,:])

# def get_internal_loads_data(mesh, column, absolute=False, real=False, imaginary=False):

#     elements = mesh.structural_elements
#     internal_loads = [np.r_[i, elements[i].internal_load[:, column]] for i in elements ]
#     if absolute:
#         return np.abs(np.array(internal_loads))
#     elif real:
#         return np.real(np.array(internal_loads))
#     elif imaginary:
#         return np.imag(np.array(internal_loads))
#     else:
#         return np.array(internal_loads) 
#%%
from time import time

import numpy as np 
import matplotlib.pyplot as plt 

from pulse.preprocessing.cross_section import CrossSection
from pulse.preprocessing.material import Material
from pulse.preprocessing.mesh import Mesh
from pulse.processing.assembly import get_global_matrices, get_lumped_matrices
from pulse.processing.solution import direct_method, modal_superposition, modal_analysis, get_reactions_at_fixed_nodes
from pulse.postprocessing.plot_data import get_frf, get_displacement_matrix
from pulse.animation.plot_function import plot_results

# PREPARING MESH
steel = Material('Steel', 7860, young_modulus=210e9, poisson_ratio=0.3)
cross_section = CrossSection(0.05, 0.034)
mesh = Mesh()

run = 2
if run==1:
    mesh.generate('examples/iges_files/tube_1.iges', 0.01)
    mesh.set_structural_boundary_condition_by_node([1, 24, 26], np.zeros(6))
if run==2:
    mesh.load_mesh('examples/mesh_files/Geometry_01/coord.dat', 'examples/mesh_files/Geometry_01/connect.dat')
    mesh.set_structural_boundary_condition_by_node([1, 1200, 1325], np.zeros(6))

mesh.set_material_by_element('all', steel)
mesh.set_cross_section_by_element('all', cross_section)

# mesh.set_boundary_condition_by_node([361], np.array([0.1,None,None,None,None,None]))
mesh.set_force_by_node([361], np.array([1,0,0,0,0,0]))

# mesh.add_spring_to_node([427],1*np.array([1e9,1e9,1e9,0,0,0]))
# mesh.add_spring_to_node([600],3*np.array([1e9,1e9,1e9,0,0,0]))
# mesh.add_mass_to_node([204],0*np.array([80,80,80,0,0,0]))
# mesh.add_damper_to_node([342],0*np.array([1e3,1e3,1e3,0,0,0]))

connect = mesh.get_connectivity_matrix(reordering=True)
coord = mesh.get_nodal_coordinates_matrix(reordering=True) 

natural_frequencies, mode_shapes = modal_analysis(mesh, modes=200, harmonic_analysis=True)

# SOLVING THE PROBLEM BY TWO AVALIABLE METHODS
f_max = 200
df = 2
frequencies = np.arange(0, f_max+df, df)
modes = 200
direct = direct_method(mesh, frequencies, is_viscous_lumped=True)
modal = modal_superposition(mesh, frequencies, modes, fastest=True)

# exit()

column = 85

ms_results = np.real(modal)

load_reactions = get_reactions_at_fixed_nodes(mesh, frequencies, direct)
load_reactions = np.real(load_reactions)
_, coord_def, _, _ = get_displacement_matrix(mesh, modal, column, Normalize=False)

plot_results( mesh,
              coord_def,
              scf = 0.5,
              out_OpenPulse = True, 
              Show_nodes = True, 
              Undeformed = False, 
              Deformed = False, 
              Animate_Mode = True, 
              Save = False)

#%%
# GETTING FRF
response_node = 361
local_DOF = 0
response_DM = get_frf(mesh, direct, response_node, local_DOF)
response_MS = get_frf(mesh, modal, response_node, local_DOF)

DOF_label = dict(zip(np.arange(6), ["Ux", "Uy", "Uz", "Rx", "Ry", "Rz"]))
Unit_label = dict(zip(np.arange(6), ["[m]", "[m]", "[m]", "[rad]", "[rad]", "[rad]"]))

# PLOTTING RESULTS
fig = plt.figure(figsize=[10,6])
ax = fig.add_subplot(1,1,1)

first_legend_label = "Direct"
second_legend_label = "Mode superposition"

if response_DM.all()==0 or response_MS.all()==0:
    first_plot, = plt.plot(frequencies, response_DM, color=[0,0,0], linewidth=3, label=first_legend_label)
    second_plot, = plt.plot(frequencies, response_MS, color=[1,0,0], linewidth=1, label=second_legend_label)
else:
    first_plot, = plt.semilogy(frequencies, response_DM, color=[0,0,0], linewidth=3, label=first_legend_label)    
    second_plot, = plt.semilogy(frequencies, response_MS, color=[1,0,0], linewidth=1, label=second_legend_label)

first_legend = plt.legend(handles=[first_plot, second_plot], loc='upper right')
plt.gca().add_artist(first_legend)

ax.set_title(("FRF - Response {} at node {}").format(DOF_label[local_DOF], response_node), fontsize = 18, fontweight = 'bold')
ax.set_xlabel(("Frequency [Hz]"), fontsize = 16, fontweight = 'bold')
ax.set_ylabel(("FRF's magnitude {}").format(Unit_label[local_DOF]), fontsize = 16, fontweight = 'bold')
plt.show()

# %%

# data = np.zeros((len(frequencies),2))
# data[:,0] = frequencies
# data[:,1] = yd
# np.savetxt("FRF_newCode_RP_n436x_direct.dat",data)

# data = np.zeros((len(frequencies),2))
# data[:,0] = frequencies
# data[:,1] = ym
# np.savetxt("FRF_newCode_RP_n436x_modesup.dat",data)

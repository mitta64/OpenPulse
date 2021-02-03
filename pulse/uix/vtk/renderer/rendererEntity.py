from pulse.uix.vtk.vtkRendererBase import vtkRendererBase
from pulse.uix.vtk.vtkInteractorBase import vtkInteractorBase
from pulse.uix.vtk.actor.actorLine import ActorLine
from pulse.uix.vtk.vtkInteractorStyleClicker import vtkInteractorStyleClicker
import vtk
import numpy as np

class RendererEntity(vtkRendererBase):
    def __init__(self, project, opv):
        super().__init__(vtkInteractorStyleClicker(self))
        self.project = project
        self.opv = opv
        self.actors = {}
        self.plotRadius = False

    def updateInfoText(self):
        listActorsIDs = self.getListPickedEntities()
        text = ''
        if len(listActorsIDs) == 0: 
            text = ''

        elif len(listActorsIDs) == 1:

            entity = self.project.get_entity(listActorsIDs[0])
            
            structural_element_type = 'undefined'
            material_name = 'undefined'
            diam_ext, thickness = 'undefined', 'undefined'
            offset_y, offset_z = 'undefined', 'undefined'
            
            if entity.material is not None:
                material_name = entity.material.name

            if entity.structural_element_type is not None:
                structural_element_type = entity.structural_element_type

            if entity.tag in (self.project.lines_multiples_cross_sections or self.project.file.lines_multiples_cross_sections):

                if len(self.project.lines_multiples_cross_sections) != 0:
                    number_cross_sections = self.project.lines_multiples_cross_sections.count(entity.tag)
                    # print(self.project.lines_multiples_cross_sections)

                if len(self.project.file.lines_multiples_cross_sections) != 0:
                    number_cross_sections = self.project.file.lines_multiples_cross_sections.count(entity.tag)
                    # print(self.project.file.lines_multiples_cross_sections)

                if entity.structural_element_type not in [None, 'beam_1']:
                
                    diam_ext, thickness = 'multiples', 'multiples'
                    offset_y, offset_z = 'multiples', 'multiples'
                    insulation_thickness, insulation_density = 'multiples', 'multiples'

                    text = 'Line ID  {} ({} cross-sections)\n\n'.format(listActorsIDs[0], number_cross_sections)              
                    text += 'Material:  {}\n'.format(entity.material.name)
                    text += f'Structural element type:  {structural_element_type}\n'
                    text += f'External diameter: {diam_ext} [m]\n'
                    text += f'Thickness: {thickness} [m]\n'
                    if offset_y != 0 or offset_z != 0:
                        text += 'Offset y: {} [m]\nOffset z: {} [m]\n'.format(offset_y, offset_z)
                    if insulation_thickness != 0 or insulation_density != 0: 
                        text += 'Insulation thickness: {} [m]\nInsulation density: {} [kg/m³]'.format(insulation_thickness, int(insulation_density))
                    
                    if entity.fluid is not None:
                        text += f'\nFluid: {entity.fluid}' 

                    if entity.acoustic_element_type is not None:
                        text += f'\nAcoustic element type: {entity.acoustic_element_type}'
                    if entity.hysteretic_damping is not None:
                        text += f'\nHysteretic damping: {entity.hysteretic_damping}'        

            else:

                text = ''
                text += f'Line ID  {listActorsIDs[0]}\n\n'

                if entity.structural_element_type is not None:
                    text += f'Structural element type:  {structural_element_type}\n'
                
                if entity.material is not None:
                    text += f'Material:  {entity.material.name}\n'

                if entity.cross_section is not None:
                    if entity.structural_element_type not in [None, 'beam_1']:
                        
                        diam_ext = entity.cross_section.external_diameter
                        thickness = entity.cross_section.thickness
                        offset_y = entity.cross_section.offset_y
                        offset_z = entity.cross_section.offset_z
                        insulation_thickness = entity.cross_section.insulation_thickness
                        insulation_density = entity.cross_section.insulation_density
                                            
                        text += f'External Diameter:  {diam_ext} [m]\n'
                        text += f'Thickness:  {thickness} [m]\n'
                        if offset_y != 0 or offset_z != 0:
                            text += 'Offset y: {} [m]\nOffset z: {} [m]\n'.format(offset_y, offset_z)
                        if insulation_thickness != 0 or insulation_density != 0: 
                            text += 'Insulation thickness: {} [m]\nInsulation density: {} [kg/m³]'.format(insulation_thickness, int(insulation_density))
                           
                    if entity.structural_element_type in ['beam_1']:

                        # text = ''
                        area = entity.cross_section.area
                        Iyy = entity.cross_section.second_moment_area_y
                        Izz = entity.cross_section.second_moment_area_z
                        Iyz = entity.cross_section.second_moment_area_yz
                        additional_section_info = entity.getCrossSection().additional_section_info

                        text += 'Line ID  {}\n\n'.format(listActorsIDs[0])
                        text += 'Material:  {}\n'.format(material_name)

                        if additional_section_info is not None:
                            text += 'Structural element type:  {} ({})\n'.format(structural_element_type, additional_section_info[0].capitalize())
                        else:
                            text += 'Structural element type:  {} (-)\n'.format(structural_element_type)

                        text += 'Area:  {} [m²]\n'.format(area)
                        text += 'Iyy:  {} [m^4]\n'.format(Iyy)
                        text += 'Izz:  {} [m^4]\n'.format(Izz)
                        text += 'Iyz:  {} [m^4]\n'.format(Iyz)

                if entity.fluid is not None:
                    text += f'\nFluid: {entity.fluid.name}' 

                if entity.acoustic_element_type is not None:
                    text += f'\nAcoustic element type: {entity.acoustic_element_type}'

                if entity.hysteretic_damping is not None:
                    text += f'\nHysteretic damping: {entity.hysteretic_damping}' 

        else:

            text = '{} lines in selection:\n\n'.format(len(listActorsIDs))
            i = 0
            for ids in listActorsIDs:
                if i == 30:
                    text += '...'

                    break
                elif i == 19: 
                    text += '{}\n'.format(ids)
                elif i == 9:
                    text += '{}\n'.format(ids)
                else:
                    text += '{}  '.format(ids)
                i+=1

        self.createInfoText(text)

    def reset(self):
        for actor in self._renderer.GetActors():
            self._renderer.RemoveActor(actor)
        self.actors = {}
        self._style.clear()

    def plot(self):
        self.reset()
        mesh = self.project.get_mesh()
        for entity in self.project.entities:#get_entities():
            elements = [mesh.structural_elements[i] for i in mesh.line_to_elements[entity.tag]]
            actor = self.createActorTubes(elements)
            self.actors[actor] = entity.get_tag()
            self._renderer.AddActor(actor)

            # plot = ActorLine(entity, self.plotRadius)
            # plot.build()
            # self.actors[plot.getActor()] = entity.get_tag()
            # self._renderer.AddActor(plot.getActor())

    def changeColorEntities(self, entity_id, color):
        self._style.clear()
        actors = [key  for (key, value) in self.actors.items() if value in entity_id]
        for actor in actors:
            actor.GetProperty().SetColor(color)
        self.updateInfoText()

    def getListPickedEntities(self):
        return self._style.getListPickedActors()

    def update(self):
        self.opv.update()
        self.opv.updateDialogs()

    def setPlotRadius(self, value):
        self.plotRadius = value

    def getPlotRadius(self):
        return self.plotRadius


    # apaga por favor tá todo mundo pedindo pra apagar...
    def createActorTubes(self, elements):
        source = vtk.vtkAppendPolyData()
        mapper = vtk.vtkPolyDataMapper()
        actor = vtk.vtkActor()

        for element in elements:
            cross_section = element.cross_section
            if cross_section and self.plotRadius:
                label, parameters, *args = cross_section.additional_section_info
                if label == "Pipe section":
                    polygon = vtk.vtkRegularPolygonSource()
                    polygon.SetRadius(cross_section.external_diameter / 2)
                    polygon.SetNumberOfSides(20)
                else:
                    polygon = self.createSectionPolygon(element)
            else:
                polygon = vtk.vtkRegularPolygonSource()
                polygon.SetRadius(self.project.get_element_size()/2)
                polygon.SetNumberOfSides(20)

            tube = self.generalSectionTube(element, polygon.GetOutputPort())
            source.AddInputData(tube.GetOutput())

        mapper.SetInputConnection(source.GetOutputPort())
        actor.SetMapper(mapper)
        return actor

    def createSectionPolygon(self, element):
        Ys, Zs = self.project.get_mesh().get_cross_section_points(element.index)
        points = vtk.vtkPoints()
        edges = vtk.vtkCellArray()
        data = vtk.vtkPolyData()
        poly = vtk.vtkPolygon()
        source = vtk.vtkTriangleFilter()

        for x, y in zip(Ys, Zs):
            points.InsertNextPoint(x, y, 0)    
        
        n = len(Ys)
        poly.GetPointIds().SetNumberOfIds(n)

        for i in range(n):
            poly.GetPointIds().SetId(i,i)
        edges.InsertNextCell(poly)
        
        data.SetPoints(points)
        data.SetPolys(edges)
        source.AddInputData(data)

        return source

    def generalSectionTube(self, element, section):
        start = element.first_node.coordinates
        size = element.length
 
        # _, directional_vectors = element.get_local_coordinate_system_info()
        u, v, w = element.directional_vectors
        
        matrix = vtk.vtkMatrix4x4()
        matrix.Identity()
        for i in range(3):
            matrix.SetElement(i, 0, v[i])
            matrix.SetElement(i, 1, w[i])
            matrix.SetElement(i, 2, u[i])

        data = vtk.vtkTransformPolyDataFilter()
        extrusion = vtk.vtkLinearExtrusionFilter()
        transformation = vtk.vtkTransform()

        extrusion.SetScaleFactor(size)
        extrusion.SetInputConnection(section)
        transformation.Translate(start)
        transformation.Concatenate(matrix)

        data.SetTransform(transformation)
        data.SetInputConnection(extrusion.GetOutputPort())
        data.Update()
        return data
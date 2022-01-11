import visualize_vtk as vsvtk
import data_import
import sys
import vtk

#reading dcm name from the command line argument
if __name__ == '__main__':
    point_clouds = vsvtk.build_vtk_pcds(data_import.import_dcm(sys.argv[1]))
    # Renderer
    for pc in point_clouds:
        renderer = vtk.vtkRenderer()
        renderer.AddActor(pc.vtkActor)
        renderer.SetBackground(.2, .3, .4)
        renderer.ResetCamera()

        # Render Window
        renderWindow = vtk.vtkRenderWindow()
        renderWindow.AddRenderer(renderer)

        # Interactor
        renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        renderWindowInteractor.SetRenderWindow(renderWindow)

        # Begin Interaction
        renderWindow.Render()
        renderWindowInteractor.Start()

import open3d as o3d
import numpy as np

def show_point_cloud(fname: str):
    print("Load a xyz point cloud and render it")
    point_cloud = np.loadtxt(fname, skiprows=1)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud[:, :])
    pcd.colors = o3d.utility.Vector3dVector(np.full(point_cloud.shape, 0.5))
    print(pcd)
    downpcd = pcd.voxel_down_sample(voxel_size=1)
    downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30))
    o3d.visualization.draw_geometries([downpcd], point_show_normal=True)
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(downpcd, voxel_size=1)
    print(voxel_grid)
    o3d.io.write_voxel_grid("voxel.out", voxel_grid, True)
    o3d.visualization.draw_geometries([voxel_grid])

    print('run Poisson surface reconstruction')
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            downpcd, depth=9)
    print(mesh)
    o3d.visualization.draw_geometries([mesh])

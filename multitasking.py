from multiprocessing import Process, Manager
import multiprocessing
import numpy


def process_3Dimage_single(image3D: numpy.ndarray, img_shape: list) -> dict:
    channels = {}
    for i in range(img_shape[0]):
        print(i)
        for j in range(img_shape[1]):
            for k in range(img_shape[2]):
                value = image3D[i, j, k]
                if value > 0 and is_boundary(image3D, img_shape, i, j, k):
                    if value in channels.keys():
                        channels[value].append([i, j, k])
                    else:
                        channels[value] = []
    return channels

def is_boundary(array: numpy.ndarray, arr_shape: list, x: int, y: int, z: int) -> bool:
    value = array[x, y, z]
    if x * y * z == 0 or x == arr_shape[0] - 1 or y == arr_shape[1] - 1 or z == arr_shape[2] - 1:
        return True
    if array[x + 1, y, z] == value and array[x, y + 1, z] == value and array[x, y, z + 1] == value \
            and array[x - 1, y, z] == value and array[x, y - 1, z] == value and array[x, y, z - 1] == value \
            and array[x + 1, y + 1, z + 1] == value and array[x + 1, y + 1, z] == value and array[
        x + 1, y, z + 1] == value \
            and array[x, y + 1, z + 1] == value and array[x, y - 1, z - 1] \
            and array[x - 1, y - 1, z - 1] == value and array[x - 1, y - 1, z] == value and array[
        x - 1, y, z - 1] == value:
        return False
    return True

def process_3Dimage_multi(image3D: numpy.ndarray, img_shape: list):
    process_count = multiprocessing.cpu_count()
    print("processing in " + str(process_count) + "processes")
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(image3D)
        ps = []
        for i in range(0, process_count + 1):
            print(i)
            ps.append(Process(target=perform_calc, args=(img_shape, l, d, int(i*img_shape[0]/process_count), int((i+1)*img_shape[0]/process_count-1))))
            ps[i].start()
        for process in ps:
            process.join()
        return d

def perform_calc(img_shape: list, image3D: list, channels: dict, zmin: int, zmax: int):
    print(zmin, zmax)
    for i in range(zmin, zmax):
        if i >= img_shape[0]:
            break
        for j in range(img_shape[1]):
            for k in range(img_shape[2]):
                value = image3D[i][j][k]
                if value > 0 and is_boundary_list(image3D, img_shape, i, j, k):
                    if value in channels.keys():
                        channels[value].append([i, j, k])
                    else:
                        channels[value] = []



def is_boundary_list(array: list, arr_shape: list, x: int, y: int, z: int):
    value = array[x][y][z]
    if x * y * z == 0 or x == arr_shape[0] - 1 or y == arr_shape[1] - 1 or z == arr_shape[2] - 1:
        return True
    if array[x + 1][y][z] == value and array[x][y + 1][z] == value and array[x][y][z + 1] == value \
            and array[x - 1][y][z] == value and array[x][y - 1][z] == value and array[x][y][z - 1] == value \
            and array[x + 1][y + 1][z + 1] == value and array[x + 1][y + 1][z] == value and array[x + 1][y][z + 1] == value \
            and array[x][y + 1][z + 1] == value and array[x][y - 1][z - 1] \
            and array[x - 1][y - 1][z - 1] == value and array[x - 1][y - 1][z] == value and array[
        x - 1][y][z - 1] == value:
        return False
    return True


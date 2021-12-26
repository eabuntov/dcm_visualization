import visualize
import data_import
import sys

#reading dcm name and image channel number(1-2) from the command line arguments
if __name__ == '__main__':
    data_import.import_dcm(sys.argv[1])
    visualize.show_point_cloud(sys.argv[2] + ".xyz")

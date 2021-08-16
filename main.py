from getIsat import *

"""if __name__ == '__main__':"""

# Global parameters
sample_sec = (100 / 16 * 10 ** 6) ** -1 * u.s
hdf5_filename = "/Users/leo/Plasma code/HDF5/8-3500A.hdf5"

isat, x, y = get_isat(hdf5_filename)
print(isat, x, y)
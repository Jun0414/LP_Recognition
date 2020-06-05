import h5py
filename = "C:\\Users\\Geon Yeol\\Desktop\\20-1\\capstone\\capstone_github\\CRNN-Keras-master\\LSTM+BN5--01--58.160.hdf5"

with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])

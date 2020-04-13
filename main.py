import utility


def main():

    ########################################### ENCODING ##########################################################
    block_size = 4
    imagePath = "test2.png"
    # name of the encoded file that will be created
    encodedFile = "encoded.npy"
    # name of the file to save the probabilty 1D numpy array in it
    probabiltyFile = "probability.npy"
    float_type = 'float64' #you can choose numpy float types as float64(default), float32, float16, and longdouble
    utility.encode(block_size, imagePath, encodedFile,probabiltyFile, float_type)

    ########################################### DECODING ##########################################################
    # rows = 183
    # columns = 275
    rows = 256
    columns = 256
    resultImage = "result.png"
    # name of the encoded file to be decoded
    encodedFile = "encoded.npy"
    # name of the file having the probabilty 1D numpy array
    probabiltyFile = "probability.npy"
    utility.decode(block_size, rows, columns, probabiltyFile, encodedFile, resultImage)


main()

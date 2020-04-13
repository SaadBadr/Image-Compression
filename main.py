import utility


def main():

    # ENCODING
    block_size = 4
    imagePath = "test2.png"
    # name of the encoded file that will be created
    encodedFile = "encoded.npy"
    float_type = 'float64' #you can choose numpy float types as float64(default), float32, float16, and longdouble
    probability = utility.encode(block_size, imagePath, encodedFile, float_type)

    # DECODING
    # rows = 183
    # columns = 275
    rows = 256
    columns = 256
    resultImage = "result.png"
    utility.decode(block_size, rows, columns, probability, encodedFile, resultImage)


main()

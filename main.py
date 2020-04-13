import utility


def main():

    # ENCODING
    block_size = 8
    imagePath = "test.jpg"
    encodedFile = "encoded.npy"
    probability = utility.encode(block_size, imagePath, encodedFile)

    # DECODING
    rows = 183
    columns = 275
    resultImage = "result.jpg"
    utility.decode(block_size, rows, columns, probability, encodedFile, resultImage)


main()

import utility


def main():

    ########################################### ENCODING ##########################################################

    mode = int(input("please choose mode:\n1.Encode then Decode the same files\n3.Encode only\n3.Decode only\n"))
    block_size = int(input("Block Size = (4 is recommended) "))

    if mode != 3:
        imagePath = input("image name: (e.g. test2.png) ")
        # name of the encoded file that will be created
        encodedFile = input("output encoded file name: (e.g. encoded.npy) ")
        # name of the file to save the probability 1D numpy array in it
        probabiltyFile = input("output probability file name: (e.g. probability.npy) ")
        float_type = "float type: (float64 is recommended) "
    if mode == 2:
        utility.encode(block_size, imagePath, encodedFile,probabiltyFile, float_type)
        return
    ########################################### DECODING ##########################################################
    # rows = 183
    # columns = 275
    columns = int(input("number of columns (WIDTH) of the original image: (e.g. 256) "))
    rows = int(input("number of rows (HEIGHT) of the original image: (e.g. 256) "))
    resultImage = input("output image name: (e.g. test2.png) ")
    # name of the encoded file to be decoded
    if mode == 3:
        encodedFile = input("encoded file name: ( e.g. encoded.npy) ")
        # name of the file having the probabilty 1D numpy array
        probabiltyFile = input("probability file name: ( e.g. encoded.npy) ")
    elif mode == 1:
        utility.encode(block_size, imagePath, encodedFile, probabiltyFile, float_type)
    utility.decode(block_size, rows, columns, probabiltyFile, encodedFile, resultImage)


main()

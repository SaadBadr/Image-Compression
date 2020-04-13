import encoding as e
import decoding as d
import collections
import cv2
import numpy


def encode(block_size ,imagePath="test.jpg",encodedFile="encoded",probabilityFile="probability.npy", float_type='float64'):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE).flatten()
    img = numpy.append(img, [0] * (block_size - len(img) % block_size))
    codes = numpy.array([])
    probability = (collections.Counter(img))
    print("Encoding Started")
    # for i in range(0, len(probability)):
        # probability[i] /= len(img)

    prob = [None]*256
    for i in range(0,256):
        prob[i] = probability[i]

    if float_type != 'float16' and float_type != 'float32' and float_type != 'float64' and float_type != 'longdouble':
        float_type = 'float64'

    prob = numpy.asarray(prob, dtype=float_type)
    prob = numpy.true_divide(prob, len(img))
    for i in range(0, len(img), block_size):
        x = e.encoding(prob, img[i:(block_size + i)])
        if not(0<=x<=1):
            print("encoding error")
        codes = numpy.append(codes, [x])
    numpy.save('original.npy', img)
    print("Encoding Done:")
    numpy.save(encodedFile, codes) # save
    print(" ->" + encodedFile + " is created")
    numpy.save(probabilityFile, prob) # save
    print(" ->" + probabilityFile + " is created\n")

    return prob


def decode(block_size, rows, columns, probability, encodedFile="encoded", resultImage="result.jpg"):
    codes = numpy.load(encodedFile)
    probability = numpy.load(probability)
    img = numpy.array([])
    print("Decoding Started")
    for i in range(0, len(codes)):
        x = d.decoding(probability, codes[i], block_size)
        img = numpy.append(img, x)
    img = img[:(len(img) - block_size + (rows * columns) % block_size)]
    print("Decoding Done:")
    img = img.reshape(rows, columns)
    cv2.imwrite(resultImage, img)
    print(" ->" + resultImage + ' is created\n')


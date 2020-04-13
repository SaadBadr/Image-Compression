import encoding as e
import decoding as d
import collections
import cv2
import numpy


def encode(block_size ,imagePath="test.jpg",encodedFile="encoded"):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE).flatten()
    img = numpy.append(img, [0] * (block_size - len(img) % block_size))
    codes = numpy.array([])
    probability = collections.Counter(img)
    for i in range(0, len(probability)):
        probability[i] /= len(img)
    for i in range(0, len(img), block_size):
        x = e.encoding(probability, img[i:(block_size + i)])
        codes = numpy.append(codes, [x])
    numpy.save('original.npy', img)
    numpy.save(encodedFile, codes) # save
    print("Encoding Done")
    return probability


def decode(block_size, rows, columns, probability, encodedFile="encoded", resultImage="result.jpg"):
    codes = numpy.load(encodedFile)
    img = numpy.array([])
    for i in range(0, len(codes)):
        x = d.decoding(probability, codes[i], block_size)
        img = numpy.append(img, x)
    img = img[:(len(img) - block_size + (rows * columns) % block_size)]
    img = img.reshape(rows, columns)
    cv2.imwrite(resultImage, img)
    print("Decoding Done")


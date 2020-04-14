# Image Compression
## using Arithmatic Coding
- Author: Saad Eldeen Mohamed Mohamed
- SEC: 1
- BN: 28

#### User interaction files:
------------
There is two options for user to use this program:
1. Run **userConsole.py**
	- the program will run and take the needed input from the user from console during running.
2. Run **main.py**
	-Before running user should enter the data manualy in **main.py** then run it.

- **Note**: User shouldn't interact with (utility.py, encoding.py, decoding.py) files.

------------

#### **userConsole.py** modes:
------------
There is three modes and the user will asked to choose one from them after running **userConsole.py**
1. Encode then Decode the same files
2. Encode only
3. Decode only
------------
#### The program input:
------------
1. Encoding:
	- Image name (e.g. test.png)
	- Output encoded file name (e.g. encoded.npy)
	- Output probability file name (e.g. probability.npy)
2. Decoding:
	- Width of the original image in pixels (e.g. 256)
	- Height of the original image in pixels (e.g. 256)
	- Output image name (e.g. result.png)
------------
#### The program output:
------------
1. Encoding:
	- original.npy
		- The original image data before encoding
	- The encoded file (e.g. encoded.npy)
	- The probability file (e.g. probability.npy)
2. Decoding:
	- Resulted Image (e.g. result.png)




import numpy
import matplotlib.pyplot as plt

number = 22

output_pattern = [int(x) for x in numpy.binary_repr(number, width=8)]


input_pattern = numpy.zeros([8, 3])
for i in range(8):
    input_pattern[i,:] = [int(x) for x in numpy.binary_repr(7-i, width=3)]

colums = 21
rows = int(colums/2)+1

canvas = numpy.zeros([rows, colums+2])
canvas[0, int(colums/2)+1] = 1

for i in numpy.arange(0, rows-1):
    for j in numpy.arange(0, colums):
        for k in range(8):
            if numpy.array_equal(input_pattern[k,:], canvas[i, j:j+3]):
                canvas[i+1, j+1] = output_pattern[k]

plt.imshow(canvas[:, 1:colums+1], cmap='Greys', interpolation='nearest')
plt.title("Elementary Cellular Automata Rule {}".format(number))
plt.show()







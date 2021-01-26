import os
import numpy as np
import matplotlib.pyplot as plt

class CA_1d:
    def __init__(self, rule, columns):
        self.MAX_GRAPH = 10
        self.rule = rule
        self.columns = columns

        self.generate_CA()


    def generate_CA(self):
        output_pattern = [int(x) for x in np.binary_repr(self.rule, width=8)]

        input_pattern = np.zeros([8, 3])
        for i in range(8):
            input_pattern[i,:] = [int(x) for x in np.binary_repr(7-i, width=3)]

        rows = int(self.columns/2)+1

        canvas = np.zeros([rows, self.columns+2])
        canvas[0, int(self.columns/2)+1] = 1

        for i in np.arange(0, rows-1):
            for j in np.arange(0, self.columns):
                for k in range(8):
                    if np.array_equal(input_pattern[k,:], canvas[i, j:j+3]):
                        canvas[i+1, j+1] = output_pattern[k]

        plt.axis('off')
        plt.imshow(canvas[:, 1:self.columns+1], cmap='Greys', interpolation='nearest')
        # plt.title("Elementary Cellular Automata Rule {}".format(self.rule))
        filename = "static/img/generated_ca_{}_{}.png".format(self.rule, self.columns)
        plt.savefig(filename, bbox_inches='tight')
        self.clearImgs()

    def clearImgs(self):
        files = os.listdir("static/img/")

        if len(files) > self.MAX_GRAPH:
            os.remove("static/img/{}".format(files[-1]))

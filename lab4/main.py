import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as patches
class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):
        return max(x * .1, x)

    def __call__(self, xs):
        return self._f(xs @ self.ws + self.b)
class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size=1):
        self.input_layer = [Neuron(1) for _ in range(input_size)]
        self.hidden_layers = [[Neuron(hidden_sizes[i - 1]) for _ in range(hidden_size)] for i, hidden_size in
                              enumerate(hidden_sizes)]
        self.output_neuron = Neuron(hidden_sizes[-1])

    def forward(self, input_data):
        current_outputs = input_data
        for layer in self.hidden_layers:
            current_outputs = [neuron(current_outputs) for neuron in layer]
        output = self.output_neuron(current_outputs)
        return output


def visualize_network(input_size, hidden_sizes, output_size=1):
    G = nx.DiGraph()

    input_nodes = [f'Input {i + 1}' for i in range(input_size)] #wejsciowe node'y
    hidden_nodes = [[f'Hidden {i + 1}-{j + 1}' for j in range(hidden_size)] for i, hidden_size in  #ukryte node'y
                    enumerate(hidden_sizes)]
    output_nodes = [f'Output {i + 1}' for i in range(output_size)]  #node'y wyjsciowe

    all_layers = [input_nodes] + hidden_nodes + [output_nodes]
    all_nodes = sum(all_layers, [])

    G.add_nodes_from(all_nodes)

    for i in range(len(all_layers) - 1):
        for source in all_layers[i]:
            for target in all_layers[i + 1]:
                G.add_edge(source, target)

    pos = {}
    layer_offsets = [0] * len(all_layers)
    y_start = 5
    y_gap = 2
    for layer_index, layer in enumerate(all_layers):
        x_pos = layer_index * 3
        y_pos_start = y_start
        for i, node in enumerate(layer):
            pos[node] = (x_pos, y_pos_start - i * y_gap)

    #labele do warstw
    layer_labels = ['Input Layer'] + [f'Hidden Layer {i + 1}' for i in range(len(hidden_sizes))] + ['Output Layer']
    layer_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow']

    fig, ax = plt.subplots(figsize=(12, 8))


    for i, layer in enumerate(all_layers):
        x = pos[layer[0]][0] - 1
        y = pos[layer[-1]][1] - y_gap / 2
        height = (y_gap * (len(layer) - 1)) + y_gap
        width = 2
        rect = patches.Rectangle((x, y), width, height, linewidth=0, edgecolor='none',
                                 facecolor=layer_colors[i % len(layer_colors)], alpha=0.3)
        ax.add_patch(rect)
        plt.text(x + 0.1, y + height - 0.5, layer_labels[i], fontsize=12, verticalalignment='top')

    nx.draw_networkx(
        G,
        pos=pos,
        with_labels=False,
        node_color='white',
        node_size=1500,
        font_weight='bold',
        font_color='black',
        edge_color='gray',
        node_shape='o',
        linewidths=1,
        edgecolors='black',
        ax=ax
    )

    plt.xlim(-2, len(all_layers) * 3)
    plt.ylim(-1, y_start + 1)
    plt.axis('off')
    plt.show()

input_size = 3
hidden_sizes = [4, 4]
output_size = 1

network = NeuralNetwork(input_size, hidden_sizes, output_size)
visualize_network(input_size, hidden_sizes, output_size)

from __future__ import unicode_literals

import datetime
import os

from pybrain.tools.xml import NetworkWriter

from pybrain_examples.nn_pygame_bird.constants import NETWORKS_DIR


class NeuralNetworkWriter(object):
    def __init__(self, trainer, hidden_neurons):
        self.trainer = trainer
        self.writer = NetworkWriter
        self.hidden_neurons = hidden_neurons

    def write_to_file(self, fnn):
        path_to_file = self.get_path()
        NetworkWriter.writeToFile(fnn, path_to_file)

    def get_path(self):
        today = datetime.date.today().strftime("%Y_%m_%d")
        network_path = os.path.join(NETWORKS_DIR, today)
        network_name = '%s_%s.xml' % (self.trainer.totalepochs, self.hidden_neurons)
        self._ensure_dir(network_path)
        return os.path.join(network_path, network_name)

    @classmethod
    def _ensure_dir(cls, network_path):
        if not os.path.exists(network_path):
            os.makedirs(network_path)

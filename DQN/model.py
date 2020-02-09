from torch import tensor
from collections import OrderedDict
import torch.nn.functional as Linear, Sequential, Relu
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.input = Linear(42, 128)
        self.hiden = Sequential(OrderedDict[
                        ('h1', Linear(128, 128)),
                        ('relu1', Relu()),
                        ('h2', Linear(128, 64)),
                        ('relu2', Relu()),
                        ('h3', Linear(64, 64)),
                        ('relu3', Relu()),
                        ('h4', Linear(64, 32)),
                        ('relu4', Relu())
                    ])
        self.output = Linear(32, 7)

    def forward(self, x):
        x = self.input(x)
        x = self.hiden(x)
        x = self.output(x)
        return x

    def paramsToList(self):
        return [list(p.tolist()) for p in list(self.parameters())]

    def setParamsByList(self, list_params):
        params = self.parameters()
        for i, param in enumerate(params):
            for j, p in enumerate(param):
                param[j] = tensor(list_params[i][j])
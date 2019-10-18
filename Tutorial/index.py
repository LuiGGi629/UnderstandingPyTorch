import torch
from IPython.core.debugger import set_trace


def f(x):
    res = x * x
    set_trace()
    return res


x = torch.randn(1, requires_grad=True)
y = f(x)


# This file is generated by PaConvert ToolKit, please Don't edit it!
import paddle

def view(self, *args, **kwargs):
    if args:
        if len(args)==1 and isinstance(args[0], (tuple, list, str)):
            return paddle.view(self, args[0])
        else:
            return paddle.view(self, list(args))
    elif kwargs:
        return paddle.view(self, shape_or_dtype = list(kwargs.values())[0])

setattr(paddle.Tensor, 'view', view)

def transpose_aux_func(dims,dim0, dim1):
    perm = list(range(dims))
    perm[dim0], perm[dim1] = perm[dim1], perm[dim0]
    return perm

def reshape(self, *args, **kwargs):
    if args:
        if len(args)==1 and isinstance(args[0], (tuple, list)):
            return paddle.reshape(self, args[0])
        else:
            return paddle.reshape(self, list(args))
    elif kwargs:
        assert 'shape' in kwargs
        return paddle.reshape(self, shape=kwargs['shape'])

setattr(paddle.Tensor, 'reshape', reshape)

def min_class_func(self, *args, **kwargs):
    if 'other' in kwargs:
        kwargs['y'] = kwargs.pop('other')
        ret = paddle.minimum(self, *args, **kwargs)
    elif len(args)==1 and isinstance(args[0], paddle.Tensor):
        ret = paddle.minimum(self, *args, **kwargs)
    else:
        if 'dim' in kwargs:
            kwargs['axis'] = kwargs.pop('dim')

        if 'axis' in kwargs or len(args) >= 1:
            ret = paddle.min(self, *args, **kwargs), paddle.argmin(self, *args, **kwargs)
        else:
            ret = paddle.min(self, *args, **kwargs)

    return ret

def max_class_func(self, *args, **kwargs):
    if 'other' in kwargs:
        kwargs['y'] = kwargs.pop('other')
        ret = paddle.maximum(self, *args, **kwargs)
    elif len(args)==1 and isinstance(args[0], paddle.Tensor):
        ret = paddle.maximum(self, *args, **kwargs)
    else:
        if 'dim' in kwargs:
            kwargs['axis'] = kwargs.pop('dim')

        if 'axis' in kwargs or len(args) >= 1:
            ret = paddle.max(self, *args, **kwargs), paddle.argmax(self, *args, **kwargs)
        else:
            ret = paddle.max(self, *args, **kwargs)

    return ret

setattr(paddle.Tensor, "min", min_class_func)
setattr(paddle.Tensor, "max", max_class_func)

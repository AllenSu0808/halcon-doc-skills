# create_dl_layer_depth_to_space (Operator)

## Name

`create_dl_layer_depth_to_space` — Create a depth to space layer.

## Signature

`create_dl_layer_depth_to_space( : : DLLayerInput, LayerName, BlockSize, Mode, GenParamName, GenParamValue : DLLayerDepthToSpace)`

## Description

The operator `create_dl_layer_depth_to_space` creates a depth to space
layer whose handle is returned in *`DLLayerDepthToSpace`*.

The parameter *`DLLayerInput`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

This layer rearranges the elements of the feeding tensor of shape
$(N,C\ast r^{2},H,W)$ to a tensor of shape
$(N,C,H\ast r,W\ast r)$.
Thereby $r$ can be considered an upscale factor, which is set with
*`BlockSize`*.

The output element $(depth,row,col)$ is mapped from
the input element
$(depth\ast r^{2}+(row%r)\ast r+col%r,row/r,col/r)$.

With *`Mode`* the ordering in the output tensor is set. Currently only
the *'column_row_depth'* order described above is available.

Certain parameters of layers created using this operator
`create_dl_layer_depth_to_space` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'block_size'* (*`BlockSize`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`BlockSize`** (input_control)  number `→`  (integer)

Block size (i.e., upscale factor).

Default:
3

**`Mode`** (input_control)  string `→`  (string)

Ordering mode.

Default:
'column_row_depth'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerDepthToSpace`** (output_control)  dl_layer `→`  (handle)

Depth to space layer.

## Example (HDevelop)

```
InputShape := [16, 16, 3]
Upscale := 2
*
create_dl_layer_input ('input', InputShape, [], [], DLLayerInput)
* Create a convolutional layer, that generates Upscale^2*NumChannel feature maps.
create_dl_layer_convolution (DLLayerInput, 'conv1', 3, 1, 1,\
                             Upscale * Upscale * InputShape[2],\
                             1, 'half_kernel_size', 'none',\
                             [],  [], DLLayerConvolution)
* Use a depth to space layer to combine Upscale^2 feature maps to upscale.
create_dl_layer_depth_to_space (DLLayerConvolution, 'upscaled', Upscale,\
                                'column_row_depth',[], [],\
                                DLLayerDepthToSpace)
* The output shape of DLLayerDepthToSpace is now [16*Upscale, 16*Upscale, 3].
create_dl_model (DLLayerDepthToSpace, DLModel)
```

## Possible Predecessors

`create_dl_layer_input`,
`create_dl_layer_concat`,
`create_dl_layer_reshape`

## Possible Successors

`create_dl_layer_convolution`,
`create_dl_layer_dense`,
`create_dl_layer_reshape`

## See also

`create_dl_layer_reshape`

## Module

Deep Learning Professional

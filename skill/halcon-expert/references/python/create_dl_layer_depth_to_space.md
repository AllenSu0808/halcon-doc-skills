# create_dl_layer_depth_to_space (Operator)

## Name

`create_dl_layer_depth_to_space` — Create a depth to space layer.

## Signature

`def create_dl_layer_depth_to_space(dllayer_input: HHandle, layer_name: str, block_size: int, mode: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_depth_to_space` creates a depth to space
layer whose handle is returned in *`dllayer_depth_to_space`*.

The parameter *`dllayer_input`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

This layer rearranges the elements of the feeding tensor of shape
$(N,C\ast r^{2},H,W)$ to a tensor of shape
$(N,C,H\ast r,W\ast r)$.
Thereby $r$ can be considered an upscale factor, which is set with
*`block_size`*.

The output element $(depth,row,col)$ is mapped from
the input element
$(depth\ast r^{2}+(row%r)\ast r+col%r,row/r,col/r)$.

With *`mode`* the ordering in the output tensor is set. Currently only
the *"column_row_depth"* order described above is available.

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
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"block_size"* (*`block_size`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`block_size`** (input_control)  number `→` int

Block size (i.e., upscale factor).

Default:
3

**`mode`** (input_control)  string `→` str

Ordering mode.

Default:
"column_row_depth"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_depth_to_space`** (output_control)  dl_layer `→` HHandle

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

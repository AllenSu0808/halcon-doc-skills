# CreateDlLayerDepthToSpace (Operator)

## Name

`CreateDlLayerDepthToSpace` — Create a depth to space layer.

## Signature

`static void HOperatorSet.CreateDlLayerDepthToSpace(HTuple DLLayerInput, HTuple layerName, HTuple blockSize, HTuple mode, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerDepthToSpace)`

`HDlLayer HDlLayer.CreateDlLayerDepthToSpace(string layerName, int blockSize, string mode, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerDepthToSpace(string layerName, int blockSize, string mode, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerDepthToSpace` creates a depth to space
layer whose handle is returned in *`DLLayerDepthToSpace`*.

The parameter *`DLLayerInput`* determines the feeding input layer
and expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

This layer rearranges the elements of the feeding tensor of shape
$(N,C\ast r^{2},H,W)$ to a tensor of shape
$(N,C,H\ast r,W\ast r)$.
Thereby $r$ can be considered an upscale factor, which is set with
*`blockSize`*.

The output element $(depth,row,col)$ is mapped from
the input element
$(depth\ast r^{2}+(row%r)\ast r+col%r,row/r,col/r)$.

With *`mode`* the ordering in the output tensor is set. Currently only
the *"column_row_depth"* order described above is available.

Certain parameters of layers created using this operator
`CreateDlLayerDepthToSpace` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"block_size"* (*`blockSize`*) |  | `x` |
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

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`blockSize`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Block size (i.e., upscale factor).

Default:
3

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Ordering mode.

Default:
"column_row_depth"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`DLLayerDepthToSpace`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

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

`CreateDlLayerInput`,
`CreateDlLayerConcat`,
`CreateDlLayerReshape`

## Possible Successors

`CreateDlLayerConvolution`,
`CreateDlLayerDense`,
`CreateDlLayerReshape`

## See also

`CreateDlLayerReshape`

## Module

Deep Learning Professional

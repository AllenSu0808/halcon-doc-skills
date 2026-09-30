# create_dl_layer_matmul (Operator)

## Name

`create_dl_layer_matmul` — Create a MatMul layer.

## Signature

`create_dl_layer_matmul( : : DLLayerA, DLLayerB, LayerName, GenParamName, GenParamValue : DLLayerMatMul)`

## Description

The operator `create_dl_layer_matmul` creates a MatMul layer
whose handle is returned in *`DLLayerMatMul`*.

A MatMul layer multiplies the 2D matrices, given in the latter two
dimensions (H, W) of input *`DLLayerA`*, with the corresponding
2D matrices of input *`DLLayerB`*, also given in the latter two
dimensions (H, W).
The output in *`DLLayerMatMul`* is hence given by
$C=A\cdot B$.

The MatMul layer supports broadcasting for the first input *`DLLayerA`*.
That means, if the batch size or the number of channels in *`DLLayerA`*
equals one then the first batch item or channel of *`DLLayerA`* is
multiplied with all batch items or channels of *`DLLayerB`*,
respectively.

To make the multiplication work, the width of *`DLLayerA`* must be equal
to the height of *`DLLayerB`*.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'num_trainable_params'*:** —

  Number of trainable parameters (weights and biases) of the layer.
- ***'transpose_a'*:** —

  Matrices of input *`DLLayerA`* are transposed:
  $C=A^{T}\cdot B$.

  Default:
   *'false'*
- ***'transpose_b'*:** —

  Matrices of input *`DLLayerB`* are transposed:
  $C=A\cdot B^{T}$.

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_matmul` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerMatMul`*) |  | `x` |
| *'shape'* |  | `x` |
| *'transpose_a'* |  | `x` |
| *'transpose_b'* |  | `x` |
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

**`DLLayerA`** (input_control)  dl_layer `→`  (handle)

Input layer A.

**`DLLayerB`** (input_control)  dl_layer `→`  (handle)

Input layer B.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output', 'num_trainable_params', 'transpose_a', 'transpose_b'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerMatMul`** (output_control)  dl_layer `→`  (handle)

MatMul layer.

## Module

Deep Learning Professional

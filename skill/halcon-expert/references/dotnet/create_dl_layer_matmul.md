# CreateDlLayerMatmul (Operator)

## Name

`CreateDlLayerMatmul` — Create a MatMul layer.

## Signature

`static void HOperatorSet.CreateDlLayerMatmul(HTuple DLLayerA, HTuple DLLayerB, HTuple layerName, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerMatMul)`

`HDlLayer HDlLayer.CreateDlLayerMatmul(HDlLayer DLLayerB, string layerName, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerMatmul(HDlLayer DLLayerB, string layerName, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerMatmul` creates a MatMul layer
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

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"num_trainable_params"*:** —

  Number of trainable parameters (weights and biases) of the layer.
- ***"transpose_a"*:** —

  Matrices of input *`DLLayerA`* are transposed:
  $C=A^{T}\cdot B$.

  Default:
   *"false"*
- ***"transpose_b"*:** —

  Matrices of input *`DLLayerB`* are transposed:
  $C=A\cdot B^{T}$.

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerMatmul` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerMatMul`*) |  | `x` |
| *"shape"* |  | `x` |
| *"transpose_a"* |  | `x` |
| *"transpose_b"* |  | `x` |
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

**`DLLayerA`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Input layer A.

**`DLLayerB`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Input layer B.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output", "num_trainable_params", "transpose_a", "transpose_b"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`DLLayerMatMul`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

MatMul layer.

## Module

Deep Learning Professional

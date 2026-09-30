# create_dl_layer_matmul (Operator)

## Name

`create_dl_layer_matmul` — Create a MatMul layer.

## Signature

`def create_dl_layer_matmul(dllayer_a: HHandle, dllayer_b: HHandle, layer_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_matmul` creates a MatMul layer
whose handle is returned in *`dllayer_mat_mul`*.

A MatMul layer multiplies the 2D matrices, given in the latter two
dimensions (H, W) of input *`dllayer_a`*, with the corresponding
2D matrices of input *`dllayer_b`*, also given in the latter two
dimensions (H, W).
The output in *`dllayer_mat_mul`* is hence given by
$C=A\cdot B$.

The MatMul layer supports broadcasting for the first input *`dllayer_a`*.
That means, if the batch size or the number of channels in *`dllayer_a`*
equals one then the first batch item or channel of *`dllayer_a`* is
multiplied with all batch items or channels of *`dllayer_b`*,
respectively.

To make the multiplication work, the width of *`dllayer_a`* must be equal
to the height of *`dllayer_b`*.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"num_trainable_params"*:** —

  Number of trainable parameters (weights and biases) of the layer.
- ***"transpose_a"*:** —

  Matrices of input *`dllayer_a`* are transposed:
  $C=A^{T}\cdot B$.

  Default:
   *"false"*
- ***"transpose_b"*:** —

  Matrices of input *`dllayer_b`* are transposed:
  $C=A\cdot B^{T}$.

  Default:
   *"false"*

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
| *"input_layer"* |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_mat_mul`*) |  | `x` |
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

**`dllayer_a`** (input_control)  dl_layer `→` HHandle

Input layer A.

**`dllayer_b`** (input_control)  dl_layer `→` HHandle

Input layer B.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output", "num_trainable_params", "transpose_a", "transpose_b"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_mat_mul`** (output_control)  dl_layer `→` HHandle

MatMul layer.

## Module

Deep Learning Professional

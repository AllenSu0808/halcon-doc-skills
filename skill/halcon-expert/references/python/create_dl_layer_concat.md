# create_dl_layer_concat (Operator)

## Name

`create_dl_layer_concat` — Create a concatenation layer.

## Signature

`def create_dl_layer_concat(dllayer_inputs: MaybeSequence[HHandle], layer_name: str, axis: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_concat` creates a concatenation layer
whose handle is returned in *`dllayer_concat`*.

The parameter *`dllayer_inputs`* determines the feeding input layers.
This layer expects at least one layer as input.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

A concatenation layer concatenates the data tensors of the input layers
in *`dllayer_inputs`* and returns a single data tensor
*`dllayer_concat`*.
The parameter *`axis`* specifies along which dimension the
inputs should be concatenated. The supported options for *`axis`*
are:

- ***"batch"*:** —

  Concatenation is applied along the
  `batch`-dimension.

  *Example:* if you concatenate two inputs *A* and *B* of
  shape (h, w, d, b) = (1, 1, 1, 2), where *A* = [*A0*,
  *A1*] and *B* = [*B0*, *B1*], you
  obtain the output [*A0*, *A1*, *B0*, *B1*]
  with shape (1, 1, 1, 4).
- ***"batch_interleaved"*:** —

  Concatenation is applied along the
  `depth`-dimension, but the output is reshaped as if the data was
  concatenated along the `batch`-dimension. For this dimension,
  all inputs need to have exactly the same shape.

  Note that when the input `batch_size` is *1*, the
  concatenation is identical for *"batch"* and
  *"batch_interleaved"*.

  *Example:* if you concatenate two inputs *A* and *B* of
  shape (h, w, d, b) = (1, 1, 1, 2), where *A* = [*A0*,
  *A1*] and *B* = [*B0*, *B1*], you
  obtain the output [*A0*, *B0*, *A1*, *B1*]
  with shape (1, 1, 1, 4).
- ***"depth"*:** —

  Concatenation is applied along the
  `depth`-dimension.

  *Example:* if you concatenate two inputs *A* and *B* of
  shape (h, w, d, b) = (1, 1, 1, 2), where *A* = [*A0*,
  *A1*] and *B* = [*B0*, *B1*], you
  obtain the output [*A0*, *A1*, *B0*, *B1*]
  with shape (1, 1, 2, 2).
- ***"height"*:** —

  Concatenation is applied along the
  `height`-dimension.
- ***"width"*:** —

  Concatenation is applied along the
  `width`-dimension.

Note that all non-concatenated dimensions must be equal for all input data
tensors.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying
  this layer in `outputs` (*"true"*) or not
  (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_concat` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_inputs`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_concat`*) |  | `x` |
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

**`dllayer_inputs`** (input_control)  dl_layer(-array) `→` MaybeSequence[HHandle]

Feeding input layers.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`axis`** (input_control)  string `→` str

Dimension along which the input layers are concatenated.

Default:
"depth"

List of values:
"batch", "batch_interleaved", "depth", "height", "width"

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

**`dllayer_concat`** (output_control)  dl_layer `→` HHandle

Concatenation layer.

## Module

Deep Learning Professional

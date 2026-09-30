# create_dl_layer_dense (Operator)

## Name

`create_dl_layer_dense` — Create a dense layer.

## Signature

`def create_dl_layer_dense(dllayer_input: HHandle, layer_name: str, num_out: int, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_dense` creates a dense or fully connected
layer (sometimes also called gemm) with *`num_out`* output neurons whose
handle is returned in *`dllayer_dense`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"bias_filler"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*.

  Default:
   *"const"*
- ***"bias_filler_const_val"*:** —

  Constant value if
  *"bias_filler"* = *"const"*.

  Default:
   *0*
- ***"bias_filler_variance_norm"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"norm_out"*, *"norm_in"*,
  *"norm_average"*, or constant value (in combination with
  *"bias_filler"* = *"msra"*).

  Default:
   *"norm_in"*
- ***"bias_term"*:** —

  Determines whether the created dense
  layer has a bias term (*"true"*) or not (*"false"*).

  Default:
   *"true"*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"learning_rate_multiplier"*:** —

  Multiplier for the learning
  rate for this layer that is used during training.
  If *"learning_rate_multiplier"* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***"learning_rate_multiplier_bias"*:** —

  Multiplier for the
  learning rate of the bias term. The total bias learning rate is the
  product of *"learning_rate_multiplier_bias"* and
  *"learning_rate_multiplier"*.

  Default:
   *1.0*
- ***"weight_filler"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"xavier"*, *"msra"*,
  *"const"*.

  Default:
   *"xavier"*
- ***"weight_filler_const_val"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  Default:
   *0.5*
- ***"weight_filler_variance_norm"*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *"norm_in"*, *"norm_out"*,
  *"norm_average"*, or constant value (in combination with
  *"bias_filler"* = *"msra"*).

  Default:
   *"norm_in"*

Certain parameters of layers created using
`create_dl_layer_dense` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"neurons_in"* |  | `x` |
| *"neurons_out"* (*`num_out`*) |  | `x` |
| *"output_layer"* (*`dllayer_dense`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"bias_filler"* | `x` | `x` |
| *"bias_filler_const_val"* | `x` | `x` |
| *"bias_filler_variance_norm"* | `x` | `x` |
| *"bias_term"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"learning_rate_multiplier"* | `x` | `x` |
| *"learning_rate_multiplier_bias"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"weight_filler"* | `x` | `x` |
| *"weight_filler_const_val"* | `x` | `x` |
| *"weight_filler_variance_norm"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`num_out`** (input_control)  number `→` int

Number of output neurons.

Default:
100

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "bias_term", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"xavier", "msra", "const", "nearest_neighbor", "bilinear", "norm_in", "norm_out", "norm_average", "true", "false", 1.0, 0.9, 0.0

**`dllayer_dense`** (output_control)  dl_layer `→` HHandle

Dense layer.

## Module

Deep Learning Professional

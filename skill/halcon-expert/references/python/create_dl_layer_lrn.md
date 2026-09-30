# create_dl_layer_lrn (Operator)

## Name

`create_dl_layer_lrn` — Create a LRN layer.

## Signature

`def create_dl_layer_lrn(dllayer_input: HHandle, layer_name: str, local_size: int, alpha: float, beta: float, k: float, norm_region: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_lrn` creates a local response
normalization layer which performs normalization
over a local window and whose handle is returned in *`dllayer_lrn`*.
Currently, for *`norm_region`* only *"across_channels"* can
be set, which results in a normalization across the channel
dimension.
More detailed, a value $x_{c}$ located in a channel with index
$c$ is normalized with a scale factor depending on a local window,
$$LRN(x_c) = x_c · \Big( K + \frac{\Alpha}{n} \sum_{c' = \max(0, c - n/2)}^{\min(N - 1, c + n/2)} x_{c'}^{2} \Big)^{-\Beta}$$ ![figure](../assets/edbdd6b40a83910d.svg)

where $n$ is the size of the local window given by *`local_size`*,
$N$ is the total number of channels,
*`alpha`* is the scaling parameter (used as a normalization constant),
*`beta`* is the exponent used as a contrast constant, and
*`k`* is a constant summand, which is used to avoid any singularities.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_lrn` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"alpha"* (*`alpha`*) |  | `x` |
| *"beta"* (*`beta`*) |  | `x` |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"k"* (*`k`*) |  | `x` |
| *"local_size"* (*`local_size`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"norm_region"* (*`norm_region`*) |  | `x` |
| *"output_layer"* (*`dllayer_lrn`*) |  | `x` |
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

**`local_size`** (input_control)  number `→` int

Size of the local window.

Default:
5

**`alpha`** (input_control)  number `→` float

Scaling factor in the LRN formula.

Default:
0.0001

**`beta`** (input_control)  number `→` float

Exponent in the LRN formula.

Default:
0.75

**`k`** (input_control)  number `→` float

Constant summand in the LRN formula.

Default:
1.0

**`norm_region`** (input_control)  string `→` str

Normalization dimension.

Default:
"across_channels"

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

**`dllayer_lrn`** (output_control)  dl_layer `→` HHandle

LRN layer.

## Module

Deep Learning Professional

# create_dl_layer_lrn (Operator)

## Name

`create_dl_layer_lrn` — Create a LRN layer.

## Signature

`create_dl_layer_lrn( : : DLLayerInput, LayerName, LocalSize, Alpha, Beta, K, NormRegion, GenParamName, GenParamValue : DLLayerLRN)`

## Description

The operator `create_dl_layer_lrn` creates a local response
normalization layer which performs normalization
over a local window and whose handle is returned in *`DLLayerLRN`*.
Currently, for *`NormRegion`* only *'across_channels'* can
be set, which results in a normalization across the channel
dimension.
More detailed, a value $x_{c}$ located in a channel with index
$c$ is normalized with a scale factor depending on a local window,
$$LRN(x_c) = x_c · \Big( K + \frac{\Alpha}{n} \sum_{c' = \max(0, c - n/2)}^{\min(N - 1, c + n/2)} x_{c'}^{2} \Big)^{-\Beta}$$ ![figure](../assets/edbdd6b40a83910d.svg)

where $n$ is the size of the local window given by *`LocalSize`*,
$N$ is the total number of channels,
*`Alpha`* is the scaling parameter (used as a normalization constant),
*`Beta`* is the exponent used as a contrast constant, and
*`K`* is a constant summand, which is used to avoid any singularities.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

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
| *'alpha'* (*`Alpha`*) |  | `x` |
| *'beta'* (*`Beta`*) |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'k'* (*`K`*) |  | `x` |
| *'local_size'* (*`LocalSize`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'norm_region'* (*`NormRegion`*) |  | `x` |
| *'output_layer'* (*`DLLayerLRN`*) |  | `x` |
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

**`LocalSize`** (input_control)  number `→`  (integer)

Size of the local window.

Default:
5

**`Alpha`** (input_control)  number `→`  (real)

Scaling factor in the LRN formula.

Default:
0.0001

**`Beta`** (input_control)  number `→`  (real)

Exponent in the LRN formula.

Default:
0.75

**`K`** (input_control)  number `→`  (real)

Constant summand in the LRN formula.

Default:
1.0

**`NormRegion`** (input_control)  string `→`  (string)

Normalization dimension.

Default:
'across_channels'

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

**`DLLayerLRN`** (output_control)  dl_layer `→`  (handle)

LRN layer.

## Module

Deep Learning Professional

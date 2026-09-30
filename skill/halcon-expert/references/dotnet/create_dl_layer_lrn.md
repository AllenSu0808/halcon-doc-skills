# CreateDlLayerLrn (Operator)

## Name

`CreateDlLayerLrn` — Create a LRN layer.

## Signature

`static void HOperatorSet.CreateDlLayerLrn(HTuple DLLayerInput, HTuple layerName, HTuple localSize, HTuple alpha, HTuple beta, HTuple k, HTuple normRegion, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerLRN)`

`HDlLayer HDlLayer.CreateDlLayerLrn(string layerName, int localSize, double alpha, double beta, double k, string normRegion, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerLrn(string layerName, int localSize, double alpha, double beta, double k, string normRegion, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerLrn` creates a local response
normalization layer which performs normalization
over a local window and whose handle is returned in *`DLLayerLRN`*.
Currently, for *`normRegion`* only *"across_channels"* can
be set, which results in a normalization across the channel
dimension.
More detailed, a value $x_{c}$ located in a channel with index
$c$ is normalized with a scale factor depending on a local window,
$$LRN(x_c) = x_c · \Big( K + \frac{\Alpha}{n} \sum_{c' = \max(0, c - n/2)}^{\min(N - 1, c + n/2)} x_{c'}^{2} \Big)^{-\Beta}$$ ![figure](../assets/edbdd6b40a83910d.svg)

where $n$ is the size of the local window given by *`localSize`*,
$N$ is the total number of channels,
*`alpha`* is the scaling parameter (used as a normalization constant),
*`beta`* is the exponent used as a contrast constant, and
*`k`* is a constant summand, which is used to avoid any singularities.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerLrn` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"alpha"* (*`alpha`*) |  | `x` |
| *"beta"* (*`beta`*) |  | `x` |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"k"* (*`k`*) |  | `x` |
| *"local_size"* (*`localSize`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"norm_region"* (*`normRegion`*) |  | `x` |
| *"output_layer"* (*`DLLayerLRN`*) |  | `x` |
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

**`localSize`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Size of the local window.

Default:
5

**`alpha`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Scaling factor in the LRN formula.

Default:
0.0001

**`beta`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Exponent in the LRN formula.

Default:
0.75

**`k`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Constant summand in the LRN formula.

Default:
1.0

**`normRegion`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normalization dimension.

Default:
"across_channels"

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

**`DLLayerLRN`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

LRN layer.

## Module

Deep Learning Professional

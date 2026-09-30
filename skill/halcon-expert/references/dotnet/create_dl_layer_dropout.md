# CreateDlLayerDropout (Operator)

## Name

`CreateDlLayerDropout` — Create a DropOut layer.

## Signature

`static void HOperatorSet.CreateDlLayerDropout(HTuple DLLayerInput, HTuple layerName, HTuple probability, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerDropOut)`

`HDlLayer HDlLayer.CreateDlLayerDropout(string layerName, double probability, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerDropout(string layerName, double probability, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerDropout` creates a DropOut layer with
probability *`probability`* and returns the handle *`DLLayerDropOut`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

During training, activations within *`DLLayerInput`* are set to zero
with probability *`probability`*. All other activations are rescaled
with (1 - *`probability`*).

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerDropout` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerDropOut`*) |  | `x` |
| *"probability"* (*`probability`*) |  | `x` |
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

**`probability`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Probability.

Default:
0.5

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

**`DLLayerDropOut`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

DropOut layer.

## Module

Deep Learning Professional

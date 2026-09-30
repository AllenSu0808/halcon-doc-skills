# CreateDlLayerDepthMax (Operator)

## Name

`CreateDlLayerDepthMax` — Create a depth max layer.

## Signature

`static void HOperatorSet.CreateDlLayerDepthMax(HTuple DLLayerInput, HTuple layerName, HTuple depthMaxMode, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerDepthMaxArg, out HTuple DLLayerDepthMaxValue)`

`HDlLayer[] HDlLayer.CreateDlLayerDepthMax(string layerName, string depthMaxMode, HTuple genParamName, HTuple genParamValue, out HDlLayer[] DLLayerDepthMaxValue)`

`HDlLayer HDlLayer.CreateDlLayerDepthMax(string layerName, string depthMaxMode, string genParamName, string genParamValue, out HDlLayer DLLayerDepthMaxValue)`

## Description

The operator `CreateDlLayerDepthMax` creates a depth max layer.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

There are two possible output layers depending on *`depthMaxMode`*:

- *`DLLayerDepthMaxArg`*: Handle to a depth max layer with mode
  *"argmax"*.
- *`DLLayerDepthMaxValue`*: Handle to a depth max layer with mode
  *"value"*.

Note, these parameters only need to be set in case such an output layer
is requested (see *`depthMaxMode`*).

The parameter *`layerName`* defines the name of the output layer(s)
depending on *`depthMaxMode`*:

- *"argmax"*: name of *`DLLayerDepthMaxArg`*.
- *"value"*: name of *`DLLayerDepthMaxValue`*.
- *"argmax_and_value"*: name of *`DLLayerDepthMaxArg`*,
  while the layer *`DLLayerDepthMaxValue`* receives the same name
  with the suffix string *"_value"* appended to it.

Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of the
created network must have a unique name.

The mode *`depthMaxMode`* indicates which depth max value is
actually returned as output.
The following values are supported:

- ***"argmax"*:** —

  The `depth` index of the maximal value is returned
  in *`DLLayerDepthMaxArg`*.
- ***"value"*:** —

  The maximal value itself is returned in *`DLLayerDepthMaxValue`*.
- ***"argmax_and_value"*:** —

  Both are returned, the `depth` index of
  the maximal value in the output layer *`DLLayerDepthMaxArg`*, and
  the maximal value itself in the output layer
  *`DLLayerDepthMaxValue`*.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerDepthMax` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"mode"* (*`depthMaxMode`*) | `x` | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerDepthMaxArg`* and/or *`DLLayerDepthMaxValue`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* |  | `x` |
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

**`depthMaxMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode to indicate type of return value.

Default:
"argmax"

List of values:
"argmax", "argmax_and_value", "value"

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

**`DLLayerDepthMaxArg`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Optional, depth max layer with mode *"argmax"*.

**`DLLayerDepthMaxValue`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Optional, depth max layer with mode *"value"*.

## Module

Deep Learning Professional

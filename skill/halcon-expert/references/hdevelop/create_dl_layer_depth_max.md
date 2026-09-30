# create_dl_layer_depth_max (Operator)

## Name

`create_dl_layer_depth_max` — Create a depth max layer.

## Signature

`create_dl_layer_depth_max( : : DLLayerInput, LayerName, DepthMaxMode, GenParamName, GenParamValue : DLLayerDepthMaxArg, DLLayerDepthMaxValue)`

## Description

The operator `create_dl_layer_depth_max` creates a depth max layer.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

There are two possible output layers depending on *`DepthMaxMode`*:

- *`DLLayerDepthMaxArg`*: Handle to a depth max layer with mode
  *'argmax'*.
- *`DLLayerDepthMaxValue`*: Handle to a depth max layer with mode
  *'value'*.

Note, these parameters only need to be set in case such an output layer
is requested (see *`DepthMaxMode`*).

The parameter *`LayerName`* defines the name of the output layer(s)
depending on *`DepthMaxMode`*:

- *'argmax'*: name of *`DLLayerDepthMaxArg`*.
- *'value'*: name of *`DLLayerDepthMaxValue`*.
- *'argmax_and_value'*: name of *`DLLayerDepthMaxArg`*,
  while the layer *`DLLayerDepthMaxValue`* receives the same name
  with the suffix string *'_value'* appended to it.

Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of the
created network must have a unique name.

The mode *`DepthMaxMode`* indicates which depth max value is
actually returned as output.
The following values are supported:

- ***'argmax'*:** —

  The `depth` index of the maximal value is returned
  in *`DLLayerDepthMaxArg`*.
- ***'value'*:** —

  The maximal value itself is returned in *`DLLayerDepthMaxValue`*.
- ***'argmax_and_value'*:** —

  Both are returned, the `depth` index of
  the maximal value in the output layer *`DLLayerDepthMaxArg`*, and
  the maximal value itself in the output layer
  *`DLLayerDepthMaxValue`*.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_depth_max` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'mode'* (*`DepthMaxMode`*) | `x` | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerDepthMaxArg`* and/or *`DLLayerDepthMaxValue`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* |  | `x` |
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

**`DepthMaxMode`** (input_control)  string `→`  (string)

Mode to indicate type of return value.

Default:
'argmax'

List of values:
'argmax', 'argmax_and_value', 'value'

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

**`DLLayerDepthMaxArg`** (output_control)  dl_layer(-array) `→`  (handle)

Optional, depth max layer with mode *'argmax'*.

**`DLLayerDepthMaxValue`** (output_control)  dl_layer(-array) `→`  (handle)

Optional, depth max layer with mode *'value'*.

## Module

Deep Learning Professional

# get_dl_layer_param (Operator)

## Name

`get_dl_layer_param` — Return the parameters of a deep learning layer.

## Signature

`get_dl_layer_param( : : DLLayer, GenParamName : GenParamValue)`

## Description

The operator `get_dl_layer_param` returns the parameter
*`GenParamName`* of the deep learning layer *`DLLayer`*
in *`GenParamValue`*.

Depending on the type of the layer, different parameter names
are valid.
Which generic and layer-specific parameters can be queried is described
in the specific references of the operators used for layer creation
(`create_dl_layer_*`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayer`** (input_control)  dl_layer `→`  (handle)

Layer.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Parameter to query.

Default:
'shape'

List of values:
'input_layer', 'name', 'shape', 'type'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (real / integer / string / handle)

Value of the queried parameter.

## Module

Deep Learning Professional

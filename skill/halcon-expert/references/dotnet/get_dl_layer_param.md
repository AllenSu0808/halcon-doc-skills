# GetDlLayerParam (Operator)

## Name

`GetDlLayerParam` — Return the parameters of a deep learning layer.

## Signature

`static void HOperatorSet.GetDlLayerParam(HTuple DLLayer, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDlLayer.GetDlLayerParam(string genParamName)`

## Description

The operator `GetDlLayerParam` returns the parameter
*`genParamName`* of the deep learning layer *`DLLayer`*
in *`genParamValue`*.

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

**`DLLayer`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Layer.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Parameter to query.

Default:
"shape"

List of values:
"input_layer", "name", "shape", "type"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Value of the queried parameter.

## Module

Deep Learning Professional

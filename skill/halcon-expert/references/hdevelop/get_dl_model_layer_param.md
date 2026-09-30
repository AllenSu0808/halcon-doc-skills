# get_dl_model_layer_param (Operator)

## Name

`get_dl_model_layer_param` — Retrieve parameter values for a given layer.

## Signature

`get_dl_model_layer_param( : : DLModelHandle, LayerName, ParamName : ParamValue)`

## Description

The operator `get_dl_model_layer_param` returns for a layer the value
of the parameter *`ParamName`* in *`ParamValue`*.
The layer is referred by its name *`LayerName`* in the model
*`DLModelHandle`*. You can retrieve the layer names using
[`get_dl_model_param`](get_dl_model_param.md) with its option *'layer_names'* or
*'summary'*.

Which generic and layer-specific parameters can be queried is described
in the specific operator references (`create_dl_layer_*`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`ParamName`** (input_control)  string `→`  (string)

Name of the queried parameter.

Default:
'type'

List of values:
'alpha', 'bias_filler', 'bias_filler_const_val', 'bias_filler_variance_norm', 'bias_term', 'input_layer', 'is_inference_output', 'learning_rate_multiplier', 'learning_rate_multiplier_bias', 'name', 'num_trainable_params', 'output_layer', 'shape', 'type', 'upper_bound', 'weight_filler', 'weight_filler_const_val', 'weight_filler_variance_norm'

Restriction:
`length(ParamName) > 0`

**`ParamValue`** (output_control)  tuple(-array) `→`  (string / real / integer)

Value of the queried parameter.

## See also

`get_dl_model_param`,
`set_dl_model_layer_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional

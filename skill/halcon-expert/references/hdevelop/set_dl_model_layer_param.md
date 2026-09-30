# set_dl_model_layer_param (Operator)

## Name

`set_dl_model_layer_param` — Set parameter values of a given layer.

## Signature

`set_dl_model_layer_param( : : DLModelHandle, LayerName, ParamName, ParamValue : )`

## Description

The operator `set_dl_model_layer_param` sets the value
*`ParamValue`* of the parameter *`ParamName`* for a layer.
The layer is referred to by its name *`LayerName`* in the model
*`DLModelHandle`*. You can retrieve the layer names using
[`get_dl_model_param`](get_dl_model_param.md) with its option *'layer_names'* or
*'summary'*.

Which generic and layer-specific parameters can be set is described
in the entries of the operators (`create_dl_layer_*`), which
are used for creating the layer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`ParamName`** (input_control)  attribute.name `→`  (string)

Name of the set parameter.

Default:
[]

List of values:
'alpha', 'bias_filler', 'bias_filler_const_val', 'bias_filler_variance_norm', 'is_inference_output', 'learning_rate_multiplier', 'learning_rate_multiplier_bias', 'name', 'upper_bound', 'weight_filler', 'weight_filler_const_val', 'weight_filler_variance_norm'

**`ParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Value of the set parameter.

Default:
[]

List of values:
'const', 'false', 'msra', 'norm_average', 'norm_in', 'norm_out', 'true', 'xavier'

## See also

`set_dl_model_param`,
`get_dl_model_param`,
`get_dl_model_layer_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional

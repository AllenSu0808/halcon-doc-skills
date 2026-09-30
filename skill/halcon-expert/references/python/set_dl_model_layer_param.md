# set_dl_model_layer_param (Operator)

## Name

`set_dl_model_layer_param` — Set parameter values of a given layer.

## Signature

`def set_dl_model_layer_param(dlmodel_handle: HHandle, layer_name: str, param_name: str, param_value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

The operator `set_dl_model_layer_param` sets the value
*`param_value`* of the parameter *`param_name`* for a layer.
The layer is referred to by its name *`layer_name`* in the model
*`dlmodel_handle`*. You can retrieve the layer names using
[`get_dl_model_param`](get_dl_model_param.md) with its option *"layer_names"* or
*"summary"*.

Which generic and layer-specific parameters can be set is described
in the entries of the operators (`create_dl_layer_*`), which
are used for creating the layer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Deep learning model.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`param_name`** (input_control)  attribute.name `→` str

Name of the set parameter.

Default:
[]

List of values:
"alpha", "bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "name", "upper_bound", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the set parameter.

Default:
[]

List of values:
"const", "false", "msra", "norm_average", "norm_in", "norm_out", "true", "xavier"

## See also

`set_dl_model_param`,
`get_dl_model_param`,
`get_dl_model_layer_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional

# SetDlModelLayerParam (Operator)

## Name

`SetDlModelLayerParam` — Set parameter values of a given layer.

## Signature

`static void HOperatorSet.SetDlModelLayerParam(HTuple DLModelHandle, HTuple layerName, HTuple paramName, HTuple paramValue)`

`static void HDlLayer.SetDlModelLayerParam(HDlModel DLModelHandle, string layerName, string paramName, HTuple paramValue)`

`static void HDlLayer.SetDlModelLayerParam(HDlModel DLModelHandle, string layerName, string paramName, string paramValue)`

## Description

The operator `SetDlModelLayerParam` sets the value
*`paramValue`* of the parameter *`paramName`* for a layer.
The layer is referred to by its name *`layerName`* in the model
*`DLModelHandle`*. You can retrieve the layer names using
[`GetDlModelParam`](get_dl_model_param.md) with its option *"layer_names"* or
*"summary"*.

Which generic and layer-specific parameters can be set is described
in the entries of the operators (`create_dl_layer_*`), which
are used for creating the layer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Deep learning model.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`paramName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the set parameter.

Default:
[]

List of values:
"alpha", "bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "name", "upper_bound", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

**`paramValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the set parameter.

Default:
[]

List of values:
"const", "false", "msra", "norm_average", "norm_in", "norm_out", "true", "xavier"

## See also

`SetDlModelParam`,
`GetDlModelParam`,
`GetDlModelLayerParam`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional

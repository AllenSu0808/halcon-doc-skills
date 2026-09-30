# GetDlModelLayerParam (Operator)

## Name

`GetDlModelLayerParam` — Retrieve parameter values for a given layer.

## Signature

`static void HOperatorSet.GetDlModelLayerParam(HTuple DLModelHandle, HTuple layerName, HTuple paramName, out HTuple paramValue)`

`static HTuple HDlLayer.GetDlModelLayerParam(HDlModel DLModelHandle, string layerName, string paramName)`

## Description

The operator `GetDlModelLayerParam` returns for a layer the value
of the parameter *`paramName`* in *`paramValue`*.
The layer is referred by its name *`layerName`* in the model
*`DLModelHandle`*. You can retrieve the layer names using
[`GetDlModelParam`](get_dl_model_param.md) with its option *"layer_names"* or
*"summary"*.

Which generic and layer-specific parameters can be queried is described
in the specific operator references (`create_dl_layer_*`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Deep learning model.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`paramName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the queried parameter.

Default:
"type"

List of values:
"alpha", "bias_filler", "bias_filler_const_val", "bias_filler_variance_norm", "bias_term", "input_layer", "is_inference_output", "learning_rate_multiplier", "learning_rate_multiplier_bias", "name", "num_trainable_params", "output_layer", "shape", "type", "upper_bound", "weight_filler", "weight_filler_const_val", "weight_filler_variance_norm"

Restriction:
`length(ParamName) > 0`

**`paramValue`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the queried parameter.

## See also

`GetDlModelParam`,
`SetDlModelLayerParam`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional

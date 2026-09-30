# optimize_dl_model_for_inference (Operator)

## Name

`optimize_dl_model_for_inference` — Optimize a model for inference on a device via the
AI
2-interface.

## Signature

`def optimize_dl_model_for_inference(dlmodel_handle: HHandle, dldevice_handle: MaybeSequence[HHandle], precision: str, dlsamples: Sequence[HHandle], gen_param: HHandle) -> Tuple[HHandle, HHandle]`

## Description

The operator `optimize_dl_model_for_inference` optimizes the
input model *`dlmodel_handle`* for inference on the device
*`dldevice_handle`* and returns the
optimized model in *`dlmodel_handle_converted`*.
This operator has two distinct functionalities:
Casting the model precision to *`precision`* and calibrating the
model based on the given samples *`dlsamples`*.
Additionally in either case the model architecture may be optimized
for the *`dldevice_handle`*.

The parameter *`dldevice_handle`* specifies the deep learning device
for which the model is optimized.
Whether the device supports optimization can be determined using
[`get_dl_device_param`](get_dl_device_param.md) with *"conversion_supported"*.
After a successful execution, `optimize_dl_model_for_inference`
sets the parameter *"precision_is_converted"* to *"true"*
for the output model *`dlmodel_handle_converted`*.
In addition, the device in *`dldevice_handle`* is automatically
set for the model if it supports the precision set by the parameter
*`precision`*. Whether the device supports the requested precision can
be determined using [`get_dl_device_param`](get_dl_device_param.md) with *"precisions"*.

The parameter *`precision`* specifies the precision to which the model
should be converted to. By default, models that are delivered by HALCON have
the *`precision`* *"float32"*.
The following values are supported for *`precision`*:

- *"bfloat16"*
- *"float32"*
- *"float16"*
- *"int8"*

The parameter *`dlsamples`* specifies the samples on
which the calibration is based.
As a consequence they should be representative.
It is recommended to provide them from the training split.
For most applications 10-20 samples per class are sufficient
to achieve good results.

Note, the samples are not needed for a pure cast operation.
In this case, an empty tuple can be passed over for *`dlsamples`*.

The parameter *`gen_param`* specifies additional, device specific
parameters and their values.
Which parameters to set for the given *`dldevice_handle`*
in *`gen_param`* and their default values can be queried
via the [`get_dl_device_param`](get_dl_device_param.md) operator with the
*"optimize_for_inference_params"* parameter.

Note, certain devices also expect only an empty dictionary.

The parameter *`conversion_report`* returns a report dictionary
with information about the conversion.

## Attention

This operator can only be used via an AI
2-interface.
Furthermore, after optimization only parameters that do not change the
underlying architecture of the model can be set for
*`dlmodel_handle_converted`*.

For [`set_dl_model_param`](set_dl_model_param.md), this includes the following parameters:

- 'Any': *"device"*, *"meta_data"*, *"runtime"*
- 'anomaly_detection': *"standard_deviation_factor"*
- 'classification': *"class_names"*, *"ood_threshold"*
- 'ocr_detection': *"min_character_score"*, *"min_link_score"*,
  *"min_word_score"*, *"orientation"*,
  *"sort_by_line"*, *"tiling"*,
  *"tiling_overlap"*
- 'ocr_recognition': *"alphabet"*, *"alphabet_internal"*,
  *"alphabet_mapping"*
- 'gc_anomaly_detection': *"anomaly_score_tolerance"*
- 'detection': *"class_names"*, *"max_num_detections"*,
  *"max_overlap"*, *"max_overlap_class_agnostic"*,
  *"min_confidence"*
- 'segmentation': *"class_names"*, *"tiling_overlap"*

For [`set_deep_ocr_param`](set_deep_ocr_param.md), this includes the following parameters:

- *"device"*, *"runtime"*
- *"detection_min_character_score"*, *"detection_min_link_score"*, *"detection_min_word_score"*,
- *"detection_orientation"*, *"detection_sort_by_line"*,
- *"detection_tiling"*, *"detection_tiling_overlap"*
- *"recognition_alphabet"*, *"recognition_alphabet_internal"*, *"recognition_alphabet_mapping"*

For [`set_deep_counting_model_param`](set_deep_counting_model_param.md), this includes the following parameters:

- *"device"*
- *"max_overlap"*, *"min_score"*

Only the AI
2-interface that was used to optimize can be set using
*"device"* or the *"runtime"*.
Additional restrictions may apply to these parameters to ensure that the
underlying architecture of the model does not change.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Input model.

**`dldevice_handle`** (input_control)  dl_device(-array) `→` MaybeSequence[HHandle]

Device handle used for optimization.

**`precision`** (input_control)  string `→` str

Precision the model shall be converted to.

**`dlsamples`** (input_control)  dict-array `→` Sequence[HHandle]

Samples required for optimization.

**`gen_param`** (input_control)  dict `→` HHandle

Parameter dict for optimization.

**`dlmodel_handle_converted`** (output_control)  dl_model `→` HHandle

Output model with new precision.

**`conversion_report`** (output_control)  dict `→` HHandle

Output report for conversion.

## Result

If the parameters are valid, the operator `optimize_dl_model_for_inference`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_dl_model_batch`,
`query_available_dl_devices`

## Possible Successors

`set_dl_model_param`,
`apply_dl_model`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional

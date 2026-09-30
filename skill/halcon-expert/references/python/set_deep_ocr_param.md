# set_deep_ocr_param (Operator)

## Name

`set_deep_ocr_param` — Set the parameters of a Deep OCR model.

## Signature

`def set_deep_ocr_param(deep_ocr_handle: HHandle, gen_param_name: str, gen_param_value: HTupleType) -> None`

## Description

`set_deep_ocr_param` sets the parameters *`gen_param_name`* of the
Deep OCR model *`deep_ocr_handle`* to the values
*`gen_param_value`*.

The possible parameters are listed and described in
[`get_deep_ocr_param`](get_deep_ocr_param.md). An overview of the
Deep OCR workflow is given in [OCR / Deep OCR](toc_ocr_deepocr.md).

## Attention

System requirements:
To successfully set *"gpu"* parameters, cuDNN and cuBLAS are
required, i.e., to set the parameter *`gen_param_name`*
*"device"* to a GPU.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deep_ocr_handle`** (input_control)  deep_ocr `→` HHandle

Handle of the Deep OCR model.

**`gen_param_name`** (input_control)  attribute.name `→` str

Name of the generic parameter.

Default:
"detection_image_width"

List of values:
"detection_device", "detection_image_height", "detection_image_size", "detection_image_width", "detection_min_character_score", "detection_min_link_score", "detection_min_word_area", "detection_min_word_score", "detection_model", "detection_optimize_for_inference", "detection_orientation", "detection_sort_by_line", "detection_tiling", "detection_tiling_overlap", "device", "recognition_alignment", "recognition_alphabet", "recognition_alphabet_internal", "recognition_alphabet_mapping", "recognition_batch_size", "recognition_device", "recognition_image_width", "recognition_model", "recognition_num_char_candidates", "recognition_optimize_for_inference"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` HTupleType

Value of the generic parameter.

Default:
1024

Suggested values:
0, 10, 50, 100, 200, 512, 768, 1024, 1280, 0.3, 0.4, 0.5, 0.6, 0.7, "true", "false", "auto", "compact", "default", "pretrained_deep_ocr_detection.hdl", "pretrained_deep_ocr_detection_compact.hdl", "pretrained_deep_ocr_recognition.hdl", "pretrained_deep_ocr_recognition_compact.hdl"

## Result

If the parameters are valid, the operator
`set_deep_ocr_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_deep_ocr`,
`get_deep_ocr_param`

## Possible Successors

`get_deep_ocr_param`,
`apply_deep_ocr`

## See also

`get_deep_ocr_param`

## Module

OCR/OCV

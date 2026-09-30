# SetDeepOcrParam (Operator)

## Name

`SetDeepOcrParam` — Set the parameters of a Deep OCR model.

## Signature

`static void HOperatorSet.SetDeepOcrParam(HTuple deepOcrHandle, HTuple genParamName, HTuple genParamValue)`

`void HDlModelOcr.SetDeepOcrParam(string genParamName, HTuple genParamValue)`

`void HDlModelOcr.SetDeepOcrParam(string genParamName, double genParamValue)`

## Description

`SetDeepOcrParam` sets the parameters *`genParamName`* of the
Deep OCR model *`deepOcrHandle`* to the values
*`genParamValue`*.

The possible parameters are listed and described in
[`GetDeepOcrParam`](get_deep_ocr_param.md). An overview of the
Deep OCR workflow is given in [OCR / Deep OCR](toc_ocr_deepocr.md).

## Attention

System requirements:
To successfully set *"gpu"* parameters, cuDNN and cuBLAS are
required, i.e., to set the parameter *`genParamName`*
*"device"* to a GPU.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deepOcrHandle`** (input_control)  deep_ocr `→` [HDlModelOcr](HDlModelOcr.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep OCR model.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
"detection_image_width"

List of values:
"detection_device", "detection_image_height", "detection_image_size", "detection_image_width", "detection_min_character_score", "detection_min_link_score", "detection_min_word_area", "detection_min_word_score", "detection_model", "detection_optimize_for_inference", "detection_orientation", "detection_sort_by_line", "detection_tiling", "detection_tiling_overlap", "device", "recognition_alignment", "recognition_alphabet", "recognition_alphabet_internal", "recognition_alphabet_mapping", "recognition_batch_size", "recognition_device", "recognition_image_width", "recognition_model", "recognition_num_char_candidates", "recognition_optimize_for_inference"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / string / int / long / HHandle)

Value of the generic parameter.

Default:
1024

Suggested values:
0, 10, 50, 100, 200, 512, 768, 1024, 1280, 0.3, 0.4, 0.5, 0.6, 0.7, "true", "false", "auto", "compact", "default", "pretrained_deep_ocr_detection.hdl", "pretrained_deep_ocr_detection_compact.hdl", "pretrained_deep_ocr_recognition.hdl", "pretrained_deep_ocr_recognition_compact.hdl"

## Result

If the parameters are valid, the operator
`SetDeepOcrParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateDeepOcr`,
`GetDeepOcrParam`

## Possible Successors

`GetDeepOcrParam`,
`ApplyDeepOcr`

## See also

`GetDeepOcrParam`

## Module

OCR/OCV

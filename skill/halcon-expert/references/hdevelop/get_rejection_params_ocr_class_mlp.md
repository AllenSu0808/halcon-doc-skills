# get_rejection_params_ocr_class_mlp (Operator)

## Name

`get_rejection_params_ocr_class_mlp` — Return the rejection class parameters of an OCR classifier.

## Signature

`get_rejection_params_ocr_class_mlp( : : OCRHandle, GenParamName : GenParamValue)`

## Description

`get_rejection_params_ocr_class_mlp` returns the rejection
class parameters of an OCR classifier that were specified with
[`set_rejection_params_ocr_class_mlp`](set_rejection_params_ocr_class_mlp.md). For a description of the
parameters, see [`set_rejection_params_ocr_class_mlp`](set_rejection_params_ocr_class_mlp.md) and
[`set_rejection_params_class_mlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→`  (handle)

Handle of the OCR classifier.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Name of the general parameter.

Default:
'sampling_strategy'

List of values:
'hyperbox_tolerance', 'random_seed', 'rejection_class_index', 'rejection_sample_factor', 'sampling_strategy'

**`GenParamValue`** (output_control)  string(-array) `→`  (string)

Value of the general parameter.

## Result

If the parameters are valid, the operator
`get_rejection_params_ocr_class_mlp` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_ocr_class_mlp`,
`read_ocr_class_mlp`

## Possible Successors

`trainf_ocr_class_mlp`

## Module

OCR/OCV

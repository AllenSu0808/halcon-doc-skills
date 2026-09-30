# GetRejectionParamsOcrClassMlp (Operator)

## Name

`GetRejectionParamsOcrClassMlp` — Return the rejection class parameters of an OCR classifier.

## Signature

`static void HOperatorSet.GetRejectionParamsOcrClassMlp(HTuple OCRHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HOCRMlp.GetRejectionParamsOcrClassMlp(HTuple genParamName)`

`string HOCRMlp.GetRejectionParamsOcrClassMlp(string genParamName)`

## Description

`GetRejectionParamsOcrClassMlp` returns the rejection
class parameters of an OCR classifier that were specified with
[`SetRejectionParamsOcrClassMlp`](set_rejection_params_ocr_class_mlp.md). For a description of the
parameters, see [`SetRejectionParamsOcrClassMlp`](set_rejection_params_ocr_class_mlp.md) and
[`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the general parameter.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Value of the general parameter.

## Result

If the parameters are valid, the operator
`GetRejectionParamsOcrClassMlp` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateOcrClassMlp`,
`ReadOcrClassMlp`

## Possible Successors

`TrainfOcrClassMlp`

## Module

OCR/OCV

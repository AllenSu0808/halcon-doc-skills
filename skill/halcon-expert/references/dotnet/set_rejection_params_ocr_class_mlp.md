# SetRejectionParamsOcrClassMlp (Operator)

## Name

`SetRejectionParamsOcrClassMlp` — Set the rejection class parameters of an OCR classifier.

## Signature

`static void HOperatorSet.SetRejectionParamsOcrClassMlp(HTuple OCRHandle, HTuple genParamName, HTuple genParamValue)`

`void HOCRMlp.SetRejectionParamsOcrClassMlp(HTuple genParamName, HTuple genParamValue)`

`void HOCRMlp.SetRejectionParamsOcrClassMlp(string genParamName, string genParamValue)`

## Description

`SetRejectionParamsOcrClassMlp` sets the rejection class
parameters of the OCR classifier passed in *`OCRHandle`*. The
parameter to be set is specified with *`genParamName`*. Its
value is specified with *`genParamValue`*. For some OCR
applications it is important to know, if a letter to be classified
is similar to the training set or not. If a letter is different to
the training set, then it can be classified a rejection class. This
additional rejection class must be specified as an additional
character in [`CreateOcrClassMlp`](create_ocr_class_mlp.md). For details on how to
specify a rejection class, see
[`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the general parameter.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Value of the general parameter.

Default:
"hyperbox_around_all_classes"

List of values:
"hyperbox_around_all_classes", "hyperbox_around_each_class", "hyperbox_ring_around_each_class", "no_rejection_class"

## Result

If the parameters are valid, the operator
`SetRejectionParamsOcrClassMlp` returns the value
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

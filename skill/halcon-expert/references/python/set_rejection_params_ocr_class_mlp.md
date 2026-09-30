# set_rejection_params_ocr_class_mlp (Operator)

## Name

`set_rejection_params_ocr_class_mlp` — Set the rejection class parameters of an OCR classifier.

## Signature

`def set_rejection_params_ocr_class_mlp(ocrhandle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[str]) -> None`

## Description

`set_rejection_params_ocr_class_mlp` sets the rejection class
parameters of the OCR classifier passed in *`ocrhandle`*. The
parameter to be set is specified with *`gen_param_name`*. Its
value is specified with *`gen_param_value`*. For some OCR
applications it is important to know, if a letter to be classified
is similar to the training set or not. If a letter is different to
the training set, then it can be classified a rejection class. This
additional rejection class must be specified as an additional
character in [`create_ocr_class_mlp`](create_ocr_class_mlp.md). For details on how to
specify a rejection class, see
[`set_rejection_params_class_mlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrhandle`** (input_control, state is modified)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the general parameter.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`gen_param_value`** (input_control)  string(-array) `→` MaybeSequence[str]

Value of the general parameter.

Default:
"hyperbox_around_all_classes"

List of values:
"hyperbox_around_all_classes", "hyperbox_around_each_class", "hyperbox_ring_around_each_class", "no_rejection_class"

## Result

If the parameters are valid, the operator
`set_rejection_params_ocr_class_mlp` returns the value
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

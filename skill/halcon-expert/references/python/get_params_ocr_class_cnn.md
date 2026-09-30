# get_params_ocr_class_cnn (Operator)

## Name

`get_params_ocr_class_cnn` — Return the parameters of a CNN-based OCR classifier.

## Signature

`def get_params_ocr_class_cnn(ocrhandle: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[int, str]]`

`def get_params_ocr_class_cnn_s(ocrhandle: HHandle, gen_param_name: MaybeSequence[str]) -> Union[int, str]`

## Description

`get_params_ocr_class_cnn` returns the parameters
*`gen_param_name`* of an OCR classifier *`ocrhandle`* in
*`gen_param_value`*. This is particularly useful if the
classifier was read with [`read_ocr_class_cnn`](read_ocr_class_cnn.md).
The output of `get_params_ocr_class_cnn`
can, for example, be used to check whether a character to be read is
contained in the classifier.

Possible values for *`gen_param_name`* are:

- ***"characters"*:** —

  Returns a list of all trained symbols which may be recognized by the
  CNN-based OCR classifier. Note that if *"characters"* is specified
  then no other generic parameter is allowed. Otherwise an exception is
  thrown.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_cnn `→` HHandle

Handle of the OCR classifier.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

A tuple of generic parameter names.

Default:
"characters"

List of values:
"characters"

**`gen_param_value`** (output_control)  string(-array) `→` Sequence[Union[int, str]]

A tuple of generic parameter values.

## Result

If the parameters are valid, the operator
`get_params_ocr_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_ocr_class_cnn`

## Possible Successors

`do_ocr_single_class_cnn`,
`do_ocr_multi_class_cnn`

## Module

OCR/OCV

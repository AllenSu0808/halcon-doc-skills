# get_params_ocr_class_cnn (Operator)

## Name

`get_params_ocr_class_cnn` — Return the parameters of a CNN-based OCR classifier.

## Signature

`get_params_ocr_class_cnn( : : OCRHandle, GenParamName : GenParamValue)`

## Description

`get_params_ocr_class_cnn` returns the parameters
*`GenParamName`* of an OCR classifier *`OCRHandle`* in
*`GenParamValue`*. This is particularly useful if the
classifier was read with [`read_ocr_class_cnn`](read_ocr_class_cnn.md).
The output of `get_params_ocr_class_cnn`
can, for example, be used to check whether a character to be read is
contained in the classifier.

Possible values for *`GenParamName`* are:

- ***'characters'*:** —

  Returns a list of all trained symbols which may be recognized by the
  CNN-based OCR classifier. Note that if *'characters'* is specified
  then no other generic parameter is allowed. Otherwise an exception is
  thrown.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_cnn `→`  (handle)

Handle of the OCR classifier.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

A tuple of generic parameter names.

Default:
'characters'

List of values:
'characters'

**`GenParamValue`** (output_control)  string(-array) `→`  (integer / string)

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

# GetParamsOcrClassCnn (Operator)

## Name

`GetParamsOcrClassCnn` — Return the parameters of a CNN-based OCR classifier.

## Signature

`static void HOperatorSet.GetParamsOcrClassCnn(HTuple OCRHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HOCRCnn.GetParamsOcrClassCnn(HTuple genParamName)`

`HTuple HOCRCnn.GetParamsOcrClassCnn(string genParamName)`

## Description

`GetParamsOcrClassCnn` returns the parameters
*`genParamName`* of an OCR classifier *`OCRHandle`* in
*`genParamValue`*. This is particularly useful if the
classifier was read with [`ReadOcrClassCnn`](read_ocr_class_cnn.md).
The output of `GetParamsOcrClassCnn`
can, for example, be used to check whether a character to be read is
contained in the classifier.

Possible values for *`genParamName`* are:

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

**`OCRHandle`** (input_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

A tuple of generic parameter names.

Default:
"characters"

List of values:
"characters"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

A tuple of generic parameter values.

## Result

If the parameters are valid, the operator
`GetParamsOcrClassCnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadOcrClassCnn`

## Possible Successors

`DoOcrSingleClassCnn`,
`DoOcrMultiClassCnn`

## Module

OCR/OCV

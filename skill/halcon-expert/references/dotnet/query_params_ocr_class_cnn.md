# QueryParamsOcrClassCnn (Operator)

## Name

`QueryParamsOcrClassCnn` — Get the names of the parameters that can be used in
[`GetParamsOcrClassCnn`](get_params_ocr_class_cnn.md)
for a given CNN-based OCR classifier.

## Signature

`static void HOperatorSet.QueryParamsOcrClassCnn(HTuple OCRHandle, out HTuple genParamName)`

`HTuple HOCRCnn.QueryParamsOcrClassCnn()`

## Description

The operator `QueryParamsOcrClassCnn` returns the parameter names
that can be used to query all parameters for a given CNN-based OCR
classifier. The resulting parameter names can be used as input parameter
when calling [`GetParamsOcrClassCnn`](get_params_ocr_class_cnn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of OCR classifier.

**`genParamName`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

## Result

The operator `QueryParamsOcrClassCnn` returns the value 2 (
H_MSG_TRUE)
if the
given handle for the OCR classifier is correct. Otherwise, an
exception is raised.

## Possible Successors

`GetParamsOcrClassCnn`

## Module

OCR/OCV

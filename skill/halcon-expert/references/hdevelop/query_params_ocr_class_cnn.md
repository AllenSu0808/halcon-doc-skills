# query_params_ocr_class_cnn (Operator)

## Name

`query_params_ocr_class_cnn` — Get the names of the parameters that can be used in
[`get_params_ocr_class_cnn`](get_params_ocr_class_cnn.md)
for a given CNN-based OCR classifier.

## Signature

`query_params_ocr_class_cnn( : : OCRHandle : GenParamName)`

## Description

The operator `query_params_ocr_class_cnn` returns the parameter names
that can be used to query all parameters for a given CNN-based OCR
classifier. The resulting parameter names can be used as input parameter
when calling [`get_params_ocr_class_cnn`](get_params_ocr_class_cnn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_cnn `→`  (handle)

Handle of OCR classifier.

**`GenParamName`** (output_control)  string(-array) `→`  (string)

Names of the generic parameters.

## Result

The operator `query_params_ocr_class_cnn` returns the value 2 (
H_MSG_TRUE)
if the
given handle for the OCR classifier is correct. Otherwise, an
exception is raised.

## Possible Successors

`get_params_ocr_class_cnn`

## Module

OCR/OCV

# reduce_ocr_class_svm (Operator)

## Name

`reduce_ocr_class_svm` — Approximate a trained SVM-based OCR classifier by a reduced SVM.

## Signature

`reduce_ocr_class_svm( : : OCRHandle, Method, MinRemainingSV, MaxError : OCRHandleReduced)`

## Description

`reduce_ocr_class_svm` reduces the classification time of an
SVM based OCR classifier *`OCRHandle`* by returning a reduced
copy of it in *`OCRHandleReduced`*. The parameters
*`Method`*, *`MinRemainingSV`* and *`MaxError`* have
the same meaning as in [`reduce_class_svm`](reduce_class_svm.md) and are described
there. Please note that classification time can also be
significantly reduced with a preprocessing step in
[`create_ocr_class_svm`](create_ocr_class_svm.md), which possibly introduces less
errors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

Original handle of SVM-based OCR-classifier.

**`Method`** (input_control)  string `→`  (string)

Type of postprocessing to reduce number of SVs.

Default:
'bottom_up'

List of values:
'bottom_up'

**`MinRemainingSV`** (input_control)  integer `→`  (integer)

Minimum number of remaining SVs.

Default:
2

Suggested values:
2, 3, 4, 5, 7, 10, 15, 20, 30, 50

Restriction:
`MinRemainingSV >= 2`

**`MaxError`** (input_control)  real `→`  (real)

Maximum allowed error of reduction.

Default:
0.001

Suggested values:
0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05

Restriction:
`MaxError > 0.0`

**`OCRHandleReduced`** (output_control)  ocr_svm `→`  (handle)

SVMHandle of reduced OCR classifier.

## Result

If the parameters are valid the operator
`reduce_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`,
`get_support_vector_num_ocr_class_svm`

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`,
`get_support_vector_ocr_class_svm`,
`get_support_vector_num_ocr_class_svm`

## See also

`create_ocr_class_svm`

## References

Bernhard Schölkopf, Alexander J.Smola: “Learning with Kernels”;
The MIT Press, London; 1999.

## Module

OCR/OCV

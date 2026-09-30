# ReduceOcrClassSvm (Operator)

## Name

`ReduceOcrClassSvm` — Approximate a trained SVM-based OCR classifier by a reduced SVM.

## Signature

`static void HOperatorSet.ReduceOcrClassSvm(HTuple OCRHandle, HTuple method, HTuple minRemainingSV, HTuple maxError, out HTuple OCRHandleReduced)`

`HOCRSvm HOCRSvm.ReduceOcrClassSvm(string method, int minRemainingSV, double maxError)`

## Description

`ReduceOcrClassSvm` reduces the classification time of an
SVM based OCR classifier *`OCRHandle`* by returning a reduced
copy of it in *`OCRHandleReduced`*. The parameters
*`method`*, *`minRemainingSV`* and *`maxError`* have
the same meaning as in [`ReduceClassSvm`](reduce_class_svm.md) and are described
there. Please note that classification time can also be
significantly reduced with a preprocessing step in
[`CreateOcrClassSvm`](create_ocr_class_svm.md), which possibly introduces less
errors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Original handle of SVM-based OCR-classifier.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of postprocessing to reduce number of SVs.

Default:
"bottom_up"

List of values:
"bottom_up"

**`minRemainingSV`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum number of remaining SVs.

Default:
2

Suggested values:
2, 3, 4, 5, 7, 10, 15, 20, 30, 50

Restriction:
`MinRemainingSV >= 2`

**`maxError`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum allowed error of reduction.

Default:
0.001

Suggested values:
0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05

Restriction:
`MaxError > 0.0`

**`OCRHandleReduced`** (output_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVMHandle of reduced OCR classifier.

## Result

If the parameters are valid the operator
`ReduceOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`,
`GetSupportVectorNumOcrClassSvm`

## Possible Successors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`,
`GetSupportVectorOcrClassSvm`,
`GetSupportVectorNumOcrClassSvm`

## See also

`CreateOcrClassSvm`

## References

Bernhard Schölkopf, Alexander J.Smola: “Learning with Kernels”;
The MIT Press, London; 1999.

## Module

OCR/OCV

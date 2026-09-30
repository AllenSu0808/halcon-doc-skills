# DoOcrMultiClassSvm (Operator)

## Name

`DoOcrMultiClassSvm` — Classify multiple characters with an SVM-based OCR classifier.

## Signature

`static void HOperatorSet.DoOcrMultiClassSvm(HObject character, HObject image, HTuple OCRHandle, out HTuple classVal)`

`HTuple HRegion.DoOcrMultiClassSvm(HImage image, HOCRSvm OCRHandle)`

`HTuple HOCRSvm.DoOcrMultiClassSvm(HRegion character, HImage image)`

## Description

`DoOcrMultiClassSvm` computes the best class for each of
the characters given by the regions *`character`* and the gray
values *`image`* with the SVM-based OCR classifier
*`OCRHandle`* and returns the classes in *`classVal`*. In
contrast to [`DoOcrSingleClassSvm`](do_ocr_single_class_svm.md),
`DoOcrMultiClassSvm` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`DoOcrSingleClassSvm`](do_ocr_single_class_svm.md) to classify single characters.
However, `DoOcrMultiClassSvm` can only return the best
class of each character. Before calling
`DoOcrMultiClassSvm`, the classifier must be trained with
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the characters with the
SVM.

## Result

If the parameters are valid the operator
`DoOcrMultiClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`,
`ReadOcrClassSvm`

## Alternatives

`DoOcrSingleClassSvm`

## See also

`CreateOcrClassSvm`,
`ClassifyClassSvm`

## Module

OCR/OCV

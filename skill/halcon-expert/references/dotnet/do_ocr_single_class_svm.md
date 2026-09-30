# DoOcrSingleClassSvm (Operator)

## Name

`DoOcrSingleClassSvm` — Classify a single character with an SVM-based OCR classifier.

## Signature

`static void HOperatorSet.DoOcrSingleClassSvm(HObject character, HObject image, HTuple OCRHandle, HTuple num, out HTuple classVal)`

`HTuple HRegion.DoOcrSingleClassSvm(HImage image, HOCRSvm OCRHandle, HTuple num)`

`HTuple HOCRSvm.DoOcrSingleClassSvm(HRegion character, HImage image, HTuple num)`

## Description

`DoOcrSingleClassSvm` computes the best *`num`*
classes of the character given by the region *`character`* and
the gray values *`image`* with the OCR classifier
*`OCRHandle`* and returns the classes in *`classVal`*.
Because multiple classes may be returned by
`DoOcrSingleClassSvm`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`DoOcrMultiClassSvm`](do_ocr_multi_class_svm.md) must
be used. Before calling `DoOcrSingleClassSvm`, the
classifier must be trained with [`TrainfOcrClassSvm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` [HRegion](HRegion.md)

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the character with the
SVM.

## Result

If the parameters are valid the operator
`DoOcrSingleClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`,
`ReadOcrClassSvm`

## Alternatives

`DoOcrMultiClassSvm`

## See also

`CreateOcrClassSvm`,
`ClassifyClassSvm`

## Module

OCR/OCV

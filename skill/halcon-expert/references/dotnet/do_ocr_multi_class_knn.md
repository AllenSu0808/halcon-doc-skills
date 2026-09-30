# DoOcrMultiClassKnn (Operator)

## Name

`DoOcrMultiClassKnn` — Classify multiple characters with an k-NN classifier.

## Signature

`static void HOperatorSet.DoOcrMultiClassKnn(HObject character, HObject image, HTuple OCRHandle, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrMultiClassKnn(HImage image, HOCRKnn OCRHandle, out HTuple confidence)`

`string HRegion.DoOcrMultiClassKnn(HImage image, HOCRKnn OCRHandle, out double confidence)`

`HTuple HOCRKnn.DoOcrMultiClassKnn(HRegion character, HImage image, out HTuple confidence)`

`string HOCRKnn.DoOcrMultiClassKnn(HRegion character, HImage image, out double confidence)`

## Description

`DoOcrMultiClassKnn` computes the best class for each of
the characters given by the regions *`character`* and the gray
values *`image`* with the k-NN classifier *`OCRHandle`* and
returns the classes in *`classVal`* and the corresponding
confidence of the classes in *`confidence`*.
The confidences lie between 0.0 and 1.0. The larger the value, the
more reliable is the classification of the single characters.
In contrast to [`DoOcrSingleClassKnn`](do_ocr_single_class_knn.md),
`DoOcrMultiClassKnn` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`DoOcrSingleClassKnn`](do_ocr_single_class_knn.md) to classify single characters.
However, `DoOcrMultiClassKnn` can only return the best
class of each character.

Before calling `DoOcrMultiClassKnn`, the classifier must be
trained with [`TrainfOcrClassKnn`](trainf_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the characters with the
k-NN.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`DoOcrMultiClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`,
`ReadOcrClassKnn`

## Alternatives

`DoOcrSingleClassKnn`

## See also

`CreateOcrClassKnn`,
`ClassifyClassKnn`

## Module

OCR/OCV

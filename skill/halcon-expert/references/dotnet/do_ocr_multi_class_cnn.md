# DoOcrMultiClassCnn (Operator)

## Name

`DoOcrMultiClassCnn` — Classify multiple characters with an CNN-based OCR classifier.

## Signature

`static void HOperatorSet.DoOcrMultiClassCnn(HObject character, HObject image, HTuple OCRHandle, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrMultiClassCnn(HImage image, HOCRCnn OCRHandle, out HTuple confidence)`

`string HRegion.DoOcrMultiClassCnn(HImage image, HOCRCnn OCRHandle, out double confidence)`

`HTuple HOCRCnn.DoOcrMultiClassCnn(HRegion character, HImage image, out HTuple confidence)`

`string HOCRCnn.DoOcrMultiClassCnn(HRegion character, HImage image, out double confidence)`

## Description

`DoOcrMultiClassCnn` computes the best class for each of
the characters given by the regions *`character`* and the gray
values *`image`* with the OCR classifier *`OCRHandle`* and
returns the classes in *`classVal`* and the corresponding
confidences (probabilities) of the classes in *`confidence`*.

In contrast to [`DoOcrSingleClassCnn`](do_ocr_single_class_cnn.md),
`DoOcrMultiClassCnn` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`DoOcrSingleClassCnn`](do_ocr_single_class_cnn.md) to classify single characters.
However, `DoOcrMultiClassCnn` can only return the best
class of each character. Because the confidences can be interpreted as
probabilities, it is easier to check whether a character has been
classified with too much uncertainty. This is usually not a disadvantage,
except in cases where the classes overlap so much that in many cases the
second best class must be examined to be able to decide the class of the
character. In these cases, [`DoOcrSingleClassCnn`](do_ocr_single_class_cnn.md) should be used.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`classVal`* signifies that the region has been classified as rejection
class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the characters with the
CNN.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`DoOcrMultiClassCnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadOcrClassCnn`

## Alternatives

`DoOcrWordCnn`,
`DoOcrSingleClassCnn`

## Module

OCR/OCV

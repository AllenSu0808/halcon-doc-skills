# DoOcrMultiClassMlp (Operator)

## Name

`DoOcrMultiClassMlp` — Classify multiple characters with an OCR classifier.

## Signature

`static void HOperatorSet.DoOcrMultiClassMlp(HObject character, HObject image, HTuple OCRHandle, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrMultiClassMlp(HImage image, HOCRMlp OCRHandle, out HTuple confidence)`

`string HRegion.DoOcrMultiClassMlp(HImage image, HOCRMlp OCRHandle, out double confidence)`

`HTuple HOCRMlp.DoOcrMultiClassMlp(HRegion character, HImage image, out HTuple confidence)`

`string HOCRMlp.DoOcrMultiClassMlp(HRegion character, HImage image, out double confidence)`

## Description

`DoOcrMultiClassMlp` computes the best class for each of
the characters given by the regions *`character`* and the gray
values *`image`* with the OCR classifier *`OCRHandle`* and
returns the classes in *`classVal`* and the corresponding
confidences (probabilities) of the classes in *`confidence`*.
In contrast to [`DoOcrSingleClassMlp`](do_ocr_single_class_mlp.md),
`DoOcrMultiClassMlp` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`DoOcrSingleClassMlp`](do_ocr_single_class_mlp.md) to classify single characters.
However, `DoOcrMultiClassMlp` can only return the best
class of each character. Because the confidences can be interpreted
as probabilities (see [`ClassifyClassMlp`](classify_class_mlp.md) and
[`EvaluateClassMlp`](evaluate_class_mlp.md)), and it is therefore easy to check
whether a character has been classified with too much uncertainty,
this is usually not a disadvantage, except in cases where the
classes overlap so much that in many cases the second best class
must be examined to be able to decide the class of the character.
In these cases, [`DoOcrSingleClassMlp`](do_ocr_single_class_mlp.md) should be used.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`classVal`* signifies that the region has been classified as rejection
class.

Before calling `DoOcrMultiClassMlp`, the classifier must be
trained with [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the characters with the
MLP.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`DoOcrMultiClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassMlp`,
`ReadOcrClassMlp`

## Alternatives

`DoOcrWordMlp`,
`DoOcrSingleClassMlp`

## See also

`CreateOcrClassMlp`,
`ClassifyClassMlp`

## Module

OCR/OCV

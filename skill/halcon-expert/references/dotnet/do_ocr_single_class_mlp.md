# DoOcrSingleClassMlp (Operator)

## Name

`DoOcrSingleClassMlp` — Classify a single character with an OCR classifier.

## Signature

`static void HOperatorSet.DoOcrSingleClassMlp(HObject character, HObject image, HTuple OCRHandle, HTuple num, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrSingleClassMlp(HImage image, HOCRMlp OCRHandle, HTuple num, out HTuple confidence)`

`string HRegion.DoOcrSingleClassMlp(HImage image, HOCRMlp OCRHandle, HTuple num, out double confidence)`

`HTuple HOCRMlp.DoOcrSingleClassMlp(HRegion character, HImage image, HTuple num, out HTuple confidence)`

`string HOCRMlp.DoOcrSingleClassMlp(HRegion character, HImage image, HTuple num, out double confidence)`

## Description

`DoOcrSingleClassMlp` computes the best *`num`*
classes of the character given by the region *`character`* and
the gray values *`image`* with the OCR classifier
*`OCRHandle`* and returns the classes in *`classVal`* and the
corresponding confidences (probabilities) of the classes in
*`confidence`*. Because multiple classes may be returned by
`DoOcrSingleClassMlp`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`DoOcrMultiClassMlp`](do_ocr_multi_class_mlp.md) must
be used. Because [`DoOcrMultiClassMlp`](do_ocr_multi_class_mlp.md) typically is faster
than a loop with `DoOcrSingleClassMlp` and because the
confidences can be interpreted as probabilities (see
[`ClassifyClassMlp`](classify_class_mlp.md) and [`EvaluateClassMlp`](evaluate_class_mlp.md)), and it
is therefore easy to check whether a character has been classified
with too much uncertainty, in most cases
[`DoOcrMultiClassMlp`](do_ocr_multi_class_mlp.md) should be used, unless the
second-best class should be examined explicitly.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`classVal`* signifies that the region has been classified as rejection
class.

Before calling `DoOcrSingleClassMlp`, the classifier must be
trained with [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` [HRegion](HRegion.md)

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the character with the
MLP.

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence(s) of the class(es) of the character.

## Result

If the parameters are valid, the operator
`DoOcrSingleClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassMlp`,
`ReadOcrClassMlp`

## Alternatives

`DoOcrMultiClassMlp`

## See also

`CreateOcrClassMlp`,
`ClassifyClassMlp`

## Module

OCR/OCV

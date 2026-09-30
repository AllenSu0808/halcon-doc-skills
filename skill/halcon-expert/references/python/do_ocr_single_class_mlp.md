# do_ocr_single_class_mlp (Operator)

## Name

`do_ocr_single_class_mlp` — Classify a single character with an OCR classifier.

## Signature

`def do_ocr_single_class_mlp(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> Tuple[Sequence[str], Sequence[float]]`

`def do_ocr_single_class_mlp_s(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> Tuple[str, float]`

## Description

`do_ocr_single_class_mlp` computes the best *`num`*
classes of the character given by the region *`character`* and
the gray values *`image`* with the OCR classifier
*`ocrhandle`* and returns the classes in *`class`* and the
corresponding confidences (probabilities) of the classes in
*`confidence`*. Because multiple classes may be returned by
`do_ocr_single_class_mlp`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_mlp`](do_ocr_multi_class_mlp.md) must
be used. Because [`do_ocr_multi_class_mlp`](do_ocr_multi_class_mlp.md) typically is faster
than a loop with `do_ocr_single_class_mlp` and because the
confidences can be interpreted as probabilities (see
[`classify_class_mlp`](classify_class_mlp.md) and [`evaluate_class_mlp`](evaluate_class_mlp.md)), and it
is therefore easy to check whether a character has been classified
with too much uncertainty, in most cases
[`do_ocr_multi_class_mlp`](do_ocr_multi_class_mlp.md) should be used, unless the
second-best class should be examined explicitly.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`class`* signifies that the region has been classified as rejection
class.

Before calling `do_ocr_single_class_mlp`, the classifier must be
trained with [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` HObject

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the character.

**`ocrhandle`** (input_control)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` Sequence[int]

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`class`** (output_control)  string(-array) `→` Sequence[str]

Result of classifying the character with the
MLP.

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence(s) of the class(es) of the character.

## Result

If the parameters are valid, the operator
`do_ocr_single_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_mlp`,
`read_ocr_class_mlp`

## Alternatives

`do_ocr_multi_class_mlp`

## See also

`create_ocr_class_mlp`,
`classify_class_mlp`

## Module

OCR/OCV

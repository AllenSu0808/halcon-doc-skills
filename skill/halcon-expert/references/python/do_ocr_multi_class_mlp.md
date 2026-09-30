# do_ocr_multi_class_mlp (Operator)

## Name

`do_ocr_multi_class_mlp` — Classify multiple characters with an OCR classifier.

## Signature

`def do_ocr_multi_class_mlp(character: HObject, image: HObject, ocrhandle: HHandle) -> Tuple[Sequence[str], Sequence[float]]`

`def do_ocr_multi_class_mlp_s(character: HObject, image: HObject, ocrhandle: HHandle) -> Tuple[str, float]`

## Description

`do_ocr_multi_class_mlp` computes the best class for each of
the characters given by the regions *`character`* and the gray
values *`image`* with the OCR classifier *`ocrhandle`* and
returns the classes in *`class`* and the corresponding
confidences (probabilities) of the classes in *`confidence`*.
In contrast to [`do_ocr_single_class_mlp`](do_ocr_single_class_mlp.md),
`do_ocr_multi_class_mlp` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`do_ocr_single_class_mlp`](do_ocr_single_class_mlp.md) to classify single characters.
However, `do_ocr_multi_class_mlp` can only return the best
class of each character. Because the confidences can be interpreted
as probabilities (see [`classify_class_mlp`](classify_class_mlp.md) and
[`evaluate_class_mlp`](evaluate_class_mlp.md)), and it is therefore easy to check
whether a character has been classified with too much uncertainty,
this is usually not a disadvantage, except in cases where the
classes overlap so much that in many cases the second best class
must be examined to be able to decide the class of the character.
In these cases, [`do_ocr_single_class_mlp`](do_ocr_single_class_mlp.md) should be used.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`class`* signifies that the region has been classified as rejection
class.

Before calling `do_ocr_multi_class_mlp`, the classifier must be
trained with [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` HObject

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the characters.

**`ocrhandle`** (input_control)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`class`** (output_control)  string(-array) `→` Sequence[str]

Result of classifying the characters with the
MLP.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`do_ocr_multi_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_mlp`,
`read_ocr_class_mlp`

## Alternatives

`do_ocr_word_mlp`,
`do_ocr_single_class_mlp`

## See also

`create_ocr_class_mlp`,
`classify_class_mlp`

## Module

OCR/OCV

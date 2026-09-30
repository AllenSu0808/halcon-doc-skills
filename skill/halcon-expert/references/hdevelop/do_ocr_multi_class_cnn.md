# do_ocr_multi_class_cnn (Operator)

## Name

`do_ocr_multi_class_cnn` — Classify multiple characters with an CNN-based OCR classifier.

## Signature

`do_ocr_multi_class_cnn(Character, Image : : OCRHandle : Class, Confidence)`

## Description

`do_ocr_multi_class_cnn` computes the best class for each of
the characters given by the regions *`Character`* and the gray
values *`Image`* with the OCR classifier *`OCRHandle`* and
returns the classes in *`Class`* and the corresponding
confidences (probabilities) of the classes in *`Confidence`*.

In contrast to [`do_ocr_single_class_cnn`](do_ocr_single_class_cnn.md),
`do_ocr_multi_class_cnn` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`do_ocr_single_class_cnn`](do_ocr_single_class_cnn.md) to classify single characters.
However, `do_ocr_multi_class_cnn` can only return the best
class of each character. Because the confidences can be interpreted as
probabilities, it is easier to check whether a character has been
classified with too much uncertainty. This is usually not a disadvantage,
except in cases where the classes overlap so much that in many cases the
second best class must be examined to be able to decide the class of the
character. In these cases, [`do_ocr_single_class_cnn`](do_ocr_single_class_cnn.md) should be used.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`Class`* signifies that the region has been classified as rejection
class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_cnn `→`  (handle)

Handle of the OCR classifier.

**`Class`** (output_control)  string(-array) `→`  (string)

Result of classifying the characters with the
CNN.

Number of elements:
Class == Character

**`Confidence`** (output_control)  real(-array) `→`  (real)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`do_ocr_multi_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_ocr_class_cnn`

## Alternatives

`do_ocr_word_cnn`,
`do_ocr_single_class_cnn`

## Module

OCR/OCV

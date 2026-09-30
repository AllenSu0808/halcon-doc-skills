# do_ocr_multi_class_knn (Operator)

## Name

`do_ocr_multi_class_knn` — Classify multiple characters with an k-NN classifier.

## Signature

`do_ocr_multi_class_knn(Character, Image : : OCRHandle : Class, Confidence)`

## Description

`do_ocr_multi_class_knn` computes the best class for each of
the characters given by the regions *`Character`* and the gray
values *`Image`* with the k-NN classifier *`OCRHandle`* and
returns the classes in *`Class`* and the corresponding
confidence of the classes in *`Confidence`*.
The confidences lie between 0.0 and 1.0. The larger the value, the
more reliable is the classification of the single characters.
In contrast to [`do_ocr_single_class_knn`](do_ocr_single_class_knn.md),
`do_ocr_multi_class_knn` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`do_ocr_single_class_knn`](do_ocr_single_class_knn.md) to classify single characters.
However, `do_ocr_multi_class_knn` can only return the best
class of each character.

Before calling `do_ocr_multi_class_knn`, the classifier must be
trained with [`trainf_ocr_class_knn`](trainf_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the k-NN classifier.

**`Class`** (output_control)  string(-array) `→`  (string)

Result of classifying the characters with the
k-NN.

Number of elements:
Class == Character

**`Confidence`** (output_control)  real(-array) `→`  (real)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

## Result

If the parameters are valid, the operator
`do_ocr_multi_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`,
`read_ocr_class_knn`

## Alternatives

`do_ocr_single_class_knn`

## See also

`create_ocr_class_knn`,
`classify_class_knn`

## Module

OCR/OCV

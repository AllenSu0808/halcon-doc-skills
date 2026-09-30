# do_ocr_multi_class_svm (Operator)

## Name

`do_ocr_multi_class_svm` — Classify multiple characters with an SVM-based OCR classifier.

## Signature

`do_ocr_multi_class_svm(Character, Image : : OCRHandle : Class)`

## Description

`do_ocr_multi_class_svm` computes the best class for each of
the characters given by the regions *`Character`* and the gray
values *`Image`* with the SVM-based OCR classifier
*`OCRHandle`* and returns the classes in *`Class`*. In
contrast to [`do_ocr_single_class_svm`](do_ocr_single_class_svm.md),
`do_ocr_multi_class_svm` can classify multiple characters in
one call, and therefore typically is faster than a loop that uses
[`do_ocr_single_class_svm`](do_ocr_single_class_svm.md) to classify single characters.
However, `do_ocr_multi_class_svm` can only return the best
class of each character. Before calling
`do_ocr_multi_class_svm`, the classifier must be trained with
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

**`Class`** (output_control)  string(-array) `→`  (string)

Result of classifying the characters with the
SVM.

## Result

If the parameters are valid the operator
`do_ocr_multi_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`,
`read_ocr_class_svm`

## Alternatives

`do_ocr_single_class_svm`

## See also

`create_ocr_class_svm`,
`classify_class_svm`

## Module

OCR/OCV

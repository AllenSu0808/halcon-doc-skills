# do_ocr_single_class_svm (Operator)

## Name

`do_ocr_single_class_svm` — Classify a single character with an SVM-based OCR classifier.

## Signature

`do_ocr_single_class_svm(Character, Image : : OCRHandle, Num : Class)`

## Description

`do_ocr_single_class_svm` computes the best *`Num`*
classes of the character given by the region *`Character`* and
the gray values *`Image`* with the OCR classifier
*`OCRHandle`* and returns the classes in *`Class`*.
Because multiple classes may be returned by
`do_ocr_single_class_svm`, *`Character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_svm`](do_ocr_multi_class_svm.md) must
be used. Before calling `do_ocr_single_class_svm`, the
classifier must be trained with [`trainf_ocr_class_svm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region `→` object

Character to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

**`Num`** (input_control)  integer-array `→`  (integer)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`Class`** (output_control)  string(-array) `→`  (string)

Result of classifying the character with the
SVM.

## Result

If the parameters are valid the operator
`do_ocr_single_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`,
`read_ocr_class_svm`

## Alternatives

`do_ocr_multi_class_svm`

## See also

`create_ocr_class_svm`,
`classify_class_svm`

## Module

OCR/OCV

# do_ocr_single_class_svm (Operator)

## Name

`do_ocr_single_class_svm` — Classify a single character with an SVM-based OCR classifier.

## Signature

`def do_ocr_single_class_svm(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> Sequence[str]`

`def do_ocr_single_class_svm_s(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> str`

## Description

`do_ocr_single_class_svm` computes the best *`num`*
classes of the character given by the region *`character`* and
the gray values *`image`* with the OCR classifier
*`ocrhandle`* and returns the classes in *`class`*.
Because multiple classes may be returned by
`do_ocr_single_class_svm`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_svm`](do_ocr_multi_class_svm.md) must
be used. Before calling `do_ocr_single_class_svm`, the
classifier must be trained with [`trainf_ocr_class_svm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` HObject

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the character.

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` Sequence[int]

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`class`** (output_control)  string(-array) `→` Sequence[str]

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

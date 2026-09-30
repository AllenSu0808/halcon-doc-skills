# do_ocr_single (Operator)

## Name

`do_ocr_single` — Classify one character.

## Warning

**`do_ocr_single` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`do_ocr_single(Character, Image : : OcrHandle : Classes, Confidences)`

## Description

The operator `do_ocr_single` assigns classes to the
*`Character`* (characters).
For gray value features gray values of the surrounding rectangles of the
regions will be used. The gray values will be taken from the
parameter *`Image`*. For each character the two classes
with the highest confidences will be returned in
*`Classes`*. The corresponding confidences will be
returned in *`Confidences`*. The confidence value indicates the
similarity between the input pattern and the assigned character.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region `→` object

Character to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`OcrHandle`** (input_control)  ocr_box `→`  (handle)

ID of the OCR classifier.

**`Classes`** (output_control)  string-array `→`  (string)

Classes (names) of the characters.

Number of elements:
2

**`Confidences`** (output_control)  real-array `→`  (real)

Confidence values of the characters.

Number of elements:
2

## Result

If the input parameters are correct, the operator
`do_ocr_single` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`traind_ocr_class_box`,
`trainf_ocr_class_box`,
`read_ocr`,
`connection`,
`sort_region`

## Alternatives

`do_ocr_multi`

## See also

`write_ocr`

## Module

OCR/OCV

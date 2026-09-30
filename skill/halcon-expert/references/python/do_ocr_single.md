# do_ocr_single (Operator)

## Name

`do_ocr_single` — Classify one character.

## Warning

**`do_ocr_single` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def do_ocr_single(character: HObject, image: HObject, ocr_handle: HHandle) -> Tuple[Sequence[str], Sequence[float]]`

## Description

The operator `do_ocr_single` assigns classes to the
*`character`* (characters).
For gray value features gray values of the surrounding rectangles of the
regions will be used. The gray values will be taken from the
parameter *`image`*. For each character the two classes
with the highest confidences will be returned in
*`classes`*. The corresponding confidences will be
returned in *`confidences`*. The confidence value indicates the
similarity between the input pattern and the assigned character.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` HObject

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the characters.

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the OCR classifier.

**`classes`** (output_control)  string-array `→` Sequence[str]

Classes (names) of the characters.

Number of elements:
2

**`confidences`** (output_control)  real-array `→` Sequence[float]

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

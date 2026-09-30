# do_ocr_multi (Operator)

## Name

`do_ocr_multi` — Classify characters.

## Warning

**`do_ocr_multi` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def do_ocr_multi(character: HObject, image: HObject, ocr_handle: HHandle) -> Tuple[Sequence[str], Sequence[float]]`

`def do_ocr_multi_s(character: HObject, image: HObject, ocr_handle: HHandle) -> Tuple[str, float]`

## Description

The operator `do_ocr_multi` assigns a class to every
*`character`* (character).
For gray value features the gray values from the surrounding rectangles
of the regions are used. The gray values will be taken from the parameter
*`image`*. For each character the corresponding class will be
returned in *`class`* and a confidence value will be
returned in *`confidence`*. The confidence value indicates the
similarity between the input pattern and the assigned character.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` HObject

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values for the characters.

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the OCR classifier.

**`class`** (output_control)  string(-array) `→` Sequence[str]

Class (name) of the characters.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence values of the characters.

Number of elements:
Confidence == Character

## Result

If the input parameters are correct, the operator
[`do_ocr_single`](do_ocr_single.md) returns the value 2 (
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

`do_ocr_single`

## See also

`write_ocr`

## Module

OCR/OCV

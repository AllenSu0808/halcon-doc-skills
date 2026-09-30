# do_ocr_multi (Operator)

## Name

`do_ocr_multi` — Classify characters.

## Warning

**`do_ocr_multi` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`do_ocr_multi(Character, Image : : OcrHandle : Class, Confidence)`

## Description

The operator `do_ocr_multi` assigns a class to every
*`Character`* (character).
For gray value features the gray values from the surrounding rectangles
of the regions are used. The gray values will be taken from the parameter
*`Image`*. For each character the corresponding class will be
returned in *`Class`* and a confidence value will be
returned in *`Confidence`*. The confidence value indicates the
similarity between the input pattern and the assigned character.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values for the characters.

**`OcrHandle`** (input_control)  ocr_box `→`  (handle)

ID of the OCR classifier.

**`Class`** (output_control)  string(-array) `→`  (string)

Class (name) of the characters.

Number of elements:
Class == Character

**`Confidence`** (output_control)  real(-array) `→`  (real)

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

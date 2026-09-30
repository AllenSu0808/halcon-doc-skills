# testd_ocr_class_box (Operator)

## Name

`testd_ocr_class_box` — Test an OCR classifier.

## Warning

**`testd_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def testd_ocr_class_box(character: HObject, image: HObject, ocr_handle: HHandle, class_val: MaybeSequence[str]) -> Sequence[float]`

`def testd_ocr_class_box_s(character: HObject, image: HObject, ocr_handle: HHandle, class_val: MaybeSequence[str]) -> float`

## Description

The operator `testd_ocr_class_box` tests the confidence with
which a character belongs to a given class. Any number of regions
of an image can be passed. For each character (region) in
*`character`* the corresponding name (class) *`class`*
must be specified. The gray values are passed in *`image`*.
When the operator has finished the parameter *`confidence`*
provides information about how sure a character belongs to the
(arbitrary chosen) class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` HObject

Characters to be tested.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values for the characters.

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the desired OCR-classifier.

**`class`** (input_control)  string(-array) `→` MaybeSequence[str]

Class (name) of the characters.

Default:
"a"

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence for the character to belong to the class.

## Result

If the parameters are correct, the operator
`testd_ocr_class_box` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`read_ocr`,
`trainf_ocr_class_box`,
`traind_ocr_class_box`

## Module

OCR/OCV

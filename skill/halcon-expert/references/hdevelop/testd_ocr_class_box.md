# testd_ocr_class_box (Operator)

## Name

`testd_ocr_class_box` — Test an OCR classifier.

## Warning

**`testd_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`testd_ocr_class_box(Character, Image : : OcrHandle, Class : Confidence)`

## Description

The operator `testd_ocr_class_box` tests the confidence with
which a character belongs to a given class. Any number of regions
of an image can be passed. For each character (region) in
*`Character`* the corresponding name (class) *`Class`*
must be specified. The gray values are passed in *`Image`*.
When the operator has finished the parameter *`Confidence`*
provides information about how sure a character belongs to the
(arbitrary chosen) class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be tested.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values for the characters.

**`OcrHandle`** (input_control)  ocr_box `→`  (handle)

ID of the desired OCR-classifier.

**`Class`** (input_control)  string(-array) `→`  (string)

Class (name) of the characters.

Default:
'a'

**`Confidence`** (output_control)  real(-array) `→`  (real)

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

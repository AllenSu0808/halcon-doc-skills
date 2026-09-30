# TestdOcrClassBox (Operator)

## Name

`TestdOcrClassBox` — Test an OCR classifier.

## Warning

**`TestdOcrClassBox` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.TestdOcrClassBox(HObject character, HObject image, HTuple ocrHandle, HTuple classVal, out HTuple confidence)`

`HTuple HRegion.TestdOcrClassBox(HImage image, HOCRBox ocrHandle, HTuple classVal)`

`double HRegion.TestdOcrClassBox(HImage image, HOCRBox ocrHandle, string classVal)`

`HTuple HOCRBox.TestdOcrClassBox(HRegion character, HImage image, HTuple classVal)`

`double HOCRBox.TestdOcrClassBox(HRegion character, HImage image, string classVal)`

## Description

The operator `TestdOcrClassBox` tests the confidence with
which a character belongs to a given class. Any number of regions
of an image can be passed. For each character (region) in
*`character`* the corresponding name (class) *`classVal`*
must be specified. The gray values are passed in *`image`*.
When the operator has finished the parameter *`confidence`*
provides information about how sure a character belongs to the
(arbitrary chosen) class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be tested.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values for the characters.

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the desired OCR-classifier.

**`classVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Class (name) of the characters.

Default:
"a"

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence for the character to belong to the class.

## Result

If the parameters are correct, the operator
`TestdOcrClassBox` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`ReadOcr`,
`TrainfOcrClassBox`,
`TraindOcrClassBox`

## Module

OCR/OCV

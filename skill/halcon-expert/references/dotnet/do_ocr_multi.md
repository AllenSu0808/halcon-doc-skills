# DoOcrMulti (Operator)

## Name

`DoOcrMulti` — Classify characters.

## Warning

**`DoOcrMulti` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.DoOcrMulti(HObject character, HObject image, HTuple ocrHandle, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrMulti(HImage image, HOCRBox ocrHandle, out HTuple confidence)`

`string HRegion.DoOcrMulti(HImage image, HOCRBox ocrHandle, out double confidence)`

`HTuple HOCRBox.DoOcrMulti(HRegion character, HImage image, out HTuple confidence)`

`string HOCRBox.DoOcrMulti(HRegion character, HImage image, out double confidence)`

## Description

The operator `DoOcrMulti` assigns a class to every
*`character`* (character).
For gray value features the gray values from the surrounding rectangles
of the regions are used. The gray values will be taken from the parameter
*`image`*. For each character the corresponding class will be
returned in *`classVal`* and a confidence value will be
returned in *`confidence`*. The confidence value indicates the
similarity between the input pattern and the assigned character.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values for the characters.

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Class (name) of the characters.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence values of the characters.

Number of elements:
Confidence == Character

## Result

If the input parameters are correct, the operator
[`DoOcrSingle`](do_ocr_single.md) returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`TraindOcrClassBox`,
`TrainfOcrClassBox`,
`ReadOcr`,
`Connection`,
`SortRegion`

## Alternatives

`DoOcrSingle`

## See also

`WriteOcr`

## Module

OCR/OCV

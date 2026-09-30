# DoOcrSingle (Operator)

## Name

`DoOcrSingle` — Classify one character.

## Warning

**`DoOcrSingle` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.DoOcrSingle(HObject character, HObject image, HTuple ocrHandle, out HTuple classes, out HTuple confidences)`

`HTuple HRegion.DoOcrSingle(HImage image, HOCRBox ocrHandle, out HTuple confidences)`

`HTuple HOCRBox.DoOcrSingle(HRegion character, HImage image, out HTuple confidences)`

## Description

The operator `DoOcrSingle` assigns classes to the
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

**`character`** (input_object)  region `→` [HRegion](HRegion.md)

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

**`classes`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Classes (names) of the characters.

Number of elements:
2

**`confidences`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Confidence values of the characters.

Number of elements:
2

## Result

If the input parameters are correct, the operator
`DoOcrSingle` returns the value 2 (
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

`DoOcrMulti`

## See also

`WriteOcr`

## Module

OCR/OCV

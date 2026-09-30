# TraindOcrClassBox (Operator)

## Name

`TraindOcrClassBox` — Train an OCR classifier by the input of regions.

## Warning

**`TraindOcrClassBox` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.TraindOcrClassBox(HObject character, HObject image, HTuple ocrHandle, HTuple classVal, out HTuple avgConfidence)`

`double HRegion.TraindOcrClassBox(HImage image, HOCRBox ocrHandle, HTuple classVal)`

`double HRegion.TraindOcrClassBox(HImage image, HOCRBox ocrHandle, string classVal)`

`double HOCRBox.TraindOcrClassBox(HRegion character, HImage image, HTuple classVal)`

`double HOCRBox.TraindOcrClassBox(HRegion character, HImage image, string classVal)`

## Description

The operator `TraindOcrClassBox` trains the classifier
directly via the input of regions in an image.
Any number of regions of an image can be passed.
For each character (region) in *`character`* the
corresponding name (class) *`classVal`* must be
specified. The gray values are passed in *`image`*.
When the procedure has finished the parameter *`avgConfidence`*
provides information about the success of the training: It contains
the average confidence of the trained characters measured by a
re-classification. The confidence of mismatched characters
is set to 0 (thus, the average confidence will be decreased significantly).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be trained.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values for the characters.

**`ocrHandle`** (input_control, state is modified)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the desired OCR-classifier.

**`classVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Class (name) of the characters.

Default:
"a"

**`avgConfidence`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Average confidence during a re-classification
of the trained characters.

## Result

If the parameters are correct, the operator
`TraindOcrClassBox` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`CreateOcrClassBox`,
`ReadOcr`

## Possible Successors

`WriteOcr`,
`DoOcrMulti`,
`DoOcrSingle`

## Alternatives

`TrainfOcrClassBox`

## Module

OCR/OCV

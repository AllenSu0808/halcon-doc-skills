# OcrGetFeatures (Operator)

## Name

`OcrGetFeatures` — Access the features which correspond to a character.

## Warning

**`OcrGetFeatures` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.OcrGetFeatures(HObject character, HTuple ocrHandle, out HTuple featureVector)`

`HTuple HImage.OcrGetFeatures(HOCRBox ocrHandle)`

`HTuple HOCRBox.OcrGetFeatures(HImage character)`

## Description

The operator `OcrGetFeatures` calculates the features for
the given *`character`*. The type and number of features is
determined by the classifier *`ocrHandle`*.
*`featureVector`* contains the same values which are used
inside operators like [`TraindOcrClassBox`](traind_ocr_class_box.md) or
[`TrainfOcrClassBox`](trainf_ocr_class_box.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Characters to be trained.

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the desired OCR-classifier.

**`featureVector`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

## Result

If the parameters are correct, the operator
`OcrGetFeatures` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`ReadOcr`,
`ReduceDomain`,
`Threshold`,
`Connection`

## See also

`TrainfOcrClassBox`,
`TraindOcrClassBox`

## Module

OCR/OCV

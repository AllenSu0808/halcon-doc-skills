# WriteOcrTrainf (Operator)

## Name

`WriteOcrTrainf` — Storing of training characters into a file.

## Signature

`static void HOperatorSet.WriteOcrTrainf(HObject character, HObject image, HTuple classVal, HTuple trainingFile)`

`void HRegion.WriteOcrTrainf(HImage image, HTuple classVal, string trainingFile)`

`void HRegion.WriteOcrTrainf(HImage image, string classVal, string trainingFile)`

## Description

The operator `WriteOcrTrainf` serves to prepare
the training with the operator [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md) or
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md).
Hereby regions, representing characters, including their
gray values (region and pixel) and the corresponding class name
will be written into a file. An arbitrary number of regions within one
image is supported. For each character (region) in *`character`*
the corresponding class name must be specified in *`classVal`*.
The gray values are passed via the parameter *`image`*.
If no file extension is specified in *`trainingFile`* the extension
'.trf' is appended to the file name. The version of the file format
used for writing data can be defined by the parameter
*"ocr_trainf_version"* of the operator [`SetSystem`](set_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be trained.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`classVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Class (name) of the characters.

**`trainingFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the training file.

Default:
"train_ocr"

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`WriteOcrTrainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`ReadOcrTrainf`

## Possible Successors

`TrainfOcrClassMlp`,
`TrainfOcrClassSvm`

## Module

OCR/OCV

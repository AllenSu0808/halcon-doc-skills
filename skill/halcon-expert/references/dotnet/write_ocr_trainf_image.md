# WriteOcrTrainfImage (Operator)

## Name

`WriteOcrTrainfImage` — Write characters into a training file.

## Signature

`static void HOperatorSet.WriteOcrTrainfImage(HObject character, HTuple classVal, HTuple trainingFile)`

`void HImage.WriteOcrTrainfImage(HTuple classVal, string trainingFile)`

`void HImage.WriteOcrTrainfImage(string classVal, string trainingFile)`

## Description

The operator `WriteOcrTrainfImage` is used to prepare the
training with the operator [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md) or
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md). Hereby
regions, representing characters, including their gray values (region
and pixel) and the corresponding class name will be written into a
file. An arbitrary number of regions within one image is
supported. For each character (region) in *`character`* the
corresponding class name must be specified in *`classVal`*. If no
file extension is specified in *`trainingFile`* the extension '.trf'
is appended to the file name. In contrast to
[`WriteOcrTrainf`](write_ocr_trainf.md) one image per character is passed. The
domain of this image defines the pixels which belong to the
character. The file format can be defined by the parameter
*"ocr_trainf_version"* of the operator [`SetSystem`](set_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2)

Characters to be trained.

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
`WriteOcrTrainfImage` returns the value 2 (
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

## Alternatives

`WriteOcrTrainf`,
`AppendOcrTrainf`

## Module

OCR/OCV

# write_ocr_trainf (Operator)

## Name

`write_ocr_trainf` — Storing of training characters into a file.

## Signature

`write_ocr_trainf(Character, Image : : Class, TrainingFile : )`

## Description

The operator `write_ocr_trainf` serves to prepare
the training with the operator [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md) or
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md).
Hereby regions, representing characters, including their
gray values (region and pixel) and the corresponding class name
will be written into a file. An arbitrary number of regions within one
image is supported. For each character (region) in *`Character`*
the corresponding class name must be specified in *`Class`*.
The gray values are passed via the parameter *`Image`*.
If no file extension is specified in *`TrainingFile`* the extension
'.trf' is appended to the file name. The version of the file format
used for writing data can be defined by the parameter
*'ocr_trainf_version'* of the operator [`set_system`](set_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be trained.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`Class`** (input_control)  string(-array) `→`  (string)

Class (name) of the characters.

**`TrainingFile`** (input_control)  filename.write `→`  (string)

Name of the training file.

Default:
'train_ocr'

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`write_ocr_trainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`threshold`,
`connection`,
`read_ocr_trainf`

## Possible Successors

`trainf_ocr_class_mlp`,
`trainf_ocr_class_svm`

## Module

OCR/OCV

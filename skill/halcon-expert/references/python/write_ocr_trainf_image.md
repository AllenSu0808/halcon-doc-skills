# write_ocr_trainf_image (Operator)

## Name

`write_ocr_trainf_image` — Write characters into a training file.

## Signature

`def write_ocr_trainf_image(character: HObject, class_val: MaybeSequence[str], training_file: str) -> None`

## Description

The operator `write_ocr_trainf_image` is used to prepare the
training with the operator [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md) or
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md). Hereby
regions, representing characters, including their gray values (region
and pixel) and the corresponding class name will be written into a
file. An arbitrary number of regions within one image is
supported. For each character (region) in *`character`* the
corresponding class name must be specified in *`class`*. If no
file extension is specified in *`training_file`* the extension '.trf'
is appended to the file name. In contrast to
[`write_ocr_trainf`](write_ocr_trainf.md) one image per character is passed. The
domain of this image defines the pixels which belong to the
character. The file format can be defined by the parameter
*"ocr_trainf_version"* of the operator [`set_system`](set_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2)

Characters to be trained.

**`class`** (input_control)  string(-array) `→` MaybeSequence[str]

Class (name) of the characters.

**`training_file`** (input_control)  filename.write `→` str

Name of the training file.

Default:
"train_ocr"

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`write_ocr_trainf_image` returns the value 2 (
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

## Alternatives

`write_ocr_trainf`,
`append_ocr_trainf`

## Module

OCR/OCV

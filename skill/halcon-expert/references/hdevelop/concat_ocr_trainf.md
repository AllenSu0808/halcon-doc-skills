# concat_ocr_trainf (Operator)

## Name

`concat_ocr_trainf` — Concat training files.

## Signature

`concat_ocr_trainf( : : SingleFiles, ComposedFile : )`

## Description

The operator `concat_ocr_trainf` stores all characters
which are contained in the files *`SingleFiles`* into a new file
with the name *`ComposedFile`*.
The file format can be defined by the parameter
*'ocr_trainf_version'* of the operator [`set_system`](set_system.md). If no
file extension is specified in *`ComposedFile`*, the extension '.trf'
is appended to the file name.
It is not possible to use any of the files in *`SingleFiles`* as the
new file *`ComposedFile`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SingleFiles`** (input_control)  filename.read(-array) `→`  (string)

Names of the single training files.

Default:
''

File extension:
.`trf`, .`otr`

**`ComposedFile`** (input_control)  filename.write `→`  (string)

Name of the composed training file.

Default:
'all_characters'

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`concat_ocr_trainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`write_ocr_trainf`,
`append_ocr_trainf`

## Possible Successors

`trainf_ocr_class_mlp`,
`trainf_ocr_class_svm`,
`write_ocr_trainf`

## Module

OCR/OCV

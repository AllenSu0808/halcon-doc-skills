# ConcatOcrTrainf (Operator)

## Name

`ConcatOcrTrainf` — Concat training files.

## Signature

`static void HOperatorSet.ConcatOcrTrainf(HTuple singleFiles, HTuple composedFile)`

`static void HMisc.ConcatOcrTrainf(HTuple singleFiles, string composedFile)`

`static void HMisc.ConcatOcrTrainf(string singleFiles, string composedFile)`

## Description

The operator `ConcatOcrTrainf` stores all characters
which are contained in the files *`singleFiles`* into a new file
with the name *`composedFile`*.
The file format can be defined by the parameter
*"ocr_trainf_version"* of the operator [`SetSystem`](set_system.md). If no
file extension is specified in *`composedFile`*, the extension '.trf'
is appended to the file name.
It is not possible to use any of the files in *`singleFiles`* as the
new file *`composedFile`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`singleFiles`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the single training files.

Default:
""

File extension:
.`trf`, .`otr`

**`composedFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the composed training file.

Default:
"all_characters"

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`ConcatOcrTrainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`WriteOcrTrainf`,
`AppendOcrTrainf`

## Possible Successors

`TrainfOcrClassMlp`,
`TrainfOcrClassSvm`,
`WriteOcrTrainf`

## Module

OCR/OCV

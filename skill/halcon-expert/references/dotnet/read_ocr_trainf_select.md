# ReadOcrTrainfSelect (Operator)

## Name

`ReadOcrTrainfSelect` — Read training specific characters from files and convert to images.

## Signature

`static void HOperatorSet.ReadOcrTrainfSelect(out HObject characters, HTuple trainingFile, HTuple searchNames, out HTuple foundNames)`

`HTuple HImage.ReadOcrTrainfSelect(HTuple trainingFile, HTuple searchNames)`

`string HImage.ReadOcrTrainfSelect(string trainingFile, string searchNames)`

## Description

`ReadOcrTrainfSelect` reads the characters given in
*`searchNames`* from the specified files and converts them
into images. It works similar to [`ReadOcrTrainf`](read_ocr_trainf.md) but here
the characters which are extracted can be specified.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`characters`** (output_object)  image-array `→` [HImage](HImage.md) (byte / uint2)

Images read from file.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`searchNames`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the characters to be extracted.

Default:
"0"

**`foundNames`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the read characters.

## Result

If the parameter values are correct the operator
`ReadOcrTrainfSelect` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`WriteOcrTrainf`

## Possible Successors

`DispImage`,
`SelectObj`,
`ZoomImageSize`

## Alternatives

`ReadOcrTrainf`

## Module

OCR/OCV

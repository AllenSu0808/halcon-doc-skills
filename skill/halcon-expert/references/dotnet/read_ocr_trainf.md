# ReadOcrTrainf (Operator)

## Name

`ReadOcrTrainf` — Read training characters from files and convert to images.

## Signature

`static void HOperatorSet.ReadOcrTrainf(out HObject characters, HTuple trainingFile, out HTuple characterNames)`

`HTuple HImage.ReadOcrTrainf(HTuple trainingFile)`

`HTuple HImage.ReadOcrTrainf(string trainingFile)`

## Description

`ReadOcrTrainf` reads all characters from the specified file names
and converts them into images. The default HALCON file extension for the
OCR training file is 'trf'. The domain is defined according to the
foreground of the characters (as specified in [`WriteOcrTrainf`](write_ocr_trainf.md)). The
names of the characters are returned in *`characterNames`*. If more
than one file name is given the files are processed in the order of the file
names.

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

**`characterNames`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the read characters.

## Result

If the parameter values are correct the operator
`ReadOcrTrainf` returns the value 2 (
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

`ReadOcrTrainfSelect`

## Module

OCR/OCV

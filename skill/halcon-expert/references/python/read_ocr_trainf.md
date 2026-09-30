# read_ocr_trainf (Operator)

## Name

`read_ocr_trainf` — Read training characters from files and convert to images.

## Signature

`def read_ocr_trainf(training_file: MaybeSequence[str]) -> Tuple[HObject, Sequence[str]]`

## Description

`read_ocr_trainf` reads all characters from the specified file names
and converts them into images. The default HALCON file extension for the
OCR training file is 'trf'. The domain is defined according to the
foreground of the characters (as specified in [`write_ocr_trainf`](write_ocr_trainf.md)). The
names of the characters are returned in *`character_names`*. If more
than one file name is given the files are processed in the order of the file
names.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`characters`** (output_object)  image-array `→` HObject (byte / uint2)

Images read from file.

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`character_names`** (output_control)  string-array `→` Sequence[str]

Names of the read characters.

## Result

If the parameter values are correct the operator
`read_ocr_trainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`write_ocr_trainf`

## Possible Successors

`disp_image`,
`select_obj`,
`zoom_image_size`

## Alternatives

`read_ocr_trainf_select`

## Module

OCR/OCV

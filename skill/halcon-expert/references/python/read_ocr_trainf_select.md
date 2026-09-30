# read_ocr_trainf_select (Operator)

## Name

`read_ocr_trainf_select` — Read training specific characters from files and convert to images.

## Signature

`def read_ocr_trainf_select(training_file: MaybeSequence[str], search_names: MaybeSequence[str]) -> Tuple[HObject, Sequence[str]]`

`def read_ocr_trainf_select_s(training_file: MaybeSequence[str], search_names: MaybeSequence[str]) -> Tuple[HObject, str]`

## Description

`read_ocr_trainf_select` reads the characters given in
*`search_names`* from the specified files and converts them
into images. It works similar to [`read_ocr_trainf`](read_ocr_trainf.md) but here
the characters which are extracted can be specified.

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

**`search_names`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of the characters to be extracted.

Default:
"0"

**`found_names`** (output_control)  string(-array) `→` Sequence[str]

Names of the read characters.

## Result

If the parameter values are correct the operator
`read_ocr_trainf_select` returns the value 2 (
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

`read_ocr_trainf`

## Module

OCR/OCV

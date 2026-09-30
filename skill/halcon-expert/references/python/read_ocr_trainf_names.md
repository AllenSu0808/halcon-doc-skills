# read_ocr_trainf_names (Operator)

## Name

`read_ocr_trainf_names` — Query which characters are stored in a training file.

## Signature

`def read_ocr_trainf_names(training_file: MaybeSequence[str]) -> Tuple[Sequence[str], Sequence[int]]`

`def read_ocr_trainf_names_s(training_file: MaybeSequence[str]) -> Tuple[str, int]`

## Description

`read_ocr_trainf_names` extracts the names and frequency of all
characters in the specified training files.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`character_names`** (output_control)  string(-array) `→` Sequence[str]

Names of the read characters.

**`character_count`** (output_control)  integer(-array) `→` Sequence[int]

Number of characters.

## Result

If the parameter values are correct the operator
`read_ocr_trainf_names` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`write_ocr_trainf`

## See also

`trainf_ocr_class_svm`,
`trainf_ocr_class_mlp`

## Module

OCR/OCV

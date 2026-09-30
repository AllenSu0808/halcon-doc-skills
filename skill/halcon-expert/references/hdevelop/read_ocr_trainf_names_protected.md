# read_ocr_trainf_names_protected (Operator)

## Name

`read_ocr_trainf_names_protected` — Query which characters are stored in a (protected) training file.

## Signature

`read_ocr_trainf_names_protected( : : TrainingFile, Password : CharacterNames, CharacterCount)`

## Description

`read_ocr_trainf_names_protected` extracts the names and frequency
of all characters in the specified training files. Its functionality
corresponds to the functionality of [`read_ocr_trainf_names`](read_ocr_trainf_names.md),
with the addition that `read_ocr_trainf_names_protected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`Password`*. If the number of passwords *`Password`*
equals 1, then every input file *`TrainingFile`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`read_ocr_trainf_names`](read_ocr_trainf_names.md). The concept of protecting OCR training
data in HALCON is described in [`protect_ocr_trainf`](protect_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TrainingFile`** (input_control)  filename.read(-array) `→`  (string)

Names of the training files.

Default:
''

File extension:
.`trf`, .`otr`

**`Password`** (input_control)  string(-array) `→`  (string)

Passwords for protected training files.

**`CharacterNames`** (output_control)  string(-array) `→`  (string)

Names of the read characters.

**`CharacterCount`** (output_control)  integer(-array) `→`  (integer)

Number of characters.

## Result

If the parameter values are correct the operator
`read_ocr_trainf_names_protected` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`protect_ocr_trainf`

## See also

`read_ocr_trainf_names`

## Module

OCR/OCV

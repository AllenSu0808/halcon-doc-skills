# ReadOcrTrainfNamesProtected (Operator)

## Name

`ReadOcrTrainfNamesProtected` — Query which characters are stored in a (protected) training file.

## Signature

`static void HOperatorSet.ReadOcrTrainfNamesProtected(HTuple trainingFile, HTuple password, out HTuple characterNames, out HTuple characterCount)`

`static HTuple HMisc.ReadOcrTrainfNamesProtected(HTuple trainingFile, HTuple password, out HTuple characterCount)`

`static string HMisc.ReadOcrTrainfNamesProtected(string trainingFile, string password, out int characterCount)`

## Description

`ReadOcrTrainfNamesProtected` extracts the names and frequency
of all characters in the specified training files. Its functionality
corresponds to the functionality of [`ReadOcrTrainfNames`](read_ocr_trainf_names.md),
with the addition that `ReadOcrTrainfNamesProtected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`trainingFile`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`ReadOcrTrainfNames`](read_ocr_trainf_names.md). The concept of protecting OCR training
data in HALCON is described in [`ProtectOcrTrainf`](protect_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`password`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Passwords for protected training files.

**`characterNames`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the read characters.

**`characterCount`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of characters.

## Result

If the parameter values are correct the operator
`ReadOcrTrainfNamesProtected` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`ProtectOcrTrainf`

## See also

`ReadOcrTrainfNames`

## Module

OCR/OCV

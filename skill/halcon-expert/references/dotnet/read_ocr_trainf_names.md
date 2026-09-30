# ReadOcrTrainfNames (Operator)

## Name

`ReadOcrTrainfNames` — Query which characters are stored in a training file.

## Signature

`static void HOperatorSet.ReadOcrTrainfNames(HTuple trainingFile, out HTuple characterNames, out HTuple characterCount)`

`static HTuple HMisc.ReadOcrTrainfNames(HTuple trainingFile, out HTuple characterCount)`

`static string HMisc.ReadOcrTrainfNames(string trainingFile, out int characterCount)`

## Description

`ReadOcrTrainfNames` extracts the names and frequency of all
characters in the specified training files.

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

**`characterNames`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the read characters.

**`characterCount`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of characters.

## Result

If the parameter values are correct the operator
`ReadOcrTrainfNames` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`WriteOcrTrainf`

## See also

`TrainfOcrClassSvm`,
`TrainfOcrClassMlp`

## Module

OCR/OCV

# DeleteFile (Operator)

## Name

`DeleteFile` — Delete a file.

## Signature

`static void HOperatorSet.DeleteFile(HTuple fileName)`

`static void HMisc.DeleteFile(string fileName)`

## Description

`DeleteFile` deletes the file given by *`fileName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename `→` [HTuple](HTuple.md) (*string*)

File to be deleted.

## Result

`DeleteFile` returns the value 2 (
H_MSG_TRUE)
if the file exists and
could be deleted. Otherwise, an exception is raised.

## Module

Foundation

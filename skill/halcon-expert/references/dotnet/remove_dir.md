# RemoveDir (Operator)

## Name

`RemoveDir` — Delete an empty directory.

## Signature

`static void HOperatorSet.RemoveDir(HTuple dirName)`

`static void HMisc.RemoveDir(string dirName)`

## Description

`RemoveDir` deletes the empty directory given by *`dirName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dirName`** (input_control)  filename.dir `→` [HTuple](HTuple.md) (*string*)

Name of directory to be deleted.

## Result

`RemoveDir` returns the value 2 (
H_MSG_TRUE)
if the directory
could be deleted. Otherwise, an exception is raised.

## Module

Foundation

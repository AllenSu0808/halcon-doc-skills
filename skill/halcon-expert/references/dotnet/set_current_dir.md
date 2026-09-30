# SetCurrentDir (Operator)

## Name

`SetCurrentDir` — Set the current working directory.

## Signature

`static void HOperatorSet.SetCurrentDir(HTuple dirName)`

`static void HMisc.SetCurrentDir(string dirName)`

## Description

`SetCurrentDir` sets the current working directory to the
directory *`dirName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dirName`** (input_control)  filename.dir `→` [HTuple](HTuple.md) (*string*)

Name of current working directory to be set.

## Result

`SetCurrentDir` returns the value 2 (
H_MSG_TRUE)
if the current
working directory could be set. Otherwise, an exception is raised.

## Module

Foundation

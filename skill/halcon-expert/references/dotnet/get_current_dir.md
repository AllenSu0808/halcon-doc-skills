# GetCurrentDir (Operator)

## Name

`GetCurrentDir` — Get the current working directory.

## Signature

`static void HOperatorSet.GetCurrentDir(out HTuple dirName)`

`static string HMisc.GetCurrentDir()`

## Description

`GetCurrentDir` returns the current working directory in
*`dirName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dirName`** (output_control)  filename.dir `→` [HTuple](HTuple.md) (*string*)

Name of current working directory.

## Result

`GetCurrentDir` returns the value 2 (
H_MSG_TRUE)
if the current
working directory could be determined. Otherwise, an exception is
raised.

## Module

Foundation

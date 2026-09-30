# FileExists (Operator)

## Name

`FileExists` — Check whether file exists.

## Signature

`static void HOperatorSet.FileExists(HTuple fileName, out HTuple fileExists)`

`static int HMisc.FileExists(string fileName)`

## Description

The operator `FileExists` checks whether the
indicated file already exists. If this is the case, the parameter
*`fileExists`* is set to TRUE, otherwise to FALSE.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename `→` [HTuple](HTuple.md) (*string*)

Name of file to be checked.

Default:
"/bin/cc"

**`fileExists`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Boolean number.

## Result

If the parameters are correct the operator `FileExists` returns
the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`OpenFile`

## Alternatives

`OpenFile`

## Module

Foundation

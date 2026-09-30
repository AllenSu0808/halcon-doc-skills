# CopyFile (Operator)

## Name

`CopyFile` — Copy a file to a new location.

## Signature

`static void HOperatorSet.CopyFile(HTuple sourceFile, HTuple destinationFile)`

`static void HMisc.CopyFile(string sourceFile, string destinationFile)`

## Description

`CopyFile` copies *`sourceFile`* to *`destinationFile`*.
Existing files are silently overwritten. The file attributes of
*`sourceFile`* are kept.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sourceFile`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File to be copied.

**`destinationFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Target location.

## Result

`CopyFile` returns the value 2 (
H_MSG_TRUE)
if the file could be copied.
Otherwise, an exception is raised.

## Module

Foundation

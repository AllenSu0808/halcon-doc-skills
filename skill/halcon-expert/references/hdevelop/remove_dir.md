# remove_dir (Operator)

## Name

`remove_dir` — Delete an empty directory.

## Signature

`remove_dir( : : DirName : )`

## Description

`remove_dir` deletes the empty directory given by *`DirName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DirName`** (input_control)  filename.dir `→`  (string)

Name of directory to be deleted.

## Result

`remove_dir` returns the value 2 (
H_MSG_TRUE)
if the directory
could be deleted. Otherwise, an exception is raised.

## Module

Foundation

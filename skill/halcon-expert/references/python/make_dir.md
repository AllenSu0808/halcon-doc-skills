# make_dir (Operator)

## Name

`make_dir` — Make a directory.

## Signature

`def make_dir(dir_name: str) -> None`

## Description

`make_dir` creates the directory given by *`dir_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dir_name`** (input_control)  filename.dir `→` str

Name of directory to be created.

## Result

`make_dir` returns the value 2 (
H_MSG_TRUE)
if the directory
could be created. Otherwise, an exception is raised.

## Module

Foundation

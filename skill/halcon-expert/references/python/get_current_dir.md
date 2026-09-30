# get_current_dir (Operator)

## Name

`get_current_dir` — Get the current working directory.

## Signature

`def get_current_dir() -> str`

## Description

`get_current_dir` returns the current working directory in
*`dir_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dir_name`** (output_control)  filename.dir `→` str

Name of current working directory.

## Result

`get_current_dir` returns the value 2 (
H_MSG_TRUE)
if the current
working directory could be determined. Otherwise, an exception is
raised.

## Module

Foundation

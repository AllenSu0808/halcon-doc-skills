# set_current_dir (Operator)

## Name

`set_current_dir` — Set the current working directory.

## Signature

`def set_current_dir(dir_name: str) -> None`

## Description

`set_current_dir` sets the current working directory to the
directory *`dir_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dir_name`** (input_control)  filename.dir `→` str

Name of current working directory to be set.

## Result

`set_current_dir` returns the value 2 (
H_MSG_TRUE)
if the current
working directory could be set. Otherwise, an exception is raised.

## Module

Foundation

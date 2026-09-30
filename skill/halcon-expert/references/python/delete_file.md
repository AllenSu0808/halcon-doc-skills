# delete_file (Operator)

## Name

`delete_file` — Delete a file.

## Signature

`def delete_file(file_name: str) -> None`

## Description

`delete_file` deletes the file given by *`file_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_name`** (input_control)  filename `→` str

File to be deleted.

## Result

`delete_file` returns the value 2 (
H_MSG_TRUE)
if the file exists and
could be deleted. Otherwise, an exception is raised.

## Module

Foundation

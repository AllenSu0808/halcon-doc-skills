# copy_file (Operator)

## Name

`copy_file` — Copy a file to a new location.

## Signature

`def copy_file(source_file: str, destination_file: str) -> None`

## Description

`copy_file` copies *`source_file`* to *`destination_file`*.
Existing files are silently overwritten. The file attributes of
*`source_file`* are kept.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`source_file`** (input_control)  filename.read `→` str

File to be copied.

**`destination_file`** (input_control)  filename.write `→` str

Target location.

## Result

`copy_file` returns the value 2 (
H_MSG_TRUE)
if the file could be copied.
Otherwise, an exception is raised.

## Module

Foundation

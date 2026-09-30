# copy_file (Operator)

## Name

`copy_file` — Copy a file to a new location.

## Signature

`copy_file( : : SourceFile, DestinationFile : )`

## Description

`copy_file` copies *`SourceFile`* to *`DestinationFile`*.
Existing files are silently overwritten. The file attributes of
*`SourceFile`* are kept.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SourceFile`** (input_control)  filename.read `→`  (string)

File to be copied.

**`DestinationFile`** (input_control)  filename.write `→`  (string)

Target location.

## Result

`copy_file` returns the value 2 (
H_MSG_TRUE)
if the file could be copied.
Otherwise, an exception is raised.

## Module

Foundation

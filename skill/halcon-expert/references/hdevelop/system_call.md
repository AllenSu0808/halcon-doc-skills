# system_call (Operator)

## Name

`system_call` — Execute a system command.

## Signature

`system_call( : : Command : )`

## Description

The operator `system_call` executes the system command given in
*`Command`*.

On Windows operating systems, the system command can be prefixed by
*'start /b'* to avoid waiting for the started application.
On Unix-like operating systems, an interactive shell ('csh -i') will be started,
if *`Command`* contains an empty string.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Command`** (input_control)  string `→`  (string)

Command to be called by the system.

Default:
'ls'

## Result

On Windows operating systems,the operator `system_call` will always
return the value 2 (
H_MSG_TRUE)
unless there was a problem creating a new process.
On other operating systems, `system_call` will always return
the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`count_seconds`

## See also

`wait_seconds`,
`count_seconds`

## Module

Foundation

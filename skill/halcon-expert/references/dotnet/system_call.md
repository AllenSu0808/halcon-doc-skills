# SystemCall (Operator)

## Name

`SystemCall` — Execute a system command.

## Signature

`static void HOperatorSet.SystemCall(HTuple command)`

`static void HSystem.SystemCall(string command)`

## Description

The operator `SystemCall` executes the system command given in
*`command`*.

On Windows operating systems, the system command can be prefixed by
*"start /b"* to avoid waiting for the started application.
On Unix-like operating systems, an interactive shell ('csh -i') will be started,
if *`command`* contains an empty string.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`command`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Command to be called by the system.

Default:
"ls"

## Result

On Windows operating systems,the operator `SystemCall` will always
return the value 2 (
H_MSG_TRUE)
unless there was a problem creating a new process.
On other operating systems, `SystemCall` will always return
the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`CountSeconds`

## See also

`WaitSeconds`,
`CountSeconds`

## Module

Foundation

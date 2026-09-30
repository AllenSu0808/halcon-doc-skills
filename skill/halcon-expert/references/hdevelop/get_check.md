# get_check (Operator)

## Name

`get_check` — State of the HALCON control modes.

## Signature

`get_check( : : : Check)`

## Description

Executing the operator `get_check` the user can inquire what
kind of control modes are currently activated and which are not.
*`Check`* gives the tuple containing the names of the control modes
(see also [`set_check`](set_check.md)) which are preceded by a tilde
(~, e.g., '~data'),
if the corresponding control is deactivated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Check`** (output_control)  string-array `→`  (string)

Tuple of the currently activated control modes.

## Result

`get_check` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`set_check`

## See also

`set_check`

## Module

Foundation

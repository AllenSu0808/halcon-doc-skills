# get_check (Operator)

## Name

`get_check` — State of the HALCON control modes.

## Signature

`def get_check() -> Sequence[str]`

## Description

Executing the operator `get_check` the user can inquire what
kind of control modes are currently activated and which are not.
*`check`* gives the tuple containing the names of the control modes
(see also [`set_check`](set_check.md)) which are preceded by a tilde
(~, e.g., '~data'),
if the corresponding control is deactivated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`check`** (output_control)  string-array `→` Sequence[str]

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

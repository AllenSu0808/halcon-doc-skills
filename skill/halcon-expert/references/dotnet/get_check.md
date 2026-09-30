# GetCheck (Operator)

## Name

`GetCheck` — State of the HALCON control modes.

## Signature

`static void HOperatorSet.GetCheck(out HTuple check)`

`static HTuple HSystem.GetCheck()`

## Description

Executing the operator `GetCheck` the user can inquire what
kind of control modes are currently activated and which are not.
*`check`* gives the tuple containing the names of the control modes
(see also [`SetCheck`](set_check.md)) which are preceded by a tilde
(~, e.g., '~data'),
if the corresponding control is deactivated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`check`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Tuple of the currently activated control modes.

## Result

`GetCheck` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`SetCheck`

## See also

`SetCheck`

## Module

Foundation

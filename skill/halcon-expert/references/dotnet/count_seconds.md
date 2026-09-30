# CountSeconds (Operator)

## Name

`CountSeconds` — Passed Time.

## Signature

`static void HOperatorSet.CountSeconds(out HTuple seconds)`

`static double HSystem.CountSeconds()`

## Description

The operator `CountSeconds` helps to measure time. Each
operator call returns a time value. The difference of the values of
two successive calls provides the time interval in seconds.
The mode of measuring time can be set with
`set_system('clock_mode',...)`.

## Attention

The time measurement is not exact and depends on the load of the computer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`seconds`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Process time since the program start.

## Example (HDevelop)

```
count_seconds(Start)
* program segment to be measured
count_seconds(End)
Seconds := End - Start
```

## Result

The operator `CountSeconds` always returns the value 2 (
H_MSG_TRUE)
.

## See also

`SetSystem`

## Module

Foundation

# count_seconds (Operator)

## Name

`count_seconds` — Passed Time.

## Signature

`count_seconds( : : : Seconds)`

## Description

The operator `count_seconds` helps to measure time. Each
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

**`Seconds`** (output_control)  real `→`  (real)

Process time since the program start.

## Example (HDevelop)

```
count_seconds(Start)
* program segment to be measured
count_seconds(End)
Seconds := End - Start
```

## Result

The operator `count_seconds` always returns the value 2 (
H_MSG_TRUE)
.

## See also

`set_system`

## Module

Foundation

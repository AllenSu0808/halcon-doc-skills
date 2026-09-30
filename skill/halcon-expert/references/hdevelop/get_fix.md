# get_fix (Operator)

## Name

`get_fix` — Get mode of fixing of current look-up-table (lut).

## Warning

**`get_fix` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`get_fix( : : WindowHandle : Mode)`

## Description

Use `get_fix` to get mode of fixing of current look-up-table
(look-up-table of valid window) set before by [`set_fix`](set_fix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Mode`** (output_control)  string `→`  (string)

Current Mode of fixing.

## Result

`get_fix` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_fix`,
`set_pixel`,
`set_rgb`

## See also

`set_fix`

## Module

Foundation

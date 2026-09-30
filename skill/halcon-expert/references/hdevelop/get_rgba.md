# get_rgba (Operator)

## Name

`get_rgba` — Get the current color in RGBA-coding.

## Signature

`get_rgba( : : WindowHandle : Red, Green, Blue, Alpha)`

## Description

`get_rgba` returns the output colors or gray values, respectively, for
the output window. They are defined by the four color components red, green,
blue and alpha.

The values returned by `get_rgba` can be set with
[`set_rgba`](set_rgba.md).

## Attention

`get_rgba` depends on the library libcanvas, which might not be
available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Red`** (output_control)  integer-array `→`  (integer)

The current color's red value.

**`Green`** (output_control)  integer-array `→`  (integer)

The current color's green value.

**`Blue`** (output_control)  integer-array `→`  (integer)

The current color's blue value.

**`Alpha`** (output_control)  integer-array `→`  (integer)

The current color's alpha value.

## Result

`get_rgba` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_rgba`,
`disp_obj`

## See also

`set_rgba`

## Module

Foundation

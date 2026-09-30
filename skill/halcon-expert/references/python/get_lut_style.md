# get_lut_style (Operator)

## Name

`get_lut_style` — Get modification parameters of look-up-table (lut).

## Warning

**`get_lut_style` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def get_lut_style(window_handle: HHandle) -> Tuple[float, float, float]`

## Description

`get_lut_style` returns the values that were set with [`set_lut_style`](set_lut_style.md).
Default is:

- ***`hue`*:** —

  0.0
- ***`saturation`*** —

  1.0
- ***`intensity`*** —

  1.0

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`hue`** (output_control)  real `→` float

Modification of color value.

**`saturation`** (output_control)  real `→` float

Modification of saturation.

**`intensity`** (output_control)  real `→` float

Modification of intensity.

## Result

`get_lut_style` returns 2 (
H_MSG_TRUE)
if the window is valid and the parameter
is correct. Otherwise an exception is raised.

## Possible Successors

`set_lut_style`,
`set_lut`

## See also

`set_lut_style`

## Module

Foundation

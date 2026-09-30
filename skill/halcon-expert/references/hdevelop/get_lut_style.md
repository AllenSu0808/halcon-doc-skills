# get_lut_style (Operator)

## Name

`get_lut_style` — Get modification parameters of look-up-table (lut).

## Warning

**`get_lut_style` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`get_lut_style( : : WindowHandle : Hue, Saturation, Intensity)`

## Description

`get_lut_style` returns the values that were set with [`set_lut_style`](set_lut_style.md).
Default is:

- ***`Hue`*:** —

  0.0
- ***`Saturation`*** —

  1.0
- ***`Intensity`*** —

  1.0

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Hue`** (output_control)  real `→`  (real)

Modification of color value.

**`Saturation`** (output_control)  real `→`  (real)

Modification of saturation.

**`Intensity`** (output_control)  real `→`  (real)

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

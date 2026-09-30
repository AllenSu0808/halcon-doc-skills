# GetLutStyle (Operator)

## Name

`GetLutStyle` — Get modification parameters of look-up-table (lut).

## Warning

**`GetLutStyle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetLutStyle(HTuple windowHandle, out HTuple hue, out HTuple saturation, out HTuple intensity)`

`double HWindow.GetLutStyle(out double saturation, out double intensity)`

## Description

`GetLutStyle` returns the values that were set with [`SetLutStyle`](set_lut_style.md).
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`hue`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of color value.

**`saturation`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of saturation.

**`intensity`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of intensity.

## Result

`GetLutStyle` returns 2 (
H_MSG_TRUE)
if the window is valid and the parameter
is correct. Otherwise an exception is raised.

## Possible Successors

`SetLutStyle`,
`SetLut`

## See also

`SetLutStyle`

## Module

Foundation

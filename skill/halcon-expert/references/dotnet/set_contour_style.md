# SetContourStyle (Operator)

## Name

`SetContourStyle` — Define the contour display fill style.

## Signature

`static void HOperatorSet.SetContourStyle(HTuple windowHandle, HTuple style)`

`void HWindow.SetContourStyle(string style)`

## Description

`SetContourStyle` defines the fill style of contour displays.
The following values are supported for *`style`*:

- *"stroke"*:
  Only the line of the contour gets displayed.
- *"fill"*:
  The area enclosed by the contour is filled.
- *"stroke_and_fill"*:
  The line of the contour gets displayed and the enclosed area filled.
  especially makes a difference for larger line widths,
  see [`SetLineWidth`](set_line_width.md).

For all styles the current drawing color is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Fill style of contour displays.

Default:
"stroke"

List of values:
"fill", "stroke", "stroke_and_fill"

## Result

`SetContourStyle` returns 2 (
H_MSG_TRUE)
if *`style`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`GetContourStyle`

## Possible Successors

`DispXld`,
`DispObj`

## See also

`GetContourStyle`,
`DispXld`,
`SetLineWidth`,
`SetLineStyle`

## Module

Foundation

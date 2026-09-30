# set_contour_style (Operator)

## Name

`set_contour_style` — Define the contour display fill style.

## Signature

`set_contour_style( : : WindowHandle, Style : )`

## Description

`set_contour_style` defines the fill style of contour displays.
The following values are supported for *`Style`*:

- *'stroke'*:
  Only the line of the contour gets displayed.
- *'fill'*:
  The area enclosed by the contour is filled.
- *'stroke_and_fill'*:
  The line of the contour gets displayed and the enclosed area filled.
  especially makes a difference for larger line widths,
  see [`set_line_width`](set_line_width.md).

For all styles the current drawing color is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Style`** (input_control)  string `→`  (string)

Fill style of contour displays.

Default:
'stroke'

List of values:
'fill', 'stroke', 'stroke_and_fill'

## Result

`set_contour_style` returns 2 (
H_MSG_TRUE)
if *`Style`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`get_contour_style`

## Possible Successors

`disp_xld`,
`disp_obj`

## See also

`get_contour_style`,
`disp_xld`,
`set_line_width`,
`set_line_style`

## Module

Foundation

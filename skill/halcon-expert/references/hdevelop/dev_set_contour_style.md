# dev_set_contour_style (Operator)

## Name

`dev_set_contour_style` — Define the contour display fill style.

## Signature

`dev_set_contour_style( : : Style : )`

## Description

`dev_set_contour_style` defines the fill style of contour displays.
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

## Attention

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Style`** (input_control)  string `→`  (string)

Fill style for contour display.

Default:
'stroke'

List of values:
'fill', 'stroke', 'stroke_and_fill'

## Result

If the values of the specified parameters are correct,
`dev_set_contour_style` returns 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised and an error code returned.

## Possible Successors

`dev_display`

## See also

`set_contour_style`

## Module

Foundation

# dev_close_window (Operator)

## Name

`dev_close_window` — Close the active floating graphics window.

## Signature

`dev_close_window( : : : )`

## Description

`dev_close_window` closes the active floating graphics window.

The operator is equivalent to pressing the `Close` button in the
title bar of the active window or selecting the appropriate menu entry from
the `Visualization` menu.

A graphics window can be activated by calling [`dev_set_window`](dev_set_window.md) or by
pressing the `Activate` button in the tool bar of the selected
graphics window.

## Attention

This operator only works for single floating graphics windows, i.e.,
graphics windows that are neither docked nor tabbed.

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Example (HDevelop)

```
* close all windows
for i := 1 to 10 by 1
  dev_close_window ()
endfor
read_image (For5, 'for5')
get_image_size (For5, Width, Height)
dev_open_window (0, 0, Width, Height, 'black', WindowHandle)
dev_display (For5)
```

## Result

`dev_close_window` returns always 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`dev_set_window`,
`dev_open_window`

## Possible Successors

`dev_open_window`,
`dev_get_window`

## See also

`close_window`

## Module

Foundation

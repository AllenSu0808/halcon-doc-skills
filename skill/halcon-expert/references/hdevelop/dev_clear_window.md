# dev_clear_window (Operator)

## Name

`dev_clear_window` — Clear the contents of the active graphics window.

## Signature

`dev_clear_window( : : : )`

## Description

`dev_clear_window` clears the contents of the active graphics window
including the history of the displayed iconic objects.
The output parameters that have been set for this window
via the context menu, the visualization parameters dialog, or the
appropriate operators (e.g., with [`dev_set_color`](dev_set_color.md),
[`dev_set_draw`](dev_set_draw.md), etc.) remain unmodified.

The operator is equivalent to pressing the
`Clear` button of the active graphics window.

A graphics window can be activated by calling [`dev_set_window`](dev_set_window.md) or by
pressing the `Activate` button in the tool bar of the selected
graphics window.

## Attention

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
read_image (Image, 'fabrik')
regiongrowing (Image, Regions, 3, 3, 6, 100)
Number := |Regions|
dev_update_window ('off')
for i := 1 to Number by 1
  select_obj (Regions, RegionSelected, i)
  dev_clear_window ()
  dev_display (RegionSelected)
  * stop ()
endfor
```

## Result

`dev_clear_window` returns always 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`dev_set_window`,
`dev_open_window`,
`dev_display`

## Possible Successors

`dev_display`

## See also

`clear_window`

## Module

Foundation

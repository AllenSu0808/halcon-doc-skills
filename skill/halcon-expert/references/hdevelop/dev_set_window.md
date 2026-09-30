# dev_set_window (Operator)

## Name

`dev_set_window` — Activate a graphics window.

## Signature

`dev_set_window( : : WindowHandle : )`

## Description

`dev_set_window` activates the graphics window with the passed
window handle.
This is equivalent to pressing the `Active` button in the tool bar
of the graphics window.

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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
dev_open_window (1, 1, 200, 200, 'black', WindowID1)
dev_open_window (1, 220, 200, 200, 'black', WindowID2)
read_image(Image,'monkey')
dev_set_window(WindowID1)
dev_display(Image)
dev_set_window(WindowID2)
dev_display(Image)
```

## Result

If the values of the specified parameters are correct,
`dev_set_window` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_open_window`

## Possible Successors

`dev_display`

## Module

Foundation

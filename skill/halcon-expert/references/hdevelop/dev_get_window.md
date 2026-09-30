# dev_get_window (Operator)

## Name

`dev_get_window` — Return the handle of the active graphics window.

## Signature

`dev_get_window( : : : WindowHandle)`

## Description

`dev_get_window` returns the window handle of the active graphics
window.
If currently no graphics window is open, the return value is *-1*.

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

**`WindowHandle`** (output_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
read_image (Image,'mreut')
threshold (Image, Region, 100, 200)
dev_open_window (1, 1, 200, 200, 'black', WindowID1)
dev_open_window (1, 220, 200, 200, 'black', WindowID2)
dev_get_window (CurrentWindowID)
dev_set_window (WindowID1)
dev_set_color ('blue')
dev_display (Image)
dev_display (Region)
dev_set_window(CurrentWindowID)
```

## Result

If the values of the specified parameters are correct,
`dev_get_window` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_close_window`

## Possible Successors

`dev_set_window`

## Module

Foundation

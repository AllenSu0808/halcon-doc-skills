# SetIcon (Operator)

## Name

`SetIcon` — Icon definition for region output.

## Signature

`static void HOperatorSet.SetIcon(HObject icon, HTuple windowHandle)`

`void HRegion.SetIcon(HWindow windowHandle)`

`void HWindow.SetIcon(HRegion icon)`

## Description

`SetIcon` defines an icon for region output
([`DispRegion`](disp_region.md)). It is displayed
in the regions center of gravity. The use of this icon is activated
with [`SetShape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`icon`** (input_object)  region `→` [HRegion](HRegion.md)

Icon for center of gravity.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (C)

```
/* draw a region and an icon */
T_draw_region(&Region,WindowHandle);
T_draw_region(&Icon,WindowHandle);
set_icon(Icon);
create_tuple_s(&icon,"icon");
T_set_shape(WindowHandle,icon);
destroy_tuple(icon);
T_disp_region(Region,WindowHandle);
```

## Result

`SetIcon` returns 2 (
H_MSG_TRUE)
, if exactly one region is supplied.
Otherwise an exception is raised.

## Possible Predecessors

`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`DrawRegion`

## Possible Successors

`SetShape`,
`DispRegion`

## Module

Foundation

# set_icon (Operator)

## Name

`set_icon` — Icon definition for region output.

## Signature

`def set_icon(icon: HObject, window_handle: HHandle) -> None`

## Description

`set_icon` defines an icon for region output
([`disp_region`](disp_region.md)). It is displayed
in the regions center of gravity. The use of this icon is activated
with [`set_shape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`icon`** (input_object)  region `→` HObject

Icon for center of gravity.

**`window_handle`** (input_control)  window `→` HHandle

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

`set_icon` returns 2 (
H_MSG_TRUE)
, if exactly one region is supplied.
Otherwise an exception is raised.

## Possible Predecessors

`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`draw_region`

## Possible Successors

`set_shape`,
`disp_region`

## Module

Foundation

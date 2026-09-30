# get_icon (Operator)

## Name

`get_icon` — Query the icon for region output

## Signature

`def get_icon(window_handle: HHandle) -> HObject`

## Description

`get_icon` queries the icon that was set with
[`set_icon`](set_icon.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`icon`** (output_object)  region `→` HObject

Icon for the regions center of gravity.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## Example (C)

```
/* draw a region and an icon.  */
/* set it and get it again.    */
T_draw_region(&Region,WindowHandle);
T_draw_region(&Icon,WindowHandle);
set_icon(Icon);
create_tuple_s(&icon,"icon");
T_set_shape(WindowHandle,icon);
destroy_tuple(icon);
T_disp_region(Region,WindowHandle);
get_icon(&OldIcon);
T_disp_region(OldIcon,WindowHandle);
```

## Result

`get_icon` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`set_icon`

## Possible Successors

`disp_region`

## Module

Foundation

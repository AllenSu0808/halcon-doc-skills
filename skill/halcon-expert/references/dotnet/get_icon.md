# GetIcon (Operator)

## Name

`GetIcon` — Query the icon for region output

## Signature

`static void HOperatorSet.GetIcon(out HObject icon, HTuple windowHandle)`

`void HRegion.GetIcon(HWindow windowHandle)`

`HRegion HWindow.GetIcon()`

## Description

`GetIcon` queries the icon that was set with
[`SetIcon`](set_icon.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`icon`** (output_object)  region `→` [HRegion](HRegion.md)

Icon for the regions center of gravity.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

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

`GetIcon` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`SetIcon`

## Possible Successors

`DispRegion`

## Module

Foundation

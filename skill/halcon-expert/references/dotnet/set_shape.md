# SetShape (Operator)

## Name

`SetShape` — Define the region output shape.

## Signature

`static void HOperatorSet.SetShape(HTuple windowHandle, HTuple shape)`

`void HWindow.SetShape(string shape)`

## Description

`SetShape` defines the shape for region output. It is
only valid for the window with the logical window number
*`windowHandle`*. The output shape is used by
[`DispRegion`](disp_region.md). The available shapes can be queried with
[`QueryShape`](query_shape.md).

Available modes:

- ***"original"*:** —

  The shape is displayed unchanged. Nevertheless
  modifications via parameters like [`SetLineWidth`](set_line_width.md)
  can take place. This is also true for
  all other modes.
- ***"outer_circle"*:** —

  Each region is displayed by the smallest surrounding
  circle. (See [`SmallestCircle`](smallest_circle.md).)
- ***"inner_circle"*:** —

  Each region is displayed by the largest included
  circle. (See [`InnerCircle`](inner_circle.md).)
- ***"ellipse"*:** —

  Each region is displayed by an ellipse with the same
  moments and orientation (See [`EllipticAxis`](elliptic_axis.md).)
- ***"rectangle1"*:** —

  Each region is displayed by the smallest surrounding
  rectangle parallel to the coordinate axes. (See
  [`SmallestRectangle1`](smallest_rectangle1.md).)
- ***"rectangle2"*:** —

  Each region is displayed by the smallest surrounding
  rectangle. (See [`SmallestRectangle2`](smallest_rectangle2.md).)
- ***"convex"*:** —

  Each region is displayed by its convex hull (See
  [`Convexity`](convexity.md).)
- ***"icon"*:** —

  Each region is displayed by the icon set with
  [`SetIcon`](set_icon.md) in the center of gravity.

## Attention

Caution is advised for gray value output operators with output
parameter settings that use region output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`shape`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Region output mode.

Default:
"original"

List of values:
"convex", "ellipse", "icon", "inner_circle", "original", "outer_circle", "rectangle1", "rectangle2"

## Example (HDevelop)

```
read_image(Image,'fabrik')
regiongrowing(Image,Seg,5,5,6,100)
set_colored(WindowHandle,12)
set_shape(WindowHandle,'rectangle2')
disp_region(Seg,WindowHandle)
```

## Result

`SetShape` returns 2 (
H_MSG_TRUE)
if the parameter is correct and
the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`SetIcon`,
`QueryShape`,
`GetShape`

## Possible Successors

`DispRegion`

## See also

`GetShape`,
`QueryShape`,
`DispRegion`

## Module

Foundation

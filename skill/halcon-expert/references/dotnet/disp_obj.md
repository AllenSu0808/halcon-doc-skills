# DispObj (Operator)

## Name

`DispObj` — Displays image objects (image, region, XLD).

## Signature

`static void HOperatorSet.DispObj(HObject objectVal, HTuple windowHandle)`

`void HObject.DispObj(HWindow windowHandle)`

`void HWindow.DispObj(HObject objectVal)`

## Description

`DispObj` displays objects depending of their kind.
`DispObj` is equivalent to [`DispImage`](disp_image.md)
for one channel images, equivalent to [`DispColor`](disp_color.md)
for three channel images, equivalent to [`DispRegion`](disp_region.md)
for regions and equivalent to [`DispXld`](disp_xld.md) for XLDs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (input_object)  object(-array) `→` [HObject](HObject.md)

Image object to be displayed.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
* Output of a gray image:
read_image(Image1,'monkey')
disp_obj(Image1,WindowHandle)
threshold(Image,Region,0,128)
disp_obj(Region,WindowHandle)
```

## Result

If the used object is valid and a correct
output mode is set, `DispObj` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`,
`ScaleImage`,
`ConvertImageType`,
`MinMaxGray`

## Alternatives

`DispColor`,
`DispImage`,
`DispXld`,
`DispRegion`

## See also

`OpenWindow`,
`ResetObjDb`,
`SetPaint`,
`SetLut`,
`PaintGray`,
`ScaleImage`,
`ConvertImageType`,
`DumpWindow`

## Module

Foundation

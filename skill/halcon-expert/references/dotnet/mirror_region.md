# MirrorRegion (Operator)

## Name

`MirrorRegion` — Reflect a region about an axis.

## Signature

`static void HOperatorSet.MirrorRegion(HObject region, out HObject regionMirror, HTuple mode, HTuple widthHeight)`

`HRegion HRegion.MirrorRegion(string mode, int widthHeight)`

## Description

`MirrorRegion` reflects a region about one of three possible
axes. If *`mode`* is set to *"row"*, it is reflected
about the horizontal axis, if *`mode`* is set to
*"column"*, about the vertical axis, and if *`mode`* is
set to *"diagonal"*, about the main diagonal x=y.

For *`mode`* = *"row"* or *"column"* the
parameter *`widthHeight`* specifies two times the coordinate
of the axis of symmetry. Hence, if *`region`* has been
extracted from an image and should be mirrored in a way such as if
it had been extracted from a mirrored version of this image,
*`widthHeight`* corresponds to one of the dimensions of this
image (according to *`mode`*). If *`mode`* =
*"diagonal"*, the parameter *`widthHeight`* is not
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be reflected.

**`regionMirror`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Reflected region(s).

Number of elements:
RegionMirror == Region

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Axis of symmetry.

Default:
"row"

List of values:
"column", "diagonal", "row"

**`widthHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Twice the coordinate of the axis of symmetry.

Default:
512

Suggested values:
128, 256, 512, 525, 768, 1024

Value range:
`1
≤
widthHeight
≤
1024` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`WidthHeight > 0`

## Example (C)

```
read_image(&Image,"monkey");
threshold(Image,&Seg,128.0,255.0);
mirror_region(Seg,&Mirror,"row",512);
disp_region(Mirror,WindowHandle);
```

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## Alternatives

`HomMat2dReflect`,
`AffineTransRegion`

## See also

`ZoomRegion`

## Module

Foundation

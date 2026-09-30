# mirror_region (Operator)

## Name

`mirror_region` — Reflect a region about an axis.

## Signature

`def mirror_region(region: HObject, mode: str, width_height: int) -> HObject`

## Description

`mirror_region` reflects a region about one of three possible
axes. If *`mode`* is set to *"row"*, it is reflected
about the horizontal axis, if *`mode`* is set to
*"column"*, about the vertical axis, and if *`mode`* is
set to *"diagonal"*, about the main diagonal x=y.

For *`mode`* = *"row"* or *"column"* the
parameter *`width_height`* specifies two times the coordinate
of the axis of symmetry. Hence, if *`region`* has been
extracted from an image and should be mirrored in a way such as if
it had been extracted from a mirrored version of this image,
*`width_height`* corresponds to one of the dimensions of this
image (according to *`mode`*). If *`mode`* =
*"diagonal"*, the parameter *`width_height`* is not
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region(s) to be reflected.

**`region_mirror`** (output_object)  region(-array) `→` HObject

Reflected region(s).

Number of elements:
RegionMirror == Region

**`mode`** (input_control)  string `→` str

Axis of symmetry.

Default:
"row"

List of values:
"column", "diagonal", "row"

**`width_height`** (input_control)  integer `→` int

Twice the coordinate of the axis of symmetry.

Default:
512

Suggested values:
128, 256, 512, 525, 768, 1024

Value range:
`1
≤
width_height
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

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`hom_mat2d_reflect`,
`affine_trans_region`

## See also

`zoom_region`

## Module

Foundation

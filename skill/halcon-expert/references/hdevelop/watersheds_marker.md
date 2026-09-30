# watersheds_marker (Operator)

## Name

`watersheds_marker` — Extract watersheds and combine basins based on markers.

## Signature

`watersheds_marker(Image, Markers : Basins : : )`

## Description

`watersheds_marker` segments an image based on the topology of
the gray values and returns the resulting regions in *`Basins`*.
The image is interpreted as a “mountain range”.
Higher gray values correspond to “mountains”, while lower gray
values correspond to “valleys”.
The image, interpreted in this particular way, is flooded, starting with the
regions defined in *`Markers`*, until the entire image is filled.
Thus, each pixel is assigned to the marker to which it has the path
with the lowest maximum height.
If this is the case for multiple markers, the pixel is assigned to either
of them.

The resulting basins, one per input region in *`Markers`*, are returned
in *`Basins`*. Note that some of those regions might be empty.
This can happen if, for example, two marker regions are in the same
watershed basin. If a pixel is contained in multiple marker regions, only
the last marker region is used as seed for that pixel. It is advised that
the marker regions do not overlap.

The flooding is performed only for the domain of *`Image`*.
Parts of the marker regions outside the domain of *`Image`* are ignored.

It is advisable to apply a smoothing operator (e.g.,
[`binomial_filter`](binomial_filter.md) or [`gauss_filter`](gauss_filter.md)) to the input image
before calling `watersheds_marker`.
To segment an image, it is also often reasonable to run an edge extractor
(such as [`edges_image`](edges_image.md) or [`edges_color`](edges_color.md)) on the image,
and pass the resulting amplitude image to `watersheds_marker`.

## Attention

If the image contains many fine structures or is noisy, many watershed
regions need to be processed internally, and thus the runtime increases
considerably.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Input image.

**`Markers`** (input_object)  region-array `→` object

Initial markers from which to flood the image.

**`Basins`** (output_object)  region-array `→` object

Basins for all markers.

## Example (HDevelop)

```
read_image (Image, 'printer_chip/printer_chip_01')
edges_image (Image, ImaAmp, ImaDir, 'canny', 1, 'nms', 20, 40)

* Compute background marker
full_domain (ImaAmp, ImageFull)
erosion_circle (Image, RegionErosion, 2.5)
difference (Image, RegionErosion, Boundary)

* Compute foreground markers
threshold (Image, Region, 200, 255)
erosion_circle (Region, RegionErosion1, 7.5)
connection (RegionErosion1, ConnectedRegions)
select_shape (ConnectedRegions, SelectedRegions, 'area', 'and', 1500, 99999)

* Apply marker-based watersheds
concat_obj (Boundary, SelectedRegions, MarkerRegions)
watersheds_marker (ImageFull, MarkerRegions, Basins)

* Display results
dev_display (Image)
dev_set_color (['#FF000055', '#00FF0055', '#0000FF55', '#FF00FF55', \
                '#FFFF0055', '#00FFFF55', '#80FF0055', '#0080FF55'])
dev_display (MarkerRegions)
dev_set_draw ('fill')
dev_display (Basins)
```

## Result

If all input parameters are valid, `watersheds_marker` returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`invert_image`,
`edges_image`

## Possible Successors

`expand_region`,
`select_shape`,
`reduce_domain`,
`opening`

## Alternatives

`watersheds`,
`pouring`,
`watersheds_threshold`

## Module

Foundation

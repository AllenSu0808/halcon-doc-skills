# Illuminate (Operator)

## Name

`Illuminate` — Illuminate image.

## Signature

`static void HOperatorSet.Illuminate(HObject image, out HObject imageIlluminate, HTuple maskWidth, HTuple maskHeight, HTuple factor)`

`HImage HImage.Illuminate(int maskWidth, int maskHeight, double factor)`

## Description

The operator `Illuminate` enhances contrast. Very dark parts of
the image are “illuminated” more strongly, very light ones are
“darkened”. If orig is the original gray value and mean is
the corresponding gray value of the low pass filtered image detected
via the operators [`MeanImage`](mean_image.md) and filter size
*`maskHeight`* x *`maskWidth`*. For byte-images val equals 127,
for int2-images and uint2-images val equals the median value.
The resulting gray value is new:
new = round ( (val - mean) * Factor + orig ).
The low pass should have rather large dimensions (30 x 30 to
200 x 200). Reasonable parameter combinations might be:
Height Width Factor
---------------------
40 40 0.55
100 100 0.7
150 150 0.8
i.e. the larger the low pass mask is chosen, the larger
*`factor`* should be as well.

The following “spotlight effect” should be noted: If, for example,
a dark object is in front of a light wall the object as well as the wall,
which is already light in the immediate proximity of the object contours,
are lightened by the operator `Illuminate`. This corresponds
roughly to the effect that is produced when the object is illuminated by a
strong spotlight. The same applies to light objects in front of a darker
background. In this case, however, the fictitious “spotlight” darkens
objects.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Image to be enhanced.

**`imageIlluminate`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

“Illuminated” image.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of low pass mask.

Default:
101

Suggested values:
31, 41, 51, 71, 101, 121, 151, 201

Minimum increment:
2

Recommended increment:
10

Restriction:
`MaskWidth < width(Image) * 2`

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of low pass mask.

Default:
101

Suggested values:
31, 41, 51, 71, 101, 121, 151, 201

Minimum increment:
2

Recommended increment:
10

Restriction:
`MaskHeight < height(Image) * 2`

**`factor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Scales the “correction gray value” added to the
original gray values.

Default:
0.7

Suggested values:
0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0

Value range:
`0.0
≤
factor`

Minimum increment:
0.01

Recommended increment:
0.2

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display (Image)
illuminate(Image,Better,40,40,0.55)
dev_display (Better)
```

## Result

If the parameter values are correct the operator `Illuminate`
returns the value 2 (
H_MSG_TRUE)
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`DispImage`

## Alternatives

`ScaleImageMax`,
`EquHistoImage`,
`EquHistoImageRect`,
`MeanImage`,
`SubImage`

## See also

`Emphasize`,
`GrayHisto`

## Module

Foundation

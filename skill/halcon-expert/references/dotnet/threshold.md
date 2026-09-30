# Threshold (Operator)

## Name

`Threshold` — Segment an image using global threshold.

## Signature

`static void HOperatorSet.Threshold(HObject image, out HObject region, HTuple minGray, HTuple maxGray)`

`HRegion HImage.Threshold(HTuple minGray, HTuple maxGray)`

`HRegion HImage.Threshold(double minGray, double maxGray)`

## Description

`Threshold` selects the pixels from the input image
whose gray values g fulfill the following condition:
$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$

All points of an image fulfilling the condition are returned as one
region. If more than one gray value interval is passed (tuples for
*`minGray`* and *`maxGray`*), one separate region is
returned for each interval. For vector field images, the threshold is
not applied to gray values but to the lengths of the vectors.
The parameters *`minGray`* and *`maxGray`* can be set to
*"min"* or *"max"* in order to leave bottom and top limits,
respectively, open.

## Attention

The usage of *`minGray`* and *`maxGray`* can be affected by the
input image type.

For images of type integer, floating point values in *`minGray`* and
*`maxGray`* are truncated. For images of type real or vector
field, floating point precision will be used for *`minGray`* and
*`maxGray`*, if they are of type double.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / vector_field)

Input image.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented region.

**`minGray`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Lower threshold for the gray values or *"min"*.

Default:
128.0

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0, "min"

**`maxGray`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Upper threshold for the gray values or *"max"*.

Default:
255.0

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0, "max"

Restriction:
`MaxGray >= MinGray`

## Example (HDevelop)

```
read_image(Image,'fabrik')
sobel_dir(Image,EdgeAmp,EdgeDir,'sum_abs',3)
threshold(EdgeAmp,Seg,50,255)
skeleton(Seg,Rand)
connection(Rand,Lines)
select_shape(Lines,Edges,'area','and',10,1000000)
```

## Complexity

Let A be the area of the input region. Then the runtime
complexity is O(A).

## Result

`Threshold` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions
can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`HistoToThresh`,
`MinMaxGray`,
`SobelAmp`,
`BinomialFilter`,
`GaussFilter`,
`ReduceDomain`,
`FillInterlace`

## Possible Successors

`Connection`,
`Dilation1`,
`Erosion1`,
`Opening`,
`Closing`,
`RankRegion`,
`ShapeTrans`,
`Skeleton`

## Alternatives

`Class2dimSup`,
`HysteresisThreshold`,
`DynThreshold`,
`BinaryThreshold`,
`CharThreshold`,
`AutoThreshold`,
`DualThreshold`

## See also

`ZeroCrossing`,
`BackgroundSeg`,
`Regiongrowing`

## Module

Foundation

# DeviationImage (Operator)

## Name

`DeviationImage` — Calculate the standard deviation of gray values within rectangular windows.

## Signature

`static void HOperatorSet.DeviationImage(HObject image, out HObject imageDeviation, HTuple width, HTuple height)`

`HImage HImage.DeviationImage(int width, int height)`

## Description

`DeviationImage` calculates the standard deviation of gray
values in the image *`image`* within a rectangular mask of size
(*`height`*, *`width`*). The resulting image is returned
in *`imageDeviation`*. To better use the range of gray values
available in the output image, the result is multiplied by 2. If
the parameters *`height`* and *`width`* are even, they are
changed to the next larger odd value. At the image borders the gray
values are mirrored.

## Attention

`DeviationImage` can be executed on OpenCL devices. As the same OpenCL
code is used, the same limitations as for [`MeanImage`](mean_image.md) apply. Since
`DeviationImage` uses single precision floating point arithmetic
internally, the results may differ slightly from the CPU version.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int4* / real* / int2* / uint2*) **allowed for compute devices*

Image for which the standard deviation is to be
calculated.

**`imageDeviation`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / int4 / real / int2 / uint2)

Image containing the standard deviation.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the mask in which the standard deviation
is calculated.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Width && odd(Width) && Width < width(Image) * 2`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the mask in which the standard deviation
is calculated.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Height && odd(Height) && Height < height(Image) * 2`

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display(Image)
deviation_image(Image,Deviation,9,9)
dev_display(Image)
```

## Result

`DeviationImage` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`DispImage`

## Alternatives

`EntropyImage`,
`EntropyGray`

## See also

`ConvolImage`,
`TextureLaws`,
`Intensity`

## Module

Foundation

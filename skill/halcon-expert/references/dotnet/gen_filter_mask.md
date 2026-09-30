# GenFilterMask (Operator)

## Name

`GenFilterMask` — Store a filter mask in the spatial domain as a real-image.

## Signature

`static void HOperatorSet.GenFilterMask(out HObject imageFilter, HTuple filterMask, HTuple scale, HTuple width, HTuple height)`

`void HImage.GenFilterMask(HTuple filterMask, double scale, int width, int height)`

`void HImage.GenFilterMask(string filterMask, double scale, int width, int height)`

## Description

`GenFilterMask` stores a filter mask in the spatial domain
as a real-image. The center of the filter mask lies in the center
of the resulting image. The parameter *`scale`* determines by
which amount the values of the filter mask are multiplied (this
results in larger values of the Fourier transform of the filter).
The corresponding filter matrix, which is given in
*`filterMask`* can be generated either from a file or a
tuple. The format of the filter matrix is described with the
operator [`ConvolImage`](convol_image.md). Example filter masks can be found in
the directory “filter” in the HALCON home directory. This
operator is useful for visualizing the frequency response of filter
masks (by applying a Fourier transform to the result image of this
operator).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageFilter`** (output_object)  image `→` [HImage](HImage.md) (real)

Filter in the spatial domain.

**`filterMask`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Filter mask as file name or tuple.

Default:
"gauss"

Suggested values:
"gauss", "laplace4", "laplace8", "lowpas_3_3", "lowpas_5_5", "lowpas_7_7", "lowpas_9_9", "sobel_c", "sobel_l"

**`scale`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Scaling factor.

Default:
1.0

Suggested values:
0.3, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0

Minimum increment:
0.001

Recommended increment:
0.1

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the image (filter).

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048, 4096, 8192

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the image (filter).

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048, 4096, 8192

## Example (HDevelop)

```
* If the filter should be read from a file:
gen_filter_mask (Filter, 'lowpas_3_3', 1.0, 512, 512)
* If the filter should be directly passed as a tuple:
gen_filter_mask (Filter, [3,3,9,1,1,1,1,1,1,1,1,1], 1.0, 512, 512)
fft_image (Filter, FilterFFT)
dev_set_paint ('3d_plot')
dev_display (FilterFFT)
```

## Possible Successors

`FftImage`,
`FftGeneric`

## See also

`ConvolImage`

## Module

Foundation

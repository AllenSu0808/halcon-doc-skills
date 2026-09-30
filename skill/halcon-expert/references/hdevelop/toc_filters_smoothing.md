## Smoothing

List of Operators ↓

This chapter contains operators for smoothing filters.
Further information about filtering can be found at
the introduction to the chapter [Filters](toc_filters.md).

### General information about smoothing filters

Smoothing operators are filters that help to suppress noise in an
image. For this purpose it is assumed, that in the undisturbed or true image
the gray value of a given data point does not completely differ from
its surroundings, ideally even varies only little.
Thus, to suppress noise, it can be useful to replace the measured gray value
with an estimate based on surrounding data points.
Such an estimate can be done in different ways, so HALCON provides
different smoothing operators.

The operators differ in speed and suitability for different kinds of noise.
Information like the complexity (runtime dependence on the image size)
is, if available, given in the operator reference.
While most operators treat a single image,
some can process depending images
(e.g., multichannel filters like [`mean_n`](mean_n.md) and [`rank_n`](rank_n.md),
or edge-preserving filters like [`guided_filter`](guided_filter.md) and
[`bilateral_filter`](bilateral_filter.md), which additionally use guidance images).
Please note that some filters have both possibilities and more information
is given in the specific operator reference.

### Smoothing filters for single images with random noise

These smoothing filters apply their smoothing function on each channel
of the input image separately and return a smoothed image with the
same number of channels.
In the following table we list implemented variants of smoothing filters
for a single image with random noise and apply them for three different
variants of random noise.
The images in the table shall give an idea of the operators capability,
but please note that the smoothed images highly depend on the
input parameters and the individual image for every operator.
For comparison, the different noisy images without filtering are given
in the first row of the table. The undisturbed image without noise is
shown in the following figure ((1) the full image as well as (2) its
part by means of which possible effects on edges and remains from Salt
& Pepper noise are visualized more clearly).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | ![figure](../assets/62081143bdb205fe.svg) | ![figure](../assets/e4d6b7cbb2deb97e.svg) | | ( 1) | ( 2) | |
| (1) Undisturbed image, (2) part of the image chosen for the visualization of the filter capabilities |

We marked filters recommended due to their special suitability
concerning speed (S), edge-preservation (E), or a compromise between
these two (C).
The numbers in square brackets refer to further information
that is given in a list below the table.

| White Noise | Gaussian Noise | Salt & Pepper Noise | Time[1] | Alternatives |
| --- | --- | --- | --- | --- |
| noisy image |
| figure | figure | figure |  |  |

|  |
| --- |
| [`binomial_filter`](binomial_filter.md)(S) |
| figure | figure | figure | 1|2 | [`gauss_filter`](gauss_filter.md), [`smooth_image`](smooth_image.md), [`derivate_gauss`](derivate_gauss.md), [`isotropic_diffusion`](isotropic_diffusion.md) |

|  |
| --- |
| [`smooth_image`](smooth_image.md) |
| figure | figure | figure | 2 | 9 | [`binomial_filter`](binomial_filter.md), [`gauss_filter`](gauss_filter.md), [`mean_image`](mean_image.md), [`derivate_gauss`](derivate_gauss.md), [`isotropic_diffusion`](isotropic_diffusion.md) |

|  |
| --- |
| [`mean_image`](mean_image.md)(S) |
| figure | figure | figure | 1 | 1 | [`binomial_filter`](binomial_filter.md), [`gauss_filter`](gauss_filter.md), [`smooth_image`](smooth_image.md), [`mean_image_shape`](mean_image_shape.md) |

|  |
| --- |
| [`anisotropic_diffusion`](anisotropic_diffusion.md)(E)[2] |
| figure | figure | figure | 805|2568 | [`bilateral_filter`](bilateral_filter.md), [`guided_filter`](guided_filter.md) |

|  |
| --- |
| [`guided_filter`](guided_filter.md)(E)[2,3] |
| figure | figure | figure | 13 | 62 | [`bilateral_filter`](bilateral_filter.md), [`anisotropic_diffusion`](anisotropic_diffusion.md), [`median_image`](median_image.md) |

|  |
| --- |
| [`bilateral_filter`](bilateral_filter.md)(E)[3] |
| figure | figure | figure | 16 | 54 | [`guided_filter`](guided_filter.md), [`anisotropic_diffusion`](anisotropic_diffusion.md), [`median_image`](median_image.md) |

|  |
| --- |
| [`gauss_filter`](gauss_filter.md) |
| figure | figure | figure | 1 | 4 | [`binomial_filter`](binomial_filter.md), [`smooth_image`](smooth_image.md), [`derivate_gauss`](derivate_gauss.md), [`isotropic_diffusion`](isotropic_diffusion.md) |

|  |
| --- |
| [`isotropic_diffusion`](isotropic_diffusion.md)(E)[2] |
| figure | figure | figure | 11 | 51 |  |

|  |
| --- |
| [`sigma_image`](sigma_image.md) |
| figure | figure | figure | 10 | 33 | [`anisotropic_diffusion`](anisotropic_diffusion.md), [`rank_image`](rank_image.md) |

|  |
| --- |
| [`midrange_image`](midrange_image.md) |
| figure | figure | figure | 3 | 11 | [`sigma_image`](sigma_image.md) |

|  |
| --- |
| [`median_image`](median_image.md)(E) |
| figure | figure | figure | 3 | 4 | [`median_rect`](median_rect.md), [`rank_image`](rank_image.md), [`rank_rect`](rank_rect.md) |

|  |
| --- |
| [`median_rect`](median_rect.md)(C) |
| figure | figure | figure | 2 | 3 | [`median_image`](median_image.md), [`rank_rect`](rank_rect.md), [`rank_image`](rank_image.md) |

|  |
| --- |
| [`median_separate`](median_separate.md)(C) |
| figure | figure | figure | 7 | 24 | [`median_image`](median_image.md) |

|  |
| --- |
| [`median_weighted`](median_weighted.md) |
| figure | figure | figure | 14 | 47 | [`median_image`](median_image.md), [`trimmed_mean`](trimmed_mean.md), [`sigma_image`](sigma_image.md) |

|  |
| --- |
| [`rank_rect`](rank_rect.md)(E) |
| figure | figure | figure | 2 | 8 | [`rank_image`](rank_image.md), [`median_rect`](median_rect.md), [`median_image`](median_image.md) |

|  |
| --- |
| [`rank_image`](rank_image.md)(E) |
| figure | figure | figure | 3 | 15 | [`rank_rect`](rank_rect.md), [`median_image`](median_image.md), [`median_rect`](median_rect.md) |

|  |
| --- |
| [`mean_sp`](mean_sp.md) |
| figure | figure | figure | 4 | 9 | [`mean_image`](mean_image.md), [`median_image`](median_image.md), [`median_separate`](median_separate.md), [`eliminate_min_max`](eliminate_min_max.md) |

|  |
| --- |
| [`eliminate_min_max`](eliminate_min_max.md) |
| figure | figure | figure | 11 | 42 |  |

|  |
| --- |
| [`eliminate_sp`](eliminate_sp.md) |
| figure | figure | figure | 1 | 10 | [`mean_sp`](mean_sp.md), [`mean_image`](mean_image.md), [`median_image`](median_image.md), [`eliminate_min_max`](eliminate_min_max.md) |

|  |
| --- |
| [`trimmed_mean`](trimmed_mean.md) |
| figure | figure | figure | 7 | 29 | [`sigma_image`](sigma_image.md), [`median_weighted`](median_weighted.md), [`median_image`](median_image.md) |

Further information related to the numbers in square brackets used in
the table above:

1. The numbers in the column 'Time' are indications about the time
   the operator uses to process an image.
   The numbers are obtained from averaging over multiple runs on
   the three different noise images and given in arbitrary units.
   Note also that the runtime of an operator depends on many factors,
   not at least on the used parameters and the image size.
   For each filter, the first number is for an image of size 800x600,
   the second for an image of size 1497x1160.
   The shown images are parts of the smaller image with parameters
   reasonable to us (we do not claim to have
   found the parameters resulting neither necessarily
   in the best image smoothing nor the smallest runtime).
   Even if two filters have the same parameter name as input, we did not
   necessarily use the same parameter value for both of them.
   Therefore, these numbers are to be understood as an indicator only.
2. This operator can be used iteratively.
3. This operator uses a guidance image
   (which can be the *`Image`* itself).

### Smoothing filters for single images with systematic noise

Video images composed of two half images can have systematic errors.
In such a case, the operator [`fill_interlace`](fill_interlace.md) can help.

### Operators designed for smoothing over multiple channels

These smoothing filters take an image with multiple channels
as input and return a single channel (gray value) image.
In HALCON, the following filters of this group are implemented:

- [`mean_n`](mean_n.md)
- [`rank_n`](rank_n.md)

### Further operators

In addition to the smoothing filters, this chapter contains the following
operator:
[`info_smooth`](info_smooth.md), which returns information related to the different
filters used by the operator [`smooth_image`](smooth_image.md).

### Glossary

In the following, the most important terms that are used in the context of
smoothing filters are described:

- **smoothing** —

  Smoothing means to apply a filter function on the
  given data to capture the main data patterns while
  removing noise.
- **random noise** —

  Random noise is a
  stationary variation of brightness or color information by a small
  random amount for every pixel with an assumed mean of 0 over the
  total image.
- **systematic noise** —

  Systematic noise is predictable noise, caused, e.g., by the specific
  setup used to acquire the images.

---

#### List of Operators

- [`anisotropic_diffusion`](anisotropic_diffusion.md) — Perform an anisotropic diffusion of an image.

- [`bilateral_filter`](bilateral_filter.md) — bilateral filtering of an image.

- [`binomial_filter`](binomial_filter.md) — Smooth an image using the binomial filter.

- [`eliminate_min_max`](eliminate_min_max.md) — Smooth an image in the spatial domain to suppress noise.

- [`eliminate_sp`](eliminate_sp.md) — Replace values outside of thresholds with average value.

- [`fill_interlace`](fill_interlace.md) — Interpolate 2 video half images.

- [`gauss_filter`](gauss_filter.md) — Smooth using discrete Gauss functions.

- [`guided_filter`](guided_filter.md) — Guided filtering of an image.

- [`info_smooth`](info_smooth.md) — Information on smoothing filter [`smooth_image`](smooth_image.md).

- [`isotropic_diffusion`](isotropic_diffusion.md) — Perform an isotropic diffusion of an image.

- [`mean_image`](mean_image.md) — Smooth by averaging.

- [`mean_image_shape`](mean_image_shape.md) — Smooth image using a mean filter with arbitrary mask.

- [`mean_n`](mean_n.md) — Average gray values over several channels.

- [`mean_sp`](mean_sp.md) — Suppress salt and pepper noise.

- [`median_image`](median_image.md) — Compute a median filter with various masks.

- [`median_rect`](median_rect.md) — Compute a median filter with rectangular masks.

- [`median_separate`](median_separate.md) — Separated median filtering with rectangle masks.

- [`median_weighted`](median_weighted.md) — Weighted median filtering with different rank masks.

- [`midrange_image`](midrange_image.md) — Calculate the average of maximum and minimum inside any mask.

- [`rank_image`](rank_image.md) — Compute a rank filter with arbitrary masks.

- [`rank_n`](rank_n.md) — Return gray values with given rank from multiple channels.

- [`rank_rect`](rank_rect.md) — Compute a rank filter with rectangular masks.

- [`sigma_image`](sigma_image.md) — Non-linear smoothing with the sigma filter.

- [`smooth_image`](smooth_image.md) — Smooth an image using various filters.

- [`trimmed_mean`](trimmed_mean.md) — Smooth an image with an arbitrary rank mask.

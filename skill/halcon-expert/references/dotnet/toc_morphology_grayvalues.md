## Gray Values

List of Operators ↓

This chapter describes operators of gray value morphology.

### Concept of Gray Value Morphology

Gray value morphology provides a set of operators that allow the non-linear
manipulation of gray values in an image, depending on their pixel
neighborhood. For instance, morphological gray value operators can be used
to smooth or emphasize structural features in images. Unlike the binary
operations in [Morphology / Region](toc_morphology_region.md), morphological gray value
operators deal with input images that contain pixels with a range of more
than one bit. Therefore gray value morphology can be seen as a
generalization of region morphology.
In the following paragraphs, we will take a closer look at the morphological
gray value operators.

### Dilation and Erosion of a Grayscale Image

To perform a dilation or erosion, each pixel of the image is assigned a gray
value depending on its neighborhood. Area and shape of the neighborhood
affecting each pixel are defined by the chosen structuring element with the
current pixel being the reference point. Implementing a dilation, every
pixel of the input image is assigned the maximum gray value of its
neighborhood, respectively the minimum gray value for an erosion.
Accordingly, bright areas of the input image are enlarged by gray value
dilation, whereas gray value erosion emphasizes dark areas.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/bc3082cead40024d.svg) | ![figure](../assets/803c9346b9282734.svg) | ![figure](../assets/57faa63c60917f51.svg) | ![figure](../assets/64d2752721b9be91.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Original gray value image,
(2) structuring element with reference point in the origin,
(3) result of eroding the input image,
(4) result of dilating the input image.

These operators can be used to dilate or erode an image:

| Morphological Operator |  | Structuring Element |
| --- | --- | --- |
| [`GrayDilation`](gray_dilation.md) | [`GrayErosion`](gray_erosion.md) | arbitrary |
| [`GrayDilationRect`](gray_dilation_rect.md) | [`GrayErosionRect`](gray_erosion_rect.md) | rectangular |
| [`GrayDilationShape`](gray_dilation_shape.md) | [`GrayErosionShape`](gray_erosion_shape.md) | rhombus/rectangle/octagon |
|  |

Morphological grayscale operations are often part of the preprocessing of
images before information can be extracted properly. The following example
displays a case where a gray value erosion is necessary to read 2D code
symbols. In order to fit a 2d code model used for decoding, the gaps between
the code elements in the image need to be reduced by enlarging local minima
in a square shape. Therefore a gray value erosion is performed, using an
adequately sized rectangle as the structuring element. The rectangle size
depends on the 2D code model created with [`CreateDataCode2dModel`](create_data_code_2d_model.md),
where the acceptable module gap size is determined.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/80a9bfe551a0542d.svg) | ![figure](../assets/67c2a00b0e9f6e33.svg) | ![figure](../assets/d70ac53d84376df9.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Image of coded object,
(2) erosion with square structuring element,
(3) applying 2D code model for decoding. These images are from the example
program `2d_data_codes_minimize_module_gaps.hdev.`

### Opening and Closing

Gray value opening and gray value closing operators each are a combination
of the operators explained above. Closing is a dilation followed by an
erosion, while for an opening an erosion precedes a dilation operation.
As seen in the example images, [`GrayClosing`](gray_closing.md) reduces or even removes
parts of the image that are darker than their neighborhood whereas
[`GrayOpening`](gray_opening.md) reduces lighter areas. Furthermore, using a suited
structuring element you can preserve shapes while removing unwanted image
artifacts.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/bc3082cead40024d.svg) | ![figure](../assets/72e3a067ead98b8d.svg) | ![figure](../assets/aae76037155d9250.svg) | ![figure](../assets/a016316f9584331d.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Original gray value image,
(2) structuring element with reference point in the origin,
(3) result of closing the input image,
(4) result of opening the input image.

### Further Operators

To take a closer look at areas that are affected by gray value opening or
closing, you can perform a [`GrayTophat`](gray_tophat.md) or [`GrayBothat`](gray_bothat.md)
transformation.
The resulting image displays the difference between the original image and
the opening respectively closing of an image. You can also use these
operators to detect structures that match the shape of the structuring
element.

The [`GrayRangeRect`](gray_range_rect.md) operator gives you the opportunity to detect
fine structures on homogeneous surfaces by visualizing the extent of local
variations in pixel values.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/7bf7ac8e92f986ce.svg) | ![figure](../assets/1466dfa464c8595b.svg) | ![figure](../assets/d8cb42b07af44027.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Top hat,
(2) bottom hat,
(3) gray value range.

By applying the [`GrayRangeRect`](gray_range_rect.md) operator you can perform a mitigated
form of a gray value opening or closing operation. You can control the
transformation by adjusting the parameter *`modePercent`*.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ![figure](../assets/944f47adb5c84abc.svg) | ![figure](../assets/c2e479d89cce106e.svg) | ![figure](../assets/adaa8baf4621f5ef.svg) | ![figure](../assets/9c617c0106f5418e.svg) | ![figure](../assets/1994f36e0bfcb693.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) | ( 5) |

Dual rank operations:
(1) *`modePercent`* = 0 (equals opening),
(2) *`modePercent`* = 25,
(3) *`modePercent`* = 50 (equals median),
(4) *`modePercent`* = 75,
(5) *`modePercent`* = 100 (equals closing).

### Glossary

In the following list, the most important terms that are used in the
context of Morphology are described.

- **non-linear operator** —

  Operator which does not necessarily preserve
  structures of the input image
- **structuring element** —

  Region which is used to scan the input
  image.

---

#### List of Operators

- [`DualRank`](dual_rank.md) — Opening, Median and Closing with circle or rectangle mask.

- [`GenDiscSe`](gen_disc_se.md) — Generate ellipsoidal structuring elements for gray morphology.

- [`GrayBothat`](gray_bothat.md) — Perform a gray value bottom hat transformation on an image.

- [`GrayClosing`](gray_closing.md) — Perform a gray value closing on an image.

- [`GrayClosingRect`](gray_closing_rect.md) — Perform a gray value closing with a rectangular mask.

- [`GrayClosingShape`](gray_closing_shape.md) — Perform a gray value closing with a selected mask.

- [`GrayDilation`](gray_dilation.md) — Perform a gray value dilation on an image.

- [`GrayDilationRect`](gray_dilation_rect.md) — Determine the maximum gray value within a rectangle.

- [`GrayDilationShape`](gray_dilation_shape.md) — Determine the maximum gray value within a selected mask.

- [`GrayErosion`](gray_erosion.md) — Perform a gray value erosion on an image.

- [`GrayErosionRect`](gray_erosion_rect.md) — Determine the minimum gray value within a rectangle.

- [`GrayErosionShape`](gray_erosion_shape.md) — Determine the minimum gray value within a selected mask.

- [`GrayOpening`](gray_opening.md) — Perform a gray value opening on an image.

- [`GrayOpeningRect`](gray_opening_rect.md) — Perform a gray value opening with a rectangular mask.

- [`GrayOpeningShape`](gray_opening_shape.md) — Perform a gray value opening with a selected mask.

- [`GrayRangeRect`](gray_range_rect.md) — Determine the gray value range within a rectangle.

- [`GrayTophat`](gray_tophat.md) — Perform a gray value top hat transformation on an image.

- [`ReadGraySe`](read_gray_se.md) — Load a structuring element for gray morphology.

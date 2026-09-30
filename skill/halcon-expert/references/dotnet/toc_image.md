## Image

List of Sections ↓

This chapter contains operators regarding the handling of images.

In order to understand the different types of images you can process in
HALCON, the three components of an image (pixels, channels and
domain) are explained in the following paragraphs.

To learn more about the basic concept of images in HALCON you can also
see the example program `halcon_basic_concepts.hdev`.

### Pixels

In HALCON pixels can be used in order to represent information of various
kinds. Therefore different pixel types are distinguished.
The following table lists the different pixel types and the corresponding
standard image types for images. Note that this list is not exclusive (e.g.,
a gray value image can be of multiple other image types as well).
You can convert the image type using [`ConvertImageType`](convert_image_type.md).

| Pixel Type | Standard Image Type |
| --- | --- |
| Gray Values | `byte, uint2` |
| Difference | `int1, int2` |
| 2D Histogram | `int4` |
| Edge Directions | `direction` |
| Derivatives | `real` |
| Fourier Transform | `complex` |
| Hue Values | `cyclic` |
| Vector Field | `vector_field` |

Note that the image type `vector_field` can be specified further
by using `vector_field_absolute` or `vector_field_relative`.
There is also the image type `int8` (64 bits with sign), which is
only available on 64 bit systems.
Further information on the different pixel types is given below.

- **Gray Values** —

  Gray images are of type `byte` (8 bits without sign) or
  `uint2` (16 bits without sign) and consist of pixels usually
  representing local intensities of light on a sensor.

  ![figure](../assets/62a909824674f2fc.svg)

  Gray value image.
- **Difference** —

  In order to show the differences between two images e.g., the image
  types `int1` (8 bits with sign) or `int2` (16 bits with
  sign) are well suited.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/a1aa95f3d3651cd2.svg) | ![figure](../assets/7cb93298db0d5035.svg) | ![figure](../assets/7f807d03da99ff81.svg) |
  | ( 1) | ( 2) | ( 3) |

  Comparing an image (1) with another (e.g., consecutively taken) one
  (2) by subtracting the latter from the former results in a
  difference image (3).
- **2D Histogram** —

  To examine image features based on the occurrence of gray values in
  two images you can use a 2D histogram, which is of type `int4`
  (32 bits with sign). Thereby, the axes of the 2D histogram each
  represent the gray values of an input image. The gray values of
  corresponding pixels in the input images are registered in the 2D
  histogram accordingly. The higher the frequency of a specific
  combination of gray values, the higher the gray value in the output
  image (see also [`Histo2dim`](histo_2dim.md)).

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/b12d20221a7bd3f1.svg) | ![figure](../assets/c98da9143b8e8e58.svg) | ![figure](../assets/ab07a0185bc02b16.svg) |
  | ( 1) | ( 2) | ( 3) |

  Two channels ((1), (2)) of an exemplary image and their respective
  2D histogram (3).
- **Edge Directions** —

  To represent the orientation of the edge gradient, the image type
  `direction` (8 bits without sign) is available.

  |  |  |
  | --- | --- |
  | ![figure](../assets/8011e9add3fa9c1f.svg) | ![figure](../assets/b0efc5c7580f5a6b.svg) |
  | ( 1) | ( 2) |

  Examining an image (1) by visualizing the orientation of its
  image edges (2).

  For images of type `direction` an edge direction of x degrees
  in mathematically positive sense and with respect to the horizontal
  axis is stored as x / 2 in the edge direction image (resulting in
  gray values from 0 to 179).
  Points with edge amplitude 0 are assigned the edge direction 255
  (undefined direction).

  ![figure](../assets/a768bc42ecaeac15.svg)

  Visualizing the edge directions for dark and bright objects using
  [`SobelDir`](sobel_dir.md).
  The edge direction (marked with an tangential arrow in the input
  image) of a pixel is encoded by a corresponding gray value in the
  result image on the right. Locations without an edge are
  represented by a gray value of 255.
- **Derivatives** —

  The image type `real` (32 bits floating point value) is used
  to represent derivatives of an image, e.g., in order to extract edges.

  |  |  |
  | --- | --- |
  | ![figure](../assets/11f5bc1e147610b9.svg) | ![figure](../assets/d1a05bff9a3f1968.svg) |
  | ( 1) | ( 2) |

  Some features of an image (1) (e.g., edges, gradients) can be
  examined by considering its derivatives (2).
- **Fourier Transform** —

  To inspect the frequency domain of an image the Fourier transform is
  used. The combination of magnitude and phase of the frequencies is
  represented by complex numbers, therefore the image type is
  `complex` (two `real` values per pixel).

  |  |  |
  | --- | --- |
  | ![figure](../assets/440ba07e1115b9c3.svg) | ![figure](../assets/10f379abd3f94883.svg) |
  | ( 1) | ( 2) |

  One strategy to identify letters (1) is to observe its frequency
  domain by calculating the Fourier transform (2).
- **Hue Values** —

  Hue values are encoded `cyclic` (8 bits without sign) so
  that $255+1=0$.

  |  |  |
  | --- | --- |
  | ![figure](../assets/62a909824674f2fc.svg) | ![figure](../assets/cabcf7a7320b1cf7.svg) |
  | ( 1) | ( 2) |

  Pixels representing hue values. When increasing a pixel value beyond
  255, it is shifted to the other end of the spectrum. Therefore
  adding a constant number to each cyclic pixel value of (1) results
  in an image like (2).
- **Vector Field** —

  A special image type to represent absolute/relative optical flow is
  `vector_field` (composed by two `real` images for x and
  y direction). The type of vector field can be specified further
  by assigning `vector_field_absolute` (interpreted as absolute
  coordinates) or `vector_field_relative` (interpreted as
  vectors).

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/0fdda9fda3dbfc2b.svg) | ![figure](../assets/ddecba1fb70fd52e.svg) | ![figure](../assets/99c9f418dc1b8dc8.svg) |
  | ( 1) | ( 2) | ( 3) |

  Relative motion of pixels (e.g., in consecutive images (1) and (2))
  can be represented in a vector field (3).

### Channels

Besides different pixel types, an image can use different image channels in
order to store specific information. Basically, you can use channels to
assign multiple values to a pixel. The following sections mention a few
cases, where different numbers of channels are useful.

- **Gray Value Images (Single-Channel Images)** —

  Often, there is only one value stored for every pixel of an image. A gray
  value image for example, stores a value representing local light
  intensity on a sensor for each pixel.
  Nevertheless, various types of information can be assigned to those
  pixels (e.g., the derivatives of gray values, distances).
  Visualizing them analogous to a gray value image can help interpreting
  the data.
- **RGB Images (Three-Channel Images)** —

  For a colored image, the pixel values are typically stored in three
  channels each representing the intensity of either red, green or blue
  light of the respective pixel (RGB image). Through additive mixing of the
  three values assigned to one pixel, a specific color is defined.

  Besides the RGB model there are several further color spaces. For more
  information about those models and how to transform between the
  different color spaces see [`TransToRgb`](trans_to_rgb.md) and
  [`TransFromRgb`](trans_from_rgb.md) respectively.

  |  |  |  |  |
  | --- | --- | --- | --- |
  | ![figure](../assets/92a81d5d688f7920.svg) | ![figure](../assets/3160d74fcd8a20ae.svg) | ![figure](../assets/2c65a00fb782824d.svg) | ![figure](../assets/b6a6139a9eee4f06.svg) |
  | ( 1) | ( 2) | ( 3) | ( 4) |

  RGB image (1) and its three channels separately: The local intensities
  differ for red (2), green (3), and blue channel (4).
- **Multispectral Images (Multi-Channel Images)** —

  With special cameras, a variety of spectral bands can be registered in an
  image, including from outside the visible light spectrum. Satellite
  cameras, for instance, often acquire multispectral data and store them in
  multiple distinct channels respectively.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/7b5aacc70634fbb4.svg) | ![figure](../assets/a31ac10b2b9df2cf.svg) | ![figure](../assets/8e952e988c588047.svg) |
  | ( 1) | ( 2) | ( 3) |
  | ![figure](../assets/6a55241ec609f7f1.svg) | ![figure](../assets/1c180aada60649b1.svg) | ![figure](../assets/2a9232ec683a0ccb.svg) |
  | ( 4) | ( 5) | ( 6) |

  Six channels of an satellite image: the different channels of a
  multispectral image can be used to extract features that are most
  prominent in a special spectral band.
- **Multi-Channel Images** —

  Besides representing light intensities, assembling multiple channels in
  one image can help with various other tasks.

  For example, combining a gray value image with an additional channel
  containing the respective depth values of the image pixels allows you to
  visualize the scene in a 3D plot.

  Instead of using a depth camera you can also use a multi-channel image
  to extract depth information.
  Therefore, each channel must contain one of a series of images taken with
  different focus levels.

  Besides containing spacial information, the channels of an image can
  also be interpreted as a feature space in order to perform a principal
  components analysis.

### Domain

The image domain determines the area of an image that is used in the
succeeding operations.
In order to focus the processing on regions of interest and/or speed up
the operations you can reduce the domain to the relevant parts of an image.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/ea60bcf4c83fae91.svg) | ![figure](../assets/14610de1f74d6cff.svg) | ![figure](../assets/3d22a848282e85bf.svg) |
| ( 1) | ( 2) | ( 3) |

The domain of the original image (1) is reduced, e.g., considering a
minimum gray value threshold (2). Areas that are still relevant for
further operations (orange) remain in the result image (3), whereas
unwanted areas of the image are excluded (black).

---

#### List of Sections

- [Access](toc_image_access.md)
- [Acquisition](toc_image_acquisition.md)
- [Channel](toc_image_channel.md)
- [Creation](toc_image_creation.md)
- [Domain](toc_image_domain.md)
- [Features](toc_image_features.md)
- [Format](toc_image_format.md)
- [Manipulation](toc_image_manipulation.md)
- [Type Conversion](toc_image_typeconversion.md)

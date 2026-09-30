## Threshold

List of Operators ↓

This chapter describes threshold operators.

### Concept of Threshold Operators

One way to perform a segmentation of an image is to use threshold operators.
In doing so, regions that fulfill a certain threshold condition, depending
on gray values, are determined within an image.

In order to fit different tasks and image properties there is a
set of threshold operators provided.

The following paragraphs give an overview of the operators by
differentiating them into histogram-based and local methods and having a
closer look at the most important ones.

### Histogram-based Threshold Operators

Histogram-based threshold segmentation does not take the position but only
the pixel value into account. Therefore thresholds are determined by
adjusting them to the histogram of an image.

- **Threshold** —

  By using [`Threshold`](threshold.md), you can select all pixels within user set gray
  value intervals.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/54107150c21d1599.svg) | ![figure](../assets/224567867d990d73.svg) | ![figure](../assets/3c5946be0f95753a.svg) |
  | ( 1) | ( 2) | ( 3) |

  (1) Input image,
  (2) histogram of the input image with manually determined thresholds
  *`minGray`* and *`maxGray`*,
  (3) resulting segmentation of the input image.

  The operator [`FastThreshold`](fast_threshold.md) also works with two manually determined
  thresholds but uses another computing algorithm.
- **Binary Threshold** —

  To divide your image into light and dark regions, [`BinaryThreshold`](binary_threshold.md)
  automatically computes a threshold to separate foreground from background.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/e28bea0f24191f59.svg) | ![figure](../assets/b918347253c34333.svg) | ![figure](../assets/a846669eb58b0852.svg) |
  | ( 1) | ( 2) | ( 3) |

  (1) Input image,
  (2) histogram of the input image with automatically determined binary threshold,
  (3) resulting segmentation of the input image.

  A segmentation using [`ThresholdSubPix`](threshold_sub_pix.md) also divides the image into
  foreground and background, but puts out the separating border with sub-pixel
  accuracy. The threshold has to be set manually.
- **Automatic Threshold** —

  [`AutoThreshold`](auto_threshold.md) computes local minima in the image histogram to
  determine thresholds. By smoothing the histogram you have influence on the
  number of classes found in the input image.

  |  |  |  |  |
  | --- | --- | --- | --- |
  | ![figure](../assets/8a02309a43771416.svg) | ![figure](../assets/9a2fc6780f215531.svg) | ![figure](../assets/0ff99b248f2b2af2.svg) | ![figure](../assets/00e91253eb1fa04b.svg) |
  | ( 1) | ( 2) | ( 3) | ( 4) |

  (1) Slightly smoothed histogram,
  (2) results in higher number of local minima,
  (3) with further smoothing,
  (4) number of local minima decreases.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/a5e704a6582c1e6d.svg) | ![figure](../assets/73fca3416f69ed36.svg) | ![figure](../assets/501bc0ef071d10d8.svg) |
  | ( 1) | ( 2) | ( 3) |

  (1) Input image,
  (2) four classes are extracted from slightly smoothed histogram,
  (3) whereas in this case a further smoothed histogram results in
  two regions.

  Use [`HistoToThresh`](histo_to_thresh.md) to get the gray values of local minima in the
  histogram.
- **Character Threshold** —

  To do a segmentation of dark text on light background, [`CharThreshold`](char_threshold.md)
  is a useful tool. The maximum peak in the histogram corresponds to the
  light background. Assuming the text is darker than the background, you
  examine the smoothed histogram left of the maximum. The parameter
  *`percent`* determines how far from the maximum the threshold is set,
  taking the frequencies of the gray values into account.

  |  |  |
  | --- | --- |
  | ![figure](../assets/e7eb4ebb6912ba75.svg) | ![figure](../assets/200a498564f1dd4d.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/d138bc18fa3e7bb2.svg) | ![figure](../assets/4de962445e38744c.svg) |
  | ( 3) | ( 4) |

  (1) Input image,
  (2) histogram is smoothed and global maximum is identified,
  (3) the parameter *`percent`* determines threshold left of the
  maximum,
  (4) resulting image.
- **Dual-Threshold** —

  Subtracting an image from another or using an edge detecting
  operator like [`LaplaceOfGauss`](laplace_of_gauss.md) usually leads to negative values in
  the resulting image. The operator [`DualThreshold`](dual_threshold.md) is suited for the
  segmentation of signed images while also taking minimum region size into
  account.

  ![figure](../assets/588f131318dbfee5.svg)

  Histogram of a signed image with *`threshold`* (inner boundaries)
  and *`minGray`*. Pixels are only selected if they fulfill the
  conditions regarding gray values and region size.

  |  |  |
  | --- | --- |
  | ![figure](../assets/bb0e715d3b6d9de2.svg) | ![figure](../assets/04aeb3bd8e3e0974.svg) |
  | ( 1) | ( 2) |

  (1) Signed input image (created with [`SubImage`](sub_image.md)),
  (2) result after applying a dual threshold.

### Local Threshold Operators

Unlike histogram-based threshold operators, a local threshold also takes
position or neighborhood of pixels into account to assign them to
the appropriate region. Instead of global thresholds that are applied to
each pixel, it is sometimes be useful to adapt the threshold to local
features of the image.

- **Local Threshold** —

  [`LocalThreshold`](local_threshold.md) takes the local mean and standard deviation into
  account and computes an individual threshold for each pixel. The size of the
  neighborhood is set by the user.
  This operator is especially suited for the segmentation of text, when
  lighting conditions or the background are not homogeneous.

  |  |  |
  | --- | --- |
  | ![figure](../assets/fcfeed5817c60b43.svg) | ![figure](../assets/6dc335aed4294da3.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/5d8eb087b0f03139.svg) | ![figure](../assets/e72359209b6a45da.svg) |
  | ( 3) | ( 4) |

  (1) Input image,
  (2) segmentation with global thresholds does not choose the desired text
  solely,
  (3) adapting the threshold to the neighborhood of each pixel individually,
  (4) segmentation of the text.

  The operator [`VarThreshold`](var_threshold.md) works in a similar way, except it selects
  those points of the image that fulfill specified conditions regarding their
  local standard deviation and brightness.
- **Dynamic Threshold** —

  With [`DynThreshold`](dyn_threshold.md) you can inspect the differences between images.
  Usually the input image and a filtered version, e.g., the mean of the
  image, are compared pixel by pixel. The parameter *`lightDark`* is used
  to determine what kind of changes in the image are relevant. The sensitivity
  of the operator is controlled by the parameter *`offset`*.

  |  |  |
  | --- | --- |
  | ![figure](../assets/81df859afd9acb64.svg) | ![figure](../assets/0e37ba0741fc24e0.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/ca9d278fa5d1ce11.svg) | ![figure](../assets/831d53747dcc86c6.svg) |
  | ( 3) | ( 4) |

  (1) Input image,
  (2) segmentation of scratches with global threshold is not possible due to
  inhomogeneous lighting conditions,
  (3) inspection of the gray value difference between the original image
  (left) and mean of the image (middle) pixel by pixel
  to segment regions (right) exceeding `offset` (image detail),
  (4) result after selecting wanted regions. For more detail have a look at
  the example `surface_scratch.hdev`.

  A similar operator is [`CheckDifference`](check_difference.md). The operator displays the
  absolute differences between two images. It is especially suited for
  change detection of consecutively acquired images.
- **Zero Crossing Threshold** —

  Operators like [`LaplaceOfGauss`](laplace_of_gauss.md) that are used for edge detection
  return signed images, where edges are located at the zero crossings.
  [`ZeroCrossing`](zero_crossing.md) and [`ZeroCrossingSubPix`](zero_crossing_sub_pix.md) can be used to
  extract those edges, taking the individual 4-neighborhood into account.

  |  |  |
  | --- | --- |
  | ![figure](../assets/e76db95f8b280325.svg) | ![figure](../assets/62be453c0f5d1e03.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/f03ead49f8715df5.svg) | ![figure](../assets/9290c80305a3b98e.svg) |
  | ( 3) | ( 4) |

  (1) Input image,
  (2) domain is reduced and Laplace-of-Gaussian filter is
  applied,
  (3) the zero-crossing operators can detect edges with pixel (red) and
  sub-pixel accuracy (green),
  (4) image details of results using [`ZeroCrossing`](zero_crossing.md) (red) and
  [`ZeroCrossingSubPix`](zero_crossing_sub_pix.md) (green).

---

#### List of Operators

- [`AutoThreshold`](auto_threshold.md) — Segment an image using thresholds determined from its histogram.

- [`BinaryThreshold`](binary_threshold.md) — Segment an image using binary thresholding.

- [`CharThreshold`](char_threshold.md) — Perform a threshold segmentation for extracting characters.

- [`CheckDifference`](check_difference.md) — Compare two images pixel by pixel.

- [`DualThreshold`](dual_threshold.md) — Threshold operator for signed images.

- [`DynThreshold`](dyn_threshold.md) — Segment an image using a local threshold.

- [`FastThreshold`](fast_threshold.md) — Fast thresholding of images using global thresholds.

- [`HistoToThresh`](histo_to_thresh.md) — Determine gray value thresholds from a histogram.

- [`LocalThreshold`](local_threshold.md) — Segment an image using local thresholding.

- [`Threshold`](threshold.md) — Segment an image using global threshold.

- [`ThresholdSubPix`](threshold_sub_pix.md) — Extract level crossings from an image with subpixel accuracy.

- [`VarThreshold`](var_threshold.md) — Threshold an image by local mean and standard deviation analysis.

- [`ZeroCrossing`](zero_crossing.md) — Extract zero crossings from an image.

- [`ZeroCrossingSubPix`](zero_crossing_sub_pix.md) — Extract zero crossings from an image with subpixel accuracy.

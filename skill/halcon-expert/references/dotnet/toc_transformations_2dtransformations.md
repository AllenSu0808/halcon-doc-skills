## 2D Transformations

List of Operators ↓

To specify a location in an image, we need a convention how to do so.
Such a convention is set via a coordinate system.
There are different coordinate systems used in HALCON. Here, we explain
the ones used in 2D.

Pixels are discrete and to address them, we have a coordinate system using
only integer values, the pixel coordinate system.
For a higher accuracy that goes beyond the pixel grid, we need floating
point coordinates, like e.g., $(3.6,4.1)$.
This leads to subpixel accurate coordinate systems.
In HALCON, we have three different implementations of subpixel coordinate
systems:

- Pixel Centered Coordinates, the HALCON Standard Subpixel
  Coordinate System
- Edge Centered Coordinates
- Polar Coordinates

Thereof the first two vary only in the coordinate origin,
as visible in the figures below.
Calibration makes it possible to map the image coordinates distances to
real-world distances. For more information about these Calibrated
Coordinates we refer to the `“Solution Guide III-C - 3D Vision”`.

### HALCON Standard Coordinate System

- ****Pixel Accurate Coordinate System**** —

  The pixel coordinate system treats the image as a grid of discrete
  elements, the pixels.
  In HALCON, we put the origin $(0,0)$ in the middle of the
  upper left pixel.
  Now, we assign the pixel coordinates specifying its row and column like
  in a matrix.

  Note that this implies for an image of size height $\times$ width =
  $m\times n$ pixels that the row coordinate
  values run from $0$ to $m-1$ and the column coordinate
  values from $0$ to $n-1$, as visualized in the figure
  below.
- ****Subpixel Accurate Coordinate System: Pixel Centered**** —

  The origin of this coordinate system is in the center of the upper left
  image pixel, the axes are in row (r) and column (c) direction, respectively.
  Therewith this convention embeds the pixel coordinate system.
  The upper left image corner has the coordinates
  $(-0.5,-0.5)$ and for an image of size height
  $\times$ width = $m\times n$ pixels
  the bottom right corner has the coordinates
  $(m-0.5,n-0.5)$
  (=$(m-1+0.5,n-1+0.5)$, remember the coordinate
  values start at 0).
  It also implies that a pixel (k,l) covers the area of the rectangle
  $(k-0.5,l-0.5)$, $(k+0.5,l-0.5)$,
  $(k-0.5,l+0.5)$, $(k+0.5,l+0.5)$.
  This convention is called the standard coordinate system, or
  also Image Coordinate System.

  |  |  |
  | --- | --- |
  | ![figure](../assets/8f88fea4e8ae01a6.svg) | ![figure](../assets/31bd1ff7d3e9a43f.svg) |
  | ( 1) | ( 2) |

  Visualization of the HALCON standard pixel and subpixel Cartesian
  coordinate systems.
  The cross indicates the pixel in the bottom right image corner. Its
  center has the coordinates $(6,5)$ (in pixel coordinates (1)),
  $(6.0,5.0)$ (in standard subpixel coordinates (2)).
  The circle center has the coordinates $(3.6,4.1)$.

### HALCON Non-Standard Cartesian Coordinate System

If we rotate an image around its origin by $\pi/2$
(=90 degrees), we want the two images with touching edges but not
overlapping with each other. Also, scaling the image is not expected to
result in negative image coordinates.
For this, the origin $(0.0,0.0)$ has to be set in an image
corner. This motivates the following coordinate system.

- ****Subpixel Accurate Coordinate System: Edge Centered**** —

  For this coordinate system we set the origin $(0.0,0.0)$
  in the upper left image corner.
  Thus the center of the upper left pixel has the coordinates
  $(0.5,0.5)$ and for an image of size height
  $\times$ width = $m\times n$ pixels
  the bottom right corner has the coordinates
  $(m,n)$.
  A pixel $(k,l)$ covers the area of the rectangle
  $(k,l)$, $(k,l+1)$, $(k+1,l)$,
  $(k+1,l+1)$.

  ![figure](../assets/0623e69dade8b1bc.svg)

  Visualization of the HALCON non-standard subpixel Cartesian coordinate
  system.
  The cross indicates the pixel in the bottom right image corner. Its
  center has the coordinates $(6.5,5.5)$.
  The circle center has the coordinates $(3.6,4.1)$.

  For this coordinate system rotations are defined in the mathematically
  positive direction and thus counterclockwise.
  A rotation of $\pi/2$ (=90 degrees) maps the first axis
  (= x-axis) onto the second axis (= y-axis).
  Accordingly, the axes have the assignment row: x coordinate, column:
  y coordinate.

  ![figure](../assets/67c8af4ed07548d7.svg)

  Visualization of a rotation ($\alpha$) using
  the edge centered coordinate system.

### Operators Expecting Parameters in any Cartesian Coordinate System

The operator [`AffineTransPoint2d`](affine_trans_point_2d.md) applies the transformation
given by *`homMat2D`* to the point coordinates.
This means, [`AffineTransPoint2d`](affine_trans_point_2d.md) works
in both Cartesian Coordinate systems, as long you make sure that the point
and the transformation are given in the same coordinate system.

The operators [`AngleLl`](angle_ll.md) and [`AngleLx`](angle_lx.md) may take the input
points in pixel centered coordinates, but the returned angle is in the
convention of rotations in a mathematically positive direction, thus
counterclockwise, and with the horizontal axis as *0*, like in the
edge centered coordinate system.

### Operators Expecting Parameters in Different Coordinate Systems

In HALCON there is also the case that an operator expects its input in
different coordinate systems.
On the one hand, the object is expected in its usual coordinates, the
standard coordinates.
On the other hand, for the transformation matrix *`homMat2D`*, the
operator expects edge centered coordinates with their advantages regarding
transformations described above.
The operator converts the coordinates of the object from HALCON's
standard coordinate system (with the origin in the center of the
upper left pixel) to the edge centered coordinate system
(with the origin in the upper left corner of the upper left pixel).
After the transformation with *`homMat2D`*, the result is
converted back to the standard coordinate system.

These operators are

- [`AffineTransContourXld`](affine_trans_contour_xld.md)
- [`AffineTransImage`](affine_trans_image.md)
- [`AffineTransImageSize`](affine_trans_image_size.md)
- [`AffineTransPixel`](affine_trans_pixel.md)
- [`AffineTransPolygonXld`](affine_trans_polygon_xld.md)
- [`AffineTransRegion`](affine_trans_region.md)
- [`ProjectiveTransContourXld`](projective_trans_contour_xld.md)
- [`ProjectiveTransImage`](projective_trans_image.md)
- [`ProjectiveTransImageSize`](projective_trans_image_size.md)
- [`ProjectiveTransPixel`](projective_trans_pixel.md)
- [`ProjectiveTransRegion`](projective_trans_region.md)

A matrix representing a transformation in pixel centered coordinates can
be converted to represent the same transformation (e.g., a rotation around
the same point) written in edge centered coordinates, e.g., through

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |

Note, the operators beginning with `projective_` mentioned above
use a projective transformation matrix. These transformation matrices can,
e.g., be obtained from a 3D camera pose. Doing so, the matrix used is
written in a projection of the xy-plane within the 3D coordinate system.
Accordingly, the axes have the assignment row: y coordinate, column:
x coordinate and therewith the coordinates need to be converted.

### Shape-based Matching and Correlation-based Matching

Results from shape-based matching, like e.g.,
[`FindGenericShapeModel`](find_generic_shape_model.md), are given in edge centered coordinates.
The returned matches are already transformed. The respective homographic
transformation matrices can be retrieved using
[`GetGenericShapeModelResult`](get_generic_shape_model_result.md).

Results from correlation-based matching, like e.g.,
[`FindNccModel`](find_ncc_model.md) and [`FindNccModels`](find_ncc_models.md),
are computed in edge centered coordinates as well, however the parameters
for the transformation are returned separately.
With these results one can create a transformation
*`homMat2D`* directly applicable for,
e.g., [`AffineTransContourXld`](affine_trans_contour_xld.md)
and the other operators listed in the paragraph above, entitled
`Operators Expecting Parameters in Different Coordinate Systems`.

To display the results found by correlation-based matching, we highly
recommend the usage of the procedure
`dev_display_ncc_matching_results`.

In the following images we give an example how a displayed
match may look when using the transformation matrix in the correct and
the erroneous coordinate system, respectively.
For the latter one, shown in image (3), the transition matrix is given in
pixel centered coordinates as well and therefore the match shown by
[`AffineTransContourXld`](affine_trans_contour_xld.md) is off by 0.5 pixels.
Note, this effect is only visible when a rotation is involved.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/510165dace432ee4.svg) | ![figure](../assets/a3b57407da52adf4.svg) | ![figure](../assets/10fa90c80b5b91ce.svg) |
| ( 1) | ( 2) | ( 3) |

The original image of the paperclip (1), a part of the match where the
inputs are given in the correct coordinates (2), and a match with
inputs given in wrong coordinates.

### Non-Cartesian Coordinate Systems

- ****Subpixel Accurate Coordinate System: Polar Coordinates**** —

  In polar coordinates, points are defined through a distance and an angle.
  The distance is called the radial coordinate and is given in relation to
  the fix point, the pole. The angular coordinate is given with respect to a
  defined axis, the polar axis.
  In HALCON, the pole is specified by
  $(\texttt{Row},\texttt{Column})$
  and the polar axis is the horizontal axis.
  The angular coordinate is given in radians.

  After a transformation with [`PolarTransImageExt`](polar_trans_image_ext.md), the
  upper left pixel in the output image always corresponds to the
  point in the input image that is specified by *`radiusStart`*
  and *`angleStart`*. Analogously, the lower right pixel in the
  output image corresponds to the point in the input image that
  is specified by *`radiusEnd`* and *`angleEnd`*. In the
  usual mode (*`angleStart`* < *`angleEnd`* and
  *`radiusStart`* < *`radiusEnd`*), the polar
  transformation is performed in the mathematically positive
  orientation (counterclockwise). Furthermore, points with smaller
  radius lie in the upper part of the output image. By suitably
  exchanging the values of these parameters (e.g., *`angleStart`*
  > *`angleEnd`* or *`radiusStart`* >
  *`radiusEnd`*), any desired orientation of the output image can
  be achieved.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/b0adc1a0ca780700.svg) | ![figure](../assets/ef54daf225150c2f.svg) | ![figure](../assets/15b95f4c5a616826.svg) |
  | ( 1) | ( 2) | ( 3) |

  As an example, we show an annular arc defined by its pole
  (*`row`*,*`column`*) (+), the polar axis (...),
  two angular coordinates *`angleStart`*
  ($\alpha1$),
  *`angleEnd`* ($\alpha2$) and two radial
  coordinates *`radiusStart`* ($r1$), *`radiusEnd`*
  ($r2$).
  (1) The original image and the parameters defining the annular arc.
  (2) The annular arc, shown in a figure where the polar
  coordinates form an equidistant grid obtained by
  [`PolarTransImageExt`](polar_trans_image_ext.md).
  (3) The annular arc in the representation of the original image.
  The Cartesian coordinates have been obtained through
  [`PolarTransImageInv`](polar_trans_image_inv.md) on image (2).
  The origin is in the center of the pixel in the upper left corner.

  Polar coordinates are used by the following operators:

  - [`PolarTransImageExt`](polar_trans_image_ext.md)
  - [`PolarTransImageInv`](polar_trans_image_inv.md)
  - [`PolarTransRegion`](polar_trans_region.md)
  - [`PolarTransRegionInv`](polar_trans_region_inv.md)
  - [`PolarTransContourXld`](polar_trans_contour_xld.md)
  - [`PolarTransContourXldInv`](polar_trans_contour_xld_inv.md)
  - [`PolarTransImage`](polar_trans_image.md) (legacy)

### Images with a reduced domain, regions, and models

In the part before we spoke about coordinates of images.
When it comes to the location of the origin of the coordinate system used,
images with reduced domains, regions, and models are treated differently
than images.

- ****Images with a reduced domain and regions**** —

  Both images with a reduced domain and regions keep the
  coordinate system of the image from which they were created.
  This means, they inherit the origin and the points keep the coordinate
  values they had in the original image.
- ****Models**** —

  Models, on the other side, can have a local coordinate system.
  E.g., models obtained over [`CreateGenericShapeModel`](create_generic_shape_model.md) have their
  origin in the center of gravity of the ROI they are created from.
  For further information see the
  `“Solution Guide II-B - Matching”`.

### Calibrated Coordinates

While working with pixel units, we can not extract any information about
real-world distances directly.
When a camera is calibrated, it is possible to rectify the images.
In this case one can assign world coordinates to the image.
For further information we refer to the
`“Solution Guide III-C - 3D Vision”`.

---

#### List of Operators

- [`AffineTransPixel`](affine_trans_pixel.md) — Apply an arbitrary affine 2D transformation to pixel coordinates.

- [`AffineTransPoint2d`](affine_trans_point_2d.md) — Apply an arbitrary affine 2D transformation to points.

- [`DeserializeHomMat2d`](deserialize_hom_mat2d.md) — Deserialize a serialized homogeneous 2D transformation matrix.

- [`GenImageWarpMap`](gen_image_warp_map.md) — Generate an image map based on non-regular correspondence points.

- [`HomMat2dCompose`](hom_mat2d_compose.md) — Multiply two homogeneous 2D transformation matrices.

- [`HomMat2dDeterminant`](hom_mat2d_determinant.md) — Compute the determinant of a homogeneous 2D transformation matrix.

- [`HomMat2dIdentity`](hom_mat2d_identity.md) — Generate the homogeneous transformation matrix of the identical 2D
  transformation.

- [`HomMat2dInvert`](hom_mat2d_invert.md) — Invert a homogeneous 2D transformation matrix.

- [`HomMat2dReflect`](hom_mat2d_reflect.md) — Add a reflection to a homogeneous 2D transformation matrix.

- [`HomMat2dReflectLocal`](hom_mat2d_reflect_local.md) — Add a reflection to a homogeneous 2D transformation matrix.

- [`HomMat2dRotate`](hom_mat2d_rotate.md) — Add a rotation to a homogeneous 2D transformation matrix.

- [`HomMat2dRotateLocal`](hom_mat2d_rotate_local.md) — Add a rotation to a homogeneous 2D transformation matrix.

- [`HomMat2dScale`](hom_mat2d_scale.md) — Add a scaling to a homogeneous 2D transformation matrix.

- [`HomMat2dScaleLocal`](hom_mat2d_scale_local.md) — Add a scaling to a homogeneous 2D transformation matrix.

- [`HomMat2dSlant`](hom_mat2d_slant.md) — Add a slant to a homogeneous 2D transformation matrix.

- [`HomMat2dSlantLocal`](hom_mat2d_slant_local.md) — Add a slant to a homogeneous 2D transformation matrix.

- [`HomMat2dToAffinePar`](hom_mat2d_to_affine_par.md) — Compute the affine transformation parameters from a homogeneous 2D
  transformation matrix.

- [`HomMat2dTranslate`](hom_mat2d_translate.md) — Add a translation to a homogeneous 2D transformation matrix.

- [`HomMat2dTranslateLocal`](hom_mat2d_translate_local.md) — Add a translation to a homogeneous 2D transformation matrix.

- [`HomMat2dTranspose`](hom_mat2d_transpose.md) — Transpose a homogeneous 2D transformation matrix.

- [`HomMat3dProject`](hom_mat3d_project.md) — Project an affine 3D transformation matrix to a 2D projective
  transformation matrix.

- [`HomVectorToProjHomMat2d`](hom_vector_to_proj_hom_mat2d.md) — Compute a homogeneous transformation matrix using given point
  correspondences.

- [`PointLineToHomMat2d`](point_line_to_hom_mat2d.md) — Approximate an affine transformation from point-to-line correspondences.

- [`ProjectiveTransPixel`](projective_trans_pixel.md) — Project pixel coordinates using a homogeneous projective
  transformation matrix.

- [`ProjectiveTransPoint2d`](projective_trans_point_2d.md) — Project a homogeneous 2D point using a projective transformation
  matrix.

- [`SerializeHomMat2d`](serialize_hom_mat2d.md) — Serialize a homogeneous 2D transformation matrix.

- [`VectorAngleToRigid`](vector_angle_to_rigid.md) — Compute a rigid affine transformation from points and angles.

- [`VectorFieldToHomMat2d`](vector_field_to_hom_mat2d.md) — Approximate an affine map from a displacement vector field.

- [`VectorToAniso`](vector_to_aniso.md) — Approximate an anisotropic similarity transformation from point
  correspondences.

- [`VectorToHomMat2d`](vector_to_hom_mat2d.md) — Approximate an affine transformation from point correspondences.

- [`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md) — Compute a projective transformation matrix using given point
  correspondences.

- [`VectorToProjHomMat2dDistortion`](vector_to_proj_hom_mat2d_distortion.md) — Compute a projective transformation matrix and the radial distortion
  coefficient using given image point correspondences.

- [`VectorToRigid`](vector_to_rigid.md) — Approximate a rigid affine transformation from point correspondences.

- [`VectorToSimilarity`](vector_to_similarity.md) — Approximate an similarity transformation from point correspondences.

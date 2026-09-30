# GenSphericalMosaic (Operator)

## Name

`GenSphericalMosaic` — Create a spherical mosaic image.

## Signature

`static void HOperatorSet.GenSphericalMosaic(HObject images, out HObject mosaicImage, HTuple cameraMatrices, HTuple rotationMatrices, HTuple latMin, HTuple latMax, HTuple longMin, HTuple longMax, HTuple latLongStep, HTuple stackingOrder, HTuple interpolation)`

`HImage HImage.GenSphericalMosaic(HHomMat2D[] cameraMatrices, HHomMat2D[] rotationMatrices, HTuple latMin, HTuple latMax, HTuple longMin, HTuple longMax, HTuple latLongStep, HTuple stackingOrder, HTuple interpolation)`

`HImage HImage.GenSphericalMosaic(HHomMat2D[] cameraMatrices, HHomMat2D[] rotationMatrices, double latMin, double latMax, double longMin, double longMax, double latLongStep, string stackingOrder, string interpolation)`

## Description

`GenSphericalMosaic` creates a spherical mosaic image
*`mosaicImage`* from the input images passed in
*`images`*. The pose of the images in space, which is used to
compute the position of the images with respect to the surface of
the sphere, can be determined with
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md). The camera and rotation
matrices computed with [`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md)
can be used in *`cameraMatrices`* and
*`rotationMatrices`*. A spherical mosaic can only be created
from images that were taken with a stationary camera (see
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md)).

The mosaic is computed in spherical coordinates (longitude and
latitude). The row axis of *`mosaicImage`* corresponds to the
latitude, while the column axis corresponds to the longitude. The
part of the sphere that is computed by `GenSphericalMosaic`
is determined by *`latMin`*, *`latMax`*, *`longMin`*,
and *`longMax`*. These parameters are specified in degrees and
determine a rectangular part of the latitude and longitude
coordinates. The latitude *-90* corresponds to the north
pole (i.e., the straight up viewing direction), while *90*
corresponds to the south pole (i.e., the straight down viewing
direction). The longitude *0* corresponds to the straight
ahead viewing direction. Negative longitudes correspond to viewing
directions to the left, while positive longitudes correspond to
viewing directions to the right. Hence, to obtain a complete image
of the sphere, *`latMin`* = *-90*, *`latMax`* =
*90*, *`longMin`* = *-180*, and
*`longMax`* = *180* must be used. In many cases, the
mosaic will not cover the entire sphere. In these cases, it is
useful to select the desired part of the sphere with the above
parameters. This can be done by explicitly specifying the desired
rectangle. However, often it is desirable to determine the smallest
rectangle that encloses all images automatically. This can be done
by using *`latMin`* < *-90*, *`latMax`* >
*90*, *`longMin`* < *-180*, and
*`longMax`* > *180*. Only the parameters that lie
outside the normal range of values are determined automatically.

The angle step per pixel in *`mosaicImage`* can be selected
with *`latLongStep`*, which also is an angle specified in
degrees. With this, the resolution of the mosaic image can be
controlled. If *`latLongStep`* is set to *0* the angle
step is calculated automatically by trying to preserve the pixel
size of the original images as well as possible.

The mode in which the images are added to the mosaic is given by
*`stackingOrder`*. For *`stackingOrder`* =
*"voronoi"*, the points in the mosaic image are determined
from the Voronoi cell of the respective input image. This means
that the gray values are taken from the points of the input image to
whose center the pixel in the mosaic image has the smallest distance
on the sphere. This mode has the advantage that vignetting and
uncorrected radial distortions are less noticeable in the mosaic
image because they typically are symmetric with respect to the image
center. Alternatively, with the choice of parameters described
described in the following, a mode can be selected that has the same
effect as if the images were painted successively into the mosaic
image. Here, the order in which the images are added to the mosaic
image is important. Therefore, an array of integer values can be
passed in *`stackingOrder`*. The first index in this array
will end up at the bottom of the image stack while the last one will
be on top. If *"default"* is given instead of an array of
integers, the canonical order (images in the order used in
*`images`*) will be used. Hence, if neither *"voronoi"*
nor *"default"* are used, *`stackingOrder`* must contain
a permutation of the numbers 1,...,n, where n is the number of
images passed in *`images`*. It should be noted that the mode
*"voronoi"* cannot always be used. For example, at least
two images must be passed to use this mode. Furthermore, for very
special configurations of the positions of the image centers on the
sphere, the Voronoi cells cannot be determined uniquely. With
*`stackingOrder`* = *"blend"*, an additional mode is
available, which blends the images of the mosaic smoothly. This way seams
between the images become less apparent. The seam lines between the images
are the same as in *"voronoi"*. This mode leads to visually more
appealing images, but requires significantly more resources. If the
mode *"voronoi"* or *"blend"* cannot be used for whatever
reason the mode is switched internally to *"default"* automatically.

The parameter *`interpolation`* selects the desired interpolation mode
for creating the mosaic. *"bilinear"* and *"bicubic"*
interpolation is available for all modes of *`stackingOrder`*.
*"nearest_neighbor"* is only available if *`stackingOrder`* is
set to *"default"* or *"voronoi"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`images`** (input_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2 / real)

Input images.

**`mosaicImage`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`cameraMatrices`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

(Array of) 3x3 projective
camera matrices that determine the internal
camera parameters.

**`rotationMatrices`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3x3
transformation matrices that determine
rotation of the camera in the respective
image.

**`latMin`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum latitude of points in the spherical
mosaic image.

Default:
-90

Suggested values:
-100, -90, -80, -70, -60, -50, -40, -30, -20, -10

Restriction:
`LatMin <= 90`

**`latMax`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum latitude of points in the spherical
mosaic image.

Default:
90

Suggested values:
10, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`LatMax >= -90 && LatMax > LatMin`

**`longMin`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum longitude of points in the spherical
mosaic image.

Default:
-180

Suggested values:
-200, -180, -160, -140, -120, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10

Restriction:
`LongMin <= 180`

**`longMax`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum longitude of points in the spherical
mosaic image.

Default:
180

Suggested values:
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200

Restriction:
`LongMax >= -90 && LongMax > LongMin`

**`latLongStep`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Latitude and longitude angle step width.

Default:
0.1

Suggested values:
0, 0.02, 0.05, 0.1, 0.2, 0.5, 1

Restriction:
`LatLongStep >= 0`

**`stackingOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Mode of adding the images to the mosaic image.

Default:
"voronoi"

Suggested values:
"blend", "voronoi", "default"

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Mode of interpolation when creating the mosaic image.

Default:
"bilinear"

Suggested values:
"nearest_neighbor", "bilinear", "bicubic"

## Example (HDevelop)

```
* For the input data to stationary_camera_self_calibration, please
* refer to the example for stationary_camera_self_calibration.
stationary_camera_self_calibration (4, 640, 480, 1, From, To, \
                                    HomMatrices2D, Rows1, Cols1, \
                                    Rows2, Cols2, NumMatches, \
                                    'gold_standard', \
                                    ['focus','principal_point'], \
                                    'true', CameraMatrix, Kappa, \
                                    RotationMatrices, X, Y, Z, Error)
gen_spherical_mosaic (Images, MosaicImage, CameraMatrix, \
                      RotationMatrices, -100, 100, -200, 200, 0, \
                      'default','bilinear')

* Alternatively, if kappa should be determined, the following calls
* can be made:
stationary_camera_self_calibration (4, 640, 480, 1, From, To, \
                                    HomMatrices2D, Rows1, Cols1, \
                                    Rows2, Cols2, NumMatches, \
                                    'gold_standard', \
                                    ['focus','principal_point','kappa'], \
                                    'true', CameraMatrix, Kappa, \
                                    RotationMatrices, X, Y, Z, Error)
cam_mat_to_cam_par (CameraMatrix, Kappa, 640, 480, CamParam)
change_radial_distortion_cam_par ('fixed', CamParam, 0, CamParOut)
gen_radial_distortion_map (Map, CamParam, CamParOut, 'bilinear')
map_image (Images, Map, ImagesRect)
gen_spherical_mosaic (ImagesRect, MosaicImage, CameraMatrix, \
                      RotationMatrices, -100, 100, -200, 200, 0, \
                      'default','bilinear')
```

## Result

If the parameters are valid, the operator
`GenSphericalMosaic` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`StationaryCameraSelfCalibration`

## Alternatives

`GenCubeMapMosaic`,
`GenProjectiveMosaic`

## References

Lourdes Agapito, E. Hayman, I. Reid: “Self-Calibration of Rotating
and Zooming Cameras”; International Journal of Computer Vision;
vol. 45, no. 2; pp. 107--127; 2001.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching

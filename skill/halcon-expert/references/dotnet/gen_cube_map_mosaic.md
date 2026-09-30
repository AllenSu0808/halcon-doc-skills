# GenCubeMapMosaic (Operator)

## Name

`GenCubeMapMosaic` — Create 6 cube map images of a spherical mosaic.

## Signature

`static void HOperatorSet.GenCubeMapMosaic(HObject images, out HObject front, out HObject rear, out HObject left, out HObject right, out HObject top, out HObject bottom, HTuple cameraMatrices, HTuple rotationMatrices, HTuple cubeMapDimension, HTuple stackingOrder, HTuple interpolation)`

`HImage HImage.GenCubeMapMosaic(out HImage rear, out HImage left, out HImage right, out HImage top, out HImage bottom, HHomMat2D[] cameraMatrices, HHomMat2D[] rotationMatrices, int cubeMapDimension, HTuple stackingOrder, string interpolation)`

`HImage HImage.GenCubeMapMosaic(out HImage rear, out HImage left, out HImage right, out HImage top, out HImage bottom, HHomMat2D[] cameraMatrices, HHomMat2D[] rotationMatrices, int cubeMapDimension, string stackingOrder, string interpolation)`

## Description

`GenCubeMapMosaic` creates 6 cube map images of a spherical
mosaic *`front`*, *`left`*, *`rear`*, *`right`*,
*`top`* and *`bottom`* from the input images passed in
*`images`*. The pose of the images in space, which is used to
compute the position of the images with respect to the surface of
the sphere, can be determined with
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md). The camera and rotation
matrices computed with [`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md)
can be used in *`cameraMatrices`* and
*`rotationMatrices`*. A spherical mosaic can only be created
from images that were taken with a stationary camera (see
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md)).

The width and height of the output cube map images can be selected by
setting the parameter *`cubeMapDimension`*. The value represents
the width and height in pixels.

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
in the following, a mode can be selected that has the same
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
for creating the cube maps. *"bilinear"* and *"bicubic"*
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

**`front`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Front cube map.

**`rear`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Rear cube map.

**`left`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Left cube map.

**`right`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Right cube map.

**`top`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Top cube map.

**`bottom`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Bottom cube map.

**`cameraMatrices`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

(Array of) 3x3 projective
camera matrices that determine the internal
camera parameters.

**`rotationMatrices`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3x3
transformation matrices that determine
rotation of the camera in the respective
image.

**`cubeMapDimension`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Width and height of the resulting cube maps.

Default:
1000

Restriction:
`CubeMapDimension >= 0`

**`stackingOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Mode of adding the images to the mosaic image.

Default:
"voronoi"

Suggested values:
"blend", "voronoi", "default"

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of image interpolation.

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
gen_cube_map_mosaic (Images, Front, Left, Rear, Right, Top, Bottom, \
                     CameraMatrix, RotationMatrices, 1000, 'default', \
                     'bicubic')

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
gen_cube_map_mosaic (Images, Front, Left, Rear, Right, Top, Bottom, \
                     CameraMatrix, RotationMatrices, 1000, 'default', \
                     'bicubic')
```

## Result

If the parameters are valid, the operator
`GenCubeMapMosaic` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`StationaryCameraSelfCalibration`

## Alternatives

`GenSphericalMosaic`,
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

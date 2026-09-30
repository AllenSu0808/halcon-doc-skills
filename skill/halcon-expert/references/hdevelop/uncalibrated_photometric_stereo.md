# uncalibrated_photometric_stereo (Operator)

## Name

`uncalibrated_photometric_stereo` — Reconstruct a surface from several, differently illuminated images.

## Signature

`uncalibrated_photometric_stereo(Images : NormalField, Gradient, Albedo : ResultType : )`

## Description

`uncalibrated_photometric_stereo` can be used to extract high-frequency
surface details from a given object with no prior knowledge about the
illumination, geometry and reflectance of the object. The geometry of
interest can be for example dents, folds or scratches. The operator can
usually not be used for measuring the overall shape of an object.
The operator returns the normals *`NormalField`* of the surface as
a 3-channel image with each image encoding a component of the normal.
This is used as a visualization of the result as a color coded image.
Further, it returns the *`Gradient`* and the *`Albedo`* of the
surface. Which result should be calculated can be controlled with
*`ResultType`*.
This operator is related to [`photometric_stereo`](photometric_stereo.md), but does not
require known (i.e. previously calibrated) light directions. Note that
[`photometric_stereo`](photometric_stereo.md) is faster and more accurate, but needs the
light direction information.
For sensible results an orthographic projection of the
camera is assumed for both the calibrated and uncalibrated case.
This is typically reached by using a telecentric lens or at least a lens
with a long focal distance.

The operator requires at least three images of the same object, taken with a
static, non-moving camera and different lighting directions for each image.
For best results, the object should exhibit Lambertian reflection properties,
no inter-reflection or shadow castings.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Images`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2)

The input images with different illumination.

**`NormalField`** (output_object)  image(-array) `→` object (real)

The normal field of the surface.

**`Gradient`** (output_object)  image `→` object (vector_field)

The gradient field of the surface .

**`Albedo`** (output_object)  image `→` object (real)

The albedo of the surface.

**`ResultType`** (input_control)  string-array `→`  (string)

The result type.

Default:
'all'

List of values:
[], 'albedo', 'all', 'gradient', 'normal_field', 'normalized_gradient'

## Example (HDevelop)

```
* read severally illuminated images
FName := 'photometric_stereo/pharma_braille_0' + [1:4] + '.png'
read_image(Images, FName)
* extract surface normals, gradients and albedo from images
uncalibrated_photometric_stereo(Images, NormalField, Gradient, Albedo, 'all')
derivate_vector_field (Gradient, Result, 0.1, 'mean_curvature')
reconstruct_height_field_from_gradient (Gradient, HeightField, 'poisson', \
                                        [], [])
```

## Result

The operator `uncalibrated_photometric_stereo` returns the
*`NormalField`* for the given images as well as the appropriate
gradients for each pixel and the *`Albedo`* of the object.

## Alternatives

`photometric_stereo`

## See also

`photometric_stereo`

## References

H. Hayakawa: “Photometric stereo under a light source with arbitrary motion”.
Journal Optical Society America,
Vol. 11, No. 11/November 1994.

## Module

3D Metrology

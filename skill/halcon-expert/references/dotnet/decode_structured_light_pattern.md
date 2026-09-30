# DecodeStructuredLightPattern (Operator)

## Name

`DecodeStructuredLightPattern` — Decode the camera images acquired with a structured light setup.

## Signature

`static void HOperatorSet.DecodeStructuredLightPattern(HObject cameraImages, HTuple structuredLightModel)`

`void HStructuredLightModel.DecodeStructuredLightPattern(HImage cameraImages)`

## Description

`DecodeStructuredLightPattern` decodes the camera images
*`cameraImages`* that have been previously acquired with a structured
light setup. The correspondence images and other intermediate results that
are created by the decoding process are stored in the model
*`structuredLightModel`* and can be accessed afterwards using the
operator [`GetStructuredLightObject`](get_structured_light_object.md).

In the following, the decoding process is explained in detail:

As mentioned in [`GenStructuredLightPattern`](gen_structured_light_pattern.md) the first purpose is to
find out whether a pixel is in a region illuminated by a light stripe or
illuminated by a dark stripe. To simplify this decision process the
normalization images are used and a locally varying threshold is
determined that is able to cope with objects of varying reflectance or
brightness and lighting conditions.
During the decoding of the acquired camera images all Gray code images are
then compared with the previously calculated threshold. A pixel within the
image is classified as bright if its gray value is greater or
equal this threshold.

Furthermore, the pattern region is segmented during the decoding process.
The segmentation is controlled by the parameter
*"min_gray_difference"*
(see [`SetStructuredLightModelParam`](set_structured_light_model_param.md)).

Assuming that n Gray code images have been processed, we get a n-bit binary
code for each pixel. From this sequence the row and column
coordinates up to $\min\_stripe\_width / 2$ ![figure](../assets/0275e6c223e1464d.svg) of
the monitor or projector can be derived.

If the *`structuredLightModel`* is a hybrid system consisting not only
of Gray code images but also of phase shift images
(see [`GenStructuredLightPattern`](gen_structured_light_pattern.md)), the next step is to decode the
latter ones. The result is a subpixel-precise correspondence image between
the monitor or projector coordinates and the camera coordinates that contains
the information which camera pixel observes which monitor or projector pixel.

If the *"pattern_type"* of the *`structuredLightModel`* is set to
*"single_stripe"*, the first step in the decoding process is to
decide which single stripe shed its light on a camera pixel. The Gray code
sequence and phase are then used to refine the position within the
found single stripe.

In real world setups it may occur that the detected Gray code sequence of a
pixel is wrong. This can then lead to values in the correspondence
images which represent monitor or projector rows or columns larger than the
monitor or projector width
and height. To avoid these problems, the last step of the decoding process is
to remove these values from the correspondence images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- structuredLightModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`cameraImages`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Acquired camera images.

**`structuredLightModel`** (input_control, state is modified)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Set the size of the monitor
set_structured_light_model_param (StructuredLightModel, \
                                  'pattern_width', 1600)
set_structured_light_model_param (StructuredLightModel, \
                                  'pattern_height', 1200)
* Set the smallest width of the stripes in the pattern
set_structured_light_model_param (StructuredLightModel, \
                                  'min_stripe_width', 8)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Set the expected black/white contrast in the region of interest
set_structured_light_model_param (StructuredLightModel, \
                                  'min_gray_difference', 70)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Get the computed correspondences and defects
get_structured_light_object (CorrespondenceImages, StructuredLightModel, \
                             'correspondence_image')
set_structured_light_model_param (StructuredLightModel, 'derivative_sigma', \
                                  Sigma)
get_structured_light_object (DefectImage, StructuredLightModel, \
                             'defect_image')
```

## Result

The operator `DecodeStructuredLightPattern` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`GenStructuredLightPattern`

## Possible Successors

`GetStructuredLightObject`,
`ReconstructSurfaceStructuredLight`

## See also

`CreateStructuredLightModel`,
`SetStructuredLightModelParam`

## Module

3D Metrology

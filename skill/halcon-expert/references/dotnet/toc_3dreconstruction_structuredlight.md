## Structured Light

List of Sections ↓

This chapter describes the usage of structured light for 3D reconstruction.

### Concept of Structured Light

The basic concept behind structured light is to use a structured
illumination, i.e. an illumination showing well known patterns.
The way those patterns appear in the scene after hitting surfaces
helps to further analyze (e.g., perform an inspection
[Inspection / Structured Light](toc_inspection_structuredlight.md)) or reconstruct the surfaces.

For non-specular (lambertian or diffuse) surfaces, a 3D surface can be
reconstructed using a projector projecting light like an 'inverse camera'.
For every projected pattern image, a camera image of the projection
on the surface is acquired. Using the decoded correspondence between
projector coordinates lighting the camera coordinates, as well as
calibration information, the 3D surface is reconstructed.

In the following, the steps that are required to use structured light
are described briefly.

- **Create a structured light model:** —

  In the first step, a structured light model is created with

  - [`CreateStructuredLightModel`](create_structured_light_model.md)
    (`modelType`=*`"3d_reconstruction"`*)

  or read with

  - [`ReadStructuredLightModel`](read_structured_light_model.md).
- **Set the model parameters:** —

  The different structured light model parameters can then be set with

  - [`SetStructuredLightModelParam`](set_structured_light_model_param.md)

  or queried with

  - [`GetStructuredLightModelParam`](get_structured_light_model_param.md).

  The pattern parameters
  *`"pattern_width"`*, *`"pattern_height"`*,
  *`"pattern_orientation"`*, and *`"pattern_type"`* specify along
  with the stripe parameters *`"min_stripe_width"`* and
  *`"single_stripe_width"`* the specifications of the pattern images to
  be used to illuminate the surface.
  Finally, the *`"persistence"`* parameter can be enabled to
  debug intermediate results.
- **Generate the pattern images:** —

  The pattern images are to be generated with
  [`GenStructuredLightPattern`](gen_structured_light_pattern.md) after setting all relevant parameters.
  Please ensure that the output images are as needed in the particular setup.
- **Use the patterns to illuminate the surface and acquire the camera
  images:** —

  At this stage, the pattern images are projected.
  The respective image of the illuminated surface is acquired by the camera
  for each pattern image.

  When calibrating the system, images of the illuminated calibration
  object need to be acquired. The calibration process is shown in detail in
  the example program `structured_light_calibration.hdev`.
  The obtained calibration information can then be specified with the
  parameter *`"camera_setup_model"`* of
  [`SetStructuredLightModelParam`](set_structured_light_model_param.md).
- **Decode the acquired images:** —

  The acquired *`cameraImages`* can be decoded with
  [`DecodeStructuredLightPattern`](decode_structured_light_pattern.md). Upon calling this operator, the
  correspondence images are created and stored in the model
  *`structuredLightModel`*.
- **Get the results:** —

  The decoded *`"correspondence_image"`*, as well as other results
  can be queried with [`GetStructuredLightObject`](get_structured_light_object.md). For more
  details of the different objects that can be queried, please refer
  to the operator's documentation.
- **Perform the reconstruction:** —

  The reconstructed surface can be obtained with
  [`ReconstructSurfaceStructuredLight`](reconstruct_surface_structured_light.md).

### Further operators

The structured light model offers various other operators that help access
and update the various parameters of the model.

The operator [`WriteStructuredLightModel`](write_structured_light_model.md) enables writing the
structured light model to a file. Please note that previously generated
pattern images are not written in this file. A structured light model file
can be read using [`ReadStructuredLightModel`](read_structured_light_model.md).

Furthermore, it is possible to serialize and deserialize the structured
light model using [`SerializeStructuredLightModel`](serialize_structured_light_model.md) and
[`DeserializeStructuredLightModel`](deserialize_structured_light_model.md).

### Further Information

See also the `“Solution Guide Basics”` for further details.
For a list of operators, please refer to [Inspection / Structured Light](toc_inspection_structuredlight.md).

---

#### List of Sections

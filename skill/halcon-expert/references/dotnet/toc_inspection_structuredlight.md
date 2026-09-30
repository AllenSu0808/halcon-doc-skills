## Structured Light

List of Operators ↓

This chapter describes the usage of structured light for surface
inspection (deflectometry).

### Concept of Structured Light

The basic concept behind structured light is to use a structured
illumination, i.e. an illumination showing well known patterns.
The way those patterns appear in the scene after hitting surfaces
helps to further analyze or reconstruct the surfaces (see
[3D Reconstruction / Structured Light](toc_3dreconstruction_structuredlight.md)).

Deflectometry is the procedure of analyzing the reflections
of known patterns from specular or semi-specular surfaces. In
such a setup, every pattern image must be shown by the display or monitor.
It is then reflected by the specular surface under test, and
a camera image of the reflection is acquired. Deformations of the pattern
in the camera image are caused by the form of the specular surface
which implies that defects on the specular surface can be detected.

In the following, the steps that are required to use structured light
are described briefly.

- **Create a structured light model:** —

  In the first step, a structured light model is created with

  - [`CreateStructuredLightModel`](create_structured_light_model.md)
    (`modelType`=*`"deflectometry"`*)

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
  be used to illuminate the surface. Finally, the
  *`"persistence"`* parameter can be enabled to debug intermediate
  results.
- **Generate the pattern images:** —

  The pattern images are to be generated with
  [`GenStructuredLightPattern`](gen_structured_light_pattern.md) after setting all relevant parameters.
  Please ensure that the output images are as needed in the particular setup.
- **Use the patterns to illuminate the surface and acquire the camera images:** —

  At this stage, the pattern images are shown on the display.
  The respective image of the illuminated surface is acquired by the camera
  for each pattern image.
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

  The *`"defect_image"`* can also be generated and queried with
  [`GetStructuredLightObject`](get_structured_light_object.md).

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

---

#### List of Operators

- [`ClearStructuredLightModel`](clear_structured_light_model.md) — Clear a structured light model and free the allocated memory.

- [`CreateStructuredLightModel`](create_structured_light_model.md) — Create a structured light model.

- [`DecodeStructuredLightPattern`](decode_structured_light_pattern.md) — Decode the camera images acquired with a structured light setup.

- [`DeserializeStructuredLightModel`](deserialize_structured_light_model.md) — Deserialize a structured light model.

- [`GenStructuredLightPattern`](gen_structured_light_pattern.md) — Generate the pattern images to be displayed in a structured light setup.

- [`GetStructuredLightModelParam`](get_structured_light_model_param.md) — Query parameters of a structured light model.

- [`GetStructuredLightObject`](get_structured_light_object.md) — Get (intermediate) iconic results of a structured light model.

- [`ReadStructuredLightModel`](read_structured_light_model.md) — Read a structured light model from a file.

- [`ReconstructSurfaceStructuredLight`](reconstruct_surface_structured_light.md) — Reconstruct a surface from a decoded structured light setup.

- [`SerializeStructuredLightModel`](serialize_structured_light_model.md) — Serialize a structured light model.

- [`SetStructuredLightModelParam`](set_structured_light_model_param.md) — Set parameters of a structured light model.

- [`WriteStructuredLightModel`](write_structured_light_model.md) — Write a structured light model to a file.

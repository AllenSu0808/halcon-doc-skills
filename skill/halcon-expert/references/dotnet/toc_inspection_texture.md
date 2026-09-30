## Texture Inspection

List of Operators ↓

This chapter describes the operators for texture inspection.

### Concept of the texture inspection model

The texture inspection model enables the inspection of
textured surfaces with only having to set few parameters. The algorithm
requires images of flawless texture for
training. The training process extracts texture features from the training
images and trains a texture inspection model that is based on
Gaussian Mixture Model (GMM) classifiers.
After a successful training, texture images can be compared to the
texture inspection model and potential defects can be identified.
Texture inspection works on image pyramids. This way, multiple frequency
ranges of the texture are analyzed.

It is possible to use multi-channel images in the texture inspection pipeline.

In the following, the steps that are required to perform the texture
inspection are described briefly.

- **Create a texture inspection model:** —

  In a first step, a texture inspection model is created with

  - [`CreateTextureInspectionModel`](create_texture_inspection_model.md)

  or read with

  - [`ReadTextureInspectionModel`](read_texture_inspection_model.md).
- **Add training samples:** —

  The operator

  - [`AddTextureInspectionModelImage`](add_texture_inspection_model_image.md)

  adds sample images to the texture inspection model.

  ![figure](../assets/d5edca1aa20c96b4.svg)

  Image of a textured surface that is used to train a texture
  inspection model.

  Images that have been added to the texture inspection model with the help
  of [`AddTextureInspectionModelImage`](add_texture_inspection_model_image.md) can be viewed with
  [`GetTextureInspectionModelImage`](get_texture_inspection_model_image.md). If all or a part of the added
  images are not needed for the current texture inspection, they can be removed
  from the model using [`RemoveTextureInspectionModelImage`](remove_texture_inspection_model_image.md).
- **Train a texture inspection model:** —

  The texture inspection model is trained with

  - [`TrainTextureInspectionModel`](train_texture_inspection_model.md).

  In the training process an image pyramid is created. For each pyramid
  level a Gaussian Mixture Model
  (GMM) is trained and a *`"novelty_threshold"`* is determined. The
  *`"novelty_threshold"`* helps to distinguish between flawless and
  defective texture. After the training, it is possible to query the
  novelty thresholds with [`GetTextureInspectionModelParam`](get_texture_inspection_model_param.md).

  Several parameters influence the training. They can be set with

  - [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md).

  We recommend the following proceeding for the training:

  - Set initial parameters for the training, if needed:

    - *`"patch_normalization"`*: Setting this parameter to
      *`"weber"`*, the features of the used texture patches are
      normalized making the texture inspection model more robust against
      illumination changes. Note, however, that sometimes a normalization
      might not be desired, e.g., if the brightness is needed to
      discriminate between flawless and defective parts. In that case, a
      controlled illumination is absolutely necessary for a successful
      classification.
    - *`"patch_rotational_robustness"`*: Setting this parameter to
      *`"true"`*, the features of the used texture patches are sorted in
      a way that is robust against rotational changes. This can be used if
      it is difficult to train all possible orientations of the textured
      surface via training samples.
  - Train the texture inspection model (using the default parameters): The
    initial training of the texture inspection model may be very time consuming,
    depending on the number of training images and their resolution. The
    following time saving strategies can be considered:

    - Zoom the images: Often, the texture inspection works even better
      on low resolution images. If it is known that the full resolution of
      the images is not needed, you can significantly reduce the training
      time by zooming the images. Zooming the image down by a factor of 2,
      e.g., reduces the training time by factor 4.
    - Accelerate the training: Another, but more risky strategy is to
      increase the threshold for the stopping criterion of the classifier
      optimization by setting the parameter *`"gmm_em_threshold"`*,
      e.g., from *0.001* to *0.1*. This leads to shorter
      training times but also to a possibly less accurate texture inspection
      model. If this strategy is used, we strongly recommend to reduce
      *`"gmm_em_threshold"`* again after most of the parameters have been
      adjusted.
  - Check the result of the training: Use a set of images with defective
    textures, classify them with the trained texture inspection model and check
    the results as is described for the step 'Apply the texture
    inspection model'. If the results are not satisfying, further parameters can
    be adjusted for the training. The most important parameters are:

    - *`"num_levels"`* or *`"levels"`*: The number of
      pyramid levels or the number of explicitly used pyramid levels.
      Higher pyramid levels work on coarser texture features.
      If the texture in your images is very coarse, the lower
      pyramid levels may not be needed for a successful inspection.
      Then runtime can be reduced by setting the
      pyramid levels of interest explicitly with *`"levels"`*. If for
      example the *`"levels"`* are set to [1,3], the training and the
      texture classification are only performed on the first and third level.
    - *`"sensitivity"`*: Controls how strict the novelty thresholds
      are set. This way, the sensitivity to novelties can be adjusted. In
      general, positive values lead to fewer detected defects and negative
      values lead to less detected defects.
    - *`"novelty_threshold"`*: Sets the novelty threshold manually.
      This can be used for fine tuning if the results of the automatic
      estimation are not optimal.
  - Repeat the training, if needed: If parameters were adjusted, usually
    the texture inspection model has to be retrained.
- **Apply the texture inspection model:** —

  After successfully training the
  texture inspection model it can be used to classify textured surfaces. Each
  test image can be compared to the texture inspection model with

  - [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md).

  ![figure](../assets/acdaaa15e9041682.svg)

  Test image with defects.

  For each test image the operator returns a *`"novelty_region"`*, which
  indicates where the image has high deviations to the trained texture samples.
  The *`"novelty_region"`* is generated by
  combining the novelty regions of the different pyramid levels. The novelty
  regions of adjacent levels in the image pyramid are intersected with each
  other. This step helps to improve the robustness towards noise within the
  single pyramid level responses. The intersected novelty regions are then
  added to the returned *`"novelty_region"`*. If a pyramid level has no
  adjacent pyramid level, the region itself is added to the
  *`"novelty_region"`*. If, for example, *`"num_levels"`* is set to 1,
  no adjacent pyramid level exists and the *`"novelty_region"`* is the
  novelty region of the first pyramid level.

  For debugging, the parameter *`"gen_result_handle"`* can be set to
  *`"true"`* with [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md). This way,
  the novelty score images and novelty regions of the individual pyramid
  levels are stored in a result handle.
  They can then be read with

  - [`GetTextureInspectionResultObject`](get_texture_inspection_result_object.md).

  In general, the novelty score images describe how well each pixel
  fits to the texture inspection model that was created within the training
  process. The novelty regions of the single pyramid levels are then
  calculated by applying the *`"novelty_threshold"`* to the
  corresponding novelty score images.

  Inspecting the novelty score images and the novelty regions provides you with
  hints which kinds of errors are detectable on which pyramid levels. Thus,
  you can decide whether parameters for the training and the classification
  should be adjusted, e.g., whether it is reasonable to explicitly select only
  a subset of pyramid levels using the parameter *`"levels"`*.

  |  |  |
  | --- | --- |
  | ![figure](../assets/064986abf85a2839.svg) | ![figure](../assets/d3783b67628498e1.svg) |
  | ( 1) | ( 2) |

  The resulting *`"novelty_score_image"`* (1) and the resulting
  *`"novelty_region"`* (2) for the test image above.

### Further operators

The functionality of the texture inspection can be altered by various
parameters. The parameters can be queried with
[`GetTextureInspectionModelParam`](get_texture_inspection_model_param.md) and altered with calls to
[`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md).

It is possible to write a texture inspection model to file with the
operator [`WriteTextureInspectionModel`](write_texture_inspection_model.md). Thereby, only the texture
inspection model is stored. The images which were possibly added can be
queried with the help of [`GetTextureInspectionModelImage`](get_texture_inspection_model_image.md)
and stored separately by calling [`WriteObject`](write_object.md).

To help reduce the memory required by the texture inspection model, it is
possible to delete previously added images from the model with
[`RemoveTextureInspectionModelImage`](remove_texture_inspection_model_image.md).

Furthermore, it is possible to serialize and deserialize the texture
inspection model with [`SerializeTextureInspectionModel`](serialize_texture_inspection_model.md)
and [`DeserializeTextureInspectionModel`](deserialize_texture_inspection_model.md).

### Glossary

In the following, the most important terms that are used in the context of
texture inspection are described:

- **Training images** —

  Images that are used for training.
- **Test images** —

  Images which are compared to the trained texture
  inspection model.
- **Patch** —

  A collection of neighboring pixels.
- **Texture feature** —

  The pixel values within a patch.
- **Sample** —

  A texture feature that is used for training.
- **Novelty Score** —

  In the test process the texture features of the test
  images are compared to the texture inspection model and their
  *novelty score* is calculated. The larger this value, the more
  probable it is that the individual texture feature does not fit to the
  texture inspection model.
- **Novelty Threshold** —

  The novelty threshold is determined during the
  training process. Texture features with a novelty score below the novelty
  threshold fit to the texture inspection model. Texture features with a higher
  novelty score do not.

---

#### List of Operators

- [`AddTextureInspectionModelImage`](add_texture_inspection_model_image.md) — Add training images to the texture inspection model.

- [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md) — Inspection of the texture within an image.

- [`ClearTextureInspectionModel`](clear_texture_inspection_model.md) — Clear a texture inspection model and free the allocated memory.

- [`ClearTextureInspectionResult`](clear_texture_inspection_result.md) — Clear a texture inspection result handle and free the allocated memory.

- [`CreateTextureInspectionModel`](create_texture_inspection_model.md) — Create a texture inspection model.

- [`DeserializeTextureInspectionModel`](deserialize_texture_inspection_model.md) — Deserialize a serialized texture inspection model.

- [`GetTextureInspectionModelImage`](get_texture_inspection_model_image.md) — Get the training images contained in a texture inspection model.

- [`GetTextureInspectionModelParam`](get_texture_inspection_model_param.md) — Query parameters of a texture inspection model.

- [`GetTextureInspectionResultObject`](get_texture_inspection_result_object.md) — Query iconic results of a texture inspection.

- [`ReadTextureInspectionModel`](read_texture_inspection_model.md) — Read a texture inspection model from a file.

- [`RemoveTextureInspectionModelImage`](remove_texture_inspection_model_image.md) — Clear all or a user-defined subset of the images of a
  texture inspection model.

- [`SerializeTextureInspectionModel`](serialize_texture_inspection_model.md) — Serialize a texture inspection model.

- [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md) — Set parameters of a texture inspection model.

- [`TrainTextureInspectionModel`](train_texture_inspection_model.md) — Train a texture inspection model.

- [`WriteTextureInspectionModel`](write_texture_inspection_model.md) — Write a texture inspection model to a file.

# set_generic_shape_model_param (Operator)

## Name

`set_generic_shape_model_param` — Set selected parameters of the shape model.

## Signature

`set_generic_shape_model_param( : : ModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_generic_shape_model_param` sets the parameters
*`GenParamName`* of the shape model *`ModelID`* to the values
given in *`GenParamValue`*.

Various aspects of the matching process can be controlled by the parameters
that can be selected by *`GenParamName`*.
In the descriptions below they are grouped into the following
categories (where the category represents the main purpose but not
necessarily the only purpose of the parameter listed within):

- **Modifying the Model** —
- **Finding Model Instances** —
  1. Modify the Instance
  2. Sort out Found Matches
  3. Gray Value Treatment
  4. Refinement
  5. Image Pyramid
  6. Clutter
  7. Regarding the Output
- **Computational Resources During a Search** —
- **Sample-based Training** —

In the following we list the settable parameters for the different categories
and specify cases in which parameter values are modified automatically.

### Modifying the Model

In this paragraph we list and explain parameters modifying the model
*`ModelID`* itself.
Changing a corresponding value makes it necessary to train the adjusted model
before the matching (see [`train_generic_shape_model`](train_generic_shape_model.md)).
The supported parameters *`GenParamName`* are:

- **Contrast** —

  The contrast is a measure for local gray value differences that are used
  to distinguish the object from the background or different parts of the
  object from each other.
  For the model only those pixels are selected which show the asked contrast,
  i.e., gray value difference to neighboring pixels.
  This asked contrast can be a simple threshold or a hysteresis threshold,
  depending on the values set for *'contrast_low'* and
  *'contrast_high'*:

  - Simple threshold:

    - Both are set to the same value which is not *'auto'*.
    - One of the parameters is set to *'auto'* while the other
      one is set to an other value.
  - Hysteresis threshold:

    - Both are set to different values which are both not *'auto'*.
    - Both are set to *'auto'*.

    In these cases the model is segmented using a method similar to the
    hysteresis threshold method used in [`edges_image`](edges_image.md).
    For more information about the hysteresis
    threshold method, see [`hysteresis_threshold`](hysteresis_threshold.md).

  Note, such a contrast is not used in case of training with XLD.
  For more information about contrast and its impact on shape model matching,
  we refer to the `“Solution Guide II-B - Matching”`.

  In certain cases, it might happen that the automatic determination of
  the contrast thresholds is not sufficient. For example, a manual setting
  of these parameters should be preferred if certain model components should
  be included or suppressed due to application-specific reasons or if the
  object features several different contrasts. The contrast
  thresholds should be verified using [`inspect_shape_model`](inspect_shape_model.md) before
  calling [`train_generic_shape_model`](train_generic_shape_model.md).

  - *'contrast_high'*:

    Determines together with
    *'contrast_low'* the gray value difference a pixel must have to
    be considered as being part of the model, see the explanation above.
    In case of a hysteresis threshold this parameter sets the maximum.

    Suggested values:
     *'auto'*, *90*, *80*.

    Restriction:
     Not used in case of training with XLD.

    Default:
     *'auto'*.
  - *'contrast_low'*:

    Determines together with
    *'contrast_high'* the gray value difference a pixel must have to
    be considered as being part of the model, see the explanation above.
    In case of a hysteresis threshold this parameter sets the minimum.

    Suggested values:
     *'auto'*, *10*, *20*.

    Restriction:
     Not used in case of training with XLD.

    Default:
     *'auto'*.
- **Rotation** —

  Shape models are created with a rotation range starting at *0* and
  ending at *6.28* (=$2\pi$), which can be restricted during
  the search. The parameter space, thus discretization steps for the angles
  can be modified using:

  - *'angle_step'*:

    Determines the step length within the selected range of angles.
    Its value should be chosen based on the size of the object.
    Smaller models do not have many different discrete rotations in the image,
    and hence it is recommended to choose larger values for smaller models.
    If set to *'auto'*, its value is estimated during the call
    of [`train_generic_shape_model`](train_generic_shape_model.md).
    The set value is clipped to a maximal value of *0.20*
    (=$\frac{\pi}{16}$ ![figure](../assets/85e34d1585cfbf57.svg)).

    Suggested values:
     *'auto'*, *0.1*, *0.2*.

    Attention:
     Modifications necessitate a model (re)training.

    Default:
     *'auto'*.
- **Scaling** —

  The parameter space, thus discretization steps for the scaling
  can be modified using scaling parameters.
  Which ones can be set depends on the type of scaling, see
  the overview in the following table.
  A scaling value of *1.0* corresponds to the original size of the
  model in the according direction.

  |  |  |  |
  | --- | --- | --- |
  | *`GenParamName`* | isotropic scaling | anisotropic scaling |
  | *'iso_scale_max'* | x |  |
  | *'iso_scale_min'* | x |  |
  | *'iso_scale_step'* | x |  |
  | *'scale_row_max'* |  | x |
  | *'scale_row_min'* |  | x |
  | *'scale_row_step'* |  | x |
  | *'scale_column_max'* |  | x |
  | *'scale_column_min'* |  | x |
  | *'scale_column_step'* |  | x |

  - *'iso_scale_max'*:

    Determines the maximum of the range of
    possible isotropic scaling for which the model is searched.

    Suggested values:
     *1.0*, *1.1*, *1.2*.

    Default:
     *1.0*.
  - *'iso_scale_min'*:

    Determines the minimum of the range of possible isotropic scaling for
    which the model is searched.

    Suggested values:
     *1.0*, *0.9*, *0.8*.

    Default:
     *1.0*.
  - *'iso_scale_step'*:

    Determines the step length within the selected range of isotropic scales.
    The value *'auto'* means its value is estimated during the call of
    [`train_generic_shape_model`](train_generic_shape_model.md).
  - *'scale_row_max'*:

    Determines the maximum of the range of possible scaling in row direction
    for which the model is searched.

    Suggested values:
     *1.0*, *1.1*, *1.2*.

    Default:
     *1.0*.
  - *'scale_row_min'*:

    Determines the minimum of the range of possible scaling in row direction
    for which the model is searched.

    Suggested values:
     *1.0*, *0.9*, *0.8*.

    Default:
     *1.0*.
  - *'scale_row_step'*:

    Determines the step length within the selected range of scales in row
    direction.
    The value *'auto'* means its value is estimated during the call of
    [`train_generic_shape_model`](train_generic_shape_model.md).
  - *'scale_column_max'*:

    Determines the maximum of the range of possible scaling in column
    direction for which the model is searched.

    Suggested values:
     *1.0*, *1.1*, *1.2*.

    Default:
     *1.0*.
  - *'scale_column_min'*:

    Determines the minimum of the range of possible scaling in column
    direction for which the model is searched.

    Suggested values:
     *1.0*, *0.9*, *0.8*.

    Default:
     *1.0*.
  - *'scale_column_step'*:

    Determines the step length within the selected range of scales in column
    direction.
    The value *'auto'* means its value is estimated during the call of
    [`train_generic_shape_model`](train_generic_shape_model.md).
- **Metric** —
  - *'metric'*:

    Determines the conditions under which
    the model is recognized in the image. Supported values for
    *'metric'* are:

    - *'auto'*:

      The value is determined during the call of
      [`train_generic_shape_model`](train_generic_shape_model.md) depending if the training is done
      using an image (*'use_polarity'*) or XLDs
      (*'ignore_local_polarity'*).
    - *'use_polarity'*:

      An instance in the image and the model must have the same contrast.

      *Example:* The model has been created with a bright object on a
      dark background.
      Only instances are found if they are also brighter than the background.

      Restriction:
       Only applied to single-channel images.
      In case of multichannel images, only the first channel is used
      (without error message).
    - *'ignore_global_polarity'*:

      An instance is found in the
      image also if the contrast reverses globally.
      This mode increases the runtime of [`find_generic_shape_model`](find_generic_shape_model.md)
      slightly compared to *'use_polarity'*.

      *Example:* The model has been created with a bright object on a
      dark background.
      Instances are found if they are brighter or darker than the background.

      Restriction:
       Only applied to single-channel images.
      In case of multichannel images, only the first channel is used
      (without error message).
    - *'ignore_local_polarity'*:

      An instance is found even if the contrast changes locally.
      This mode increases the runtime of [`find_generic_shape_model`](find_generic_shape_model.md)
      significantly compared to *'use_polarity'*.

      It is usually recommendable to create several models that reflect the
      possible contrast variations of the object and to match them
      simultaneously.

      *Example:* The model or instance contains a part with
      medium gray values, within which either darker or brighter sub-objects
      may lie.

      Restriction:
       Only applied to single-channel images.
      In case of multichannel images, only the first channel is used
      (without error message).
    - *'ignore_color_polarity'*:

      An instance is found even if the color contrast changes locally.
      This mode can increase the runtime of [`find_generic_shape_model`](find_generic_shape_model.md)
      significantly compared to *'use_polarity'*.

      This metric can be used for images of an arbitrary number of channels,
      which do not need to contain a spectral subdivision of the light
      (like in an RGB image).
      For single-channel images it has the same effect as
      *'ignore_local_polarity'*.
      The number of channels is allowed to differ from the training
      with [`train_generic_shape_model`](train_generic_shape_model.md) to the
      search with [`find_generic_shape_model`](find_generic_shape_model.md).

      *Example:* Instances are found even if parts of the object can
      change their color, e.g., from red to green.

    Restriction:
     Using XLDs, resetting the metric requires that
    the edge-direction information is available as XLD contour attribute.
    For more information see [`set_shape_model_metric`](set_shape_model_metric.md).

    Default:
     *'auto'*.
- **Size** —
  - *'min_size'*:

    Determines the minimum number of points a model
    component must have in order to be considered. Thus, components having
    fewer points than *'min_size'* are suppressed.
    As *'min_size'* is applied on the extent of the components, the
    derived model contours can still be smaller than the specified minimum
    size. This threshold for the minimum size is divided by two for each
    successive pyramid level.
    The effect of this parameter can be checked in advance with
    [`inspect_shape_model`](inspect_shape_model.md).

    If set to *'auto'*, its value is estimated during the call
    of [`train_generic_shape_model`](train_generic_shape_model.md).

    Restriction:
     Not used in case of training with XLD.

    Default:
     *'auto'*.
  - *'optimization'*:

    Determines the number of points by which the model is reduced.
    This reduction can be useful for particularly large models.
    Possible values:

    - *'auto'*:

      The number of points is automatically determined by
      [`train_generic_shape_model`](train_generic_shape_model.md).
    - *'none'*:

      All model points are stored.
    - *'point_reduction_low'*:

      The number of points is reduced to roughly $\frac{1}{2}$ ![figure](../assets/219975bf50d91210.svg).
    - *'point_reduction_medium'*:

      The number of points is reduced to roughly $\frac{1}{3}$ ![figure](../assets/caba96eb9bb80bc3.svg).
    - *'point_reduction_high'*:

      The number of points is reduced to roughly $\frac{1}{4}$ ![figure](../assets/6ceca909d365750f.svg).

    In case the number of model points is reduced it may be necessary to set
    the parameter *'greediness'* to a smaller value,
    e.g., *0.7* or *0.8*.
    Note, for small models reducing the number of model points usually does
    not speed up the search as more potential instances will be examined.

    Default:
     *'auto'*.
- **Image Pyramid** —
  - *'num_levels'*:

    Number of considered image pyramid levels.
    Its value must be chosen such that the model is still recognizable and
    contains a sufficient number of points (at least four) on the highest
    pyramid level.
    This can be checked using the output of [`inspect_shape_model`](inspect_shape_model.md).
    It is advisable to set a value as large as possible as it reduces the
    runtime to find an instance significantly.

    If set to *'auto'*, its value is estimated during the call
    of [`train_generic_shape_model`](train_generic_shape_model.md).

    It can happen that the automatically determined value does not suit.
    If the number of pyramid levels is chosen too large, the model may not be
    recognized in the image or only with very low values for the parameters
    *'min_score'* or *'greediness'*.
    If the number of pyramid levels is chosen too small, the time required
    to find the model in [`find_generic_shape_model`](find_generic_shape_model.md) may increase.
    In both cases, the number of pyramid levels should be selected
    using the output of [`inspect_shape_model`](inspect_shape_model.md).

    Default:
     *'auto'*.
- **Naming** —
  - *'model_identifier'*:

    Overwrites the current identifier string with *`GenParamValue`*.
    The given identifier should be unique to avoid ambiguities
    at e.g., a later match retrieval with
    [`get_generic_shape_model_result`](get_generic_shape_model_result.md).

    Restriction:
     *'model_identifier'*
    must be a non-empty string.
    The following words are reserved and
    cannot be used as identifier names: *'all'*, *'best'*.

    Default:
     The string which is automatically set
    at the shape model creation.

### Finding Model Instances

In this paragraph we list parameters modifying the search of a
*`ModelID`*.
Modifying these parameters does not necessitate a model training,
except they are set from a not-estimated value to a value leading to an
automatic estimation during [`train_generic_shape_model`](train_generic_shape_model.md).
The descriptions of these parameters contain a corresponding note.
The supported parameters *`GenParamName`* are:

1. **Modify the Instance**

   - **Rotation** —
     - *'angle_start'*:

       Determines the start of the range of
       possible rotations for which the model is searched.

       Suggested values:
        *0.0*, *-3.14*,
       *3.14*.

       Default:
        *0.0*.
     - *'angle_end'*:

       Determines the end of the range of
       possible rotations for which the model is searched.

       Suggested values:
        *0.0*, *3.14*, *6.28*.

       Default:
        *6.28* (= $2\pi$).

     *Example:* *'angle_start'* = *'-rad(10)'*,
     *'angle_end'* = *'rad(10)'* searches for matches in the
     range from [rad(350), rad(360)] to [0, rad(10)].
   - **Scaling** —

     The scaling range specified for the trained model
     can be restricted further for the search.
     For these parameters the value *'auto'* means that they do not
     restrict the according range.

     Note, that these restrictions can only be applied if the parameter space is
     further limited. Thus, a smaller maximum and a higher minimum scaling
     parameter needs to be set. Otherwise, the model has to be trained
     anew with adjusted scaling parameters.

     |  |  |  |
     | --- | --- | --- |
     | *`GenParamName`* | isotropic scaling | anisotropic scaling |
     | *'restrict_iso_scale_max'* | x |  |
     | *'restrict_iso_scale_min'* | x |  |
     | *'restrict_scale_row_max'* |  | x |
     | *'restrict_scale_row_min'* |  | x |
     | *'restrict_scale_column_max'* |  | x |
     | *'restrict_scale_column_min'* |  | x |

     - *'restrict_iso_scale_max'*:

       Determines a possibly restricted
       maximum of the range of possible scaling for which the model is
       searched.

       Suggested values:
        *'auto'*, *1.1*, *1.2*.

       Default:
        *'auto'*.
     - *'restrict_iso_scale_min'*:

       Determines a possibly restricted
       minimum of the range of possible scaling for which the model is
       searched.

       Suggested values:
        *'auto'*, *0.9*, *0.8*.

       Default:
        *'auto'*.
     - *'restrict_scale_row_max'*:

       Determines a possibly restricted
       maximum of the range of possible scaling in row direction for which
       the model is searched.

       Suggested values:
        *'auto'*, *1.1*, *1.2*.

       Default:
        *'auto'*.
     - *'restrict_scale_row_min'*:

       Determines a possibly restricted
       minimum of the range of possible scaling in row direction for which
       the model is searched.

       Suggested values:
        *'auto'*, *0.9*, *0.8*.

       Default:
        *'auto'*.
     - *'restrict_scale_column_max'*:

       Determines a possibly
       restricted maximum of the range of possible scaling in column direction
       for which the model is searched.

       Suggested values:
        *'auto'*, *1.1*, *1.2*.

       Default:
        *'auto'*.
     - *'restrict_scale_column_min'*:

       Determines a possibly
       restricted minimum of the range of possible scaling in column direction
       for which the model is searched.

       Suggested values:
        *'auto'*, *0.9*, *0.8*.

       Default:
        *'auto'*.
   - **Deformation** —
     - *'max_deformation'*:

       Determines by how much an object is
       allowed to deviate from the model in order to be considered as a
       match. The maximal allowable object deformation is specified in pixels.
       A value of *0* means no deformation is allowed during the
       search.

       *Example:* An object with a shape deformed by up to 2 pixels with
       respect to the shape of the model can be found with
       *'max_deformation'* = *2*.

       Increasing the value for *'max_deformation'* often results in an
       increased runtime.

       Furthermore, increasing the value for *'max_deformation'*
       increases the risk of obtaining unwanted matches.
       This is especially the case for small objects or objects with fine
       structures because they lose their characteristic shape, which is
       important for a robust search.

       Interplay with *'subpixel'*:
       When deformation is allowed (thus, a value larger *0* is set),
       the score computation depends on the possible subpixel refinement.
       In most cases the score changes if a least-squares adjustment is set.
       Using an adjustment the score might increase when increasing the maximum
       deformation because then for the model points more corresponding image
       points can be found.

       Default:
        *0*.
2. **Sort out Found Matches**

   - *'min_score'*:

     Determines the minimum score a potential match
     must have to be regarded as model instance in the image.
     The larger *'min_score'* is chosen, the faster is the search.
     If the model can be expected never to be occluded in the images,
     *'min_score'* may be set as high as *0.8* or even
     *0.9*.
     If the matches are not tracked to the lowest pyramid level during
     [`find_generic_shape_model`](find_generic_shape_model.md) it might happen that instances with
     a score slightly below *'min_score'* are returned.

     The interplay with *'num_matches'* is explained in the
     description of the latter one.

     Value range:
      [*0.0*, .., *1.0*].

     Default:
      *0.5*.
   - *'num_matches'*:

     Determines the maximum number of returned instances.

     The value *'all'* (or *0*) mean that every instance whose
     score is higher than *'min_score'* is returned.
     The value of *'num_matches_global_enable'* specifies whether a
     certain value of *'num_matches'* is used to restrict the total
     number of matches, regardless of the model.
     For the rest the interplay between *'num_matches'* and
     *'min_score'* as well as *'max_clutter'* (if set) is as
     follows:

     - No clutter set:

       In case there are more than *'num_matches'*
       instances found with a required score, only the *'num_matches'*
       instances with the highest scores are returned.

       In case there are less than *'num_matches'* instances found
       with a required score, only the instances fulfilling the score
       requirement are returned.
     - With clutter set:

       In case there are more than
       *'num_matches'* instances found with a required score and an
       allowed clutter score, only the *'num_matches'* instances with
       the best clutter score are returned.

       In case there are less than *'num_matches'* instances found
       with a required score and / or allowed clutter score, only the
       instances fulfilling the score and clutter score requirement are
       returned.

     Tracking matches through the image pyramid depends whether clutter is
     set:

     - No clutter set:

       On each level (except the top level) less promising matches are rejected
       based on *'num_matches'*.
       By doing so matches may be rejected although they would have obtained
       a higher score on the lowest pyramid level.
       As a result the returned instance for e.g., *'num_matches'* set
       to *1* can differ from the instance with the highest score
       returned when more matches are returned by setting
       *'num_matches'* to *'all'* or a value higher *1*.
       This explains why it might be preferable to return several instances
       and then select the instance with the highest score in case multiple
       objects with a similar score are expected, but only the one with
       the highest score is of interest.
     - With clutter set:

       No matches are rejected during tracking.
       As a result the runtime using clutter parameters will be at least as
       high as the runtime without clutter parameters but returning all
       matches, thus *'num_matches'* set to *'all'*.

     When searching for multiple models at once, *'num_matches'* is
     applied as set for each model individually.

     Default:
      *'all'*.
   - *'num_matches_global_enable'*:

     Determines whether the maximum number of returned matches is restricted
     by *'num_matches'* regardless of the model corresponding to each
     found instance (*'true'*) or not (*'false'*).
     I.e. the instances that best fulfill the given parameter values (such as
     *'min_score'* and *'max_clutter'*) are returned, irrespective
     of the model corresponding to each of those instances.
     For detailed information on the maximum number of returned instances see
     *'num_matches'*.

     It is important to note that the global number of matches is applied to
     all models that are used in a search even if only one model has enabled
     *'num_matches_global_enable'*.

     The value used for the maximum number of returned instances is determined
     as the minimum value of allowed matches set in *'num_matches'* of
     all passed models.

     List of values:
      *'true'*, *'false'*.

     Default:
      *'false'*.
   - *'strict_boundaries'*:

     Determines whether found instances are
     only returned when they are strictly within the given parameter space
     boundaries (*'true'*) or not (*'false'*). The parameter
     space includes all determined angle and scaling ranges (see above).
     Note that such a sort out appears after the reduction to the desired
     *'num_matches'* matches and as a consequence may lead in extreme
     cases to no returned match.

     *Compatibility:* Setting this value on a model not created by
     [`create_generic_shape_model`](create_generic_shape_model.md) will change internal model settings.
     As a consequence, setting for such models *'strict_boundaries'*
     to *'true'* and back to *'false'* may result in a
     different behavior regarding matches found outside the requested search
     range.

     Default:
      *'false'*.
   - *'max_overlap'*:

     Determines by what fraction two instances
     may overlap at most in order to be considered as different instances
     and hence to be returned separately.
     If two instances overlap each other by
     more than *'max_overlap'* only the one with the higher score is
     returned.
     The calculation of the overlap is based on the smallest enclosing
     rectangle of arbitrary orientation (see [`smallest_rectangle2`](smallest_rectangle2.md))
     of the found instances.
     *'max_overlap'* set to *0* means the returned instances
     may not overlap at all, while for *'max_overlap'* = *1*
     all instances are returned, independent of possible overlapping.
     For more information about *'max_overlap'*, we refer to the
     `“Solution Guide II-B - Matching”`.

     Whether the overlap of different models with each other is
     considered when searching for multiple models at once depends on
     *'max_overlap_global_enable'*.

     Restriction:
      *0* $\le$ *'max_overlap'*
     $\le$ *1*.

     Default:
      *0.5*.
   - *'max_overlap_global_enable'*:

     Determines whether the overlap is computed for all found instances
     regardless of the model (*'true'*) or not (*'false'*).
     I.e., the overlap of an instance is computed to the found instances of all
     models and a larger overlap leads to an elimination of this instance.
     For detailed information on the overlap computation see
     *'max_overlap'*.

     It is important to note that the global overlap is applied to all models
     that are used in a search even if only one model has enabled
     *'max_overlap_global_enable'*.

     The value used for the maximum allowed global overlap is determined as the
     minimum of the values set for *'max_overlap'* of all passed
     models.

     List of values:
      *'true'*, *'false'*.

     Default:
      *'false'*.
   - *'max_clutter'*:

     Determines the maximal clutter score a
     potential match can have to be regarded as model instance in the image.
     Of course this applies only to models where clutter is considered, thus
     *'use_clutter'* is set to *'true'*.

     Default:
      *0.0*.
3. **Gray Value Treatment**

   - *'min_contrast'*:

     Determines the minimal contrast
     (gray value difference to neighboring pixels) a point in a search image
     must at least have in order to be compared with the model.
     The main use of this parameter is to exclude noise,
     from the matching process. The operator [`estimate_noise`](estimate_noise.md) can be
     used to assess the noise.

     *Example:* The gray values fluctuate within a range of 10 gray
     levels. In this case it is advisable to set *'min_contrast'*
     = *10*.

     Multichannel images: For a search in a multichannel image using
     *'metric'* set to *'ignore_color_polarity'*, the noise
     in one channel must be multiplied by the square root of the number of
     channels to determine *'min_contrast'*.

     *Example:* The gray values of a 3 channel image fluctuate
     within a range of 10 gray levels in a single channel. In this case
     it is advisable to set *'min_contrast'* = *17*.

     Note, *'min_contrast'* must be smaller than the contrast
     threshold set using *'contrast_low'* and
     *'contrast_high'*, see above.

     The value *'auto'* means its value is estimated during the call
     of [`train_generic_shape_model`](train_generic_shape_model.md) based on the noise in the model
     image.
     Consequently, for a meaningful automatic determination the noise in the
     model image must be similar to the one in the images used during
     recognition.

     *Training*: Changing this value to *'auto'* necessitates
     a training of the shape model.

     Suggested values:
      *'auto'*, *10*, *20*.

     Default:
      *'auto'*.
   - *'border_shape_models'*:

     Determines whether the shape model *`ModelID`* to be found with,
     e.g., [`find_generic_shape_model`](find_generic_shape_model.md), may lie partially outside
     the image (i.e., whether it may cross the image border, independent of
     the domain). Partially means that the model's origin still must be located
     within the image. A different origin set with
     `set_generic_shape_model_param` is not taken into account.

     The value *'system'* means the model uses the system-wide set
     value set by [`set_system`](set_system.md) for the parameter
     *'border_shape_models'*.

     List of values:
      *'system'*, *'true'*,
     *'false'*.

     Default:
      *'system'*.
4. **Refinement**

   - *'subpixel'*:

     Determines which type of subpixel refinement should be carried out.
     Possible values:

     - *'none'*:

       The pose of the model is only determined with pixel accuracy and the
       angle resolution that was specified with *'angle_step'*.
     - *'interpolation'*:

       The pose of the model is interpolated from the score function.
       This mode features very low computation costs.
     - *'least_squares'*:

       The pose of the model is refined using least squares adjustment,
       i.e., by minimizing the distances of the model points to their
       corresponding image points.
     - *'least_squares_high'*:

       The pose of the model is refined using least squares adjustment,
       i.e., by minimizing the distances of the model points to their
       corresponding image points. More minimization iterations are allowed
       than for *'least_squares'*, resulting in a possibly increased
       runtime.
     - *'least_squares_very_high'*:

       The pose of the model is refined using least squares adjustment,
       i.e., by minimizing the distances of the model points to their
       corresponding image points. More minimization iterations are allowed
       than for *'least_squares_high'*, resulting in a possibly
       increased runtime.

     The interplay with *'max_deformation'* is explained in the
     description of latter one.

     Default:
      *'least_squares'*.
   - *'greediness'*:

     Determines how “greedily” the search should be carried out.
     A higher value results in a faster search but a less safe search
     heuristic.

     Restriction:
      *0* $\le$ *'greediness'*
     $\le$ *1*.

     Default:
      *0.9*.
5. **Image Pyramid**

   - *'pyramid_level_highest'*:

     Determines the highest level of the image pyramid used in the search.
     This allows to lower the highest image pyramid level set by the model
     uses during a search.
     Its value can not be higher than the highest image pyramid level of the
     model, which is set through *'num_levels'*.
     As a consequence, *'pyramid_level_highest'* is clipped.
     The value *'auto'* means no lowering is applied, thus the model
     uses the highest pyramid level set through *'num_levels'*.

     Default:
      *'auto'*.
   - *'pyramid_level_lowest'*:

     Determines the lowest level of the image pyramid to which the found
     matches are tracked.
     Not tracking the matches down to the lowest level decreases the runtime
     of the search. But in general the higher the lowest level, the lower the
     accuracy of the extracted pose parameters.
     In extreme cases this can even lead to finding wrong instances of that
     the desired accuracy cannot be achieved.

     Default:
      *1*.
   - *'pyramid_level_robust_tracking'*:

     Determines whether the so-called “increased tolerance mode” is
     active (*'true'*) or not (*'false'*).
     In this mode the lowest image pyramid level on which at least one match
     can be found is automatically determined during the search.
     This mode can be helpful in case of input images of poor quality, e.g.,
     defocused, deformed, or noisy images. In such cases the edge information
     on the lowest image pyramid level may be missing or deformed and as a
     consequence no instances of the shape model can be found.
     Nevertheless, the edge information may be sufficient on higher pyramid
     levels.
     The selection of the suitable pyramid level, i.e., the lowest pyramid
     level on which at least one instance of the shape model can be found,
     depends on the model and on the input image.
     Of course the restrictions on accuracy and robustness mentioned
     for *'pyramid_level_lowest'* occur.
     *Example:* *'pyramid_level_highest'* is set to
     *4*, *'pyramid_level_lowest'* is set to *2*,
     and *'pyramid_level_robust_tracking'* is set to *'true'*.
     Now the matching starts at the fourth pyramid level and tracks the
     matches down to the second lowest pyramid level.
     If no instance of the model can be found on the pyramid level 2, but
     matches have been obtained at a higher level, the lowest pyramid level
     is determined on which at least one instance of the model is found.
     The instances of this pyramid level will then be returned.

     Default:
      *'false'*.
6. **Clutter**

   The following parameters are used to specify the clutter region. Note that
   for this the clutter region has to be set beforehand using
   [`set_generic_shape_model_object`](set_generic_shape_model_object.md).

   - *'use_clutter'*:

     Determines whether the model *`ModelID`*
     considers clutter parameters (*'true'*) or not (*'false'*).
     The runtime using clutter parameters will be at least as high as the
     runtime without clutter parameters but returning all matches, thus
     *'num_matches'* set to *'all'*.

     List of values:
      *'false'*, *'true'*.

     Default:
      *'false'*.
   - *'clutter_contrast'*:

     Determines the minimal contrast which edges in the clutter region must
     have in order to be counted as clutter.

     The polarity of the found clutter edges is ignored, i.e., bright objects
     on a dark background will yield the same clutter score as dark objects
     on a bright background, independent of the parameter *'metric'*
     of the shape model.

     For the value *'auto'* the contrast will be estimated
     automatically.
     Note, a suitable estimation requires that the defining region is
     representative.
     We recommend to check if the estimated value is suitable and adapt it
     otherwise.

     Please note that clutter scores are strongly affected by
     illumination variations.

     Suggested values:
      *'auto'*, *5*, *10*.

     Restriction:
      *'clutter_contrast'* must be larger or
     equal to *'min_contrast'*.

     Default:
      *'auto'*.

     Attention:
      A suitable automatic estimation is not possible for
     shape models generated from XLD contours. Therefore, in such a case
     the estimated value is set to *'min_contrast'*,
     see also the section “Automatic modifications” below.
   - *'max_clutter'*:

     The value *'max_clutter'* specifies the maximum clutter
     score that a match can have in order to be accepted.

     Note, the value of this parameter has no effect on the runtime.

     Value range:
      [*0.0*, *1.0*].

     Default:
      *0.0*.
   - *'clutter_hom_mat_2d'*:

     The clutter region is set relative to the model.
     The transformation matrix *'clutter_hom_mat_2d'* maps
     the model origin to the position of the model instance
     (or rather its center of gravity)
     in the image when the clutter region has been set using
     [`set_generic_shape_model_object`](set_generic_shape_model_object.md).
     Possible Values are:

     - *'auto'*:

       Value is estimated automatically. The clutter region is set relative to
       the model in the template image used by
       [`set_generic_shape_model_object`](set_generic_shape_model_object.md).
     - Transformation matrix: Transformation is given by the user.

     Default:
      *'auto'*.
   - *'clutter_border_mode'*:

     With *'clutter_border_mode'* the behavior of the clutter score
     can be influenced in cases where the clutter region of a found match
     is not entirely contained in the image domain. The corresponding
     values for *'clutter_border_mode'* are:

     - *'clutter_border_average'*:

       When *'clutter_border_average'* is set, the hidden
       part of the clutter region is assumed to be filled on average as is
       its visible part. If the clutter region is not visible at all,
       the clutter score of the found match is set to *0.0*.
     - *'clutter_border_empty'*:

       When *'clutter_border_empty'* is set, the clutter region is
       assumed to be clutter-free where it is not visible.

     Note that *'clutter_border_average'* may result in higher clutter
     scores than *'clutter_border_empty'* even if the match is not
     located at the border of the image domain.

     List of values:
      *'clutter_border_average'*,
     *'clutter_border_empty'*.

     Default:
      *'clutter_border_average'*.
7. **Regarding the Output**

   - *'score_visualization'*:

     Determines whether the score contribution of every model point
     for a found match should be calculated in
     [`find_generic_shape_model`](find_generic_shape_model.md).
     Calculating these score contributions is necessary for
     returning model contours of a score contribution interval from
     `MatchResultID`.
     For how to query the generated contours, see the documentation
     of [`get_generic_shape_model_result_object`](get_generic_shape_model_result_object.md).

     The parameter *'score_visualization'* cannot be
     used in the next call to [`find_generic_shape_model`](find_generic_shape_model.md) if one or
     more of the following is true:

     - the shape model was trained using XLD templates,
     - the shape model was pregenerated,
     - the parameter *'max_deformation'* is set to a value different
       from *0*,
     - the parameter *'pyramid_level_lowest'* is set to a value
       different from *1*,
     - the parameter *'pyramid_level_robust_tracking'* is set to a
       value different from *'false'*.

     To check whether the current model is compatible
     with *'score_visualization'*,
     *'score_visualization_enabled'* can be queried using
     [`get_generic_shape_model_param`](get_generic_shape_model_param.md).

     Attention:
      Activating *'score_visualization'*
     clearly increases the runtime.

     List of values:
      *'true'*, *'false'*.

     Default:
      *'false'*.
   - Origin:

     The origin (reference point) is specified relative to the center of
     gravity of the domain (region) of the image that was used to train the
     shape model with [`train_generic_shape_model`](train_generic_shape_model.md).
     Hence, an origin of (0,0) means that the center of gravity of the domain
     of the template image is used as the origin.
     The origin can be set to a new value using the following parameters:

     - *'origin_row'*:

       Determines the column coordinate of a new, shifted center of origin.

       Default:
        *0*.
     - *'origin_column'*:

       Determines the column coordinate of a new, shifted center of origin.

       Default:
        *0*.

     *Example:* Setting *'origin_column'* = *-20*
     and *'origin_row'* = *-40* results in a new origin lying
     in the upper left of the center of gravity of the model. Please note
     that changing the origin influences the used transformation matrices,
     i.e., the *'clutter_hom_mat_2d'* set by the user and the calculated
     *'hom_mat_2d'* of a match.
   - *'prepare_contours_for_visualization'*:

     Determines whether a found contour of a match should be prepared in
     [`find_generic_shape_model`](find_generic_shape_model.md) and returned in
     `MatchResultID` (*'true'*) or not (*'false'*).
     Deactivating *'prepare_contours_for_visualization'* decreases the
     runtime.
     For how to query the generated contour, see the documentation of
     [`get_generic_shape_model_result_object`](get_generic_shape_model_result_object.md).

     List of values:
      *'true'*, *'false'*.

     Default:
      *'true'*.
   - *'prepare_clutter_region_for_visualization'*:

     Determines whether the clutter region of a match should be prepared in
     [`find_generic_shape_model`](find_generic_shape_model.md) and returned in
     `MatchResultID` (*'true'*) or not (*'false'*).
     Deactivating *'prepare_clutter_region_for_visualization'*
     decreases the runtime.
     For how to query the generated clutter region, see the documentation of
     [`get_generic_shape_model_result_object`](get_generic_shape_model_result_object.md).

     List of values:
      *'true'*, *'false'*.

     Default:
      *'true'*.
   - *'time_measurement'*:

     Determines whether during the search, the time spent in
     individual parts should be measured.
     The individual times are returned in `MatchResultID`,
     see [`get_generic_shape_model_result`](get_generic_shape_model_result.md).

     List of values:
      *'pipeline'*, *'false'*.

     Default:
      *'false'*.

### Computational Resources During a Search

In this paragraph we list parameters concerning technical influences when
searching the model *`ModelID`*.
The supported parameters *`GenParamName`* are:

- *'model_cache'*:

  Determines whether an internal
  cache based on temporary memory is used (*'true'*) or not
  *'false'* during e.g., [`find_generic_shape_model`](find_generic_shape_model.md).
  Switching the *'model_cache'* off (by setting *'false'*)
  sometimes results in slightly longer execution times but constantly
  smaller memory footprint.

  The size of the cache depends on the parameter space, thus if the
  parameter space contains many discretization steps.
  This means a fine search grid with small `step` values covering
  large ranges for `start` to `end` values results in a large
  memory consumption.

  Default:
   *'true'*.
- *'timeout'*:

  Determines the maximum runtime of the operators
  used to find the shape model *`ModelID`*
  (e.g., [`find_generic_shape_model`](find_generic_shape_model.md)).
  The temporal accuracy depends on several factors including the size of
  the model, the speed of the used computer, and the *'timer_mode'*
  set via [`set_system`](set_system.md).
  Be aware that the runtime of the search increases by up to 10 percent with
  activated timeout.

  The value for *'timeout'* must be given in milliseconds.
  To disable the timeout you can either use a negative value or
  *'false'*.

  Suggested values:
   *'false'*, *-1*, *100*.

  Default:
   *'false'*.

### Sample-based Training

Sample-based training allows for the optimization of the model and its
parameters. By providing representative samples before training,
enhanced estimation of specific parameters and/or the removal of
unstable model parts can be performed.
In this paragraph, we list parameters for sample-based training of
*`ModelID`*.
Changing a corresponding value makes it necessary to train the model before
the matching.
The supported parameters *`GenParamName`* are:

- *'training_samples'*:

  Adds training samples to the model for sample-based training. The training
  samples must be passed as a tuple of dictionaries, where each dictionary
  defines exactly one sample. The following keys and associated objects are
  required for a valid sample:

  - `image`:
    Training image.
    The image domain of the training image is disregarded.
  - `region`:
    Region(s), that define(s) the respective ground truth of an instance.
    In order to find the instance, the region must include the model origin
    as well as the model contours.

  All other keys in the dictionary are ignored.
  As soon as new training samples are added, training samples that have
  already been set are overwritten or, in the case of an empty tuple,
  the training samples are removed from the shape model.

  Restriction:
   *'training_samples'* cannot be set together
  with other parameters.
- *'sample_based_training'* (legacy:
  *'extended_parameter_estimation'*):

  Controls which sample-based training methods are performed in the
  next call to [`train_generic_shape_model`](train_generic_shape_model.md). After successful training,
  the estimated parameter values are set in the model if a parameter
  estimation method was enabled. Also, the model's contour is refined as
  specified if a model refinement method was enabled.

  In order to obtain good training results, it is essential to set all
  relevant parameters before the model training (thus, before the call of
  [`train_generic_shape_model`](train_generic_shape_model.md)), such that the model can be found
  in the sample images. Accordingly, some search parameters might have to
  be set more generous for the training than for the eventual searching.

  Multiple sample-based training methods can be selected by providing
  multiple values in a tuple.

  To check whether the current model is compatible with the methods set
  in *'sample_based_training'*,
  *'sample_based_training_compatible'* can be
  queried using [`get_generic_shape_model_param`](get_generic_shape_model_param.md).

  Possible values:

  - *'none'*:

    Deselects all sample-based training methods.

    Restriction:
     *'none'* cannot be selected together with any
    other method.
  - *'contour_pruning'*:

    Prunes the model's contour by removing parts of the contour which are
    considered unstable in the provided samples. Here, unstable means that
    the mean score of a contour part over all samples is below
    *'contour_pruning_threshold'*.

    Please note that this method is not compatible with a shape model where
    one or more of the following is true:

    - the shape model was trained using XLD templates,
    - the parameter *'max_deformation'* is set to a value
      different from *0*,
    - the parameter *'pyramid_level_lowest'* is set to a value
      different from *1*, whether directly or indirectly (e.g. by
      setting *'high_noise_sample'* or calling
      [`adapt_shape_model_high_noise`](adapt_shape_model_high_noise.md)),
    - the parameter *'pyramid_level_robust_tracking'* is set to
      *'true'*.
  - *'linear'*:

    Determines a suitable value for *'min_score'*.

    Restriction:
     *'linear'* cannot be selected together with
    *'per_level'*.
  - *'per_level'*:

    Determines suitable values replacing *'greediness'* and
    *'min_score'*.

    Attention:
     *'per_level'* depends on the number of used
    pyramid levels. Thus, it is important not to change the pyramid levels
    after the sample-based training anymore. As a consequence, possible
    changes of the number of pyramid levels whether directly (e.g., setting
    *'pyramid_level_highest'*) or indirectly (e.g., calling
    [`adapt_shape_model_high_noise`](adapt_shape_model_high_noise.md)) must be done before applying the
    sample-based training (meaning, before the call of
    [`train_generic_shape_model`](train_generic_shape_model.md)).
    Furthermore, the parameter *'max_deformation'* must stay constant.

    Restriction:
     *'per_level'* cannot be selected together with
    *'linear'*.

  Restriction:
   *'sample_based_training'* cannot be set
  or queried together with other parameters.

  Restriction:
   All values except *'none'* require representative
  training samples. If training samples are not provided, sample-based
  training is not executed and the affected parameters are set to the last
  user-provided values or the default and the model is left unmodified.

  Default:
   *'per_level'*.
- *'contour_pruning_threshold'*:

  Sets the score threshold which distinguishes stable and unstable contour parts
  for the sample-based training method *'contour_pruning'*.

  Value range:
   *'min'* $=$ *-1.0*
  $\le$ *'contour_pruning_threshold'* $\le$
  *1.0* $=$ *'max'*

  Default:
   *0.5*.

### Automatic Modifications

The following parameters are subject to automatic modifications without
further notice:

- *'num_levels'*:

  If a number of levels is set such that on the
  asked levels not enough model points are generated, the number of pyramid
  levels is reduced internally until enough model points are found on the
  highest pyramid level.

  If this procedure would lead to a model with no pyramid levels, i.e.,
  if the number of model points is already too small on the lowest pyramid
  level, [`train_generic_shape_model`](train_generic_shape_model.md) returns with an error message.
- Parameters determining a *step_size*:

  In case the range is not a multiple of the *step_size*, latter one
  is modified accordingly.

  *Examples:* *'angle_step'*, *'iso_scale_step'*.
- `start` and `end` value of a specified range:

  To ensure that for model instances in the exact model position are
  returned by [`find_generic_shape_model`](find_generic_shape_model.md), ranges may modified as
  follows:
  If there is no positive integer value n such that the *start* value
  plus n times the *step_size* gives 0.0 (for angles) and
  1.0 (for scalings), respectively, the *start* value is decreased by
  up to one `step_size` and the *end* value increased such that
  the total range is increased by exactly
  one `step_size`.

  *Examples:* *'angle_start'*, *'restrict_iso_scale_max'*.
- *'clutter_hom_mat_2d'*:

  Changing the origin (*'origin_row'* and *'origin_column'*)
  influences the used transformation matrices, i.e., the
  *'clutter_hom_mat_2d'* set by the user.
- *'clutter_contrast'*:

  If *'min_contrast'* is changed such that it gets bigger than
  *'clutter_contrast'*, *'clutter_contrast'* is increased if
  the user set the value *'auto'*.

Note that the transformations are treated internally such that the
scalings are applied first, followed by the rotation. Therefore,
the model should usually be aligned such that it appears
horizontally or vertically in the model image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  shape_model `→`  (handle)

Handle of the shape model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Parameter name.

Default:
'min_score'

List of values:
'angle_end', 'angle_start', 'angle_step', 'border_shape_models', 'clutter_border_mode', 'clutter_contrast', 'clutter_hom_mat_2d', 'contour_pruning_threshold', 'contrast_high', 'contrast_low', 'greediness', 'iso_scale_max', 'iso_scale_min', 'iso_scale_step', 'max_clutter', 'max_deformation', 'max_overlap', 'max_overlap_global_enable', 'metric', 'min_contrast', 'min_score', 'min_size', 'model_cache', 'model_identifier', 'num_levels', 'num_matches', 'num_matches_global_enable', 'optimization', 'origin_column', 'origin_row', 'prepare_clutter_region_for_visualization', 'prepare_contours_for_visualization', 'pyramid_level_highest', 'pyramid_level_lowest', 'pyramid_level_robust_tracking', 'restrict_iso_scale_max', 'restrict_iso_scale_min', 'restrict_scale_column_max', 'restrict_scale_column_min', 'restrict_scale_row_max', 'restrict_scale_row_min', 'sample_based_training', 'scale_column_max', 'scale_column_min', 'scale_column_step', 'scale_row_max', 'scale_row_min', 'scale_row_step', 'score_visualization', 'strict_boundaries', 'subpixel', 'time_measurement', 'timeout', 'training_samples', 'use_clutter'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string / handle)

Parameter value.

Default:
0.5

Suggested values:
-3.14, -1.57, -0.79, -0.39, 0.0, 0.39, 0.79, 1.57, 3.14

## Result

If the parameters are valid, the operator
`set_generic_shape_model_param` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`create_generic_shape_model`

## Possible Successors

`get_generic_shape_model_param`,
`train_generic_shape_model`,
`find_generic_shape_model`

## Module

Matching

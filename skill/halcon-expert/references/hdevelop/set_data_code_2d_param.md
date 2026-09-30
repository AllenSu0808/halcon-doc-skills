# set_data_code_2d_param (Operator)

## Name

`set_data_code_2d_param` — Set selected parameters of the 2D code model.

## Signature

`set_data_code_2d_param( : : DataCodeHandle, GenParamName, GenParamValue : )`

## Description

The operator `set_data_code_2d_param` is used to set or change
the different parameters of a 2D code model in order to
adapt the model to a particular symbol appearance.
All parameters can also be set while creating a 2D code model
with [`create_data_code_2d_model`](create_data_code_2d_model.md).
The current configuration of the 2D code model can be queried with
[`get_data_code_2d_param`](get_data_code_2d_param.md).
A list with the names of all parameters that can be set for the
given 2D code type is returned by
[`query_data_code_2d_params`](query_data_code_2d_params.md).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

Note that the symbol structure of GS1 DataMatrix, GS1 QR Code,
GS1 Aztec Code, and GS1 DotCode is identical to the structure of
Data Matrix ECC 200, QR Code, Aztec Code, and DotCode, respectively.
Therefore, all symbology specific parameters applying to Data Matrix ECC 200,
QR Code, Aztec Code, or DotCode apply to their corresponding GS1variant as well.
In the following, the explicit enumeration of the
parameters for any particular GS1 code is omitted for sake of readability.
Instead, the relevant parameters names are to be inferred from the
parameters for the corresponding non-GS1 code type or can be explicitly
queried by [`query_data_code_2d_params`](query_data_code_2d_params.md) with parameter
*'set_model_params'*.

The following overview lists the different generic parameters with
the respective value ranges and default values in standard mode
(*'standard_recognition'*). If the default values in enhanced
mode (*'enhanced_recognition'*) differ from those in the
standard mode, they are listed additionally. The same holds, if the
default values in the maximum mode *'maximum_recognition'*
differ from those in the enhanced mode:

**Basic default settings:**

- All 2D code types:

  - ***'default_parameters'*:** —

    Reset all model parameters to one of the three basic
    default settings *standard*, *enhanced*, or
    *maximum* (see the following summary and
    [`create_data_code_2d_model`](create_data_code_2d_model.md)). In addition to the
    parameter values, the training state of the model is reset.

    List of values:
     *'standard_recognition'*,
    *'enhanced_recognition'*,
    *'maximum_recognition'*

    Default:
     *'standard_recognition'*

    Attention:
     If this parameter is set together with a list of other
    parameters, this parameter must be at the first position.
  - ***'trained'*:** —

    Set for the given parameters the training state to trained.
    The next training will not overwrite this parameters.
    If necessary only the parameter range is extended to cover the already
    trained symbols.
    For all possible parameters which can be trained see
    [`find_data_code_2d`](find_data_code_2d.md). With *'all'* the training
    state of all trainable parameters is set to trained.

**Size and shape of the symbol:**

- Data Matrix ECC 200 (including the finder pattern):

  Attention:
   After calling
  `set_data_code_2d_param` to change size or shape of
  the symbol, the parameters are evaluated in the given
  order. After each parameter, the consistency of the current
  settings is checked, and if necessary the current settings
  are adjusted. Therefore the order in which the changes are
  done may influence the final setting.

  - ***'symbol_cols_min'*:** —

    Minimum number of module columns in the symbol.

    Value range:
     [*10*, *12*, *14*,
    .. *144*]

    Attention:
     Changing *'symbol_cols_min'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.

    Default:
     *10*
  - ***'symbol_cols_max'*:** —

    Maximum number of module columns in the symbol.

    Value range:
     [*10*, *12*, *14*,
    .. *144*]

    Attention:
     Changing *'symbol_cols_max'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.

    Default:
     *144*
  - ***'symbol_rows_min'*:** —

    Minimum number of module rows in the symbol.

    Value range:
     [*8*, *10*, *12*,
    .. *144*]

    Attention:
     Changing *'symbol_rows_min'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.

    Default:
     *8*
  - ***'symbol_rows_max'*:** —

    Maximum number of module rows in the symbol.

    Value range:
     [*8*, *10*, *12*,
    .. *144*]

    Attention:
     Changing *'symbol_rows_max'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.

    Default:
     *144*
  - ***'symbol_cols'*:** —

    Set *'symbol_cols_min'* and *'symbol_cols_max'*
    to the given value.

    Value range:
     [*10*, *12*, *14*,
    .. *144*]

    Attention:
     Changing *'symbol_cols'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.
  - ***'symbol_rows'*:** —

    Set *'symbol_rows_min'* and *'symbol_rows_max'*
    to the given value.

    Value range:
     [*8*, *10*, *12*,
    .. *144*]

    Attention:
     Changing *'symbol_rows'* sets
    *'symbol_shape'* to *'any'*. If the size of the
    current symbol is only consistent with one shape type
    *'symbol_shape'* is restricted to *'rectangle'* or
    *'square'*.
  - ***'symbol_shape'*:** —

    Possible restrictions on the symbol shape
    (*'rectangle'* and/or *'square'*).

    Attention:
     setting the symbol shape all previously made
    restrictions concerning the symbol size may change. For
    *'square'* the minimum of *'symbol_cols_min'*
    and *'symbol_rows_min'* and the maximum of
    *'symbol_cols_max'* and *'symbol_rows_max'* will be
    used.
    Additional restrictions can be seen in the following table:

    | symbol_shape | 'any' | 'rectangle' | 'square' |
    | --- | --- | --- | --- |
    | *'symbol_cols_min'* | >= 10 | >= 18 | >= 10 |
    | *'symbol_cols_max'* | <= 144 | <= 144 | <= 144 |
    | *'symbol_rows_min'* | >= 8 | >= 8 | >= 10 |
    | *'symbol_rows_max'* | <= 144 | <= 26 | <= 144 |

    Furthermore, if *'symbol_cols_min'* is larger than
    *'symbol_rows_max'*, the setting for *'symbol_shape'*
    is ignored and its value set to *'rectangle'*.

    The same search algorithm is used for both
    shapes if *'finder_pattern_tolerance'* is set to
    *'low'*. Thus, *'symbol_shape'* has no effect
    for the symbol search in this case.
    However, if
    *'finder_pattern_tolerance'* is set to
    *'high'* or *'any'*, the value of
    *'symbol_shape'* may speed up the symbol search
    significantly if it is set to *'rectangle'* or
    *'square'*.

    List of values:
     *'rectangle'*, *'square'*, *'any'*

    Default:
     *'any'*
  - ***'symbol_size_min'*:** —

    Set *'symbol_cols_min'* and *'symbol_rows_min'*
    to the given value and *'symbol_shape'* to
    *'square'*.
  - ***'symbol_size_max'*:** —

    Set *'symbol_cols_max'* and *'symbol_rows_max'*
    to the given value and *'symbol_shape'* to
    *'square'*.
  - ***'symbol_size'*:** —

    Set *'symbol_cols_min'*, *'symbol_cols_max'*,
    *'symbol_rows_min'* and *'symbol_rows_max'* to
    the given value and *'symbol_shape'* to *'square'*.
- QR Code (including the finder pattern):

  - ***'model_type'*:** —

    Type of the QR Code model.
    The old QR Code Model *1* (which has been removed
    from ISO/IEC 18004 in 2006) and the newer Model *2*
    are supported. With the specification *'any'* or
    *'0'* both models are carried out.

    List of values:
     *1*, *2*, *'any'*,
    *'0'*

    Default:
     *2* (enhanced: *2*, maximum: *'any'*)
  - ***'version_min'*:** —

    Minimum symbol version.
    The symbol version is directly linked to the symbol size.
    Symbols of version 1 are 21x21 modules in size,
    version 2 = 25x25 modules, etc. up to version
    40 = 177x177 modules.
    The maximum size of Model 1 symbols is 73x73 =
    version 14.

    Value range:
     [*1* .. *40*]
    (Model 1: [*1* .. *14*])

    Default:
     *1*
  - ***'version_max'*:** —

    Maximum symbol version.

    Value range:
     [*1* .. *40*]
    (Model 1: [*1* .. *14*])

    Default:
     *40*
  - ***'version'*:** —

    Set *'version_min'* and *'version_max'*
    to the same value.
  - ***'symbol_size_min'*:** —

    Minimum size of the symbol in modules.
    This parameter can be used as an alternative to
    *'version_min'*.

    Value range:
     [*21* .. *177*]
    (Model 1: [*21* .. *73*])

    Default:
     *21*
  - ***'symbol_size_max'*:** —

    Maximum size of the symbol in modules.
    This parameter can be used as an alternative to
    *'version_max'*:

    Value range:
     [*21* .. *177*]
    (Model 1: [*21* .. *73*])

    Default:
     *177*
  - ***'symbol_size'*:** —

    Set *'symbol_size_min'* and *'symbol_size_max'*
    to the same value.
- Micro QR Code:

  - ***'version_min'*:** —

    Minimum symbol version.
    The symbol version is directly linked to the symbol size.
    Symbols are between 11x11 (version M1) and
    17x17 (version M4) modules in size.

    Value range:
     [*1* .. *4*]

    Default:
     *1*
  - ***'version_max'*:** —

    Maximum symbol version.

    Value range:
     [*1* .. *4*]

    Default:
     *4*
  - ***'version'*:** —

    Set *'version_min'* and *'version_max'*
    to the same value.
  - ***'symbol_size_min'*:** —

    Minimum size of the symbol in modules.
    This parameter can be used as an alternative to
    *'version_min'*.

    Value range:
     [*11* .. *17*]

    Default:
     *11*
  - ***'symbol_size_max'*:** —

    Maximum size of the symbol in modules.
    This parameter can be used as an alternative to
    *'version_max'*:

    Value range:
     [*11* .. *17*]

    Default:
     *17*
  - ***'symbol_size'*:** —

    Set *'symbol_size_min'* and *'symbol_size_max'*
    to the same value.
- PDF417:

  - ***'symbol_cols_min'*:** —

    Minimum number of data columns in the symbol in codewords,
    i.e., excluding the codewords of the start/stop
    pattern and of the two row indicators.

    Value range:
     [*1* ..
    *30*]

    Default:
     *1*
  - ***'symbol_cols_max'*:** —

    Maximum number of data columns in the symbol in codewords,
    i.e., excluding the two codewords of the start/stop
    pattern and of the two indicators.

    Value range:
     [*1* ..
    *30*]

    Default:
     *20* (enhanced: *30*)
  - ***'symbol_rows_min'*:** —

    Minimum number of module rows in the symbol.

    Value range:
     [*3* ..
    *90*]

    Default:
     *5* (enhanced: *3*)
  - ***'symbol_rows_max'*:** —

    Maximum number of module rows in the symbol.

    Value range:
     [*3* ..
    *90*]

    Default:
     *45* (enhanced: *90*)
  - ***'symbol_cols'*:** —

    Set *'symbol_cols_min'* and *'symbol_cols_max'*
    to the same value.
  - ***'symbol_rows'*:** —

    Set *'symbol_rows_min'* and *'symbol_rows_max'*
    to the same value.
- Aztec Code (including the finder pattern):

  - ***'format'*:** —

    Format of the Aztec Code: space separated list with the
    values *'compact'*, *'full_range'*, or
    *'rune'*.

    Default:
     *'compact full_range'*
  - ***'symbol_size_min'*:** —

    Minimum size of the symbol in modules.

    Value range:
     [*11* .. *151*]

    Default:
     *11*
  - ***'symbol_size_max'*:** —

    Maximum size of the symbol in modules.

    Value range:
     [*11* .. *151*]

    Default:
     *151*
  - ***'symbol_size'*:** —

    Set *'symbol_size_min'* and *'symbol_size_max'*
    to the same value.
- DotCode:
  A valid DotCode according to AIM DotCode Revision 4.0-1 consists
  of one even and one odd dimension. Within HALCON, the column dimension of
  a DotCode symbol is defined by the reading direction and always refers to
  the odd dimension.

  - ***'symbol_cols_min'*:** —

    Minimum number of module columns in the symbol. Must be odd.

    Value range:
     [*5* .. *999*]

    Default:
     *5*
  - ***'symbol_cols_max'*:** —

    Maximum number of module columns in the symbol. Must be odd.

    Value range:
     [*5* .. *999*]

    Default:
     *999*
  - ***'symbol_rows_min'*:** —

    Minimum number of module rows in the symbol. Must be even.

    Value range:
     [*4* .. *998*]

    Default:
     *4*
  - ***'symbol_rows_max'*:** —

    Maximum number of module rows in the symbol. Must be even.

    Value range:
     [*4* .. *998*]

    Default:
     *998*
  - ***'symbol_cols'*:** —

    Set *'symbol_cols_min'* and *'symbol_cols_max'*
    to the given value. Must bee odd.

    Value range:
     [*5* .. *999*]
  - ***'symbol_rows'*:** —

    Set *'symbol_rows_min'* and *'symbol_rows_max'*
    to the given value. Must be even.

    Value range:
     [*4* .. *998*]

**Appearance of the modules in the image:**

- All 2D code types:

  - ***'polarity'*:** —

    Describes the polarity of the symbol in the image, i.e.,
    the parameter determines if the symbol appears light on a
    dark background or dark on a light background.

    List of values:
     *'dark_on_light'*,
    *'light_on_dark'*, *'any'*.

    Default:
     *'dark_on_light'*
    (enhanced: *'any'*)
  - ***'mirrored'*:** —

    Describes whether the symbol is or may be mirrored (which is
    equivalent to swapping rows and columns of the symbol).

    List of values:
     *'no'*, *'yes'*, *'any'*

    Default:
     *'any'*
- All 2D code types except Data Matrix ECC 200, QR Code, Micro QR Code, and DotCode:

  - ***'contrast_min'*:** —

    Minimum contrast between the foreground and the background of
    the symbol (specified as gray value difference). This measure
    corresponds with the minimum gradient between the symbol's
    foreground and the background and is therefore also depending on
    the image sharpness.

    Value range:
     [*1* .. *255*]

    Default:
     *30* (enhanced: *10*)
- Data Matrix ECC 200, Micro QR Code, and QR Code:

  - ***'contrast_tolerance'*:** —

    Describes the tolerance of the search with respect to local
    contrast variations (e.g., in the presence of glare or
    reflections). Depending on the value of the parameter two
    different algorithms are applied. If
    *'contrast_tolerance'* is set to *'high'* the
    robustness in the presence of strong local contrast
    variations is improved. In the case where
    *'contrast_tolerance'* is set to *'low'* the
    algorithm used is less robust to strong local contrast variations,
    however, it is faster and still able to handle contrast
    variations under normal circumstances and therefore
    *'low'* should be used in most cases. If
    *'contrast_tolerance'* is set to *'any'* both
    algorithms are applied.

    List of values:
     *'low'*, *'high'*, *'any'*

    Default:
     *'low'* (enhanced: *'low'*,
    maximum: *'any'*)
- All 2D code types except PDF417:

  - ***'module_size_min'*:** —

    Minimum size of the modules in the image in pixels. Please
    note that for optimal reading performance a module size of
    at least 3-4 pixels is recommended.

    Value range:
     [*1* .. *100*]

    Default:
     *6*
    (enhanced: *2*, maximum: *1*)

    For DotCode:

    Default:
     *4* (enhanced, maximum: *2*)
  - ***'module_size_max'*:** —

    Maximum size of the modules in the image in pixels.

    Value range:
     [*2* .. *100*]

    Default:
     *20* (enhanced: *100*)

    For DotCode:

    Default:
     *100*
  - ***'module_size'*:** —

    Set *'module_size_min'* and *'module_size_max'*
    to the same value.

  The gap between modules can be set via the *'module_gap*'*
  parameters as explained in the following paragraph:

  It is possible to specify whether neighboring foreground
  modules are connected or whether there is or may be a gap between
  them.
  If the foreground modules are connected and fill the module
  space completely, the gap parameter can be set to *'no'*.
  The parameter is set to *'small'* if there is a very
  small gap between two modules, i.e.,< 10% of the module size.
  It can be set to *'big'*
  if the gap is bigger
  (in relation to the module size: < 50%).
  The last two settings may also be useful if the foreground
  modules - although being connected - appear thinner as
  their entitled space (e.g., as a result of blooming caused by a
  bright illuminant).
  If the foreground modules appear only as very small dots,
  in general, an
  appropriate preprocessing of the image for detecting or
  enlarging the modules will be necessary (e.g., by
  [`gray_erosion_shape`](gray_erosion_shape.md) or [`gray_dilation_shape`](gray_dilation_shape.md)).

  - ***'module_gap_min'*:** —

    Minimum gap.

    List of values:
     *'no'*, *'small'*,
    *'big'* (*'big'* is not available for DotCode)

    Default:
     *'no'*
  - ***'module_gap_max'*:** —

    Maximum gap.

    List of values:
     *'no'*, *'small'*,
    *'big'*

    For Data Matrix ECC 200, Micro QR Code, and QR Code:

    Default:
     *'no'* (enhanced: *'small'*,
    maximum: *'big'*)

    For DotCode:

    Default:
     *'no'* (enhanced: *'small'*,
    maximum: *'small'*)

    For Aztec Code:

    Default:
     *'small'* (enhanced: *'big'*)
  - ***'module_gap'*:** —

    Set *'module_gap_min'* and
    *'module_gap_max'* to the same value.
- All 2D code types except DotCode:

  - ***'small_modules_robustness'*:** —

    Robustness of the decoding of 2D codes with very small
    module sizes. Setting the parameter
    *'small_modules_robustness'* to *'high'*
    increases the likelihood of being able to
    decode 2D codes with very small module sizes. Additionally,
    in that case the minimum module size should also be adapted
    accordingly, thus *'module_size_min'* and
    *'module_width_min'* (PDF417) should be set to
    the expected minimum module size and width, respectively. Setting
    *'small_modules_robustness'* to *'high'* can
    significantly increase the internal memory usage of
    [`find_data_code_2d`](find_data_code_2d.md). Thus, in the default case
    *'small_modules_robustness'* should be set to *'low'*.
    If *'small_modules_robustness'* is set to *'high'*
    the maximal accepted image size is bisected (see
    [`get_system`](get_system.md) *'halcon_xl'*).
    If this image size is exceeded when calling [`find_data_code_2d`](find_data_code_2d.md),
    an exception is raised.

    List of values:
     *'low'*, *'high'*

    Default:
     *'low'* (enhanced: *'low'*,
    maximum: *'high'*)
- PDF417:

  - ***'module_width_min'*:** —

    Minimum module width in the image in pixels.

    Value range:
     [*1* .. *100*]

    Default:
     *3* (enhanced: *2*,
    maximum: *1*)
  - ***'module_width_max'*:** —

    Maximum module width in the image in pixels.

    Value range:
     [*2* .. *100*]

    Default:
     *15* (enhanced: *100*)
  - ***'module_width'*:** —

    Set *'module_width_min'* and *'module_width_max'*
    to the same value.
  - ***'module_aspect_min'*:** —

    Minimum module aspect ratio (module height to module width).

    Value range:
     [*0.5* .. *20.0*]

    Default:
     *1.0*
  - ***'module_aspect_max'*:** —

    Maximum module aspect ratio (module height to module width).

    Value range:
     [*0.5* .. *20.0*]

    Default:
     *4.0* (enhanced: *10.0*)
  - ***'module_aspect'*:** —

    Set *'module_aspect_min'* and
    *'module_aspect_max'* to the same value.
- Data Matrix ECC 200:

  - ***'slant_max'*:** —

    Maximum deviation of the angle of the L-shaped finder pattern
    from the (ideal) right angle (the angle is specified
    in radians and corresponds to the distortion that occurs
    when the symbol is printed or during the image
    acquisition).

    Value range:
     [*0.0* .. *0.5235*]

    Default:
     *0.1745* = $10^{\circ}$
    (enhanced: *0.5235* = $30^{\circ}$)
  - ***'finder_pattern_tolerance'*:** —

    Tolerance of the search with respect to a defect or
    partially occluded finder pattern. The finder pattern
    includes the L-shaped side as well as the opposite
    alternating side. Dependent on this parameter, different
    algorithms are used during the symbol search in
    [`find_data_code_2d`](find_data_code_2d.md). In one case (*'low'*),
    it is assumed that the finder pattern is present to a high
    degree and shows almost no disturbances. In the other case
    (*'high'*), the finder pattern may be defect or
    partially occluded without influencing the recognition and
    the reading of the symbol.
    Note, however,
    that in this mode the parameters for the symbol search
    should be restricted as narrow as possible by using
    `set_data_code_2d_param` because otherwise the
    runtime of [`find_data_code_2d`](find_data_code_2d.md) may significantly
    increase.
    Also note that the two algorithms slightly differ
    from each other in terms of robustness. This may lead to
    different results depending on the value of
    *'finder_pattern_tolerance'* even if the finder
    pattern of the symbol is not disturbed. For example, if
    *'high'* is chosen, only symbols with an equidistant
    module grid can be found (see below), and hence the
    robustness to perspective distortions is
    decreased. Finally, if *'finder_pattern_tolerance'*
    is set to *'any'* both algorithms are applied.

    List of values:
     *'low'*, *'high'*, *'any'*

    Default:
     *'low'*
    (enhanced: *'low'*, maximum: *'any'*)
  - ***'alternating_pattern_tolerance'*:** —

    Tolerance of the search with respect to the variation of the
    module widths along the two sides with the alternating pattern. The
    alternating pattern analysis is decisive if
    *'finder_pattern_tolerance'* is set to *'low'*
    (or *'any'* which includes *'low'*).
    Note, however, that this parameter has no
    effect if *'finder_pattern_tolerance'* has been
    set to *'high'*.
    A total of three different values are allowed for this
    parameter, with a higher setting always including the lower
    values: *'low'* allows only a small variation of the
    module widths along the sides with the alternating pattern.
    *'medium'* first tries to meet the strict requirements
    of *'low'*, and if this fails, a larger variation of the
    module widths along the sides with the alternating pattern is
    allowed. Finally, *'high'* includes everything that
    *'medium'* allowed and additionally expands the parameter
    space for the symbol's outer boundaries through further
    attempts. It also softens the relation between the number
    of edges detected and the symbol type used for subsequent decoding.
    The greater robustness in difficult cases comes with the
    disadvantage that *'high'* in particular can lead to a
    significant runtime increase. To counteract this, the parameter
    space should be reduced in total, e.g., by setting the expected
    symbol sizes as tight as possible.

    List of values:
     *'low'*, *'medium'*, *'high'*

    Default:
     *'low'*
    (enhanced: *'medium'*, maximum: *'high'*)
  - ***'module_grid'*:** —

    Describes whether the size of the modules may vary (in a
    specific range) or not. Dependent on this parameter
    different algorithms are used for calculating the module's
    center positions. If it is set to *'fixed'*, an
    equidistant grid is used. Allowing a variable module size
    (*'variable'*), the grid is aligned only to the
    alternating side of the finder pattern. With
    *'any'* both approaches are tested one after the
    other. Please note that the value of *'module_grid'*
    is ignored if *'finder_pattern_tolerance'* is set to
    *'high'*. In this case an equidistant grid is
    assumed.

    List of values:
     *'fixed'*,
    *'variable'*, *'any'*

    Default:
     *'fixed'* (enhanced: *'any'*)
- Data Matrix ECC 200 and QR Code:

  - ***'deformation_tolerance'*:** —

    Search tolerance regarding the deformation of codes. Depending on this
    parameter, an algorithm for compensating curvature (*'curved'*)
    is used in [`find_data_code_2d`](find_data_code_2d.md) or not (*'low'*).

    Print quality inspection is not available if a code cannot be decoded
    without this compensation algorithm.

    List of values:
     *'low'*, *'curved'*

    Default:
     *'low'* (maximum: *'curved'*)
- QR Code and Micro QR Code:

  - ***'position_pattern_min'*:** —

    Number of position detection patterns that have to be visible
    for generating a new symbol candidate.

    Value range:
     [*2*, *3*]

    Default:
     *3* (enhanced: *2*)

    Attention:
     For the Micro QR Code, *'position_pattern_min'*
    is always equal to *1* and can't be changed.
- Aztec Code:

  - ***'finder_pattern_tolerance'*:** —

    Tolerance of the search with respect to a defect or partially
    occluded finder pattern. Depending on this parameter, different
    algorithms are used during the symbol search in
    [`find_data_code_2d`](find_data_code_2d.md). In one case (*'low'*), it is
    assumed that all rings of the finder pattern can be extracted. In
    the other case (*'high'*) it is assumed that at least one of
    the rings of the finder pattern can be extracted.
    As a consequence the runtime of the reader increases, if this
    parameter is set to *'high'*.

    List of values:
     *'low'*, *'high'*

    Default:
     *'low'* (enhanced: *'high'*)
  - ***'additional_levels'*:** —

    To increase the robustness of the Aztec Code reader, a number of
    additional search levels (in addition to the search levels derived
    from the minimum and maximum module dimensions) can be specified via
    this parameter. Be aware that this increases the runtime of the
    reader, especially if no code is found.

    Value range:
     [*0* .. *2*]

    Default:
     *0*

**General model behavior:**

- All 2D code types:

  - ***'persistence'*:** —

    Controls whether certain intermediate results of the symbol
    search with [`find_data_code_2d`](find_data_code_2d.md) are stored
    temporarily or persistently in the model.
    The memory requirements of [`find_data_code_2d`](find_data_code_2d.md) are
    significantly smaller if the data is stored temporarily
    (default).
    On the other hand, by using the persistent storage it is
    possible to access some of the data for debugging reasons
    after searching for symbols, e.g., to investigate why a
    symbol could not be read.
    The memory requirements of [`find_data_code_2d`](find_data_code_2d.md) can further
    be reduced by setting *'persistence'* to *-1* such
    that only the data necessary for retrieving the decoded data is
    stored with the model. Be aware that print quality inspection
    can only be performed for Data Matrix ECC 200 symbols with this
    setting of *'persistence'*.

    List of values:
     *-1* (only decoded data),
    *0* (temporary), *1* (persistent)

    Default:
     *0*
  - ***'discard_undecoded_candidates'*** —

    Controls whether candidates that could not be successfully decoded
    are stored in the model.
    Set this parameter to *'yes'* to reduce the amount of
    memory consumed by the model. Note that in this case
    information about undecoded candidates cannot be queried by
    using [`get_data_code_2d_objects`](get_data_code_2d_objects.md) or
    [`get_data_code_2d_results`](get_data_code_2d_results.md).

    List of values:
     *'yes'*, *'no'*

    Default:
     *'no'*
  - ***'strict_model'*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) while
    detecting symbols that could be read but that do not fit
    the model restrictions on the size of the symbols.
    They can be rejected (strict model, set to *'yes'*) or
    returned as a result independent of their size and the
    size specified in the model (lax model, set to
    *'no'*). Please note that the module
    size restrictions (*'module_size_min'* and
    *'module_size_max'*) are not checked even if
    *'strict_model'* is set to *'yes'*.

    List of values:
     *'yes'* (strict),
    *'no'* (not strict)

    Default:
     *'yes'*
  - ***'string_encoding'*:** —

    Sets the expected string encoding of the string that is encoded in
    the symbol.
    It's possible to switch between UTF-8, Latin-1, Shift JIS, GB2312 and the
    string encoding of the current locale. If necessary, the string will
    be transcoded accordingly. In raw mode, the string will be passed
    unchanged.

    In *'auto'* mode, heuristics are used to derive the
    encoding of the string.

    List of values:
     *'utf8'*, *'locale'*, *'latin1'*,
    *'shiftjis'*, *'raw'*, *'auto'*

    Default:
     *'auto'*
  - ***'timeout'*:** —

    By the use of this parameter, it is possible to abort
    [`find_data_code_2d`](find_data_code_2d.md) after a defined period in
    milliseconds. This is especially useful in cases where a
    maximum cycle time has to be ensured. All results gained before
    the timeout can be accessed by
    [`get_data_code_2d_results`](get_data_code_2d_results.md). Passing values less or
    equal zero implies a deactivation of the timeout (default).

    The temporal accuracy is about 10 ms. It
    depends on several factors including the speed of your computer, the
    image size and the *'timer_mode'* set via
    [`set_system`](set_system.md).

    [`find_data_code_2d`](find_data_code_2d.md) does not raise an exception if a
    timeout occurs. To check whether [`find_data_code_2d`](find_data_code_2d.md) has been
    interrupted, check the parameter *'aborted'* in
    [`get_data_code_2d_results`](get_data_code_2d_results.md).

    Note that the timeout is ignored if [`find_data_code_2d`](find_data_code_2d.md)
    runs in training mode.

    Suggested values:
     *'false'*, *-1*,
    *20* .. *100*

    Default:
     *'false'*
  - ***'abort'*:** —

    Using this option, it is possible to abort [`find_data_code_2d`](find_data_code_2d.md)
    from another thread. When `set_data_code_2d_param` is called
    with *'abort'*, an instance of [`find_data_code_2d`](find_data_code_2d.md) with
    the model *`DataCodeHandle`* running in another thread is
    requested to abort. If there is no [`find_data_code_2d`](find_data_code_2d.md) running
    with this model, nothing happens.

    The operator [`find_data_code_2d`](find_data_code_2d.md) might not return immediately.
    It has to reach a cancellation point to ensure a proper cleanup.
    Depending on different factors like the computer performance this
    may take up to 10 ms.

    All decoded results until this moment are still returned.

    Note: This is the only action with a 2D code handle, which can be
    used from different threads without requiring additional
    synchronization.

    Default:
     *'true'* (The value is not processed.)
- All 2D code types except Aztec Code:

  - ***'strict_quiet_zone'*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) while
    detecting symbols that could be read but show defects in
    their quiet zone. If *'strict_quiet_zone'* is set to
    *'yes'* the quiet zone of all decoded symbol is validated
    similar to the method used for print quality inspection.
    Symbols with poor grades for their quiet zone are not returned
    as a result. Their *'status'* is set to
    *'quiet zone is missing'*.
    If *'strict_quiet_zone'* is set to *'no'*
    (this is the default case), all readable symbols are
    returned as a result.

    List of values:
     *'yes'*,
    *'no'*

    Default:
     *'no'*
- All 2D code types except DotCode:

  - ***'quality_isoiec15415_aperture_size'*:** —

    The reference image, on which the quality grades *symbol
    contrast*, *modulation*, *fixed pattern damage*, and
    *print growth x/y* are assessed, is obtained by applying a
    synthetic aperture (circular mean filter) on the original image.
    This parameter determines the filter size as the part of the
    module size. According to the standard, this value should be
    chosen between 0.5 and 0.8 depending on the application
    (ISO/IEC 15415:2024 section 5.6.2 and 7.3.1).

    For further guidance on selecting the aperture, see ISO/IEC
    15415:2024 Annex C.2.

    Value range:
     [*0* .. *1*]

    Default:
     *0.8*
  - ***'quality_isoiec15415_reflectance_reference'*:** —

    The contrast used to assess the quality grade
    *symbol contrast* is normalized with a reference
    grayvalue for reflectance, see ISO/IEC 15415:2024 section 5.6.1.
    This value can be obtained, e.g., with barium sulfate or
    magnesium oxide samples.

    Value range:
     [*1* .. *255*]

    Default:
     *255*
  - ***'quality_isoiec15415_smallest_module_size'*:** —

    The module size used to determine the size of the synthetic aperture.
    This can either be a fixed value in pixel or *'adaptive'*. In
    the latter case, the averaged module size obtained by the preceding
    [`find_data_code_2d`](find_data_code_2d.md) is used.
    The final diameter of the filter is given by multiplying
    *'quality_isoiec15415_aperture_size'* with this size.
    See ISO/IEC 15415:2024 section 7.3.1.

    Value range:
     >= *0*

    Default:
     *'adaptive'*
- Data Matrix ECC 200:

  - ***'quality_isoiec15415_decode_algorithm'*:** —

    The computation of the quality grades is based on the module grid
    determined for print quality grading. Use this parameter to
    choose the algorithm used to obtain this grid.

    - ***'robust'*:** —

      Recommended for process control matters in which no
      calibrated camera and lighting setup based on ISO/IEC 15415:2024 is
      provided. The returned quality grades as well as the calculation of the
      grading parameters is in compliance with the international standard
      ISO/IEC 15415:2024. To compensate for variances caused by the
      flexibility in hardware setups additional information gathered during
      decoding of the code as well as assumptions regarding the hardware
      setups are used to increase the robustness of the quality inspection.
    - ***'reference'*:** —

      Recommended for verification of print quality.
      In compliance with the international standard ISO/IEC 15415:2024 the
      verification requires a specific camera calibration as well as lighting
      setup to return standard compliant grading results.
      In contrast to the standard, we explicitly apply a lower bound of 20%
      for the relative aperture factor during the computation of the constants
      $d\_min$, $m\_min$, and $g\_max$. Additionally,
      if the module size (as determined by the preceding [`find_data_code_2d`](find_data_code_2d.md)
      call) drops below 4 pixels, the algorithm cannot be used and all
      grades are reported as -1.0. The stated lower bounds help to define a reasonable
      application window for the reference decoding algorithm. Finally, all grades
      will be set to -1.0 if the algorithm fails during the module grid determination.

    Default:
     *'robust'*
  - ***'decoding_scheme'*:** —

    Controls the decoding step of Data Matrix ECC 200. When setting this
    to *'raw'*, this allows to read symbols where the appearance
    and the error correction step conform to ISO/IEC 16022:2024, but where
    the encoding is custom. The decoded data are the error corrected data,
    are retrieved with the *'decoded_data'* parameter of
    [`get_data_code_2d_results`](get_data_code_2d_results.md) and must be further processed by
    the user.

    List of values:
     *'default'*,
    *'raw'*

    Default:
     *'default'*
  - ***'strict_fp_and_qz'*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) when detecting readable
    symbols with a low number of rows ($\le$ 12) and columns ($\le$ 18).
    The main intention of this parameter is to avoid false positives, i.e.,
    successfully decoded symbols with incorrect content, either on an
    actual symbol or in the background. The symbol sizes mentioned are particularly
    at risk due to their low error correction capacity. Possible values:

    - ***'true'*, *'yes'*:** —

      All successfully decoded symbols that meet the criteria
      described above are checked. Symbols with a disturbed outer
      finder pattern, whereby the L-pattern and the alternating pattern
      are assessed both individually and in combination, or with a
      disturbed quiet zone might be discarded. The evaluation is based
      on the classification results of the corresponding module positions.
      The evaluation of the quiet zone differs from
      *'strict_quiet_zone'*. Symbols with a high number of bad
      module positions are discarded and therefore not returned as a result.
      Their corresponding *'status'* values are returned starting
      with *'strict_fp_and_qz: ...'*. The colon is followed by more
      detailed information about the failed check.
    - ***'tolerant'* (Default):** —

      In this mode, only symbols of the specified size and with
      an increased probability of actually showing a false positive result
      run through the additional checks. Different information is taken
      into account for this decision, such as the search pass used and
      the unused error correction (UEC).
    - ***'false'*, *'no'*:** —

      The additional checks are completely deactivated. This can be useful if
      you want to read symbols with a low number of rows and columns and
      border areas that are known to be disturbed. However, deactivation
      carries the risk of unnoticed false positives.

    List of values:
     *'true'*, *'yes'*, *'tolerant'*,
    *'false'*, *'no'*

    Default:
     *'tolerant'*
- Data Matrix ECC 200, DotCode, Micro QR Code, and QR Code:

  - ***'candidate_selection'*:** —

    Controls the selection of candidate regions that are used for symbol
    detection. Setting this parameter to *'extensive'* increases
    the number of generated candidate regions and thus the likelihood of
    detecting a code. When this parameter is set to *'all'*, all
    possible candidates are used.
    If *'candidate_selection'* is set to
    *'default'*, less candidate regions are used.

    List of values:
     *'default'*, *'extensive'*,*'all'*
    (*'all'* is not available for Data Matrix ECC 200)

    For Data Matrix ECC 200:

    Default:
     *'default'*
    (enhanced: *'extensive'*, maximum: *'extensive'*)

    For DotCode, Micro QR Code, and QR Code:

    Default:
     *'default'*
    (enhanced: *'extensive'*, maximum: *'all'*)
- DotCode:

  - ***'max_allowed_error_correction'*:** —

    Controls the maximum allowed error correction.
    Due to the high error correction capacity, it is possible to
    successfully decode false positive DotCode candidates.
    Especially candidates which only cover a small part of a
    real DotCode may be decoded successfully because of the
    error correction capabilities. This is the case because DotCode symbols
    can consist of almost every size. So there are fewer criteria
    to decide whether the candidate is valid or not. In order to tackle
    this problem, the parameter *'max_allowed_error_correction'* can
    be used to specify the percentage of maximum allowed error correction.
    Per default the value is set to *0.9*, which means
    90%. This choice helps to reduce the number of false reads without any
    significant impact on the number of correct decodes.
    Setting the value to e.g., *0.5* means, only candidates which
    could be decoded with maximum 50% used error correction, will be
    returned as successfully decoded results.

    Value range:
     [*0.0* .. *1.0*]

    Default:
     *'0.9'*

When setting the model parameters, **attention** should be payed
especially to the following issues:

- Symbols whose size does not comply with the size restrictions
  made in the model (with the generic parameters
  *'symbol_rows*'*, *'symbol_cols*'*,
  *'symbol_size*'*, *'version*'*, or *'format'*)
  will not be read if *'strict_model'* is set to *'yes'*,
  which is the default.
  This behavior is useful if symbols of a specific size have to be
  detected while other symbols should be ignored.
  On the other hand, neglecting this parameter can lead to
  problems, e.g., if one symbol of an image sequence is
  used to adjust the model (including the symbol size), but later
  in the application the symbol size varies, which is quite common
  in practice.
- The runtime of [`find_data_code_2d`](find_data_code_2d.md) depends mostly on the
  following model parameters, namely in cases where the requested
  number of symbols *cannot* be found in the image:
  *'polarity'*, *'module_size_min'* (Data Matrix ECC 200, QR
  Code, and Micro QR Code) and *'module_size_min'* together with
  *'module_aspect_min'* (PDF417), and if the minimum module
  size is very small also the parameters *'module_gap_*'*
  (Data Matrix ECC 200, Aztec Code, QR Code, and Micro QR Code), for QR Code also
  *'position_pattern_min'*.
  For Data Matrix ECC 200 symbols, if
  *'finder_pattern_tolerance'* is set to *'high'* or
  *'any'*, the symbol size should be restricted with
  *'symbol_size_min'*, *'symbol_size_max'*,
  *'symbol_size'*, and *'symbol_shape'* as narrow as
  possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DataCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DataCodeHandle`** (input_control, state is modified)  datacode_2d `→`  (handle)

Handle of the 2D code model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters that shall be
adjusted for the 2D code.

Default:
'polarity'

List of values:
'abort', 'additional_levels', 'alternating_pattern_tolerance', 'candidate_selection', 'contrast_min', 'contrast_tolerance', 'decoding_scheme', 'default_parameters', 'deformation_tolerance', 'discard_undecoded_candidates', 'finder_pattern_tolerance', 'format', 'max_allowed_error_correction', 'mirrored', 'model_type', 'module_aspect', 'module_aspect_max', 'module_aspect_min', 'module_gap', 'module_gap_max', 'module_gap_min', 'module_grid', 'module_size', 'module_size_max', 'module_size_min', 'module_width', 'module_width_max', 'module_width_min', 'persistence', 'polarity', 'position_pattern_min', 'quality_isoiec15415_aperture_size', 'quality_isoiec15415_decode_algorithm', 'quality_isoiec15415_reflectance_reference', 'quality_isoiec15415_smallest_module_size', 'slant_max', 'small_modules_robustness', 'strict_fp_and_qz', 'strict_model', 'strict_quiet_zone', 'string_encoding', 'symbol_cols', 'symbol_cols_max', 'symbol_cols_min', 'symbol_rows', 'symbol_rows_max', 'symbol_rows_min', 'symbol_shape', 'symbol_size', 'symbol_size_max', 'symbol_size_min', 'timeout', 'trained', 'version', 'version_max', 'version_min'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Values of the generic parameters that are
adjusted for the 2D code.

Default:
'light_on_dark'

Suggested values:
'standard_recognition', 'enhanced_recognition', 'maximum_recognition', 'all', 'yes', 'no', 'any', 'dark_on_light', 'light_on_dark', 'square', 'rectangle', 'small', 'big', 'fixed', 'variable', 'low', 'high', 'default', 'extensive', 'utf8', 'locale', 'raw', 'shiftjis', 'gb2312', 'auto', 'robust', 'reference', 'curved', 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 30, 50, 70, 90, 12, 14, 16, 18, 20, 22, 24, 26, 32, 36, 40, 44, 48, 52, 64, 72, 80, 88, 96, 104, 120, 132, 144

## Example (HDevelop)

```
* This examples shows how a model can be adapted to a specific symbol if
* the symbol parameters are known

* Create a model for reading Data Matrix ECC 200 codes
create_data_code_2d_model ('Data Matrix ECC 200', [], [], DataCodeHandle)
* Restrict the model by setting the module size
set_data_code_2d_param (DataCodeHandle, \
                        ['module_size_min','module_size_max'], [4,7])
* Change the polarity setting of the model from 'dark_on_light' to
* 'light_on_dark'
set_data_code_2d_param (DataCodeHandle, 'polarity', \
                        'light_on_dark')

* Read an image
read_image (Image, 'datacode/ecc200/ecc200_cpu_010')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)
* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `set_data_code_2d_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`create_data_code_2d_model`,
`read_data_code_2d_model`

## Possible Successors

`get_data_code_2d_param`,
`find_data_code_2d`,
`write_data_code_2d_model`

## Alternatives

`read_data_code_2d_model`

## See also

`query_data_code_2d_params`,
`get_data_code_2d_param`,
`get_data_code_2d_results`,
`get_data_code_2d_objects`

## Module

Data Code

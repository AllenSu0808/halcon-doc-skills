# get_data_code_2d_param (Operator)

## Name

`get_data_code_2d_param` — Get one or several parameters that describe the 2D code model.

## Signature

`def get_data_code_2d_param(data_code_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[int, str, float]]`

`def get_data_code_2d_param_s(data_code_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Union[int, str, float]`

## Description

The operator `get_data_code_2d_param` allows to query the
parameters that are used to describe the 2D code model.
The names of the desired parameters are passed in the generic
parameter *`gen_param_name`*, the corresponding values are
returned in *`gen_param_value`*.
All these parameters can be set and changed at any time with the
operator [`set_data_code_2d_param`](set_data_code_2d_param.md).
A list with the names of all parameters that are valid for the used
2D code type is returned by the operator
[`query_data_code_2d_params`](query_data_code_2d_params.md).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

Note that the symbol structure of GS1 DataMatrix, GS1 QR Code, GS1 Aztec Code,
and GS1 DotCode is identical to the structure of Data Matrix ECC 200, QR Code,
Aztec Code, and DotCode, respectively. Therefore, all symbology specific parameters
applying to Data Matrix ECC 200, QR Code, Aztec Code, or DotCode apply to their
corresponding GS1 variant
as well. In the following, the explicit enumeration of the parameters for
any particular GS1 code is omitted for sake of readability. Instead, the
relevant parameters names are to be inferred from the parameters for the
corresponding non-GS1 code type or can be explicitly queried by
[`query_data_code_2d_params`](query_data_code_2d_params.md) with parameter
*"get_model_params"*.

The following parameters can be queried - ordered by different
categories and 2D code types:

**Size and shape of the symbol:**

- Data Matrix ECC 200 (including the finder pattern):

  - ***"symbol_cols_min"*:** —

    Minimum number of module columns in the symbol.
  - ***"symbol_cols_max"*:** —

    Maximum number of module columns in the symbol.
  - ***"symbol_rows_min"*:** —

    Minimum number of module rows in the symbol.
  - ***"symbol_rows_max"*:** —

    Maximum number of module rows in the symbol.
  - ***"symbol_shape"*:** —

    Possible restrictions concerning the symbol
    shape (rectangle and/or square)

    List of values:
     *"square"*, *"rectangle"*,
    *"any"*.
- QR Code (including the finder pattern):

  - ***"model_type"*:** —

    Type of the QR Code model specification: *1*,
    *2*, *0* (for *"any"*)
  - ***"version_min"*:** —

    Minimum symbol version to be read:
    [*1*..*40*]
    (Model 1: [*1*..*14*])
  - ***"version_max"*:** —

    Maximum symbol version to be read:
    [*1*..*40*]
    (Model 1: [*1*..*14*])
  - ***"symbol_size_min"*:** —

    Minimum symbol size (this value is directly linked to the
    version *"version_min"*):
    [*21*..*177*]
    (Model 1: [*21*..*73*])
  - ***"symbol_size_max"*:** —

    Maximum symbol size (this value is directly linked to the
    version *"version_max"*):
    [*21*..*177*]
    (Model 1: [*21*..*73*])
- Micro QR Code:

  - ***"version_min"*:** —

    Minimum symbol version to be read:
    [*1*..*4*]
  - ***"version_max"*:** —

    Maximum symbol version to be read:
    [*1*..*4*]
  - ***"symbol_size_min"*:** —

    Minimum symbol size (this value is directly linked to the
    version *"version_min"*):
    [*11*..*17*]
  - ***"symbol_size_max"*:** —

    Maximum symbol size (this value is directly linked to the
    version *"version_max"*):
    [*11*..*17*]
- PDF417:

  - ***"symbol_cols_min"*:** —

    Minimum number of data columns in the symbol in codewords,
    i.e., excluding the codewords of the start/stop
    pattern and of the two row indicators.
  - ***"symbol_cols_max"*:** —

    Maximum number of data columns in the symbol in codewords,
    i.e., excluding the codewords of the start/stop
    pattern and of the two row indicators.
  - ***"symbol_rows_min"*:** —

    Minimum number of module rows in the symbol.
  - ***"symbol_rows_max"*:** —

    Maximum number of module rows in the symbol.
- Aztec Code (including the finder pattern):

  - ***"format"*:** —

    Format of the Aztec Code: space separated list with the
    values *"compact"*, *"full_range"*, or
    *"rune"*
  - ***"symbol_size_min"*:** —

    Minimum symbol size
    [*11*..*151*]
  - ***"symbol_size_max"*:** —

    Maximum symbol size
    [*11*..*151*]
- DotCode:

  - ***"symbol_cols_min"*:** —

    Minimum number of module columns in the symbol.
  - ***"symbol_cols_max"*:** —

    Maximum number of module columns in the symbol.
  - ***"symbol_rows_min"*:** —

    Minimum number of module rows in the symbol.
  - ***"symbol_rows_max"*:** —

    Maximum number of module rows in the symbol.

**Appearance of the modules in the image:**

- All 2D code types:

  - ***"polarity"*:** —

    Possible restrictions concerning the polarity of the
    modules, i.e., if they are printed dark on a light
    background or vice versa: *"dark_on_light"*,
    *"light_on_dark"*, *"any"*.
  - ***"discard_undecoded_candidates"*** —

    Controls whether candidates that could not be successfully decoded
    are stored in the model: *"yes"*, *"no"*.
  - ***"mirrored"*:** —

    Describes whether the symbol is or may be mirrored (which is
    equivalent to swapping the rows and columns of the symbol):
    *"yes"*, *"no"*, *"any"*.
- Aztec Code and PDF417:

  - ***"contrast_min"*:** —

    Minimum contrast between the foreground and the background
    of the symbol (specified as gray value difference).
    This measure corresponds to the minimum
    gradient between the symbol's foreground and the
    background.
- Data Matrix ECC 200, Micro QR Code, and QR Code:

  - ***"contrast_tolerance"*:** —

    Describes the tolerance of the search with respect to local
    contrast variations (e.g., in the presence of glare or
    reflections). Depending on the value of the parameter two
    different algorithms are applied. If
    *"contrast_tolerance"* is set to *"high"* the
    robustness in the presence of strong local contrast
    variations is improved. In the case where
    *"contrast_tolerance"* is set to *"low"* the
    algorithm used is less robust to strong local contrast variations,
    however, it is faster and still able to handle contrast
    variations under normal circumstances and therefore
    *"low"* should be used in most cases. If
    *"contrast_tolerance"* is set to *"any"* both
    algorithms are applied.
- All 2D code types except PDF417:

  - ***"module_size_min"*:** —

    Minimum module size in the image in pixels.
  - ***"module_size_max"*:** —

    Maximum module size in the image in pixels.

  With the following parameters it is possible to specify whether
  neighboring foreground modules are connected or whether there is
  or may be a gap between them (possible values are *"no"*
  (no gap) < *"small"* < *"big"*)
  (for DotCode, only *"no"* and *"small"* are
  available):

  - ***"module_gap_min"*:** —

    Minimum gap.
  - ***"module_gap_max"*:** —

    Maximum gap.
- All 2D code types except DotCode:

  - ***"small_modules_robustness"*:** —

    Robustness of the decoding of 2D codes with very small
    module sizes. Setting the parameter
    *"small_modules_robustness"* to *"high"*
    increases the likelihood of being able to
    decode 2D codes with very small module sizes. Additionally,
    in that case the minimum module size should also be adapted
    accordingly, thus *"module_size_min"* and
    *"module_width_min"* (PDF417) should be set to
    the expected minimum module size and width, respectively. Setting
    *"small_modules_robustness"* to *"high"* can
    significantly increase the internal memory usage of
    [`find_data_code_2d`](find_data_code_2d.md). Thus, in the default case
    *"small_modules_robustness"* should be set to *"low"*.

    List of values:
     *"low"*, *"high"*

    Default:
     *"low"* (enhanced: *"low"*,
    maximum: *"high"*)
- PDF417:

  - ***"module_width_min"*:** —

    Minimum module width in the image in pixels.
  - ***"module_width_max"*:** —

    Maximum module width in the image in pixels.
  - ***"module_aspect_min"*:** —

    Minimum module aspect ratio (module height to module width).
  - ***"module_aspect_max"*:** —

    Maximum module aspect ratio (module height to module width).
- Aztec Code:

  - ***"finder_pattern_tolerance"*:** —

    Tolerance of the search with respect to a defect or partially
    occluded finder pattern. Depending on this parameter, different
    algorithms are used during the symbol search in
    [`find_data_code_2d`](find_data_code_2d.md). In one case (*"low"*), it is assumed
    that all rings of the finder pattern can be extracted. In the other
    case (*"high"*) it is assumed that at least one of the
    rings of the finder pattern can be extracted.
  - ***"additional_levels"*:** —

    To increase the robustness of the Aztec Code reader, a number of
    additional search levels (in addition to the search levels derived
    from the minimum and maximum module dimensions) can be specified via
    this parameter. [*0*..*2*]
- Data Matrix ECC 200:

  - ***"slant_max"*:** —

    Maximum slant of the L-shaped finder pattern (the angle is returned
    in radians and corresponds to the distortion that occurs when the
    symbol is printed or during the image acquisition).
  - ***"finder_pattern_tolerance"*:** —

    Tolerance of the search with respect to a defect or
    partially occluded finder pattern. The finder pattern
    includes the L-shaped side as well as the opposite
    alternating side. Depending on this parameter, different
    algorithms are used during the symbol search in
    [`find_data_code_2d`](find_data_code_2d.md). In one case (*"low"*),
    it is assumed that the finder pattern is present to a high
    degree and shows almost no disturbances. In the other case
    (*"high"*), the finder pattern may be defect or
    partially occluded without influencing the recognition and
    the reading of the symbol.
    Note, however, that in this mode
    the parameters for the symbol search should be restricted
    as narrow as possible by using
    [`set_data_code_2d_param`](set_data_code_2d_param.md) because otherwise the
    runtime of [`find_data_code_2d`](find_data_code_2d.md) may increase
    significantly.
    Also note that the two algorithms slightly
    differ from each other in terms of robustness. This may
    lead to different results depending on the value of
    *"finder_pattern_tolerance"* even if the finder
    pattern of the symbol is not disturbed. For example, if
    *"high"* is chosen, only symbols with an equidistant
    module grid can be found (see below), and hence the
    robustness to perspective distortions is
    decreased. Finally, if *"finder_pattern_tolerance"*
    is set to *"any"* both algorithms are applied.
  - ***"alternating_pattern_tolerance"*:** —

    Tolerance of the search with respect to the variation of the
    module widths along the two sides with the alternating pattern.
    The alternating pattern analysis is decisive if
    *"finder_pattern_tolerance"* is set to *"low"*
    (or *"any"* which includes *"low"*).
    Note, however, that this parameter has no
    effect if *"finder_pattern_tolerance"* has been
    set to *"high"*.
    A total of three different values are allowed for this
    parameter, with a higher setting always including the lower
    values: *"low"* allows only a small variation of the
    module widths along the sides with the alternating pattern.
    *"medium"* first tries to meet the strict requirements
    of *"low"*, and if this fails, a larger variation of the
    module widths along the sides with the alternating pattern is
    allowed. Finally, *"high"* includes everything that
    *"medium"* allowed and additionally expands the parameter
    space for the symbol's outer boundaries through further
    attempts. It also softens the relation between the number
    of edges detected and the symbol type used for subsequent
    decoding. The greater robustness in difficult cases comes with
    the disadvantage that *"high"* in particular can lead
    to a significant runtime increase. To counteract this, the
    parameter space should be reduced in total by using
    [`set_data_code_2d_param`](set_data_code_2d_param.md), e.g., by setting
    the expected symbol sizes as tight as possible.
  - ***"module_grid"*:** —

    Describes whether the size of the modules may vary (in a
    specific range) or not. Dependent on the parameter
    different algorithms are used for the calculation of the
    module's center positions. If it is set to
    *"fixed"*, an equidistant grid is used. Allowing a
    variable module size (*"variable"*), the grid is
    aligned only to the alternating side of the finder pattern.
    With *"any"* both approaches are tested one after
    the other. Please note that the value of
    *"module_grid"* is ignored if
    *"finder_pattern_tolerance"* is set to
    *"high"*. In this case, an equidistant grid is
    assumed.
- Data Matrix ECC 200 and QR Code:

  - ***"deformation_tolerance"*:** —

    Search tolerance regarding the deformation of codes. Depending on this
    parameter, an algorithm for compensating curvature (*"curved"*)
    is used in [`find_data_code_2d`](find_data_code_2d.md) or not (*"low"*).
- QR Code and Micro QR Code:

  - ***"position_pattern_min"*:** —

    Number of position detection patterns that have to be visible
    for generating a new symbol candidate.

**General model behavior:**

- All 2D code types:

  - ***"persistence"*:** —

    Controls whether certain intermediate results of the symbol
    search with [`find_data_code_2d`](find_data_code_2d.md) are stored only
    temporarily or persistently in the model: *0*
    (temporary), *1* (persistent).
  - ***"strict_model"*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) while
    detecting symbols that could be read but that do not fit
    the model restrictions concerning the size of the symbols:
    *"yes"* (strict: such symbols are rejected),
    *"no"* (not strict: all readable symbols are
    returned as a result independent of their size and the
    size specified in the model). Please note that
    the module size restrictions (*"module_size_min"* and
    *"module_size_max"*) are not checked even if
    *"strict_model"* is set to *"yes"*.
  - ***"string_encoding"*:** —

    Returns the expected encoding of the string that is encoded in the
    symbol:
    *"utf8"*, *"locale"*, *"latin1"*, *"shiftjis"*,
    *"gb2312"*, *"raw"*, or *"auto"*.
  - ***"symbol_type"*:** —

    Returns symbol type which was set with [`create_data_code_2d_model`](create_data_code_2d_model.md).
  - ***"timeout"*:** —

    Enables aborting [`find_data_code_2d`](find_data_code_2d.md) after a defined period in
    milliseconds: *"false"*, *-1*,
    *20* .. *100*.
- All 2D code types except Aztec Code:

  - ***"strict_quiet_zone"*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) while
    detecting symbols that could be read but show defects in
    their quiet zone.
    Possible values:

    - ***"yes"*:** —

      Decoded symbols with poor grades for their quiet zone are not
      returned as a result.
      The quiet zone is validated similar to the method used for
      print quality inspection, but regarded as being only one module
      large.
      The *"status"* for rejected symbols is set to
      *"quiet zone is missing"*.
    - ***"no"* (default):** —

      All readable symbols are returned as a result.
- All 2D code types except DotCode:

  - ***"quality_isoiec15415_aperture_size"*:** —

    Defines the aperture sizes for ISO/IEC 15415:2024 print quality
    inspection as fraction of the module width
    (see ISO/IEC 15415:2024 section 5.6.2 and 7.3.1).
  - ***"quality_isoiec15415_reflectance_reference"*:** —

    Defines the reference reflectance for ISO/IEC 15415:2024 print quality
    inspection as grayvalue (see ISO/IEC 15415:2024 section 5.6.1).
  - ***"quality_isoiec15415_smallest_module_size"*:** —

    Defines the module size used to obtain the synthetic aperture for
    ISO/IEC 15415:2024 print quality inspection
    (see ISO/IEC 15415:2024 section 7.3.1).
- Data Matrix ECC 200:

  - ***"strict_fp_and_qz"*:** —

    Controls the behavior of [`find_data_code_2d`](find_data_code_2d.md) when detecting readable
    symbols with a low number of rows ($\le$ 12) and columns ($\le$ 18).
    These symbols are particularly at risk of being false positive decodes due to their
    low error correction capacity. Possible values:

    - ***"true"*:** —

      All successfully decoded symbols that meet the criteria described above
      are checked. Symbols with a disturbed outer finder pattern or with a
      disturbed quiet zone might be discarded based on the classification results
      of the corresponding module positions. Discarded results are not returned
      as a result. Their corresponding *"status"* values are returned
      starting with *"strict_fp_and_qz: ..."*. The colon is followed by
      more detailed information regarding the failed check.
    - ***"tolerant"* (Default):** —

      In this mode, only symbols of the specified size and with an increased
      probability of actually showing a false positive result run through the
      additional checks.
    - ***"false"*:** —

      The additional checks are completely deactivated.

    See also [`set_data_code_2d_param`](set_data_code_2d_param.md) for more information.
- Data Matrix ECC 200, DotCode, Micro QR Code, and QR Code:

  - ***"candidate_selection"*:** —

    Controls the selection of candidate regions that are used for symbol
    detection. Setting this parameter to *"extensive"* increases
    the number of generated candidate regions and thus the likelihood of
    detecting a code. When this parameter is set to *"all"*, all
    possible candidates are used.
    If *"candidate_selection"* is set to
    *"default"*, less candidate regions are used.
- DotCode:

  - ***"max_allowed_error_correction"*:** —

    Controls the maximum allowed error correction.
    Due to the high error correction capacity, it is possible to
    successfully decode false positive DotCode candidates.
    Especially candidates which only cover a small part of a
    real DotCode may be decoded successfully because of the
    error correction capabilities. This is the case because DotCode symbols
    can consist of almost every size. So there are fewer criteria
    to decide whether the candidate is valid or not. In order to tackle
    this problem, the parameter *"max_allowed_error_correction"* can
    be used to specify the percentage of maximum allowed error correction.
    Per default the value is set to *"0.9"*, which means
    90%. Setting the value to e.g., *"0.5"* means, only candidates which
    could be decoded with maximum 50% used error correction, will be
    returned as successfully decoded results.

    Value range:
     [*0.0* .. *1.0*]

    Default:
     *"0.9"*

It is possible to query the values of several or all parameters
with a single operator call by passing a tuple containing the names
of all desired parameters to *`gen_param_name`*.
As a result a tuple of the same length with the corresponding values
is returned in *`gen_param_value`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`data_code_handle`** (input_control)  datacode_2d `→` HHandle

Handle of the 2D code model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that
are to be queried for the 2D code model.

Default:
"polarity"

List of values:
"additional_levels", "alternating_pattern_tolerance", "candidate_selection", "contrast_min", "contrast_tolerance", "decoding_scheme", "deformation_tolerance", "discard_undecoded_candidates", "finder_pattern_tolerance", "format", "max_allowed_error_correction", "mirrored", "model_type", "module_aspect_max", "module_aspect_min", "module_gap_max", "module_gap_min", "module_grid", "module_size_max", "module_size_min", "module_width_max", "module_width_min", "persistence", "polarity", "position_pattern_min", "quality_isoiec15415_aperture_size", "quality_isoiec15415_decode_algorithm", "quality_isoiec15415_reflectance_reference", "quality_isoiec15415_smallest_module_size", "slant_max", "small_modules_robustness", "strict_fp_and_qz", "strict_model", "strict_quiet_zone", "string_encoding", "symbol_cols_max", "symbol_cols_min", "symbol_rows_max", "symbol_rows_min", "symbol_shape", "symbol_size_max", "symbol_size_min", "symbol_type", "timeout", "version_max", "version_min"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[Union[int, str, float]]

Values of the generic parameters.

## Result

The operator `get_data_code_2d_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`query_data_code_2d_params`,
`set_data_code_2d_param`,
`find_data_code_2d`

## Possible Successors

`find_data_code_2d`,
`write_data_code_2d_model`

## Alternatives

`write_data_code_2d_model`

## See also

`query_data_code_2d_params`,
`set_data_code_2d_param`,
`get_data_code_2d_results`,
`get_data_code_2d_objects`,
`find_data_code_2d`

## Module

Data Code

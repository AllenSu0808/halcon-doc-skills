# FindDataCode2d (Operator)

## Name

`FindDataCode2d` — Detect and read 2D code symbols in an image or
train the 2D code model.

## Signature

`static void HOperatorSet.FindDataCode2d(HObject image, out HObject symbolXLDs, HTuple dataCodeHandle, HTuple genParamName, HTuple genParamValue, out HTuple resultHandles, out HTuple decodedDataStrings)`

`HXLDCont HDataCode2D.FindDataCode2d(HImage image, HTuple genParamName, HTuple genParamValue, out HTuple resultHandles, out HTuple decodedDataStrings)`

`HXLDCont HDataCode2D.FindDataCode2d(HImage image, string genParamName, int genParamValue, out int resultHandles, out string decodedDataStrings)`

`HXLDCont HImage.FindDataCode2d(HDataCode2D dataCodeHandle, HTuple genParamName, HTuple genParamValue, out HTuple resultHandles, out HTuple decodedDataStrings)`

`HXLDCont HImage.FindDataCode2d(HDataCode2D dataCodeHandle, string genParamName, int genParamValue, out int resultHandles, out string decodedDataStrings)`

## Description

The operator `FindDataCode2d` detects 2D code symbols
in the input image (*`image`*) and reads the data that is encoded
in the symbol.
Before calling `FindDataCode2d`, a model of a class of 2D
2D codes that matches the symbols in the images must be
created with [`CreateDataCode2dModel`](create_data_code_2d_model.md) or
[`ReadDataCode2dModel`](read_data_code_2d_model.md).
The handle returned by these operators is passed to
`FindDataCode2d` in *`dataCodeHandle`*.
To look for more than one symbol in an image, the generic parameter
*"stop_after_result_num"* can be passed to
*`genParamName`* together with the number of requested
symbols as *`genParamValue`*.

As a result the operator returns for every successfully decoded
symbol the surrounding XLD contour (*`symbolXLDs`*), a
result handle, which refers to a candidate structure that stores
additional information about the symbol as well as the search and
decoding process (*`resultHandles`*), and the string that is
encoded in the symbol (*`decodedDataStrings`*).
Passing the candidate handle from *`resultHandles`* together
with the generic parameter *"decoded_data"*,
[`GetDataCode2dResults`](get_data_code_2d_results.md) returns a tuple with the ASCII code
of all characters of the string (see also
[Tuple / String Operations](toc_tuple_stringoperations.md)).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

The symbol structure of GS1 DataMatrix, GS1 QR Code, GS1 Aztec Code,
and GS1 DotCode is identical to the structure of
Data Matrix ECC 200, QR Code, Aztec Code, and DotCode, respectively.
Therefore, all parameters, settings, and rules applying to Data Matrix
ECC 200, QR Code, Aztec Code, or DotCode apply to their GS1 variants as
well. The GS1 symbologies enforce merely additional rules for the format of
the data carried by the codes. The data has to be organized in so called GS1
application element strings according to the GS1 General Specifications.
For example, if the 2D code model *`dataCodeHandle`* is created as
GS1 DataMatrix, then `FindDataCode2d` only returns a result if
the underlying symbol is a valid Data Matrix ECC 200 symbol, and only if its
data conforms to the GS1 application element strings rules.
For the GS1 application element strings it is only checked if the
application identifiers exist in the GS1 General Specifications.
In contrast,
`FindDataCode2d` will return no results for Data Matrix ECC 200
containing general data. The same is valid for GS1 QR Code, GS1 Aztec Code,
and GS1 DotCode Code.

**Adjusting the model**

If there is a symbol in the image that cannot be read, it should be
verified, whether the properties of the symbol fit the model parameters.
Special attention should be paid to

- the correct polarity (*"polarity"*, light-on-dark or
  dark-on-light),
- the symbol size (*"symbol_size"* for Data Matrix ECC 200,
  Aztec Code, and DotCode),
- *"version"* for QR Code,
- *"format"* for Aztec Code,
- the module size (*"module_size"* for Data Matrix ECC 200,
  QR Code, Micro QR Code, Aztec Code, and DotCode,
  *"module_width"* and *"module_aspect"* for PDF417),
- the possibility of a mirroring of the symbol (*"mirrored"*),
- and the specified minimum contrast (*"contrast_min"* for
  Aztec Code and PDF417).

Further relevant parameters are the gap between neighboring
foreground modules and, for Data Matrix ECC 200, the maximum slant of the
L-shaped finder pattern (*"slant_max"*).
The current settings for these parameters are returned by the
operator [`GetDataCode2dParam`](get_data_code_2d_param.md).
If necessary, the corresponding model parameters can be adjusted with
[`SetDataCode2dParam`](set_data_code_2d_param.md).

It is recommended to adjust the model as well as possible to the
symbols in the images also for runtime reasons.
In general, the runtime of `FindDataCode2d` is higher for
a more general model than for a more specific model.
One should take into account that a general model leads to a high
runtime especially if *no* valid 2D code can be found.

**Train the model**

Besides setting the model parameters manually with
[`SetDataCode2dParam`](set_data_code_2d_param.md), the model can also be trained with
`FindDataCode2d` based on one or several sample images.
For this, the generic parameter *"train"* must be passed in
*`genParamName`*.
The corresponding value passed in *`genParamValue`* determines
the model parameters that should be learned.
The following values are possible:

- All 2D code types:

  - ***"all"*:** —

    All model parameters that can be trained.
  - ***"symbol_size"*:** —

    Size of the 2D code symbol.

    The model parameters trained for Data
    Matrix ECC200, PDF417, and DotCode are
    *"symbol_cols_min"*, *"symbol_cols_max"*,
    *"symbol_rows_min"*, and *"symbol_rows_max"*.
    Additionally, the model parameter *"symbol_shape"* (square or
    rectangular) is trained for Data Matrix ECC 200 only.

    For QR Code and Micro QR Code it is also possible to pass
    *"version"*. The model parameters trained hereby are
    *"symbol_size_min"*, *"symbol_size_max"*,
    *"version_min"*, and *"version_max"*.

    The model parameters trained for Aztec Code are
    *"symbol_size_min"* and *"symbol_size_max"*.
  - ***"module_size"*:** —

    Size of the modules.
    The model parameters trained are *"module_size_min"* and
    *"module_size_max"*.

    For PDF417 this includes the module width and the module
    aspect ratio, so thereby the respective model parameters are
    *"module_width_min"*, *"module_width_max"*,
    *"module_aspect_min"*, and *"module_aspect_max"*.
  - ***"polarity"*:** —

    Polarity of the symbols, i.e. they may appear dark on a light
    background or light on a dark background.
    The model parameter trained is *"polarity"*.
  - ***"mirrored"*:** —

    Whether the symbols in the image are mirrored or not.
    The model parameter trained is *"mirrored"*.
- Data Matrix ECC 200, Aztec Code, PDF417, QR Code, and Micro QR Code only:

  - ***"small_modules_robustness"*:** —

    Robustness of the decoding of 2D codes with very small
    module sizes. This parameter is not trained for DotCode.
    The model parameter trained is *"small_modules_robustness"*.
    Note that the training of the parameter is deactivated
    internally if the training image exceeds the maximum
    image size (see [`GetSystem`](get_system.md) *"halcon_xl"*).
- Aztec Code and PDF417 only:

  - ***"contrast"*:** —

    Minimum contrast for detecting the symbols.
    The model parameter trained is *"contrast_min"*.
- Data Matrix ECC 200, Micro QR Code, and QR Code only:

  - ***"contrast_tolerance"*:** —

    The tolerance of the symbol search with respect to strong
    local contrast variations.
    The model parameter trained is *"contrast_tolerance"*.
- All 2D code types except PDF417::

  - ***"module_shape"*:** —

    Whether there is a gap between neighboring foreground modules or
    whether they are connected.
    The model parameters trained are *"module_gap_min"* and
    *"module_gap_max"*.
- Data Matrix ECC 200 and Aztec Code only:

  - ***"finder_pattern_tolerance"*:** —

    The allowed tolerance of the symbol search with respect to
    a defect or partially occluded finder pattern.
    The model parameter trained is *"finder_pattern_tolerance"*.
- Data Matrix ECC 200, DotCode, Micro QR Code, and QR Code only:

  - ***"candidate_selection"*:** —

    Selection of candidate regions to be processed.
    The model parameter trained is *"candidate_selection"*.
- Data Matrix ECC 200 only:

  - ***"alternating_pattern_tolerance"*:** —

    The tolerance of the symbol search with respect to a
    variation of the module widths along the two sides
    with the alternating pattern.
    The model parameter trained is
    *"alternating_pattern_tolerance"*.
  - ***"module_grid"*:** —

    Algorithm for calculating the module positions
    (fixed or variable grid).
    The model parameter trained is *"module_grid"*.
  - ***"image_proc"*:** —

    Adjusting different internal image processing parameters.
    Until now, only the maximum slant of the L-shaped finder
    pattern of the Data Matrix ECC 200 symbols is set (more parameters
    may follow in future).
    The model parameter trained is *"slant_max"*.
- QR Code only:

  - ***"model_type"*:** —

    Whether the QR Code symbols follow the Model 1 or Model 2
    specification.
    The model parameter trained is *"model_type"*.
  - ***"position_pattern_min"*:** —

    Number of position detection patterns that have to be visible
    for generating a new symbol candidate.
    The model parameter trained is *"position_pattern_min"*.
- Aztec Code only

  - ***"additional_levels"*:** —

    The number of additional pyramid levels.
    The model parameter trained is *"additional_levels"*.

It is possible to train several of these parameters in one
call of `FindDataCode2d` by passing the generic parameter
*"train"* in a tuple more than once in conjunction with the
corresponding parameters: e.g.,
*`genParamName`* = *["train","train"]* and
*`genParamValue`* = *["polarity","module_size"]*.
Furthermore, in conjunction with *"train"* = *"all"*
it is possible to exclude single parameters from training
explicitly again by passing *"train"* more than once.
The names of the parameters to exclude, however, must be prefixed
by *"~"*:
*`genParamName`* = *["train","train"]* and
*`genParamValue`* =
*["all","~contrast"]*,
e.g., trains all parameters except the minimum contrast.

For training the model, the following aspects should be considered:

- To use several images for the training, the operator
  `FindDataCode2d` must be called with the parameter
  *"train"* once for every sample image.
- It is also possible to train the model with several symbols in
  one image.
  Here, the generic parameter *"stop_after_result_num"*
  must be passed as a tuple to *`genParamName`* together with
  *"train"*.
  The number of symbols in the image is passed in
  *`genParamValue`* together with the training parameters.
- If the training image contains more symbols than the one that
  shall be used for the training the domain of the image should
  be reduced to the symbol of interest with [`ReduceDomain`](reduce_domain.md).
- In an application with very similar images, *one* image for
  training may be sufficient if the following assumptions are true:
  The symbol size (in modules) is the same for all symbols used in
  the application, foreground and background modules are of the
  same size and there is no gap between neighboring foreground
  modules, the background has no distinct texture; and the
  contrast of all images is almost the same.
  Otherwise, several images should be used for training.
- In applications where the symbol size (in modules) is not fixed,
  the smallest as well as the biggest symbols should be used for
  the training.
  If this can not be guaranteed, the limits for the symbol size
  should be adapted manually after the training, or the symbol
  size should entirely be excluded from the training.
- During the first call of `FindDataCode2d` in the
  training mode, the trained model parameters are restricted to
  the properties of the detected symbol.
  Any successive training call will, where necessary, extend the
  parameter range to cover the already trained symbols as well as
  the new symbols.
  Resetting the model with [`SetDataCode2dParam`](set_data_code_2d_param.md) to one of
  its default settings (*"default_parameters"* =
  *"standard_recognition"*, *"enhanced_recognition"*, or
  *"maximum_recognition"*) will also reset the training
  state of the model.
  With [`SetDataCode2dParam`](set_data_code_2d_param.md) and *"trained"* the training
  state of parameters can be set to trained. Subsequent training of this
  parameter will not reset its value, but extend it, so symbols readable
  by the previous value can still be read after training.
- If `FindDataCode2d` is not able to read the
  symbol in the training image, this will produce no error or
  exception handling.
  This can simply be tested in the program by checking the
  results of `FindDataCode2d`: *`symbolXLDs`*,
  *`resultHandles`*, *`decodedDataStrings`*.
  These tuples will be empty, and the model will not be modified.

Note that during training, a possibly set timeout is ignored (see
[`SetDataCode2dParam`](set_data_code_2d_param.md)).

**Functionality of the symbol search**

- All 2D code types:

  Depending on the current settings of the 2D code model (see
  [`SetDataCode2dParam`](set_data_code_2d_param.md)), the operator
  `FindDataCode2d` performs several passes for searching
  the 2D code symbols.
  The search starts at the highest pyramid level, where -
  according to the maximum module size defined in the 2D code model
  - the modules can be separated.
  In addition, in every pyramid level the preprocessing can vary
  depending on the presets for the module gap.
  If the 2D code model enables dark symbols on a light background as
  well as light symbols on a dark background, within the current pyramid
  level, the dark symbols are searched first.
  Then the passes for searching light symbols follow.
  A pass consists of two phases: The search phase is used to
  look for the finder patterns and to generate a symbol candidate for
  every detected finder pattern, and the evaluation phase, where in a
  lower pyramid level all candidates are investigated and - if
  possible - read.

  The operator call is either terminated after successfully decoding
  the requested number of symbols, after processing all search passes,
  or due to a timeout (see [`SetDataCode2dParam`](set_data_code_2d_param.md)). The
  number of requested symbols can be specified via the generic
  parameter *`genParamName`* = *"stop_after_result_num"*.
  Without specifying this number the search stops as soon as one
  symbol could be decoded.
- Data Matrix ECC 200, QR Code, and Micro QR Code:

  The complexity of the symbol search can be controlled with the
  generic parameter *`genParamName`* = *"symbol_search"*.
  Per default, *"symbol_search"* is set to
  *`genParamValue`* = *"default"*.

  - For simple images, i.e. images that:

    - only contain symbols with high contrast and a large quiet
      zone and
    - show a homogeneous background

    a less complex and (in simple cases) faster symbol search method can
    be used by setting *"symbol_search"* to *"rudimental"*.
    Please note that in this case the following
    parameters do not have any effect: *"module_gap_min"*,
    *"module_gap_max"*, *"module_gap"*,
    *"finder_pattern_tolerance"*,*"contrast_tolerance"*,
    and *"candidate_selection"*.
    Further, no parameters can be trained with this method.
  - For large images with many codes and a highly structured
    background, the number of code candidates can be very high for
    certain parameter settings, e.g. for *"maximum_recognition"*.
    For performance reasons, the Data Matrix ECC 200 reader, the QR Code
    reader, and the Micro QR Code reader stop by default after 10000
    processed candidates.

    For cases, where more candidates need to be considered in order to
    decode all codes in the image the *"symbol_search"* can be set
    to *"exhaustive"*. This will stop the search only when
    *"stop_after_result_num"* codes have been decoded or all
    candidates have been processed. Please note that this may increase
    the runtime accordingly. The actual number of candidates can be
    queried with [`GetDataCode2dResults`](get_data_code_2d_results.md).

**Query results of the symbol search**

With the result handles and the operators
[`GetDataCode2dResults`](get_data_code_2d_results.md) and
[`GetDataCode2dObjects`](get_data_code_2d_objects.md), additional data can be requested
about the search process, e.g., the number of internal search passes
or the number of investigated candidates, and - together with
the *`resultHandles`* - about the symbols, like the symbol
and module size, the contrast, or the raw 2D coded in the symbol.
In addition, these operators provide information about all
investigated candidates that could not be read.
In particular, this helps to determine if a candidate was actually
generated at the symbol's position during the preprocessing and
- by the value of a status variable - why the search or
reading was aborted.
Further information about the parameters can be found with the
operators [`GetDataCode2dResults`](get_data_code_2d_results.md) and
[`GetDataCode2dObjects`](get_data_code_2d_objects.md).

**Timeout and Abort**

The operator `FindDataCode2d` can be aborted by a timeout and
dynamically. With the operator [`SetDataCode2dParam`](set_data_code_2d_param.md) you can
specify a timeout. If `FindDataCode2d` reaches this timeout, it
returns all codes decoded so far. Alternatively, you can call
[`SetDataCode2dParam`](set_data_code_2d_param.md) with *"abort"* from another thread to
abort `FindDataCode2d` dynamically.

The information whether the operator was aborted or not can be queried by
calling [`GetDataCode2dResults`](get_data_code_2d_results.md) with the parameter *"aborted"*.

Furthermore, the operator `FindDataCode2d` can be canceled, which
means no result is returned but instead an error is returned. This can be done
with the operator [`SetOperatorTimeout`](set_operator_timeout.md) or [`InterruptOperator`](interrupt_operator.md).
If `FindDataCode2d` is canceled by [`SetOperatorTimeout`](set_operator_timeout.md),
H_ERR_TIMEOUT (9400) is returned. If `FindDataCode2d` is
canceled by [`InterruptOperator`](interrupt_operator.md), H_ERR_CANCEL (22) is returned.
Note: Both mentioned operators are only supported in cancel mode.

**Special parallelization for Data Matrix ECC 200**

The operator `FindDataCode2d` supports special parallelization
features for Data Matrix ECC 200. This additional internal parallelization
can lead to a significantly shorter execution time under certain
circumstances. In general, faster calculation times can be expected if,
e.g., [`SetDataCode2dParam`](set_data_code_2d_param.md) is used to set the value *"any"*
for one or more of the parameters *"polarity"*, *"contrast_tolerance"*
and *"finder_pattern_tolerance"*, or if the set values for
*"module_gap_min"* and *"module_gap_max"* differ. In all these cases,
a series of parameter values must be taken into account. This applies in particular
if *"default_parameters"* has been set to *"enhanced_recognition"*
or *"maximum_recognition"*.

Please note, that the memory consumption increases with the number of parallel
running threads. To reduce the memory consumption [`SetSystem`](set_system.md) can be used
to either set the number of threads with the parameter *"thread_num"*, or
to switch off the temporary memory cache with the parameter *"temporary_mem_cache"*.
The Data Matrix ECC 200 specific parallelization can also be easily disabled
by setting the generic parameter *`genParamName`* = *"specific_parallelization"*
to *"disable"*. Note that this will only switch off the additional internal
parallelization for Data Matrix ECC 200. Certain sub-tasks might be still
processed in parallel. For more information on how to disable the entire
parallelization, see the operator reference of [`SetSystem`](set_system.md) with its
parameters *"thread_num"* and *"parallelize_operators"*. In general,
however, it should not be necessary to switch off the specific parallelization.
Per default, *"specific_parallelization"* is set to *"enable"*.

**Chinese characters**

If a QR Code contains Chinese characters encoded according to the
Chinese national standard GBT 18284-2000, `FindDataCode2d`
returns these characters UTF-8 encoded in *`decodedDataStrings`*, if
the system parameter *"filename_encoding"* is set to *"utf8"*.
The contents of *"decoded_data"*, which can be retrieved with
[`GetDataCode2dResults`](get_data_code_2d_results.md), are never converted to UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- dataCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Input image. If the image has a reduced domain, the 2D code
search is reduced to that domain. This usually reduces the runtime of the
operator. However, if the 2D code is not fully inside the domain, the
2D code might not be found correctly.
In rare cases, 2D codes may be found outside the domain. If these results
are undesirable, they have to be subsequently eliminated.

**`symbolXLDs`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

XLD contours that surround the successfully decoded 2D
code symbols. The order of the contour points reflects the
orientation of the detected symbols. The contours begin in
the top left corner (see *"orientation"* in the
reference of [`GetDataCode2dResults`](get_data_code_2d_results.md)) and
continue clockwise.

![figure](../assets/582bef634a8fc270.svg)

Order of points of *`symbolXLDs`*

![figure](../assets/6b71e61674616929.svg)

**`dataCodeHandle`** (input_control, state is modified)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of (optional) parameters for
controlling the behavior of the operator.

Default:
[]

List of values:
"specific_parallelization", "stop_after_result_num", "symbol_search", "train"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the optional generic parameters.

Default:
[]

Suggested values:
"all", "model_type", "symbol_size", "version", "module_size", "small_modules_robustness", "module_shape", "polarity", "mirrored", "contrast", "candidate_selection", "module_grid", "alternating_pattern_tolerance", "finder_pattern_tolerance", "deformation_tolerance", "contrast_tolerance", "position_pattern_min", "additional_levels", "image_proc", "rudimental", "default", "exhaustive", 1, 2, 3, "enable", "disable"

**`resultHandles`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Handles of all successfully decoded 2D code
symbols.

**`decodedDataStrings`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Decoded data strings of all detected 2D code
symbols in the image.

## Example (HDevelop)

```
* Examples showing the use of find_data_code_2d.
* First, the operator is used to train the model, afterwards it is used to
* read the symbol in another image.

* Create a model for reading Data Matrix ECC 200 codes
create_data_code_2d_model ('Data Matrix ECC 200', [], [], DataCodeHandle)
* Read a training image
read_image (Image, 'datacode/ecc200/ecc200_cpu_007')
* Train the model with the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, 'train', 'all', \
                   ResultHandles, DecodedDataStrings)
*
* End of training / begin of normal application
*

* Read an image
read_image (Image, 'datacode/ecc200/ecc200_cpu_010')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)

* Display all symbols, the strings encoded in them, and the module size
dev_set_color ('green')
for i := 0 to |ResultHandles| - 1 by 1
    select_obj (SymbolXLDs, SymbolXLD, i+1)
    dev_display (SymbolXLD)
    get_contour_xld (SymbolXLD, Row, Col)
    set_tposition (WindowHandle, max(Row), min(Col))
    write_string (WindowHandle, DecodedDataStrings[i])
    get_data_code_2d_results (DataCodeHandle, ResultHandles[i], \
                              ['module_height','module_width'], ModuleSize)
    new_line (WindowHandle)
    write_string (WindowHandle, 'module size = ' + ModuleSize[0] + 'x' + \
                                 ModuleSize[1])
endfor

* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `FindDataCode2d` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`CreateDataCode2dModel`,
`ReadDataCode2dModel`,
`SetDataCode2dParam`

## Possible Successors

`GetDataCode2dResults`,
`GetDataCode2dObjects`,
`WriteDataCode2dModel`

## See also

`CreateDataCode2dModel`,
`SetDataCode2dParam`,
`GetDataCode2dResults`,
`GetDataCode2dObjects`

## References

GS1 General Specifications; Version 12; Issue 1, Jan-2012; GS1.

## Module

Data Code

# SetBarCodeParam (Operator)

## Name

`SetBarCodeParam` — Set selected parameters of the bar code model.

## Signature

`static void HOperatorSet.SetBarCodeParam(HTuple barCodeHandle, HTuple genParamName, HTuple genParamValue)`

`void HBarCode.SetBarCodeParam(HTuple genParamName, HTuple genParamValue)`

`void HBarCode.SetBarCodeParam(string genParamName, double genParamValue)`

## Description

The operator `SetBarCodeParam` is used to set or change the
different parameters of a bar code model in order to adapt to special
properties of the bar codes or to a particular appearance in the image.
All parameters can also be set while creating the bar code model with
[`CreateBarCodeModel`](create_bar_code_model.md). The current configuration of the bar code
model can be queried with [`GetBarCodeParam`](get_bar_code_param.md).

The following overview lists the different generic parameters with the
respective value ranges and default values:

### Size of bar code elements:

The first two parameters, *"element_size_min"* and
*"element_size_max"*, influence the search for candidate
regions and the decoding of the bar code. But note that these values
are not used as strict limits for the size of the elements of found bar
codes, i.e., also bar codes with elements that are smaller
than *"element_size_min"* or larger than
*"element_size_max"* may be found.

Attention:
 When the size is changed by calling the operator
`SetBarCodeParam`, the consistency of the parameters
*"element_size_min"* and *"element_size_max"* is verified. Both
parameters should be set in the same call.

- ***"element_size_min"*:** —

  Minimum size of the base bar code elements (also called 'modules'
  or 'narrow bars', depending on the specific bar code type), i.e.,
  the minimum width of the narrowest bars and spaces for the specific
  bar code type. The value of this parameter is defined in pixels.
  For low resolution bar codes, the value should be reduced
  to *1.5*, and in some cases even as low as *0.6*.
  If the *"element_size_min"* is specified below *2.0* pixels an
  additional decoding attempt is made (see
  *"small_elements_robustness"* for more details on this attempt).
  In the case of huge bar codes, the value should be increased, which
  results in a shorter execution time and fewer candidates.

  Suggested values:
   [*1.2*, ..., *10.0*]

  Value range:
   [*0.6*, ..., *64*]

  Default:
   *2.0*
- ***"element_size_max"*:** —

  Maximum size of the base bar code elements (also called 'modules'
  or 'narrow bars', depending on the specific bar code type), i.e.,
  the maximum width of the narrowest bars and spaces for the specific
  bar code type. The value of *"element_size_max"* is defined in
  pixels. It should be adequately low such that two neighboring bar
  codes are not fused into a single one. On the other hand the value should be
  sufficiently high in order to find the complete bar code region.

  Suggested values:
   [*4.0*, ..., *60.0*]

  Value range:
   [*1*, ..., *256*]

  Default:
   *8.0*
- ***"element_size_variable"*:** —

  In some bar code images, the
  smallest element size may vary across a given bar code object. These
  deformations might be caused by printing errors, perspective projection,
  or by deformations of the surface on which the bar code is printed
  (e.g., barrel distortion on a bottle).
  By default, the bar code reader cannot handle such distortions.
  However, if *"element_size_variable"* is set to
  *"true"*, the bar code reader tries to compensate for such
  distortions. Please note that in some situations it is still not possible
  to undistort the bar code image.

  The parameter *"element_size_variable"* applies to the
  following bar code types only:

  - Code 128
  - GS1-128
  - GS1 DataBar Limited
  - GS1 DataBar Expanded
  - GS1 DataBar Expanded Stacked

  Any other bar code type is unaffected by this parameter.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*
- ***"barcode_height_min"*:** —

  Minimum bar code height. The value of this parameter is defined
  in pixels. The default value is *-1*, meaning that the
  bar code reader automatically derives
  a reasonable height from the other parameters. Just for very flat
  and very high bar codes a manual adjustment of this parameter can
  be necessary. In the case of a bar code with a height of less than
  16 pixels the respective height should be set by the user. Note,
  that the minimum value is 8 pixels. If the bar code is very high,
  i.e. 70 pixels and more, manually adjusting to the respective height
  can lead to a speed-up of the subsequent finding and reading
  operation.

  Suggested values:
   *-1*, *8*, *64*

  Default:
   *-1*
- ***"barcode_width_min"*:** —

  Minimum bar code width. The value of this parameter is defined in pixels.
  The width of a bar code depends on many factors:

  - resolution of the camera
  - distance between camera and bar code
  - bar code type
  - number of encoded characters

  If these properties are constant throughout the application, this
  parameter should be set in order to increase both speed and robustness.
  The default value is *-1*, meaning that the reader estimates
  a minimum bar code width based on symbology specifications
  and the parameter *"element_size_min"*.

  Suggested values:
   *-1*, *40*,
  *50*, *60*

  Default:
   *-1*
- ***"barcode_width_max"*:** —

  Maximum bar code width. The value of this parameter is defined in pixels.
  The width of a bar code depends on many factors:

  - resolution of the camera
  - distance between camera and bar code
  - bar code type
  - number of encoded characters

  If the maximum bar code width is known, this parameter can increase the
  robustness. Especially the unintended merging of bar codes lying close to
  each other can be avoided reliably. In general it should not be necessary
  to set this parameter. The default value is *-1*, meaning that the
  maximum bar code width is not restricted.

  Suggested values:
   *-1*, *300*,
  *400*, *500*

  Default:
   *-1*

### Scanning settings:

- ***"num_scanlines"*:** —

  Maximum number of scanlines used during the scanning of a (candidate)
  bar code.
  If *"num_scanlines"* is not set (the parameter has a value
  of *0*), the maximum number of scanlines is determined internally
  and it will be *10* for all single-row bar codes, *20* for
  GS1 DataBar Stacked and GS1 DataBar Stacked Omnidirectional,
  and *55* for GS1 DataBar Expanded Stacked.
  With this parameter, you can improve performance in two cases. In
  the first case, the image contains many false candidates. While the
  bar code itself is usually decoded after one or two scans (except
  for stacked bar codes, see below), a false
  candidate is scanned with the default value of 10 scanlines, which
  increases the runtime unnecessarily. Reducing the number of scanlines
  can therefore improve performance in images with many
  false candidates. As a rule of thumb, images with higher quality
  need less scanlines than images of lower quality. For an average
  image, a value between 2 and 5 should be sufficient. If a bar code
  can, however, not be detected after reducing the number of scanlines,
  the number has to be increased again.
  The second case concerns stacked bar codes (currently GS1 DataBar
  Stacked, GS1 DataBar Stacked Omnidirectional, and GS1 DataBar Expanded
  Stacked). Here, all scanlines are evaluated, in contrast to single-row
  bar codes (e.g., Code 128, EAN 13, or GS1 DataBar Limited) where the
  scanning stops after the code is decoded successfully.
  Since the scanning of the scanlines is actually one of the most time
  consuming parts of the [`FindBarCode`](find_bar_code.md) algorithm, adjusting
  *"num_scanlines"* might result in essential performance
  improvements. This is especially valid for GS1 DataBar Expanded Stacked.
  A GS1 DataBar Expanded Stacked symbol might have up to 11 rows and
  therefore 55 scanlines are required to robustly detect all of them.
  If only symbols with smaller number of rows are expected,
  you can reduce *"num_scanlines"*, leaving 1.5 to 5 scanlines
  per row.

  If this parameter is set to a value that is smaller than the specified
  *"min_identical_scanlines"* value, the value of the parameter
  *"min_identical_scanlines"* is automatically reduced to the value
  of the specified *"num_scanlines"*.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  Suggested values:
   *0*, *5*, *10*,
  *20*

  Default:
   *0*
- ***"min_identical_scanlines"*:** —

  With this parameter, the probability can be lowered to read bar codes
  wrongly or in places where no bar codes is present. The parameter
  specifies the minimum number of decoded scanlines which return
  identical data to read the bar code successfully.

  If this parameter is set to 0 (which is the default for all code types,
  except for '2/5 Industrial' and '2/5 Interleaved'), a bar code
  is considered decoded with the first successfully decoded scanline (in
  the case of stacked codes, there must be a successful scanline per symbol
  row). If *"majority_voting"* is enabled, a different scheme
  applies (see the section on *"majority_voting"* for more details).
  Increasing this parameter to 2 or more is particularly useful, to prevent
  that a bar code is detected accidentally. This can typically happen if a
  scanline extracted erroneous or false edges out of a low quality image or
  in a very noisy image fragment. This parameter can be used to reduce the
  number of false detections also in cases where a specific bar code type
  is searched for in an image containing symbols from other bar code
  symbologies.

  Note that the default value of this parameter is *0* for most
  code types. However, the default value is *2* for
  *"2/5 Industrial"* and *"2/5 Interleaved"* bar code types.
  The reason for this is that these bar code types are easily misread in
  other structures like clutter and text with a
  *"min_identical_scanlines"* setting of *1*.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  If merged scanlines (see *"merge_scanlines"*) are used,
  *"min_identical_scanlines"* specifies in how many scanlines each
  edge must be recognized successfully (see [`GetBarCodeObject`](get_bar_code_object.md),
  *"scanlines_merged_edges"*).

  For *"GS1 DataBar Expanded Stacked"*,
  *"min_identical_scanlines"* specifies in how many scanlines each
  segment must be recognized successfully.

  Suggested values:
   *0*, *2*, *3*

  Default:

  | Bar code Type | *"min_identical_scanlines"* |
  | --- | --- |
  | 2/5 Industrial | 2 |
  | 2/5 Interleaved | 2 |
  | all others | 0 |
- ***"majority_voting"*:** —

  This parameter controls the decode result selection mode. If this
  parameter is *"false"*, a successful decode result is returned if
  the minimum number of identically decoded scanlines are found (see
  section on *"min_identical_scanlines"* for more details). By
  setting this parameter to *"true"* a majority voting scheme is
  used to select between different scanline results. The result
  which is decoded by the majority of all scanlines is selected as the
  overall result. Please note that setting this parameter to
  *"true"* leads to a slightly increased runtime since nearly all
  scanlines have to be considered instead of just the minimum identical
  ones.

  In order to reduce false decode results this parameter should be
  enabled.

  This parameter is only supported for non-stacked bar code types.

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*
- ***"stop_after_result_num"*:** —

  Number of successfully decoded bar codes after which the decoding
  will stop.
  If this parameter is not set (has a value of *0*), all bar code
  candidates are decoded.
  Typically, this parameter is set if the number of expected
  bar codes is known in advance. Then the bar code reader can abort
  further decoding of candidates after a certain number of bar codes has
  been found and the overall decoding time will decrease.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  Suggested values:
   *0*, *1*, *2*

  Default:
   *0*
- ***"orientation"*:** —

  Expected bar code orientation. A potential (candidate) bar code
  contains bars with similar orientation. The *"orientation"*
  and *"orientation_tol"* parameters are used to specify the
  range [*"orientation"*-*"orientation_tol"*,
  *"orientation"*+*"orientation_tol"*].
  [`FindBarCode`](find_bar_code.md) processes a candidate bar code only when the
  average orientation of its bars lies in this range. If the bar codes
  are expected to appear only in certain orientations in the processed
  images, you can reduce the orientation range adequately. This enables
  an early identification of false candidates and hence shorter
  execution times. This adjustment can be used for images with a lot
  of texture, which includes fragments tending to result in false bar
  code candidates.

  The actual orientation angle of a bar code is explained with
  [`GetBarCodeResult`](get_bar_code_result.md)(...,*"orientation"*,...) with the
  only difference that for the early identification of false candidates
  the reading direction of the bar codes is ignored, which results in
  relevant orientation values only in the range
  [*-90.0* ... *90.0*]. The only exception to
  this rule constitutes the bar code symbol PharmaCode, which possesses
  a forward and a backward reading direction at the same time: here,
  *"orientation"* can take values in the range [*-180.0*
  ... *180.0*] and the decoded result is unique
  corresponding to just one reading direction.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  Suggested values:
   [*-90.0*, ..., *90.0*]

  Default:
   *0.0*
- ***"orientation_tol"*:** —

  Orientation tolerance. Please refer to the explanation of
  *"orientation"* parameter for further information. As explained
  there, relevant orientation values are only
  in the range of [*-90.0* ... *90.0*], which
  means that with *"orientation_tol"* = *90* the whole
  range is spanned. Therefore, valid values for *"orientation_tol"*
  are only in the range of [*0.0* ... *90.0*].
  The default value *90.0* means that no restriction on the bar
  code candidates is performed.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  Suggested values:
   [*0.0*, ..., *90.0*]

  Default:
   *90.0*
- ***"quiet_zone"*:** —

  Enforces the verification of the quiet zones of a bar code symbol.
  When enabled, scanlines are rejected when unexpected bars are
  detected within the quiet zones both left or right of a detected bar
  code sequence.
  Possible values:

  - *"false"*: The quiet zones verification is disabled.
  - *"true"*: The quiet zones must be at least as wide as
    specified by the corresponding bar code standard.
    The following values apply (in X units, where X stands for "module
    width" and corresponds to the smallest width of a bar in the
    sequence):

    | Bar code Type | Left QZ | Right QZ | Bar code Type | Left QZ | Right QZ |
    | --- | --- | --- | --- | --- | --- |
    | 2/5 Industrial | 10 | 10 | UPC-A | 9 | 9 |
    | 2/5 Interleaved | 10 | 10 | UPC-A Add-On 2 | 9 | 5 |
    | Codabar | 10 | 10 | UPC-A Add-On 5 | 9 | 5 |
    | Code 39 | 10 | 10 | UPC-E | 9 | 7 |
    | Code 93 | 10 | 10 | UPC-E Add-On 2 | 9 | 5 |
    | Code 128 | 10 | 10 | UPC-E Add-On 5 | 9 | 5 |
    | MSI | 10 | 10 | GS1-128 | 10 | 10 |
    | PharmaCode | 5 | 5 | GS1 DataBar Omnidir | 1 | 1 |
    | EAN-8 | 7 | 7 | GS1 DataBar Truncated | 1 | 1 |
    | EAN-8 Add-On 2 | 7 | 5 | GS1 DataBar Stacked | 1 | 1 |
    | EAN-8 Add-On 5 | 7 | 5 | GS1 DataBar Stacked Omnidir | 1 | 1 |
    | EAN-13 | 11 | 7 | GS1 DataBar Limited | 1 | 5 |
    | EAN-13 Add-On 2 | 11 | 5 | GS1 DataBar Expanded | 1 | 1 |
    | EAN-13 Add-On 5 | 11 | 5 | GS1 DataBar Expanded Stacked | 1 | 1 |
  - An integer value (>= *1*): The quiet zones must be at least
    as wide as *"quiet_zone"* x X.
  - *"tolerant"*: A limited number of edges are allowed in the
    quiet zones, but at most 1 per 4 module widths.
    The intent of this is to prevent detecting only part of a bar code,
    while still allowing to read bar codes with simple quiet zone
    violations.

    *Note:* Even for code types with a specified quiet zone smaller
    than four module widths, the edges are checked within a range of four
    module widths around the code. In this case, this criterion can be
    stricter than the verification with
    *"quiet_zone"*=*"true"*.

  The quiet zone verification is very useful when using the bar code
  reader in multi-type or 'auto' reading mode. It prevents that
  simple bar code types are detected inside of a bar sequence
  representing a longer bar code or inside another, typically
  more complex bar code type. Usually, values between *2* and
  *4* achieve optimal results by effectively suppressing false bar
  codes, but still tolerating small disturbances, textures, label edges,
  etc. next to the symbol.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  *Note:* The quiet zones serve as a check, that no bar is detected
  within this zones, but it is not required that the quiet zones are
  contained as a whole in the image.
  This means, if a set quiet zone is not contained as a whole, only the
  part within the image is assessed and the part outside the image is
  assumed to be free of defects.

  Suggested values:
   *"false"*, *"true"*,
  *"tolerant"*, *1*, ...,
  *100*

  Default:
   *"false"*
- ***"start_stop_tolerance"*:** —

  Enforces a tolerant (*"high"*) or strict (*"low"*)
  searching criteria while inspecting a scanline for a start or stop
  pattern, respectively. A more tolerant criteria will generally
  increase the detection chances of a bar code, provided that a
  clear symbol is imaged in the processed image. On the other side, it
  might result in false detections in noisy images or images containing
  symbols from other symbologies. Less tolerant criteria increase the
  robustness against false detections, but might reduce the general
  detection rate. Currently, there are two distinct criteria
  implemented only for Code 128 and GS1-128.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md). As already
  mentioned, currently this makes a difference only for Code 128 and
  GS1-128.

  List of values:
   *"high"*, *"low"*

  Default:
   *"high"*
- ***"min_code_length"*:** —

  Minimum number of decoded characters. If a bar code is found with a code
  length below *"min_code_length"*, the result is discarded and not
  returned by [`FindBarCode`](find_bar_code.md) or [`DecodeBarCodeRectangle2`](decode_bar_code_rectangle2.md).
  This parameter is useful to reduce the number of false reads in
  applications where the minimum number of characters is known in
  advance.

  Note that the default value of this parameter is *0* for most
  code types. However, the default value is *3* for
  *"2/5 Industrial"* and *"2/5 Interleaved"* bar code types.
  The reason for this is that these bar code types are easily misread in
  other structures like clutter and text with a code length of *2*.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  Suggested values:
   *0*, *1*, *2*

  Default:

  | Bar code Type | *"min_code_length"* |
  | --- | --- |
  | 2/5 Industrial | 3 |
  | 2/5 Interleaved | 3 |
  | all others | 0 |
- ***"max_code_length"*:** —

  Maximum number of decoded characters. If a bar code is found with a code
  length exceeding *"max_code_length"*, the result is discarded and not
  returned by [`FindBarCode`](find_bar_code.md) or [`DecodeBarCodeRectangle2`](decode_bar_code_rectangle2.md).
  This parameter is useful to reduce the number of false reads in
  applications where the maximum number of characters is known in
  advance.

  Value range:
   *1* ... *2147483647*

  Default:
   *2147483647*
- ***"merge_scanlines"*:** —

  If not enough scanlines (see *"min_identical_scanlines"*) can be
  read successfully, i.e., because the bar code is partly occluded or
  damaged, an attempt is being made to merge the existing scanlines. Then,
  these merged scanlines are decoded again.
  This additional decoding step is only performed for non-stacked bar code
  types and can be disabled for performance reasons.

  List of values:
   *"true"*, *"false"*

  Default:
   *"true"*
- ***"small_elements_robustness"*:** —

  If not enough scanlines (see *"min_identical_scanlines"*) can be
  read successfully, i.e., because the bar code contains small elements
  (smaller than *2.0* pixels in element size), an attempt is being made to
  read the code with an advanced algorithm which tries to solve the low
  resolution problem.

  This additional decoding attempt is only performed for non-stacked bar
  code types and if the specified *"element_size_min"* is smaller
  than *2.0* pixels.

  The status result of this attempt can be retrieved by calling the
  operator [`GetBarCodeResult`](get_bar_code_result.md) with
  *"status_small_elements_robustness"*.

  In case of very small elements (smaller than *1.3* pixels in
  element size) it is beneficial if the camera sensor is rotated slightly
  with respect to the bar code (e.g., around 7 degrees). This is important
  because in such low resolution cases the bar code information is
  contained in multiple rows/columns of the perceived image only if it is
  rotated. See the following two figures for examples.

  ![figure](../assets/46c260c53cb4f70f.svg)

  A bar code at *0.9* element size without sensor rotation. The
  relevant information of the bar code is not present in the image.

  ![figure](../assets/40b438afef2386ca.svg)

  The same bar code as in the previous figure with sensor rotation. The
  rows of the image contain more information about the code and thus it
  can be decoded successfully.

  Another important advice is to reduce the amount of blur introduced by
  the optical system.

  The input image should not be preprocessed with filter operations such as
  [`Emphasize`](emphasize.md), [`ZoomImageSize`](zoom_image_size.md) or [`MeanImage`](mean_image.md). Those
  operators would remove important information.

  Note, if optical conditions are optimal (small amount of blur and slight
  rotation with respect to the bar code) it is possible to read bar codes
  as small as *0.6* pixels in element size.

  This feature is only compatible with byte input images and can be
  disabled for performance reasons.

  List of values:
   *"true"*, *"false"*

  Default:
   *"true"*

### Appearance of the bar code in the image:

- ***"meas_thresh"*:** —

  *"meas_thresh"* defines a threshold which is a
  relative value with respect to the dynamic range of the scanline pixels.
  The bar-space-sequence of a bar code is determined with a scanline
  measuring the position of the edges. Finding these edges requires the
  mentioned threshold.
  In the case of disturbances in the bar code region or a high noise
  level, the value of *"meas_thresh"* should be increased.

  Suggested values:
   [*0.05*, ..., *0.2*]

  Value range:
   (*0.0*, .., *1.0*]
  - without *0.0*

  Default:
   *0.05*
- ***"meas_thresh_abs"*:** —

  If a scanline is laid in an image region with no or just very small
  gray value dynamic range (e.g., in a white region with all
  gray values near 255), the edge detection threshold based on
  *"meas_thresh"* would be computed unreasonably small. This
  leads typically to the detection of a big amount of false edges.
  *"meas_thresh_abs"* is used to prevent such misdetections.
  If the threshold value based on *"meas_thresh"* gets smaller
  than the value of *"meas_thresh_abs"*, the latter is used as
  threshold instead. By default, *"meas_thresh_abs"* is set to
  *5.0*. A greater value might be more appropriate for images
  with high noise levels. On the other hand, in noise-free images
  with very weak contrast, this parameter might disturb the detection
  of real edges, so it might be necessary to reduce it or even
  completely disable it by setting it to *0.0*.

  Suggested values:
   [*0.0*, ..., *10.0*]

  Value range:
   [*0.0*, .., *65535*]

  Default:
   *5.0*
- ***"contrast_min"*:** —

  Minimum contrast between the foreground and the background of the bar
  code elements. Setting this parameter to values greater than 5 will help
  the operator [`FindBarCode`](find_bar_code.md) to optimize the candidate region
  search. [`FindBarCode`](find_bar_code.md) will reject all candidate regions with a
  contrast value below *"contrast_min"*. Hence, setting a high
  *"contrast_min"* value will improve the runtime performance of
  [`FindBarCode`](find_bar_code.md). However, please note, that all bar codes with a
  contrast value below *"contrast_min"* will not be read. The
  calculated contrast value is an approximation in order to speed up the
  execution time. Try to set a lower threshold for *"contrast_min"*
  in order to find bar codes which might get rejected and have a contrast
  value that is close to the specified *"contrast_min"*.

  Suggested values:
   *0*, *40*, *90*,
  *120*

  Default:
   *0*

### Values specific for print quality inspection:

- ***"quality_isoiec15416_reflectance_reference"*:** —

  The reflectances used to assess the quality grades Symbol Contrast,
  Minimum Reflectance, and Minimum Edge Contrast is
  normalized with a reference gray value for reflectance.
  This value can be obtained with barium sulfate or magnesium oxide
  samples, i.a., see ISO/IEC 15416:2016 section 5.2.
  Value range:
   [*1* .. *255*]

  Default:
   *255*

### Values that only apply to certain code types:

- ***"check_char"*:** —

  Bar codes with an optional check character are interpreted according
  to this parameter.
  These bar code types include, e.g., Code 39, Codabar, 2/5
  Industrial and 2/5 Interleaved.
  The default setting of *"absent"* assumes that
  no check character is present. In this case, no check is performed and
  all characters are returned as data.

  When set to *"present"*, a check character is expected and used
  to verify the correctness of the bar code.
  If the check sum matches, the check character itself is
  stripped from the data. If this stripping is undesired, the mode
  *"preserved"* allows to verify the bar code while still keeping
  the check character in the data.
  In the case the check sum does not match, no bar code result is
  returned.

  For bar code types with a mandatory check character the
  parameter *"check_char"* is set to *"present"*.
  However, if the check character is removed from the data or stays,
  depends on the standard of the specific code type.
  Such code types include, e.g., Code 128, EAN-8, EAN-13, and UPC-A.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  List of values:
   *"absent"*, *"present"*,
  *"preserved"*

  Default:
   *"absent"*
- ***"composite_code"*:** —

  Most of the GS1 conform bar codes can have an additional 2D GS1
  Composite code component appended. If *"composite_code"* is set
  to *"CC-A/B"* the composite component will be found and decoded.
  By default, *"composite_code"* is set to *"none"* and
  thus it is disabled. If the searched bar code symbol has no attached
  composite component, just the result of the bar code itself is returned
  by [`FindBarCode`](find_bar_code.md). Currently, composite codes are supported only
  for bar codes of the GS1 DataBar family.

  This parameter can be set specifically for different types of bar codes
  by using the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md).

  List of values:
   *"none"*, *"CC-A/B"*

  Default:
   *"none"*
- ***"upce_encodation"*:** —

  For UPC-E bar codes, different output formats can be used. By default,
  *"upce_encodation"* is set to *"ucc-12"* and the decoded
  string will be returned in UCC-12 format (consisting of 12 digits). If
  *"upce_encodation"* is set to *"zero-suppressed"*, the
  result will be returned in zero-suppressed format (with suppressed zeros
  at defined places). This format consists of a leading zero (or a leading one,
  see *"upce1_enable"*), six encoded
  digits, and an implicitly encoded check digit. This corresponds to the
  format demanded by ISO/IEC 15420:2009 standard.

  List of values:
   *"ucc-12"*, *"zero-suppressed"*

  Default:
   *"ucc-12"*
- ***"upce1_enable"*:** —

  The parameter *"upce1_enable"* enables the decoding of UPC-E
  bar codes with number system 1, if the parameter is set to
  *"true"*. UPC-E bar codes with number system 1 are an extension
  of UPC-E bar codes with number system 0, but are not documented in
  the underlying standard ISO/IEC 15420:2009.
  UPC-E bar codes with number system 1 also support the different output
  formats mentioned in *"upce_encodation"*, noting that the formats
  contain a leading one instead of a leading zero in UPC-E bar codes
  with number system 0.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*
- ***"strict_ean13_upc_a"*:** —

  The parameter *"strict_ean13_upc_a"* defines the distinction
  between EAN-13 and UPC-A codes.

  Bar codes of type UPC-A are handled as a subset of bar codes of type
  EAN-13, if *"strict_ean13_upc_a"* is set to *"false"*.
  This means that codes of type UPC-A are decoded with a data string
  consisting of a leading zero and the 12 digits of actual data.
  Furthermore, bar codes of type UPC-A can be found with `codeType`
  set to *"EAN-13"* when calling [`FindBarCode`](find_bar_code.md). This will
  result in the UPC-A bar code being decoded as an EAN-13 bar code.

  If *"strict_ean13_upc_a"* is set to *"true"*, bar codes of
  type UPC-A are strictly distinguished from bar codes of type EAN-13 in
  accordance with ISO/IEC 15420:2009, Table 3. This means that codes of
  type UPC-A are decoded with a data string consisting of 12 digits.
  Furthermore, bar codes of type UPC-A can only be found if
  *"UPC-A"* is included in `codeType` when calling
  [`FindBarCode`](find_bar_code.md).

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

### Training:

Besides setting the model parameters manually with
`SetBarCodeParam`, the model can also be trained with
[`FindBarCode`](find_bar_code.md) based on one or several sample images.
For this, a bar code model must be created in training mode or an existing
bar code model must be put into training mode by passing the generic
parameter *"train"* in *`genParamName`* of
`SetBarCodeParam`.
The corresponding value passed in *`genParamValue`* determines
the model parameters that should be learned.
The following values are possible:

- ***"all"*:** —

  Train all possible model parameters.
- ***"element_size_min"*:** —

  Minimum size of the base bar code elements.
  This setting activates the training mode for the parameter
  *"element_size_min"*.
- ***"element_size_max"*:** —

  Maximum size of the base bar code elements.
  This setting activates the training mode for the parameter
  *"element_size_max"*.
- ***"barcode_width_min"*:** —

  Minimum bar code width.
  This setting activates the training mode for the parameter
  *"barcode_width_min"*.
- ***"barcode_width_max"*:** —

  Maximum bar code width.
  This setting activates the training mode for the parameter
  *"barcode_width_max"*.
- ***"meas_thresh"*:** —

  Relative threshold for measuring the edge position within a scanline.
  This setting activates the training mode for the parameter
  *"meas_thresh"*.
- ***"meas_thresh_abs"*:** —

  Absolute threshold for measuring the edge position within a scanline.
  This setting activates the training mode for the parameter
  *"meas_thresh_abs"*.
- ***"orientation"*:** —

  Orientation of the bar code. This setting activates the training mode
  for
  the parameters *"orientation"* and *"orientation_tol"*.
  After ending the training the value for *"orientation_tol"*
  can be increased by a tolerance value to be able to find bar codes
  with orientations slightly beyond the trained orientations.

It is possible to train several of these parameters in one
call of [`FindBarCode`](find_bar_code.md) by passing the generic parameter
*"train"* in `SetBarCodeParam` in a tuple more than once in
conjunction with the appropriate parameters: e.g.,
*`genParamName`* = *["train","train"]* and
*`genParamValue`* = *["element_size_min","element_size_max"]*.
Furthermore, in conjunction with *"train"* = *"all"*
it is possible to exclude single parameters from training
explicitly again by passing *"train"* more than once.
The names of the parameters to exclude, however, must be prefixed
by *"~"*:
*`genParamName`* = *["train","train"]* and
*`genParamValue`* =
*["all","~orientation"]*,
e.g., trains all parameters except the orientation.

Afterwards, the operator [`FindBarCode`](find_bar_code.md) has to be called for every
image to be trained.

For training the model, the following aspects should be considered:

- Additionally needed, non-trained parameters (e.g., *"check_char"*)
  must be set manually before the training.
- To use several images for the training, the operator
  [`FindBarCode`](find_bar_code.md) must be called once for every sample image.
- On a single training image there may be multiple bar codes of the selected
  code type visible.
- Please check the output of [`FindBarCode`](find_bar_code.md) during training.
  Every decoded bar code will contribute to the trained bar code
  model. Hence, please make sure, that there are no false decodes. If you
  encounter false decodes, you may have to discard the image or set appropriate
  parameters in advance (e.g., you may need to increase the value of the
  parameter *"min_identical_scanlines"* or you may try to reduce the
  domain of the image appropriately).
- In an application with very similar images, *one* image for
  the training may be sufficient for the parameters
  *"element_size_min"*, *"element_size_max"*,
  *"meas_thresh"*, and *"meas_thresh_abs"*.

  For the training of the parameter *"orientation"*, at least two
  images are needed showing the bar code at its minimum and maximum
  orientations.
- In applications where the element size is not fixed,
  the smallest as well as the biggest symbols should be used for
  the training.
  If this can not be guaranteed, the limits for the element size
  should be adapted manually after the training or the element
  sizes should entirely be excluded from the training.
- During the first call of [`FindBarCode`](find_bar_code.md) in the
  training mode, the trained model parameters are restricted to
  the properties of the detected bar code.
  Any successive training call will, where necessary, extend the
  parameter range to cover the already trained bar codes as well as
  the new bar code.
- The training can be stopped when enough images have been trained.
  Before this, the trained parameters should be retrieved.
  With the operator [`QueryBarCodeParams`](query_bar_code_params.md) the names of the
  trained parameters - split into specific and general parameters -
  can be determined. The values of the parameters can then be retrieved
  with the operators [`GetBarCodeParamSpecific`](get_bar_code_param_specific.md)
  and [`GetBarCodeParam`](get_bar_code_param.md).

  To stop the training, all trained parameters are excluded from the
  training by calling the operator `SetBarCodeParam`
  with the parameters *`genParamName`* = *"train"* and
  *`genParamValue`* = *"~all"*.

  Alternatively, the existing bar code model can simply be cleared with
  the operator [`ClearBarCodeModel`](clear_bar_code_model.md).
- The value of any trained parameter should not be set explicitly with
  `SetBarCodeParam` or [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md)
  during training mode. If this is done, the complete internal training
  data is being reset and training will be started again at the beginning
  with the next call of [`FindBarCode`](find_bar_code.md).
- If [`FindBarCode`](find_bar_code.md) is not able to read the bar code
  in the training image, this will produce no error or
  exception handling.
  It can simply be tested in the program by checking the
  output parameter DecodedDataStrings or SymbolRegions.
  These tuples will then be empty and the parameters of the model
  (especially the trained parameters) will not be modified.
- Timeouts are disabled during the training.

### Miscellaneous:

- ***"timeout"*:** —

  By the use of this parameter, it is possible to abort
  [`FindBarCode`](find_bar_code.md) after a defined period in milliseconds. This
  is especially useful in cases where a maximum cycle time has to be
  ensured.
  All results gained before the timeout can be accessed by
  [`GetBarCodeResult`](get_bar_code_result.md). Passing values less or equal zero
  implies a deactivation of the timeout (default).

  The temporal accuracy of this timeout is about 10 ms. It
  depends on several factors including
  the speed of your computer and the *"timer_mode"* set
  via [`SetSystem`](set_system.md).

  [`FindBarCode`](find_bar_code.md) does not raise an exception if a
  timeout occurs. To check whether [`FindBarCode`](find_bar_code.md) has been
  aborted, check the parameter *"aborted"* in
  [`GetBarCodeResult`](get_bar_code_result.md).

  Note that the timeout is ignored if [`FindBarCode`](find_bar_code.md)
  runs in training mode.

  Suggested values:
   *"false"*, *-1*, *20*,
  *100*

  Default:
   *"false"*
- ***"abort"*:** —

  Using this option, it is possible to abort [`FindBarCode`](find_bar_code.md)
  from another thread. When `SetBarCodeParam` is called with
  *"abort"*, an instance of [`FindBarCode`](find_bar_code.md) with the model
  *`barCodeHandle`* running in another thread is requested to abort.
  If there is no [`FindBarCode`](find_bar_code.md) running with this model, nothing
  happens.

  The operator [`FindBarCode`](find_bar_code.md) might not return immediately. It has
  to reach a cancellation point to ensure a proper cleanup. Depending on
  different factors like the computer performance this may take up to 10
  ms.

  All decoded results until this moment, are still returned. Note that the
  parameter is ignored if [`FindBarCode`](find_bar_code.md) runs in training mode.

  Note: This is the only action with a bar code handle, which can be used
  from different threads without requiring additional synchronization.

  Default:
   *"true"* (The value is not processed.)
- ***"persistence"*:** —

  Setting the model in persistence mode to *1*, makes it store
  some intermediate results during bar code decoding. These results
  are required if the bar code print quality has to be assessed
  ([`GetBarCodeResult`](get_bar_code_result.md) with *"quality_isoiec15416"*) or
  the decoding scanlines have to be inspected ([`GetBarCodeObject`](get_bar_code_object.md)
  with, e.g., *"scanlines_all"* or *"scanlines_valid"*). Yet,
  enabling the *"persistence"* mode results in increased memory
  requirements for the bar code model structures.

  List of values:
   *0*, *1*

  Default:
   *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- barCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`barCodeHandle`** (input_control, state is modified)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that shall be
adjusted for finding and decoding bar codes.

Default:
"element_size_min"

List of values:
"abort", "barcode_height_min", "barcode_width_max", "barcode_width_min", "check_char", "composite_code", "contrast_min", "element_size_max", "element_size_min", "element_size_variable", "majority_voting", "max_code_length", "meas_thresh", "meas_thresh_abs", "merge_scanlines", "min_code_length", "min_identical_scanlines", "num_scanlines", "orientation", "orientation_tol", "persistence", "quality_isoiec15416_reflectance_reference", "quiet_zone", "small_elements_robustness", "start_stop_tolerance", "stop_after_result_num", "strict_ean13_upc_a", "timeout", "train", "upce1_enable", "upce_encodation"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters that are
adjusted for finding and decoding bar codes.

Default:
8

Suggested values:
0, 0.1, 1, 1.5, 2, 8, 32, 45, "true", "false", "present", "absent", "none", "CC-A/B", "auto", "high", "low", "ucc-12", "zero-suppressed"

## Result

The operator `SetBarCodeParam` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBarCodeModel`

## Possible Successors

`FindBarCode`

## Alternatives

`SetBarCodeParamSpecific`

## Module

Bar Code

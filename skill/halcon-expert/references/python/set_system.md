# set_system (Operator)

## Name

`set_system` — Set HALCON system parameters.

## Signature

`def set_system(system_parameter: MaybeSequence[str], value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

The operator `set_system` allows to change different system
parameters.

**Parallelization information:**
Note that some of these parameters are set exclusively only,
meaning they block other threads until no other
operators are accessing the HALCON library.

- Parameters marked by a *) are globally valid and are set exclusively.
- Parameters without the mark *) and without the prefix *'tsp_'* are also globally
  valid but are not set exclusively, i.e., the operator call does not block other operator calls.
- Parameters with *'tsp_'* variant are thread specific.

  1. Without *'tsp_'*, they are set for all threads that are started
     after this call as well as for the current thread. Threads that are
     already running will not be affected.
  2. Parameters called with *'tsp_'* are only set for the current thread. Other
     threads that are already running will not be affected.

Available system parameters:

- **Graphic:**

  - ***"backing_store"*:** —

    Determines whether the window content will be
    refreshed in case of overlapping of the windows. Some
    implementations of X Windows are faulty; in order to
    avoid these errors, the storing of contents can be
    deactivated.
    In some cases it may be advisable to deactivate
    the security mechanism, if e.g., performance / memory
    is critical.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"flush_graphic"*:** —

    After each HALCON operation which creates a graphic output,
    a flush operation will be executed in order to display the
    data immediately on screen. This is not necessary for all
    programs, e.g., if everything is done with the help of the
    mouse. In this case *"flush_graphic"* can be set to *"false"*
    to improve the runtime. Note that this parameter has no
    effect on Unix-like systems because there, the window
    managers flush the display buffer automatically.

    *Note:* Using *"flush_graphic"* is not recommended,
    since it can lead to unexpected results.
    Instead, please set the parameter *"flush"* of
    [`set_window_param`](set_window_param.md) to *"false"* and call [`flush_buffer`](flush_buffer.md)
    to transfer the buffer to the graphics window.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"int2_bits"*:** —

    Number of significant bits of int2 images.
    This number is used when scaling the gray values.
    If the value is set to -1 the gray values will be
    scaled automatically (default).

    *`value`*: *-1* or *9..16*

    Default:
     *-1*
  - ***"icon_name"*:** —

    Name of iconified graphics windows under X Windows. By default
    the number of the graphics window is displayed.

    *`value`*: Name of iconified graphics window.

    Default:
     *"default"*
  - ***"default_font"* *):** —

    Default font for text output in text and graphic windows.
    Available fonts can be queried with [`query_font`](query_font.md). The
    syntax of possible fontnames in *`value`* is described at
    [`set_font`](set_font.md).

    *`value`*: Name of Font.

    Default:
     *"fixed"*
  - ***"update_lut"*:** —

    Determines whether the HALCON look-up color tables are adapted
    according to their environment or not.
    Such hardware-dependent color tables are no longer in use,
    so the parameter is obsolete.
    You can use the operator [`query_lut`](query_lut.md) to query all possible look-up
    tables and set a specific one using [`set_lut`](set_lut.md).

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"use_window_thread"*:** —

    On Microsoft Windows systems, calling any of the HALCON graphics operators
    from a thread other than the one that created the output window requires
    that there be an active message loop for that window. Setting this
    parameter to *"true"* will automatically open all top level HALCON
    graphics and text windows in a special window thread that will handle the
    message loop; all graphics operators directed at these windows will also
    be executed by that thread automatically. This parameter has no effect on
    non-Windows systems.

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"x_package"*:** —

    The output of image data via the network may cause errors
    due to the heavy load on the computer or on the network.
    In order to avoid this, the data are
    transmitted in small packages. If the display is used
    locally (as opposed to using it via network),
    these units can be enlarged at will. This can
    lead to a recognizably improved output performance.
    On X Window systems the maximum request size is queried
    when the first window is opened.

    *`value`*: Package size (in bytes).

    Default:
     *131072*
- **Image Processing:**

  - ***"neighborhood"*, *"tsp_neighborhood"*:** —

    This parameter checks either four pixels
    (in horizontal and vertical direction)
    or all eight neighboring pixels
    around one pixel. It is used with all operators
    that examine neighborhood relations: [`connection`](connection.md),
    [`get_region_contour`](get_region_contour.md),
    [`get_region_polygon`](get_region_polygon.md), [`get_region_thickness`](get_region_thickness.md),
    [`boundary`](boundary.md),
    [`paint_region`](paint_region.md), [`disp_region`](disp_region.md), [`fill_up`](fill_up.md),
    [`contlength`](contlength.md), [`shape_histo_all`](shape_histo_all.md).

    *`value`*: *4* or *8*

    Default:
     *8*

    |  |  |
    | --- | --- |
    | ![figure](../assets/f36e8d29fa68f368.svg) | ![figure](../assets/5ffc45e490874dd0.svg) |
    | ( 1) | ( 2) |

    (1) Four neighboring pixels,
    (2) eight neighboring pixels.
  - ***"init_new_image"*, *"tsp_init_new_image"*:** —

    Determines whether new images shall be set to 0 before using
    filters and thus to make sure that the values returned by a
    filtering are consistent if the program is executed repeatedly
    on systems with the same configuration. Note that this is not
    necessary if always the whole image is filtered or if the data
    of unfiltered image areas is unimportant.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"no_object_result"*, *"tsp_no_object_result"*:** —

    Determines how operations processing iconic objects shall
    react if the object tuple is empty (= no objects).

    Available values for *`value`*:

    - *"true"*: The error will be ignored.
    - *"exception"*: An exception is raised.

    Default:
     *"true"*
  - ***"empty_region_result"*, *"tsp_empty_region_result"*:** —

    Controls the reaction of operators concerning input
    objects with empty regions which actually are not
    useful for such objects (e.g., certain region features,
    segmentation, etc.).

    Available values for *`value`*:

    - *"true"*: The error will be ignored if possible.
    - *"exception"*: An exception is raised.

    Default:
     *"true"*
  - ***"store_empty_region"*, *"tsp_store_empty_region"*:** —

    Quite a number of operations will lead to the creation
    of objects with an empty region (= no image points)
    (e.g., [`intersection`](intersection.md),[`threshold`](threshold.md), etc.).
    This parameter determines whether the object with
    an empty region will be returned as a result ('true')
    or whether it will be ignored (*"false"*) that is no result
    will be returned.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"clip_region"*, *"tsp_clip_region"*:** —

    Determines whether the regions of iconic objects will
    be clipped to the currently used image size or not.
    This parameter can be used with
    operators that have a region as output, for example,
    [`gen_circle`](gen_circle.md),
    [`gen_rectangle1`](gen_rectangle1.md) or [`dilation1`](dilation1.md).

    See also: [`reset_obj_db`](reset_obj_db.md)

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"int_zooming"*:** —

    Determines the precision of certain steps of the image processing.
    By setting *"int_zooming"* to *"true"* integer arithmetic or
    fast floating point arithmetic is used. High precision floating point
    arithmetic will be used by setting it to *"false"*.
    More information how a specific operator is affected by the parameter
    *"int_zooming"* can be found in the documentation of the directly
    concerned operator.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"pregenerate_shape_models"*:** —

    This parameter determines whether the shape models
    are completely pregenerated (*"true"*) or not (*"false"*)
    if this behavior is not explicitly specified in the shape model operator.
    Affected operators:

    - [`create_shape_model`](create_shape_model.md)
    - [`create_shape_model_xld`](create_shape_model_xld.md)
    - [`create_scaled_shape_model`](create_scaled_shape_model.md)
    - [`create_scaled_shape_model_xld`](create_scaled_shape_model_xld.md)
    - [`create_aniso_shape_model`](create_aniso_shape_model.md)
    - [`create_aniso_shape_model_xld`](create_aniso_shape_model_xld.md)

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"border_shape_models"*:** —

    This parameter determines whether the shape models to be found may lie
    partially outside the image, i.e., whether they may cross the image border,
    (*"true"*) or not (*"false"*). Partially means that the
    model's origin still must be located within the image. A different origin
    set with [`set_shape_model_origin`](set_shape_model_origin.md) is not taken into account.

    Affected operators:

    - [`find_generic_shape_model`](find_generic_shape_model.md)
    - [`find_shape_model`](find_shape_model.md)
    - [`find_shape_models`](find_shape_models.md)
    - [`find_scaled_shape_model`](find_scaled_shape_model.md)
    - [`find_scaled_shape_models`](find_scaled_shape_models.md)
    - [`find_aniso_shape_model`](find_aniso_shape_model.md)
    - [`find_aniso_shape_models`](find_aniso_shape_models.md)
    - [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md)
    - [`find_planar_calib_deformable_model`](find_planar_calib_deformable_model.md)
    - [`find_local_deformable_model`](find_local_deformable_model.md)
    - [`find_component_model`](find_component_model.md) (legacy)

    Note, if a value has been set for shape models using
    [`set_generic_shape_model_param`](set_generic_shape_model_param.md), the specific value set for the model
    dominates the system-wide setting.
    When searching multiple shape models *"border_shape_models"*
    is treated as *"true"* for all shape models even if
    *"border_shape_models"* only evaluates to *"true"*
    for one of the shape models in a search.

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"opengl_context_cache_enable"*:** —

    This parameter determines if the graphic card context used in the
    operator [`render_object_model_3d`](render_object_model_3d.md) is cached for future uses of
    this operator. The caching speeds up future uses of this operator but
    requires additional resources.
    To explicitly delete the context, set
    *"opengl_context_cache_enable"* to *"false"* and call
    [`render_object_model_3d`](render_object_model_3d.md) once.
    *"opengl_context_cache_enable"* can only be set
    to *"true"* if the graphic card supports the rendering of
    3D object models.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if supported by the graphics card.
  - ***"opengl_hidden_surface_removal_enable"*:** —

    This parameter determines if the graphics card accelerated
    hidden surface removal is used in [`create_shape_model_3d`](create_shape_model_3d.md),
    [`find_shape_model_3d`](find_shape_model_3d.md), [`project_shape_model_3d`](project_shape_model_3d.md), and
    [`project_object_model_3d`](project_object_model_3d.md).
    *"opengl_hidden_surface_removal_enable"* can only be set
    to *"true"* if the graphics card supports the acceleration
    of the hidden surface removal algorithm.
    The minimum requirements are OpenGL 2.0 and the extensions
    GL_EXT_framebuffer_object and GL_ARB_texture_float.
    Use [`get_system`](get_system.md) with the parameter Query set to
    *"opengl_hidden_surface_removal_available"* to
    determine if these requirements are fulfilled.
    Please note that these features are not available via
    Windows Remote Desktop or X11 forwarding.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if supported by the graphics card.
  - ***"opengl_compatibility_mode_enable"*:** —

    This parameter determines if the visualization of 3D object models
    via [`disp_object_model_3d`](disp_object_model_3d.md) uses advanced OpenGL features
    or OpenGL 1.1 features only. If set to *"false"* HALCON determines
    the capabilities of the graphics card automatically. Set this parameter
    to *"true"*, if you face visualization problems.

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*.
  - ***"image_dpi"*:** —

    This parameter determines the DPI resolution that is stored in
    image files written with [`write_image`](write_image.md) in a format that
    supports the storing of the DPI resolution.

    *`value`*: Resolution in DPI.

    Default:
     *300*
  - ***"width"*, *"tsp_width"*:** —

    Determines the internal image width of the system. This
    size is used for clipping regions or implementing an
    assumption of memory sizes, if an operator has no further
    image information. This size is interpreted as maximum
    width of all HALCON image objects. It will be increased,
    if images of greater width will subsequently be instantiated.
    See also [`reset_obj_db`](reset_obj_db.md).
    Note that the default value is *512* within HDevelop (also if you
    export your code), otherwise it is *128*.

    *`value`*: Internal image width.

    Default:
     *128* or *512* (HDevelop)
  - ***"height"*, *"tsp_height"*:** —

    Determines the internal image height of the system. This
    size is used for clipping regions or implementing an
    assumption of memory sizes, if an operator has no further
    image information. This size is interpreted as maximum
    height of all HALCON image objects. It will be increased
    if images of greater height will subsequently be instantiated.
    See also [`reset_obj_db`](reset_obj_db.md).
    Note that the default value is *512* within HDevelop (also if you
    export your code), otherwise it is *128*.

    *`value`*: Internal image height.

    Default:
     *128* or *512* (HDevelop)
  - ***"current_runlength_number"*, *"tsp_current_runlength_number"*:** —

    Regions will be stored internally in a certain runlength code.
    This parameter can determine the maximum number of chords
    which may be used for representing a region.
    Please note that some operators raise the number automatically
    if necessary.

    The value can be enlarged as well as reduced.

    *`value`*: Maximum number of chords.

    Default:
     *50000*
- **Parallelization:**

  - ***"parallelize_operators"* *):** —

    Determines whether HALCON uses an automatic parallelization
    to speed up the processing of operators on multiprocessor machines. This
    feature can be switched off by setting *"parallelize_operators"*
    to *"false"*.
    Even then, HALCON will remain reentrant (and thread-safe),
    unless the parameter *"reentrant"* is set to
    *"false"* via `set_system`.
    Changing the value for *"parallelize_operators"* can be helpful, for
    example, if HALCON operators are called by a multithreaded application
    that also automatically performs the scheduling and load balancing of
    operators and data. Then, it may be undesired that
    HALCON performs additional parallelization steps, which may
    disturb the application's scheduling and
    load balancing concepts. For a more detailed control of automatic
    parallelization, single methods of data parallelization can
    be switched on and off. *"split_tuple"* enables the tuple
    parallelization method, *"split_channel"* the parallelization
    on image channels, *"split_domain"* the parallelization on
    the image domain, and *"split_partial"* the partial,
    internal parallelization of an operator.
    A preceding '~' disables the corresponding method.
    The method strings can also be passed within a control tuple
    to switch on or off methods of automatic data parallelization
    at once. E.g., [*"split_tuple"*,*"split_channel"*,
    *"split_domain"*, *"split_partial"*] is equivalent
    to *"true"*.

    The methods supported by a specific operator can be
    viewed in this reference manual or obtained via the operator
    [`get_operator_info`](get_operator_info.md) with the parameter value
    *"parallel_method"*.

    *`value`*: *"true"*, *"false"*, *"split_tuple"*,
    *"split_channel"*, *"split_domain"*,
    *"split_partial"*, *"~split_tuple"*,
    *"~split_channel"*, *"~split_domain"*,
    *"~split_partial"*

    Default:
     *"true"*
  - ***"reentrant"* *):** —

    Determines whether HALCON must be reentrant for being used within a
    parallel programming environment (e.g., a multithreaded application). If
    it is set to *"true"*, HALCON internally uses synchronization
    mechanisms to protect shared data objects from concurrent accesses.
    Though this is inevitable with any effectively parallel working
    application, it may cause undesired overhead, if used within an
    application which works purely sequentially. The latter case can be
    signaled by setting *"reentrant"* to *"false"*. This
    switches off all internal synchronization mechanisms and
    thus reduces overhead. Of course, HALCON is then no longer thread-safe,
    which causes another side-effect: HALCON will as a consequence no longer
    use the internal parallelization of operators, because this requires
    reentrancy. Setting *"reentrant"* to *"true"* resets HALCON
    to its default state, i.e., it is reentrant (and thread-safe) and it
    uses the automatic parallelization to speed up the processing of
    operators on multiprocessor machines.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"thread_num"* *), *"tsp_thread_num"*:** —

    Sets the number of threads used by the automatic
    operator parallelization (aop) of HALCON. The number includes
    the calling thread and is restricted to the number of
    processors for efficiency reasons. Decreasing the number
    of threads is helpful if processors are occupied by user
    worker threads besides the threads of the automatic
    parallelization. With this, the number of processing
    threads can be adapted to the number of processors for
    best efficiency. If a processor affinity was set for the
    HALCON process, the parameter value *"default"* resets
    the number of threads to the number of assigned processors.
    Else, *"default"* sets the number of threads to the
    number of processors. If the thread-specific variant is used,
    HALCON reserves the specified number of threads exclusively
    for the calling thread. If no thread number was set so far for a
    specific thread, [`get_system`](get_system.md) returns value -1 for
    parameter value *"tsp_thread_num"*. In case the sum of all
    thread-specific reserved aop threads exceeds the number of threads set by
    *"thread_num"*, the latter one is increased accordingly.
    Specifying thread number 1 switches off the automatic parallelization
    (thread-specific when indicated).

    *`value`*: *1* <= Value <= *"processor_num"*,
    *"default"*

    Default:
     *"default"*
  - ***"thread_pool"* *):** —

    Denotes whether HALCON always creates new threads
    for automatic parallelization (*"false"*) or uses an existing
    pool of threads (*"true"*). Using a pool is more efficient
    for automatic parallelization. When switching off automatic
    parallelization permanently, deactivating the pool can save
    resources of the operating system.

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
- **File:**

  - ***"flush_file"*:** —

    This parameter determines whether the output characters of
    the operator [`fwrite_string`](fwrite_string.md) are displayed directly on the
    output medium. If set to *"false"* the characters will be
    flushed only after entering the operator [`fnew_line`](fnew_line.md).

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"*
  - ***"ocr_trainf_version"*:** —

    This parameter determines the format that is used for
    writing an OCR training file. The operators
    [`write_ocr_trainf`](write_ocr_trainf.md), [`write_ocr_trainf_image`](write_ocr_trainf_image.md)
    and [`concat_ocr_trainf`](concat_ocr_trainf.md) write training data in ASCII
    format for version number *1* or in binary format
    for version number *2* and *3*.
    Version number *3* stores images of type byte and uint2.
    The binary version is faster in
    reading and writing data and stores training files more packed.
    The ASCII format is compatible to older HALCON releases.
    Depending on the file version, the OCR training files
    can be read by the following HALCON releases:

    - *1* - All HALCON releases
    - *2* - 7.0.2 and higher
    - *3* - 7.1 and higher

    *`value`*: *1*, *2*, *3*

    Default:
     *3*
  - ***"filename_encoding"*:** —

    This parameter only exists for legacy reasons and should not be used
    anymore.
    It determines how the HALCON library internally represents strings. The
    default is UTF-8, which supports all characters of the Unicode standard.

    The string encoding of the 2D code readers, file handles, sockets, tuple
    operators, the HALCON/C++ interface and the HALCON/C interface is
    independent of this parameter. For each, the string encoding can
    individually be changed to local-8-bit encoding.
    See the respective documentation for details.

    The setting of *"filename_encoding"* is a global setting and
    effects all threads.
    This means, changing this value in a thread while other threads are
    processing strings results in an undefined behavior which may lead to
    crashes.
    If a legacy application still requires the HALCON library to use
    local-8-bit encoding, see the
    [Technical Updates](https://www.mvtec.com/doc/halcon/manuals/technical_updates/technical_updates_0000.html)
    for further explanations.

    *`value`*: *"utf8"* or *"locale"*

    Default:
     *"utf8"*
  - ***"write_halcon_files_encoding"*:** —

    Starting with HALCON 18.05 all proprietary HALCON files which store user
    defined strings use UTF-8 as the default string encoding when the data is
    serialized or written into a file.
    The encoding concerns mainly HALCON tuples as well as OCR and OCV
    classifiers, and training data, which all store user
    defined class or character names.
    This allows to share these files easily between different operating
    systems, countries, and locales.
    If such a file with special characters should be used by an application
    that was built with an older HALCON version (before HALCON 18.05) and
    relies on the locale encoding of the strings, this option can be used
    to force HALCON to write its files with the current locale system
    encoding instead of UTF-8.
    Note that the changed encoding concerns only files that store strings
    with special characters, i.e. characters that are not plain ASCII.
    In addition, this option does not affect user files which
    can be opened with [`open_file`](open_file.md).

    *`value`*: *"locale"* or *"utf8"*

    Default:
     *"utf8"*
  - ***"read_halcon_files_encoding_fallback"*:** —

    Older proprietary HALCON files (before HALCON 18.05) are read by default
    with the locale system encoding.
    If an old HALCON file was written with UTF-8 instead, this parameter can
    be used to change the encoding for reading.
    This concerns mainly the HALCON tuples as well as OCR and OCV
    classifiers, and training data, which all store user
    defined class or character names.
    Note that this option has no effect on reading new HALCON files and on
    files which contain only plain ASCII characters.
    In addition, this option does not affect user files which
    can be opened with [`open_file`](open_file.md).

    *`value`*: *"locale"* or *"utf8"*

    Default:
     *"locale"*
  - ***"tuple_string_operator_mode"*,
    *"tsp_tuple_string_operator_mode"*:** —

    This parameters determines how UTF-8 strings are processed by tuple string
    operators, like [`tuple_ord`](tuple_ord.md), [`tuple_strlen`](tuple_strlen.md), or
    [`tuple_substr`](tuple_substr.md), when *"filename_encoding"* is set to
    *"utf8"*, which is the default now.
    The standard behavior is that these strings are processed by characters or
    Unicode code points and not by bytes.
    I.e., the string length (operator [`tuple_strlen`](tuple_strlen.md)) of all characters
    that are build from a single Unicode code point is 1, and accessing the n-th
    element of a string will always return the corresponding Unicode code
    point, no matter how many bytes are used to represent that code point or
    the code points before in UTF-8.
    This behavior can be changed by setting
    *"tuple_string_operator_mode"* to *"byte"*.
    In that mode strings are processed byte by byte.

    *`value`*: *"codepoint"* or *"byte"*

    Default:
     *"codepoint"*
- **Directories:**

  - ***"halcon_dir"* *):** —

    This parameter returns the root directory of the HALCON installation.

    *`value`*: Name of the directory.
  - ***"example_dir"* *):** —

    HDevelop example programs (e.g., loaded via the `Browse
    HDevelop Program Examples` dialog or via the `HDevelop
    examples` sections in the reference manual) will be looked for in
    the directory *"example_dir"*. Note that if you set
    *"example_dir"* to a directory that does not contain the
    installed HDevelop example programs, the above mentioned mechanisms
    to load HDevelop example programs will fail.

    *`value`*: Name of the directory.
  - ***"calib_dir"* *):** —

    Camera parameter files (e.g., acquired via [`read_cam_par`](read_cam_par.md))
    will be looked for in the
    currently used directory and in *"calib_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).

    *`value`*: Name of the directory.
  - ***"dl_dir"* *):** —

    Deep learning models (e.g., acquired via [`read_dl_model`](read_dl_model.md))
    will be looked for in the
    currently used directory and in *"dl_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).

    *`value`*: Name of the directory.
  - ***"filter_dir"* *):** —

    Filter masks (e.g., used via [`convol_image`](convol_image.md))
    will be looked for in the
    currently used directory and in *"filter_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).

    *`value`*: Name of the directory.
  - ***"image_dir"* *):** —

    Image files (e.g., acquired via [`read_image`](read_image.md) and
    [`read_sequence`](read_sequence.md)) will be looked for in the
    currently used directory and in *"image_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).
    The path can also be determined using the environment variable
    HALCONIMAGES.

    *`value`*: Name of the directory.
  - ***"3d_model_dir"* *):** —

    3D object model files (e.g., acquired via [`read_object_model_3d`](read_object_model_3d.md))
    will be looked for in the
    currently used directory and in *"3d_model_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).

    *`value`*: Name of the directory.
  - ***"lut_dir"* *):** —

    Color tables ([`set_lut`](set_lut.md)) which are realized as an ASCII-file
    will be looked for in the currently used directory and in *"lut_dir"*
    (if no absolute paths are indicated).
    As default, HALCON will search the color tables in the
    sub-directory `'lut'`.

    *`value`*: Name of the directory.
  - ***"help_dir"* *):** —

    The online text files {German or English}.hlp, .sta, .key
    .num and .idx will be looked for in the currently used
    directory or in the path specified by *"help_dir"*.
    This system parameter is necessary
    for instance when using the operators [`get_operator_info`](get_operator_info.md) and
    [`get_param_info`](get_param_info.md).
    It can also be set by the environment variable
    HALCONROOT before initializing HALCON.
    In this case the variable must indicate the directory above
    the help directories (that is the HALCON home directory).

    *`value`*: Name of the directory.
  - ***"ocr_dir"* *):** —

    OCR classifiers (e.g., acquired via [`read_ocr_class_knn`](read_ocr_class_knn.md))
    will be looked for in the
    currently used directory and in *"ocr_dir"*
    (if no absolute paths are indicated).
    More than one directory name can be indicated (search paths), separated
    by semicolons (Windows) or colons (Unix-like systems).

    *`value`*: Name of the directory.
- **Other:**

  - ***"disabled_operators"*:** —

    This parameter allows disabling of specific HALCON operators. This can be
    useful if a program allows running user-created HDevelop scripts, but certain
    operators should not be allowed for security reasons, e.g., the
    [`system_call`](system_call.md) operator. Any attempt to execute a disabled operator will
    raise the exception H_ERR_OP_DISABLED (9055). Note that once an operator is
    disabled, it cannot be reenabled during the remaining lifetime of the
    process.

    The value for this parameter is a tuple containing the names of all operators
    to be disabled.
  - ***"do_low_error"* *):** —

    Determines the behavior regarding HALCON low level errors.

    - If the parameter *"do_low_error"* is set to
      *"false"*, then no low level errors are thrown. However,
      the low level error messages still appear in the output console
      (a window containing a log of the most recent messages) that can
      be opened via the window menu.
    - If the parameter *"do_low_error"* is set to *"disabled"*,
      the low level errors are suppressed and are not listed in the output console.
    - If the parameter is set to *"stderr"*, the corresponding
      low level error message is printed to standard error.
    - If it is set to *"message_box"*, then a message
      box containing the error text is opened
      (this functionality is implemented on Windows systems
      only).
    - The parameter value *"callback"* can
      be used to determine a callback function, which should be
      called in case of a low level error. The address of this
      callback function is specified in the second index entry of the
      parameter *`value`*.

      The signature of the callback function is the following:
      void LowErrorCallbackProc(const char* err_text)
      On Windows 32 bit systems, the __stdcall naming convention is used:
      void (__stdcall LowErrorCallbackProc)(const char* err_text)

      The parameter
      value *"callback"* can be used in HDevelop only
      if the callback procedure is set to 0, in which case the
      output of low level error messages is omitted.

      The string encoding of the message corresponds to the HALCON library
      encoding defined by *"filename_encoding"*.
    - If low level error messages should be printed to file,
      then the parameter value *"file"* should be used together
      with a file handle referring to a corresponding file
      previously opened via [`open_file`](open_file.md).
    - The parameter values *"callback"*
      and *"file"* can be used only in combination with a
      corresponding procedure and file handle, respectively.
    - With the exception of the parameter value
      *"false"*, the parameter *"do_low_error"*
      can be assigned multiple
      values. In case of a low level error, the corresponding
      actions are executed in the order of the values as passed in
      the input parameter tuple. If the tuple contains a certain
      parameter value multiple times, then only the first
      occurrence of the value in the tuple is taken into account, i.e., it
      is not possible to execute the same action multiple times in
      case of a low level error . If *"do_low_error"* is
      assigned multiple values or either the value *"file"*
      or *"callback"*, then it cannot be set in combination
      with other system parameters in the same call of
      `set_system`.
    - Every setting of *"do_low_error"*
      via `set_system` overrides the previous setting of the
      parameter.
    - The single parameter value *"true"*
      corresponds to the parameter value *"message_box"* on
      Windows systems and *"stderr"* on Unix-like systems.

    *`value`*: *"true"*, *"false"*, *"disabled"*,
    *"stderr"*, *"message_box"*,
    *"callback"*, *"file"*

    Default:
     *"false"*
  - ***"cancel_draw_result"*, *"tsp_cancel_draw_result"*:** —

    Many draw operators (like, e.g., [`draw_region`](draw_region.md) or
    [`draw_rectangle1`](draw_rectangle1.md)) can be canceled
    by ending the drawing with the right mouse button without
    new objects being drawn or existing objects being modified. The
    stop button of HDevelop can also be used to abort draw operators.
    The aborted draw operators return empty objects or empty tuples,
    respectively.
    *"cancel_draw_result"* controls the behavior of aborted draw
    operators.

    The following values are available for
    *`value`*:

    - *"true"*: The draw operator returns no error.
    - *"exception"*: An exception is raised.

    Default:
     *"true"*
  - ***"seed_rand"*:** —

    Sets the seed of the thread specific random generator used in
    operators like, e.g., [`tuple_rand`](tuple_rand.md). If no seed has been set,
    the random generator is seeded with the current system time (amongst others)
    on the first call of one of the operators listed above. Afterwards
    the value used as seed can be queried with [`get_system`](get_system.md).

    This parameter accepts integer values or the string *"default"*
    to re-establish the default behavior.
  - ***"cudnn_deterministic"*:** —

    Determines whether the cuDNN library for deep learning uses deterministic
    algorithms to enforce bit-wise reproducibility "when executed on GPUs with
    the same architecture and the same number of SMs". Afterwards the value used
    can be queried with [`get_system`](get_system.md).

    Please note that reproducibility is not guaranteed across different cuDNN
    versions. Further using deterministic algorithms can slow down the
    computation on some architectures.

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"cudnn_tuning"*:** —

    Defines the strategy used by the cuDNN library for deep learning to select
    the convolution algorithms. The value that is used can be queried with
    [`get_system`](get_system.md).

    This setting only affects models that are initialized with the CUDA-based
    runtime after the setting has been set. Models that are already initialized
    will not change their convolution algorithms.

    Please note that this setting only applies if
    *"cudnn_deterministic"* is set to *"false"*.

    Available values for *`value`*:

    - *"heuristic"*:
      Uses a static heuristic. The same algorithms are selected for the same
      convolutions on the same GPU.
    - *"deterministic"*:
      Behaves the same as *"cudnn_deterministic"* set to *"true"*.
    - *"fastest"*:
      Selects the fastest available convolution algorithms. Please note that
      these algorithms can require more GPU memory. See more information below.
    - *"memory"*:
      Selects convolution algorithms that require less GPU memory. Please
      note that these algorithms tend to exhibit slower performance. See more
      information below.

    Please note that for *"fastest"* and *"memory"* the algorithm
    selection is based on an online device measurement. As a result, the device
    initialization of the deep learning model is significantly slower than
    for *"heuristic"* or *"deterministic"*. Furthermore, for
    *"fastest"* and *"memory"*, different algorithms may be
    selected for the same convolutions on the same GPU, as their selection
    strongly depends on the current system load.

    Default:
     *"heuristic"*
  - ***"clock_mode"*:** —

    Determines the mode of the measurement of time intervals with
    [`count_seconds`](count_seconds.md).

    *`value`*:

    - *"performance_counter"* measures the elapsed system time
      with preferably high precision. HALCON uses the most accurate time
      measurement method provided by the operating system. If no high precision
      measurement method is available, a lower resolution method is used. On
      Windows systems the Performance Counter is used. For more information
      about the Performance Counter on Windows refer to the Microsoft Developer
      Network (MSDN) documentation. The Performance Counter provides the
      highest precision (below one millisecond). However, it may not work
      correctly on some systems due to issues with energy management and/or
      multithreading. If the Performance Counter is not supported by the
      operating system, the setting *"multimedia_timer"* applies. On
      Unix-like systems (e.g., Linux) the precision is also
      generally below one millisecond, and it may also be affected by problems
      due to energy management and/or multithreading. If you encounter such
      problems you should use the *"elapsed_time"* setting.
    - *"elapsed_time"* measures the elapsed system time similar to
      the setting *"performance_counter"*. The difference is that other
      measurement methods are used which are less accurate but generally not
      much affected by problems due to energy management and/or multithreading.
      The precision is in general one millisecond. This setting should be used,
      if the measurements using *"performance_counter"* are unreliable
      and a precision of one millisecond is acceptable.
    - *"multimedia_timer"* measures the elapsed system time using
      Multimedia Timers on Windows. Please refer to the Microsoft Developer
      Network (MSDN) documentation for more information on Multimedia Timers.
      This method has in general a resolution of one millisecond. If such a
      resolution cannot be achieved on your system you may use the Windows
      functions 'timerBeginPeriod' and 'timerEndPeriod' in order to increase
      the precision (see MSDN). On Unix-like systems there are no Multimedia
      Timers and therefor the setting *"performance_counter"* applies.
    - *"processor_time"* measures the time the running HALCON
      process occupies the CPU. This kind of measuring time is independent of
      the CPU load caused by other processes, but it features a lower
      resolution on most systems and is therefore less accurate for smaller
      time intervals. Please note that the runtime of many applications is not
      only affected by CPU processing time. A lot of applications will be
      affected by input/output or memory management. For such applications the
      setting *"performance_counter"* or *"elapsed_time"* should
      be used instead.

    Default:
     *"performance_counter"*

    Please note that the settings *"performance_counter"* and
    *"elapsed_time"* measure the elapsed system time. As a consequence
    the measured time intervals are affected by the system load while
    measuring. If these settings are used to measure the runtime of a given
    application it should be ensured that other processes do not affect the
    measurement.
  - ***"timer_mode"*:** —

    Determines the mode of measurement used by the operators supporting
    timeouts.

    Available values for *`value`*:

    - *"elapsed_time"*: see description in section
      *"clock_mode"*
    - *"multimedia_timer"*: see description in section
      *"clock_mode"*
    - *"performance_counter"*: see description in section
      *"clock_mode"*

    Default:
     *"multimedia_timer"* on Windows systems,
    *"elapsed_time"* on Linux systems
  - ***"tsp_clear_extended_error"*:** —

    Clears the extended error information of the current thread.
  - ***"system_time_base"*:** —

    Determines how the system time is read.
    The system time can be read using [`get_system_time`](get_system_time.md).

    *`value`*: *"UTC"* (Coordinated Universal Time), *"localtime"* (local time configured on the used system)

    Default:
     *"localtime"*
  - ***"max_connection"*:** —

    Determines the maximum number of regions returned by
    [`connection`](connection.md). For *`value`*=*0*, all regions
    are returned.

    *`value`*: >=*0*

    Default:
     *0*
  - ***"extern_alloc_funct"*:** —

    Pointer to external function for memory allocation
    of result images. This function should have the following
    signature: 'void* ExternAllocFunc(size_t)'. If *0* is passed
    the HALCON allocation function will be used.

    *`value`*: Function pointer.

    Default:
     *0*
  - ***"extern_free_funct"* *):** —

    Pointer to external function for memory deallocation
    of result images. This function should have the following
    signature: 'void ExternFreeFunct(void*)'. If *0* is passed
    the HALCON deallocation function will be used.

    *`value`*: Function pointer.

    Default:
     *0*
  - ***"image_cache_capacity"* *):** —

    To speed up allocation of new images, HALCON does not free
    image memory of image objects but caches it to reuse it. With this parameter,
    you can set an upper limit in bytes for this HALCON image cache. Freed
    images are cached as long as the upper limit is not reached.
    This functionality can be switched off by setting
    *"image_cache_capacity"* to *0*.

    *`value`*: Limit for HALCON image cache.

    Default:
     16777216 (16MByte)
  - ***"global_mem_cache"*:** —

    Cache mode of global memory, i.e., memory that is visible
    beyond an operator. It specifies whether unused global
    memory should be cached for each thread separately
    (*"exclusive"*) or freed (*"idle"*). When using
    *"exclusive"* to cache memory, memory allocation and processing
    are sped up at the cost of memory consumption.
    With the action parameter
    *"cleanup"*, cached memory can be freed physically
    again. For more information on HALCON's caching mechanism, please
    refer to the technical note `HALCON Memory Management`.

    *`value`*: *"idle"*, *"exclusive"*, *"cleanup"*

    Default:
     *"exclusive"*
  - ***"temporary_mem_cache"* *), *"tsp_temporary_mem_cache"*:** —

    This parameter controls the operating mode of the temporary memory cache.
    The temporary memory cache is used to speed up an application by caching
    memory used temporarily during the execution of an operator. For most
    applications the default setting (*"exclusive"*) will produce the
    best results. For more information on HALCON's caching mechanism,
    please refer to the technical note `HALCON Memory Management`.

    The following modes are supported:

    - *"idle"*
      The temporary memory cache is turned off. This mode will use the least
      memory, but will also reduce performance compared to the other modes.
    - *"shared"*
      All temporary memory is cached globally in the temporary memory
      reservoir. This mode will use less memory than *"exclusive"* mode,
      but will also generally offer less performance.
    - *"exclusive"*
      All temporary memory is cached locally for each thread. This mode will
      use the most memory, but will generally also offer the best performance.
    - *"aggregate"*
      Temporary memory superblocks that are larger than the threshold set with
      the *"alloctmp_max_blocksize"* parameter are cached in the global
      memory reservoir, while all smaller superblocks are aggregated into a
      single superblock that is cached locally for each thread.
      If the global memory reservoir is disabled, the large superblocks are
      freed instead. The aggregated superblock will be sized according to the
      temporary memory usage the thread has seen so far, but it will not be
      larger than *"alloctmp_max_blocksize"* (if set) or smaller than
      *"alloctmp_min_blocksize"* (if set).

    Note, the action of setting the temporary memory cache mode to
    *"idle"* (or *"false"*) itself runs exclusively, see
    the section “Parallelization information” above.
    In contrast, the action of setting the temporary memory cache mode to an
    other mode runs in reentrant mode, meaning without blocking other
    HALCON operators.

    For backward compatibility, the values *"false"* and *"true"*
    are also accepted; they correspond to *"idle"* and
    *"exclusive"*, respectively.

    *`value`*: *"idle"*, *"shared"*, *"exclusive"*,
    or *"aggregate"*

    Default:
     *"exclusive"*
  - ***"temporary_mem_reservoir"*,
    *"tsp_temporary_mem_reservoir"*:** —

    If set to *"true"*, the global temporary memory reservoir is
    enabled. If it is set to *"false"*, it is disabled and any memory
    superblocks put into the reservoir are freed instead.

    Any thread that needs new temporary memory will first check
    if the reservoir has a superblock available and only allocate more memory
    from the system if it does not. Superblocks are put into
    the reservoir by threads operating their caches in the *"shared"* or
    *"aggregate"* modes.

    Note that the global setting of this parameter overrides the
    thread-specific setting, i.e., if *"temporary_mem_reservoir"* is set
    to *"false"*, *"tsp_temporary_mem_reservoir"* will have no
    effect.

    *`value`*: *"false"* or *"true"*

    Default:
     *"true"*
  - ***"temporary_mem_reservoir_size"*:** —

    The maximum amount of memory the global temporary memory reservoir may
    cache, in bytes. If set to *-1*, the cache is limited only by the
    amount of available memory.

    *`value`*: *-1* or >= *0*

    Default:
     *-1*
  - ***"alloctmp_min_blocksize"*,
    *"tsp_alloctmp_min_blocksize"*:** —

    Minimum size of memory superblocks used by the temporary memory cache, in
    bytes. (No effect if *"temporary_mem_cache"* == *"idle"*).
    With the default setting *-1*, HALCON will use a heuristic based on
    the current image size to determine a sensible superblock size. For most
    applications this will be the best choice. If the parameter is set to a
    value greater than or equal to zero, HALCON will use this size instead.
    Note that if an operator requires temporary memory objects larger than the
    *"alloctmp_min_blocksize"*, it will ignore this parameter.

    *`value`*: *-1* or >= *0*

    Default:
     *-1*
  - ***"alloctmp_max_blocksize"*,
    *"tsp_alloctmp_max_blocksize"*:** —

    Setting this parameter to a value greater than or equal to zero will
    limit the size of temporary memory cache superblocks determined by
    a heuristic if *"alloctmp_min_blocksize"* is set to *-1*
    (no effect if *"temporary_mem_cache"* == *"idle"*).
    HALCON is still able to allocate superblocks larger than the limit,
    if necessary. With the default setting *-1*, the superblock size
    determined by the heuristic is not limited by HALCON.
    For most applications, this will be the best choice.
    In *"aggregate"* mode, this parameter additionally limits the size of
    the aggregated cache superblock, and determines the size threshold for
    superblocks to be placed into the temporary memory reservoir.

    *`value`*: *-1* or >= *0*

    Default:
     *-1*
  - ***"database"* *):** —

    Determines whether instantiated iconic objects should be
    listed in one of the five relations (gray-value data, region
    data, XLDs, iconic objects and object tuples) of the
    HALCON database. The relations can be used for, e.g.,
    debugging purposes. See also [`count_relation`](count_relation.md),
    [`reset_obj_db`](reset_obj_db.md). Note that collecting database information is not
    thread-safe when passing iconic objects between threads, meaning when
    deleting objects in a different thread than generating them.

    *`value`*: *"true"*, *"false"*

    Default:
     *"false"*
  - ***"reset_used_modules"* *):** —

    Set this to any value to reset the used modules reported by
    [`get_modules`](get_modules.md).
  - ***"mmx_enable"*:** —

    Flag, if MMX operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"mmx_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports MMX, else
    *"false"*
  - ***"sse_enable"*:** —

    Flag, if SSE operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"sse_supported"* == *"false"*,
    see also
    operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSE, else
    *"false"*
  - ***"sse2_enable"*:** —

    Flag, if SSE2 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"sse2_supported"* == *"false"*,
    see also
    operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSE2, else
    *"false"*
  - ***"sse3_enable"*:** —

    Flag, if SSE3 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"sse3_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSE3, else
    *"false"*
  - ***"ssse3_enable"*:** —

    Flag, if SSSE3 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"ssse3_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSSE3, else
    *"false"*
  - ***"sse41_enable"*:** —

    Flag, if SSE41 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"sse41_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSE41, else
    *"false"*
  - ***"sse42_enable"*:** —

    Flag, if SSE42 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"sse42_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports SSE42, else
    *"false"*
  - ***"avx_enable"*:** —

    Flag, if AVX operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX, else
    *"false"*
  - ***"avx2_enable"*:** —

    Flag, if AVX2 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx2_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX2, else
    *"false"*
  - ***"avx2_gather_enable"*:** —

    Flag, if AVX2 gather operations are used to accelerate selected
    image processing operators (*"true"*) or not (*"false"*).
    (No effect, if *"avx2_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     corresponds to *"avx2_gather_recommended"*
  - ***"avx512f_enable"*:** —

    Flag, if AVX-512F operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512f_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512F, else
    *"false"*
  - ***"avx512dq_enable"*:** —

    Flag, if AVX-512DQ operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512dq_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512DQ, else
    *"false"*
  - ***"avx512bw_enable"*:** —

    Flag, if AVX-512BW operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512bw_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512BW, else
    *"false"*
  - ***"avx512cd_enable"*:** —

    Flag, if AVX-512CD operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512cd_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512CD, else
    *"false"*
  - ***"avx512vl_enable"*:** —

    Flag, if AVX-512VL operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512vl_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512VL, else
    *"false"*
  - ***"avx512vbmi_enable"*:** —

    Flag, if AVX-512VBMI operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512vbmi_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512VBMI, else
    *"false"*
  - ***"avx512ifma_enable"*:** —

    Flag, if AVX-512IFMA operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512ifma_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512IFMA, else
    *"false"*
  - ***"avx512vbmi2_enable"*:** —

    Flag, if AVX-512VBMI2 operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512vbmi2_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512VBMI2, else
    *"false"*
  - ***"avx512vpopcntdq_enable"*:** —

    Flag, if AVX-512VPOPCNTDQ operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512vpopcntdq_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512VPOPCNTDQ, else
    *"false"*
  - ***"avx512bitalg_enable"*:** —

    Flag, if AVX-512BITALG operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512bitalg_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512BITALG, else
    *"false"*
  - ***"avx512vnni_enable"*:** —

    Flag, if AVX-512VNNI operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"avx512vnni_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports AVX-512VNNI, else
    *"false"*
  - ***"neon_enable"*:** —

    Flag, if NEON operations are used to accelerate selected
    image processing operators (*"true"*) or
    not (*"false"*).
    (No effect, if *"neon_supported"* == *"false"*,
    see also operator [`get_system`](get_system.md))

    *`value`*: *"true"*, *"false"*

    Default:
     *"true"* if CPU supports NEON, else
    *"false"*
  - ***"language"* *):** —

    Language used for error messages.

    *`value`*: *"english"*, *"german"*.

    Default:
     *"english"*
  - ***"add_progress_callback"*, *"remove_progress_callback"*:** —

    Adds or removes a callback function for operator progress and messages.
    The callback function is called by some operators in irregular
    intervals to signal their progress or a message to the application.

    The signature of the callback is
    void HProgressBarCallback(Hlong id,
    const char *operator_name,
    double progress,
    const char *message)
    On Windows 32 bit systems, the __stdcall naming convention is used:
    void (__stdcall HProgressBarCallback)(Hlong id,
    const char *operator_name,
    double progress,
    const char *message)

    A corresponding delegate HalconAPI.HProgressBarCallback is defined
    for HALCON/.NET. Note that in order to pass a delegate to
    `set_system` you will need to call
    Marshal.GetFunctionPointerForDelegate and make sure the delegate is
    not garbage collected as long as the pointer remains in use.

    public delegate void HProgressBarCallback(IntPtr id,
    string operatorName,
    double progress,
    string message)

    The parameters are:

    - *"id"*:
      Thread-ID from which the operator was originally called.
      If the automatic operator parallelization is active, the callback
      might happen in a thread that is different from the one that was
      originally used to start the operator.
      Applications which display the progress in a GUI might have to consider
      this.
    - *"operator_name"*:
      Name of the currently executed operator.
    - *"progress"*:
      The interpretation of this parameter depends on its value.
      Between 0 and 1: The approximate current progress of the operator.
      -1: The operator shows only a message and does not set the progress.
      This parameter should be ignored.
      -2: The operator completed execution. This is the last callback for this
      operator and a chance for the application to perform cleanups.
      Note that this call happens only for operators that have called
      the callback at least once to set a progress or a message.
    - *"message"*:
      Optional message in english that usually describes the progress
      of the operator such as the current error when training classifiers.
      If the operator has no message to show, this parameter can be NULL.
  - ***"gs1_syntax_dictionary"*** —

    Provides a file containing the GS1 Application Identifier Syntax
    Dictionary to replace the list of GS1 Application Identifiers accepted by
    HALCON. The latest version can be obtained from the official GS1 website.

    GS1 Application Identifiers are prefixes to define the meaning and format
    of data attributes.

    The following values are supported:

    - Filename of the file containing the syntax dictionary.
    - *"default"*: Factory setting is recovered.

    *`value`*: Filename, *"default"*.
  - ***"memory_allocator"*** —

    Set the memory allocator used to manage HALCON's heap. The available
    allocators can be queried with [`get_system`](get_system.md) using the parameter
    *"memory_allocators_supported"*. The following allocators are
    available:

    - *"system"*:
      Use the system's default heap allocator. On Windows this is Win32's
      HeapAlloc, on other operating systems it is the C runtime's malloc
      function.
    - *"mimalloc"*:
      Use the mimalloc heap allocator (see the official mimalloc documentation
      for more details).

    Default:
     *"mimalloc"* on Windows systems, *"system"*
    otherwise

    Please note that this setting does neither replace nor divert the system's
    standard heap allocator, it only changes which function HALCON calls to
    allocate memory internally. It also does not affect any of the third-party
    libraries HALCON uses. As a result, using any setting other than
    *"system"* will increase overall memory consumption, as the HALCON
    process will be using multiple separate heap managers. Depending on the
    operating system and application, this may improve performance.

## Attention

Note that despite the information under 'Parallelization' concerning
the multithreading type, not all parameters are reentrant. Operators that
are followed by '*)' are set exclusively only.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`system_parameter`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the system parameter to be changed.

Default:
"init_new_image"

List of values:
"3d_model_dir", "add_progress_callback", "alloctmp_max_blocksize", "alloctmp_min_blocksize", "avx2_enable", "avx2_gather_enable", "avx512bitalg_enable", "avx512bw_enable", "avx512cd_enable", "avx512dq_enable", "avx512f_enable", "avx512ifma_enable", "avx512vbmi2_enable", "avx512vbmi_enable", "avx512vl_enable", "avx512vnni_enable", "avx512vpopcntdq_enable", "avx_enable", "backing_store", "border_shape_models", "calib_dir", "cancel_draw_result", "clip_region", "clock_mode", "cudnn_deterministic", "cudnn_tuning", "current_runlength_number", "database", "default_font", "disabled_operators", "dl_dir", "do_low_error", "empty_region_result", "example_dir", "extern_alloc_funct", "extern_free_funct", "filename_encoding", "filter_dir", "flush_file", "flush_graphic", "global_mem_cache", "gs1_syntax_dictionary", "height", "help_dir", "icon_name", "image_cache_capacity", "image_dir", "image_dpi", "init_new_image", "int2_bits", "int_zooming", "language", "lut_dir", "max_connection", "memory_allocator", "mmx_enable", "neighborhood", "neon_enable", "no_object_result", "ocr_dir", "ocr_trainf_version", "opengl_compatibility_mode_enable", "opengl_context_cache_enable", "opengl_hidden_surface_removal_enable", "parallelize_operators", "pregenerate_shape_models", "read_halcon_files_encoding_fallback", "reentrant", "remove_progress_callback", "reset_used_modules", "seed_rand", "sse2_enable", "sse3_enable", "sse41_enable", "sse42_enable", "sse_enable", "ssse3_enable", "store_empty_region", "system_time_base", "temporary_mem_cache", "temporary_mem_reservoir", "temporary_mem_reservoir_size", "thread_num", "thread_pool", "timer_mode", "tsp_alloctmp_max_blocksize", "tsp_alloctmp_min_blocksize", "tsp_cancel_draw_result", "tsp_clear_extended_error", "tsp_clip_region", "tsp_current_runlength_number", "tsp_empty_region_result", "tsp_height", "tsp_init_new_image", "tsp_neighborhood", "tsp_no_object_result", "tsp_store_empty_region", "tsp_temporary_mem_cache", "tsp_temporary_mem_reservoir", "tsp_thread_num", "tsp_tuple_string_operator_mode", "tsp_width", "tuple_string_operator_mode", "update_lut", "use_window_thread", "width", "write_halcon_files_encoding", "x_package"

**`value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

New value of the system parameter.

Default:
"true"

Suggested values:
"true", "false", 0, 4, 8

## Result

The operator `set_system` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct.
Otherwise an exception will be raised.

## Possible Predecessors

`reset_obj_db`,
`get_system`,
`set_check`

## See also

`get_system`,
`set_check`,
`count_seconds`

## Module

Foundation

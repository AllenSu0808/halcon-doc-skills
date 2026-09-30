# get_system (Operator)

## Name

`get_system` — Get current value of HALCON system parameters.

## Signature

`def get_system(query: MaybeSequence[str]) -> Sequence[Union[int, float, str]]`

`def get_system_s(query: MaybeSequence[str]) -> Union[int, float, str]`

## Description

The operator `get_system` returns information concerning the
currently activated HALCON system parameters.

**Readable and Writable Parameters**

`get_system` returns information about all parameters that are set
with [`set_system`](set_system.md).
For more information on read- and writable parameters, please refer to the
reference documentation of [`set_system`](set_system.md).

**Read-Only Parameters**

The following system parameters can be queried:

- **Versions:**

  - ***"halcon_xl"*:** —

    The currently used variant of HALCON:
    HALCON XL, which allows images larger than 32768 x 32768 (*"true"*)
    or HALCON, which restricts the maximal image size to 32768 x 32768
    (*"false"*).
  - ***"version"*:** —

    HALCON version number.
  - ***"last_update"*:** —

    Creation date of the HALCON library.
  - ***"revision"*:** —

    Revision number of the HALCON library.
  - ***"file_version"*:** —

    File version number of the HALCON library. The number is made up of the
    HALCON version number, the revision number, and the build number.
- **Upper Limits:**

  - ***"max_inp_obj_par"*:** —

    Maximum number of input parameters.
  - ***"max_outp_obj_par"*:** —

    Maximum number of output parameters.
  - ***"max_inp_ctrl_par"*:** —

    Maximum number of input control parameters.
  - ***"max_outp_ctrl_par"*:** —

    Maximum number of output control parameters.
  - ***"max_window"*:** —

    Maximum number of windows.
- **Graphic:**

  - ***"window_name"*:** —

    Returns the value that may have been set with `set_window_attr('window_title',...)`.
    If nothing has been set yet, the string *"default"* is returned.
- **Parallelization:**

  - ***"processor_num"*:** —

    Returns the number of processors that HALCON has
    found on the hardware it is running on.
  - ***"tsp_used_thread_num"*:** —

    Returns the number of threads the last operator was
    using for automatic operator parallelization. Only operators that were run by
    the calling thread and support automatic parallelization are
    considered.
    Note that using this parameter in HDevelop works
    only in run mode, not in single step mode.
  - ***"tsp_used_split_levels"*** —

    Returns all split levels the last operator was
    using for automatic parallelization. Only operators that were run by
    the calling thread and support automatic parallelization are considered.
    If the last operator was not parallelized, the string
    *"false"* is returned.
    Note that using this parameter in HDevelop works
    only in run mode, not in single step mode.
- **Licensing:**

  - ***"available_license_files"*** —

    The list of license files HALCON can find.
  - ***"current_license_info"*** —

    A tuple containing information about the current license. If the license
    is invalid, the tuple contains a single element with the value
    *"invalid"*. Otherwise, the tuple contains the following elements
    in order:

    - The name of the license file used to obtain the current license.
    - The type of license, either *"runtime"*,
      *"development"*, or *"sasl"*.
    - The highest version of HALCON licensed by the current license.
    - The expiration date of the current license in ISO 8601 format, or
      *"permanent"* for licenses without an expiration date.
    - The list of HALCON modules licensed by the current license as a single
      string, separated by *' | '*.
    - The number of concurrent licenses, or 0 for unlimited concurrent use.
    - The number of concurrent sessions, or 0 for unlimited concurrent
      sessions.
    - The host ID used to obtain the current license.
    - The flags of the current license.
    - The contents of the license info field.

    If a particular piece of information is not available, an empty string is
    returned instead.
  - ***"expiration_date"*** —

    The date the HALCON license will expire, in ISO 8601 format, or
    *"permanent"* if the license does not expire.
  - ***"failed_license_rechecks"*** —

    The number of failed license rechecks since process start.
  - ***"is_license_valid"*** —

    This parameter triggers an immediate license check and returns
    *"true"* if a valid license could be found, or *"false"*
    otherwise.
  - ***"licensed_hostid"*** —

    The host ID used to obtain the current license.
  - ***"licensed_modules"*** —

    A list of all modules licensed by the currently used license.
  - ***"licensed_version"*** —

    The highest HALCON version the current license is valid for.
  - ***"licensed_product_edition"*** —

    The HALCON product edition. Will be one of *"Progress"*,
    *"Steady"*, *"Steady Deep Learning"*, or
    *"Student Edition"* depending on the license being used. If there is
    no valid license, an empty string is returned instead.
  - ***"supported_editions"*** —

    Return an array containing the editions this HALCON binary supports.
    Possible values are *"steady"* and *"progress"*.
  - ***"unlicensed_operators"*** —

    A list of operators that require a module that is not licensed and thus
    cannot be used.
- **Other:**

  - ***"available_parameters"*** —

    The list of parameters `get_system` understands.
  - ***"hostids"*:** —

    The host IDs of the computer that can be used for licensing HALCON.
  - ***"num_proc"*:** —

    Total number of the available HALCON procedures
    (*"num_sys_proc"* + *"num_user_proc"*).
  - ***"num_sys_proc"*:** —

    Number of the system procedures (supported procedures).
  - ***"num_user_proc"*:** —

    Number of the user defined procedures (see also `“Extension
    Package Programmer's Manual”`).
  - ***"byte_order"*:** —

    Byte order of the processor (*"msb_first"* or
    *"lsb_first"*).
  - ***"operating_system"*:** —

    Name of the operating system of the computer on which the HALCON
    process is being executed. Note that for all Windows versions,
    'Windows NT' is returned. Use the parameter *"operating_system_version"*
    to query the precise version.
  - ***"operating_system_version"*:** —

    Version number of the operating system of the computer on which
    the HALCON process is being executed. To decode the Windows version numbers,
    please refer to the website information on operating systems and version
    numbers provided by Microsoft.
  - ***"operating_system_build"*:** —

    Additional information about the operating system the HALCON process is run
    on. For Windows, the Windows build number is returned. For Linux, the
    version as returned by the uname system call is returned.
  - ***"hostname"*:** —

    Name of the computer on which the HALCON process is being executed. On
    Windows systems, if the computer is part of a cluster the name of the
    cluster is returned, not the name of the local computer. If the name cannot
    be determined, an empty string is returned.
  - ***"locale_raw"*:** —

    Locale setting that is used by the runtime environment for encoding
    system strings (according to the locale category LC_CTYPE).
    The result corresponds to the result of the system C function setlocale or
    the result of the shell command 'locale' called in a Linux terminal.
    In general, it contains data about the language, the country, and the
    code page or code set - under Windows, for instance,
    *"German_Germany.1252"* or under Linux *"en_US.utf8"*.
    Note, that on Linux the names are not clearly defined because they
    depend on the system and the current configuration.
    Thus, the code set can be set to 'utf8' or 'UTF-8', or may completely be
    missing.
    On systems that do not support locale an empty string is returned.
  - ***"locale_codeset"*:** —

    Code set that is used by the runtime environment for encoding
    system strings (according to the locale category LC_CTYPE).
    In contrast to *"locale_raw"*, this result contains only the
    code set or code page and no information about language and country.
    The code set is returned in a normalized way so that it can easier be used
    in tests.
    The result contains only lowercase letters and numbers, with different
    results for Windows code pages and Linux code sets, as the code sets
    used are usually not identical.
    Under Windows typically the code page number prefixed by 'cp' is returned,
    e.g., *"cp1252"* (for code page 1252 which is commonly used in the
    western world and correlates widely with Latin-1) or *"cp932"*
    (which correlates with ShiftJIS, which is common in Japan).
    Common results under Linux are *"utf8"* (which is the
    default locale on most of the recent Linux distributions),
    *"iso885915"* (Latin-9), *"shiftjis"*, and *"ascii"*
    (referred to as ANSI_X3.4-1968, US-ASCII, POSIX, C).
  - ***"halcon_64"*:** —

    Flag, if the HALCON version is a 64 bit version (*"true"*)
    or not, i.e., if it is a 32 bit version (*"false"*).
  - ***"halcon_arch"*:** —

    Name of the HALCON architecture of the running HALCON process.
  - ***"library_fullname"*:** —

    Path to the currently loaded HALCON library including the file name.
  - ***"temp_mem"*:** —

    Amount of temporary memory used by the last operator
    in byte. The return value is only defined if
    `set_check('memory')` was called before.
  - ***"mmx_supported"*:** —

    Flag, if the processor supports MMX operations (*"true"*)
    or not (*"false"*).
  - ***"sse_supported"*:** —

    Flag, if the processor supports SSE operations (*"true"*)
    or not (*"false"*).
  - ***"sse2_supported"*:** —

    Flag, if the processor supports SSE2 operations (*"true"*)
    or not (*"false"*).
  - ***"sse3_supported"*:** —

    Flag, if the processor supports SSE3 operations (*"true"*)
    or not (*"false"*).
  - ***"ssse3_supported"*:** —

    Flag, if the processor supports SSSE3 operations (*"true"*)
    or not (*"false"*).
  - ***"sse41_supported"*:** —

    Flag, if the processor supports SSE41 operations (*"true"*)
    or not (*"false"*).
  - ***"sse42_supported"*:** —

    Flag, if the processor supports SSE42 operations (*"true"*)
    or not (*"false"*).
  - ***"avx_supported"*:** —

    Flag, if the processor supports AVX operations (*"true"*)
    or not (*"false"*).
  - ***"avx2_supported"*:** —

    Flag, if the processor supports AVX2 operations (*"true"*)
    or not (*"false"*).
  - ***"avx2_gather_recommended"*:** —

    Flag, if the usage of AVX2 gather instructions is recommended on the
    processor (*"true"*) or not (*"false"*).
  - ***"avx512f_supported"*:** —

    Flag, if the processor supports AVX-512F operations (*"true"*)
    or not (*"false"*).
  - ***"avx512dq_supported"*:** —

    Flag, if the processor supports AVX-512DQ operations (*"true"*)
    or not (*"false"*).
  - ***"avx512bw_supported"*:** —

    Flag, if the processor supports AVX-512BW operations (*"true"*)
    or not (*"false"*).
  - ***"avx512cd_supported"*:** —

    Flag, if the processor supports AVX-512CD operations (*"true"*)
    or not (*"false"*).
  - ***"avx512vl_supported"*:** —

    Flag, if the processor supports AVX-512VL operations (*"true"*)
    or not (*"false"*).
  - ***"avx512vbmi_supported"*:** —

    Flag, if the processor supports AVX-512VBMI operations (*"true"*)
    or not (*"false"*).
  - ***"avx512ifma_supported"*:** —

    Flag, if the processor supports AVX-512IFMA operations (*"true"*)
    or not (*"false"*).
  - ***"avx512vbmi2_supported"*:** —

    Flag, if the processor supports AVX-512VBMI2 operations (*"true"*)
    or not (*"false"*).
  - ***"avx512vpopcntdq_supported"*:** —

    Flag, if the processor supports AVX-512VPOPCNTDQ operations (*"true"*)
    or not (*"false"*).
  - ***"avx512bitalg_supported"*:** —

    Flag, if the processor supports AVX-512BITALG operations (*"true"*)
    or not (*"false"*).
  - ***"avx512vnni_supported"*:** —

    Flag, if the processor supports AVX-512VNNI operations (*"true"*)
    or not (*"false"*).
  - ***"neon_supported"*:** —

    Flag, if the processor supports NEON operations (*"true"*)
    or not (*"false"*).
  - ***"opengl_hidden_surface_removal_available"*:** —

    Flag, if the graphic card supports the acceleration of the
    hidden surface removal used in [`create_shape_model_3d`](create_shape_model_3d.md),
    [`find_shape_model_3d`](find_shape_model_3d.md), [`project_shape_model_3d`](project_shape_model_3d.md), and
    [`project_object_model_3d`](project_object_model_3d.md).
    The minimum requirements are OpenGL 2.0 and the extensions
    GL_EXT_framebuffer_object and GL_ARB_texture_float.
    Please note that these features are not available via
    Windows Remote Desktop or X11 forwarding.
  - ***"alloctmp_max_used"*** —

    The maximum amount of temporary memory required so far for a thread, in
    bytes. The first element of the tuple contains the value for the
    current thread, while any following elements contain the values of
    currently idle threads from the thread pool.

    The maximum is reset when the temporary memory cache mode is set to
    *"idle"*.
  - ***"tsp_temporary_mem_cache_block_sizes"*** —

    Returns a tuple containing the block sizes of all temporary memory blocks
    currently cached in the thread's temporary memory cache, in bytes.
  - ***"temporary_mem_reservoir_block_sizes"*** —

    Returns a tuple containing the block sizes of all temporary memory blocks
    currently cached in the global temporary memory reservoir, in bytes.
  - ***"memory_allocators_supported"*:** —

    Returns a tuple containing the list of available memory allocators that can
    be set using parameter *"memory_allocator"* of [`set_system`](set_system.md).
- **CUDA support for deep learning:**

  - ***"cuda_loaded"*:** —

    Returns *"true"* if the CUDA library could be loaded.
  - ***"cuda_version"*:** —

    Returns the version of the CUDA library.
    If the CUDA library could not be loaded, *-1* is returned.
  - ***"cuda_devices"*:** —

    Returns the names of available devices that are compatible with CUDA.
  - ***"cudnn_frontend_version"*:** —

    Returns the version of the cuDNN Frontend library. If CUDA or cuDNN could
    not be loaded, *-1* is returned.
  - ***"cudnn_loaded"*:** —

    Returns *"true"* if the cuDNN library could be loaded.
  - ***"cudnn_version"*:** —

    Returns the version of the cuDNN library. If the cuDNN library could not
    be loaded, *-1* is returned.
  - ***"cublas_loaded"*:** —

    Returns *"true"* if the cuBLAS library could be loaded.
  - ***"cublas_version"*:** —

    Returns the version of the cuBLAS library. If the cuBLAS library could not
    be loaded, *-1* is returned.
  - ***"nvrtc_version"*:** —

    Returns the version of the NVRTC library.
    If the NVRTC library could not be loaded, *-1* is returned.
- **Arm Compute Library support:**

  - ***"arm_compute_loaded"*:** —

    Returns *"true"* if the Arm Compute Library could be loaded,
    *"false"* otherwise.
  - ***"arm_compute_version"*:** —

    Returns the version of the Arm Compute Library. If the Arm Compute Library
    could not be loaded, an empty string is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`query`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Desired system parameter.

Default:
"init_new_image"

List of values:
"3d_model_dir", "alloctmp_max_blocksize", "alloctmp_max_used", "alloctmp_min_blocksize", "available_license_files", "available_parameters", "avx2_enable", "avx2_gather_enable", "avx2_gather_recommended", "avx2_supported", "avx512bitalg_enable", "avx512bitalg_supported", "avx512bw_enable", "avx512bw_supported", "avx512cd_enable", "avx512cd_supported", "avx512dq_enable", "avx512dq_supported", "avx512f_enable", "avx512f_supported", "avx512ifma_enable", "avx512ifma_supported", "avx512vbmi2_enable", "avx512vbmi2_supported", "avx512vbmi_enable", "avx512vbmi_supported", "avx512vl_enable", "avx512vl_supported", "avx512vnni_enable", "avx512vnni_supported", "avx512vpopcntdq_enable", "avx512vpopcntdq_supported", "avx_enable", "avx_supported", "backing_store", "border_shape_models", "bundle_version", "byte_order", "calib_dir", "cancel_draw_result", "clip_region", "clock_mode", "cublas_loaded", "cublas_version", "cuda_devices", "cuda_loaded", "cuda_version", "cudnn_deterministic", "cudnn_loaded", "cudnn_tuning", "cudnn_version", "current_license_info", "current_runlength_number", "database", "default_font", "disabled_operators", "dl_dir", "do_low_error", "empty_region_result", "example_dir", "expiration_date", "extern_alloc_funct", "extern_free_funct", "failed_license_rechecks", "file_version", "filename_encoding", "filter_dir", "flush_file", "flush_graphic", "global_mem_cache", "halcon_64", "halcon_arch", "halcon_dir", "halcon_xl", "height", "help_dir", "hostids", "hostname", "hthread_id", "icon_name", "image_cache_capacity", "image_dir", "image_dpi", "init_new_image", "int2_bits", "int_zooming", "is_license_valid", "language", "last_update", "library_fullname", "licensed_hostid", "licensed_modules", "licensed_product_edition", "licensed_version", "locale_codeset", "locale_raw", "lut_dir", "max_connection", "max_inp_ctrl_par", "max_inp_obj_par", "max_outp_ctrl_par", "max_outp_obj_par", "max_window", "memory_allocator", "memory_allocators_supported", "mmx_enable", "mmx_supported", "neighborhood", "neon_enable", "neon_supported", "no_object_result", "num_proc", "num_sys_proc", "num_user_proc", "ocr_dir", "ocr_trainf_version", "opengl_compatibility_mode_enable", "opengl_context_cache_enable", "opengl_hidden_surface_removal_available", "opengl_hidden_surface_removal_enable", "operating_system", "operating_system_version", "parallelize_operators", "pregenerate_shape_models", "processor_num", "read_halcon_files_encoding_fallback", "reentrant", "revision", "seed_rand", "sse2_enable", "sse2_supported", "sse3_enable", "sse3_supported", "sse41_enable", "sse41_supported", "sse42_enable", "sse42_supported", "sse_enable", "sse_supported", "ssse3_enable", "ssse3_supported", "store_empty_region", "supported_editions", "system_time_base", "temp_mem", "temporary_mem_cache", "temporary_mem_reservoir", "temporary_mem_reservoir_size", "thread_num", "thread_pool", "timer_mode", "tsp_cancel_draw_result", "tsp_clip_region", "tsp_current_runlength_number", "tsp_empty_region_result", "tsp_height", "tsp_init_new_image", "tsp_neighborhood", "tsp_no_object_result", "tsp_store_empty_region", "tsp_temporary_mem_cache", "tsp_temporary_mem_cache_block_sizes", "tsp_temporary_mem_reservoir", "tsp_thread_num", "tsp_tuple_string_operator_mode", "tsp_used_split_levels", "tsp_used_thread_num", "tsp_width", "tuple_string_operator_mode", "unlicensed_operators", "update_lut", "use_window_thread", "version", "width", "window_name", "write_halcon_files_encoding", "x_package"

**`information`** (output_control)  attribute.value(-array) `→` Sequence[Union[int, float, str]]

Current value of the system parameter.

## Result

The operator `get_system` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct.
Otherwise an exception is raised.

## Possible Predecessors

`reset_obj_db`

## Possible Successors

`set_system`

## See also

`set_system`

## Module

Foundation

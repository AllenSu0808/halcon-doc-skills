# get_system_info (Operator)

## Name

`get_system_info` — Get current value of system information without requiring a license.

## Signature

`get_system_info( : : Query : Information)`

## Description

The operator `get_system_info` returns information concerning the
currently activated HALCON system parameters. Unlike the very similar
[`get_system`](get_system.md), `get_system_info` can be called without a valid
license.

`get_system_info` supports the same parameters supported by
[`get_system`](get_system.md). For more information about the parameters, please refer
to the reference documentation of [`get_system`](get_system.md) and [`set_system`](set_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Query`** (input_control)  attribute.name(-array) `→`  (string)

Desired system parameter.

Default:
'available_parameters'

List of values:
'3d_model_dir', 'alloctmp_max_blocksize', 'alloctmp_max_used', 'alloctmp_min_blocksize', 'available_license_files', 'available_parameters', 'avx2_enable', 'avx2_gather_enable', 'avx2_gather_recommended', 'avx2_supported', 'avx512bitalg_enable', 'avx512bitalg_supported', 'avx512bw_enable', 'avx512bw_supported', 'avx512cd_enable', 'avx512cd_supported', 'avx512dq_enable', 'avx512dq_supported', 'avx512f_enable', 'avx512f_supported', 'avx512ifma_enable', 'avx512ifma_supported', 'avx512vbmi2_enable', 'avx512vbmi2_supported', 'avx512vbmi_enable', 'avx512vbmi_supported', 'avx512vl_enable', 'avx512vl_supported', 'avx512vnni_enable', 'avx512vnni_supported', 'avx512vpopcntdq_enable', 'avx512vpopcntdq_supported', 'avx_enable', 'avx_supported', 'backing_store', 'border_shape_models', 'bundle_version', 'byte_order', 'calib_dir', 'cancel_draw_result', 'clip_region', 'clock_mode', 'cublas_loaded', 'cublas_version', 'cuda_devices', 'cuda_loaded', 'cuda_version', 'cudnn_loaded', 'cudnn_version', 'current_license_info', 'current_runlength_number', 'database', 'default_font', 'disabled_operators', 'dl_dir', 'do_low_error', 'edition', 'empty_region_result', 'example_dir', 'expiration_date', 'extern_alloc_funct', 'extern_free_funct', 'failed_license_rechecks', 'file_version', 'filename_encoding', 'filter_dir', 'flush_file', 'flush_graphic', 'global_mem_cache', 'halcon_64', 'halcon_arch', 'halcon_dir', 'halcon_xl', 'height', 'help_dir', 'hostids', 'hostname', 'hthread_id', 'icon_name', 'image_cache_capacity', 'image_dir', 'image_dpi', 'init_new_image', 'int2_bits', 'int_zooming', 'is_license_valid', 'language', 'last_update', 'library_fullname', 'licensed_hostid', 'licensed_modules', 'licensed_product_edition', 'licensed_version', 'locale_codeset', 'locale_raw', 'lut_dir', 'max_connection', 'max_inp_ctrl_par', 'max_inp_obj_par', 'max_outp_ctrl_par', 'max_outp_obj_par', 'max_window', 'memory_allocator', 'memory_allocators_supported', 'mmx_enable', 'mmx_supported', 'neighborhood', 'neon_enable', 'neon_supported', 'no_object_result', 'num_proc', 'num_sys_proc', 'num_user_proc', 'ocr_dir', 'ocr_trainf_version', 'opengl_compatibility_mode_enable', 'opengl_context_cache_enable', 'opengl_hidden_surface_removal_available', 'opengl_hidden_surface_removal_enable', 'operating_system', 'operating_system_build', 'operating_system_version', 'parallelize_operators', 'pregenerate_shape_models', 'processor_num', 'read_halcon_files_encoding_fallback', 'reentrant', 'revision', 'seed_rand', 'sse2_enable', 'sse2_supported', 'sse3_enable', 'sse3_supported', 'sse41_enable', 'sse41_supported', 'sse42_enable', 'sse42_supported', 'sse_enable', 'sse_supported', 'ssse3_enable', 'ssse3_supported', 'store_empty_region', 'system_time_base', 'temp_mem', 'temporary_mem_cache', 'temporary_mem_reservoir', 'temporary_mem_reservoir_size', 'thread_num', 'thread_pool', 'timer_mode', 'tsp_cancel_draw_result', 'tsp_clip_region', 'tsp_current_runlength_number', 'tsp_empty_region_result', 'tsp_height', 'tsp_init_new_image', 'tsp_neighborhood', 'tsp_no_object_result', 'tsp_store_empty_region', 'tsp_temporary_mem_cache', 'tsp_temporary_mem_cache_block_sizes', 'tsp_temporary_mem_reservoir', 'tsp_thread_num', 'tsp_tuple_string_operator_mode', 'tsp_used_split_levels', 'tsp_used_thread_num', 'tsp_width', 'tuple_string_operator_mode', 'unlicensed_operators', 'update_lut', 'use_window_thread', 'version', 'width', 'window_name', 'write_halcon_files_encoding', 'x_package'

**`Information`** (output_control)  attribute.value(-array) `→`  (integer / real / string)

Current value of the system parameter.

## Result

The operator `get_system_info` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct. Otherwise an exception is raised.

## See also

`get_system`

## Module

none

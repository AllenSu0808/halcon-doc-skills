# list_files (Operator)

## Name

`list_files` — List all files in a directory.

## Signature

`list_files( : : Directory, Options : Files)`

## Description

`list_files` returns all files in the directory given by
*`Directory`* in the parameters *`Files`*. The current
directory can be specified with *''* or *'.'*. The
parameter *`Options`* can be used to specify different
processing options by passing a tuple of values.

If *`Options`* contains *'files'* only the files present in
*`Directory`* are returned. If *'directories'* is
passed, only the directories present in *`Directory`* are
returned. On Unix-like systems *'symlinks'* may be passed to list
symbolic links. Directories are marked by a trailing
'' (Windows) or a trailing
*'/'* (Unix-like systems). If files as well as directories should be
returned, *['files','directories']* must be passed. If
none of *'files'*, *'directories'* or *'symlinks'*
is passed, `list_files` returns an empty tuple.

By passing *'recursive'*, it can be specified that the directory tree
should be searched recursively by examining all sub-directories. On
Unix-like systems, *'follow_links'* can be used to specify that
symbolic links to files or directories should be followed. In the
default setting, symbolic links are not dereferenced, and hence are
not searched if they point to directories, and not returned if they
point to files. The option *'follow_links'* can not be used
in conjunction with the option *'symlinks'*.

For the recursive search, a maximum search depth
can be specified with *'max_depth <d>'*, where *'<d>'*
is a number that specifies the maximum depth.
Hence, *'max_depth 2'* specifies that *`Directory`* and
all immediate sub-directories should be searched. If symbolic links
should be followed it might happen that the search does not
terminate if the symbolic links lead to a cycle in the directory
structure. Because of this, at most 1000000 files (and directories)
are returned in *`Files`*. By specifying a different number
with *'max_files <d>'*, this value
can be modified.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Directory`** (input_control)  filename.dir `→`  (string)

Name of directory to be listed.

**`Options`** (input_control)  string(-array) `→`  (string)

Processing options.

Default:
'files'

Suggested values:
'files', 'directories', 'symlinks', 'recursive', 'follow_links', 'max_depth 5', 'max_files 1000'

**`Files`** (output_control)  string-array `→`  (string)

Found files (and directories).

## Result

`list_files` returns the value 2 (
H_MSG_TRUE)
if the directory exists
and could be read. Otherwise, an exception is raised.

## Possible Successors

`tuple_regexp_select`

## Module

Foundation

# export_def (Operator)

## Name

`export_def` — Insert arbitrary text into the export code of a procedure.

## Signature

`export_def( : : Position, Declaration : )`

## Description

`export_def` allows to define
code lines or text blocks that are written verbatim into the output file
of a procedure or program that is exported.

The parameter *`Position`* controls the placement of the text given
in *`Declaration`*.
The following options are supported:

- ***'in_place'* - #** —

  The text is inserted in the procedure at the actual place, i.e.,
  in between the neighboring program lines.
- ***'at_file_begin'* - #^^** —

  The text is exported at the very beginning of the exported file.
- ***'before_procedure'* - #^** —

  The text is exported immediately before the procedure it is defined in.
- ***'after_procedure'* - #$** —

  The text is exported immediately after the procedure it is defined in.
- ***'at_file_end'* - #$$** —

  The text is exported at the very end of the exported file.

In the program listing, `export_def` is not
represented in normal operator syntax but marked by a special character
sequence.
The first character within the line is the export marker `#` that
can be followed by a position marker as listed above.
If entering an export definition in the full text editor, please note that
there must not be any spaces before `#`.

For better readability, the export character sequence may be followed by
one space character that is not interpreted as part of the export text.
All additional spaces are added to the export.

For lines that are exported within the current procedure, the export
gets the same indentation as the current program lines get.
There is one exception: if the export text starts with `#`
immediately after the export markers or the optional space, the export
text will not be indented at all, e.g.:

```
for Index := 1 to 5 by 1
# #ifdef MY_SWITCH
# int cnt = 100;
  * an optional code block
# #endif
endfor
```

is exported to:

```
proc (...)
{
  ...
  for (...)
  {
#ifdef MY_SWITCH
    int cnt = 100;
    // an optional block
#endif
  }
  ...
}
```

An export definition can be activated and deactivated as any normal operator.
Deactivated export definitions are not exported.

## Parameters

**`Position`** (input_control)  string `→`  (string)

Place where the export text is written.

List of values:
'after_procedure', 'at_file_begin', 'at_file_end', 'before_procedure', 'in_place'

**`Declaration`** (input_control)  string `→`  (string)

Text that is exported.

## Result

`export_def` is never executed.

## See also

`comment`

## Module

Foundation

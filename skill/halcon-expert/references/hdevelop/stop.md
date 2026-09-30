# stop (Operator)

## Name

`stop` — Stop program execution.

## Signature

`stop( : : : )`

## Description

The `stop` operator stops the continuous program execution of the
HDevelop program.
If this happens, the `PC` remains on the `stop` statement
(instead of being placed at the next executable program line)
to show the reason for the program interruption directly even
if numerous comments or other non-executable program lines follow.

The operator is equivalent to the `Stop` action (F9)
in the menu bar.
Unless parallel execution is used (via the `par_start` qualifier),
the program can easily be continued with the `Run` action (F5).
See also “Parallel Execution” in the
[HDevelop User's Guide.](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_0000.html)

It is possible to redefine the behavior by setting a time parameter in
the preferences dialog. In this case, the execution will not stop but
continue after waiting for the specified period of time.
Within this period of time, the program can be interrupted with F9
or continued with one of the run commands.
This is marked by an icon in the first column of the program window.

## Attention

This operator is not supported for code export.

Trying to continue a program that uses parallel execution after calling
`stop` may cause non-deterministic thread behavior or errors.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
regiongrowing (Image, Regions, 3, 3, 6, 100)
count_obj (Regions, Number)
dev_update_window ('off')
for i := 1 to Number by 1
  select_obj (Regions, RegionSelected, i)
  dev_clear_window ()
  dev_display (RegionSelected)
  stop ()
endfor
```

## Result

If the program stops at a `stop` statement, the return state
of the previous operator is kept.
If the program is continued with the `stop` operator,
`stop` always returns 2 (
H_MSG_TRUE)
.

## See also

`exit`

## Module

Foundation

@set PATH=\Bin\imagetools;%PATH%

@for %%f in (mecan*.png) do optipng -o 6 %%f
pause
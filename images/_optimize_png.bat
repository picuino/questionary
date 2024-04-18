@set PATH=\Bin\imagetools;%PATH%

@for %%f in (dino*.png) do optipng -o 6 %%f
pause
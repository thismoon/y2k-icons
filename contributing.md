# Icon guide

I recommended using [inkscape](https://inkscape.org) but you can use your favorite svg editor

## Setting up

> :information_source: instructions may be different between programs, ~~goog-~~ use your search engine for help

> :information_source: if you use inkscape, you can skip this part and use [the template](template.svg), i am not sure of other programs support for the file

- set the unit to `px`
- set page size to `100x100px`
- create a grid with `5` spacing
- major line every `5` OR create another grid with `25` spacing

## design guidelines
 - shapes should be either filled with black or have a stroke
 - stroke shapes should have `5px` stroke width (can be changed in special cases) 
 - to fix stroke shapes getting out of the page, deselect "scale the stroke width" icon then set the icon size to `100x100px` and center it in the page
 - save as optimized svg
 - optimize the icon with [svgo](https://github.com/svg/svgo)
 ```sh
 svgo -f icons/
 ```
Changelog
=========

v0.3.0 - Unreleased
-------------------
This release will focus on supporting Pint quantities.

Highlights
``````````
* If (at least 1) arguments are xarray.DataArray wrapped by pint-xarray, the result is wrapped into a pint-xarray quantity.

v0.2.1 - 2022-03-22
-------------------
Despite all the checking, we missed a bad bug.

Bug Fixes
`````````
* Fixed a bug where attributes would attempt to be be added to non xr.DataArray objects if the gsw function has multiple return values.

v0.2.0 - 2022-03-22
-------------------
This is a major release that is ready for widespread usage.
Our focus was on ensuring compatibility with the upstream API and a units overhaul.

Highlights
``````````
* Upstream compatibility with package layout.
  All the ways you can import gsw and its submodule should now Just Work.
  This includes wildcard imports: ``from gsw_xarray import *`` and even some private members in the upstream that have leaked out.
* All returned xr.DataArray objects will have the units attr set to the correct unit, or be "1" if the result is unitless.
  The unit style is compatible with both UDUNITS (the CF requirement) and the python pint library.
  Several mistakes were found in the upstream documentation, both in the python and matlab sources.
* Functions returning practical salinity or sea water temperature will have the OceanSITES reference_scale attribute set to "PSS-78" or "ITS-90" if appropriate.
* Some standard names assume information about the surface or geopotential that a property is being calculated against.
  We now have some check functions that ensure the standard name is not set if one of these assumptions is not true.

Breaking Changes
````````````````
* The attrs of the returned xr.DataArray object are now completely replaced by attrs controlled by us.
  Previously we would only set the standard_name or units attributes and leave everything else untouched.
  We found this to be confusing and inaccurate since the behavior of xarray would copy the attributes of the first argument to a gsw function.
  This resulted in attributes like long_name to be incorrect.
* The xr.DataArray.name property is now set to the return name of the gsw function.
  For example, SA_from_SP will return a DataArray with name property set to "SA".

v0.1.0 - 2021-12-15
-------------------
* Original release, was basically a proof of concept.
  Only a few functions were wrapped.

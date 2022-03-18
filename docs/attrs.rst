Added Attributes
================
This rather long list shows all the attributes that will be set on the returned DataArray objects and their exact value.

There are some things to be aware of:

* Functions which return unitless values will have the ``units`` attribute set to ``"1"`` folloing the CF recomended practice (based on SI).
  Rather than omit the ``units`` attribute entirely, we want to explicitly state that something is unitless.

* The unit strings were selected to be compatable with both UDUNITS2 (the requrement in CF), and the python pint library.

* Not every returned value has a CF standard name, in which case we must not include the standard name attribute.
  As names are added to the CF table, we will attempt to update this list.
  The current standard names were taken from v78 last published on 2021-09-21.

  Additionally, some standard names are only valid for speciifc input values e.g. z_from_p has geopotential parameters and the normal standard name does not apply if these are not 0.

* We include the OceanSITES ``reference_scale`` attribute for functions that return PSS-78 or ITS-90.

* Finally, we did out best to include the correct units and standard name based on the published TEOS-10 documentation.
  If erorrs are noted, please open an issue on github so we can correct these errors.

.. include:: _attr_table.rst
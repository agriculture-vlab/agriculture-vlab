# Atmospheric sensors
***
### AEM-2
#### Source : FedEO (NASA_CMR)
> **Description** : The GOZCARDS Merged Data for Ozone 1 month L3 10 degree Zonal Averages on a Vertical Pressure Grid product (GozMmlpO3) contains zonal means and related information (standard deviation, minimum/maximum value, etc.), calculated as a result of a merging process that ties together the source datasets, after bias removal and averaging. The merged O3 data are from the following satellite instruments: SAGE I (v5.9_rev; 1979-1981), SAGE II (v6.2; 1984-2005), HALOE (v19; 1991-2005), UARS MLS (v5; 1991-1997), ACE-FTS (v2.2; 2004-onward), Aura MLS (v2.2; 2004 onward) others as validation (e.g., SAGE III, v4.0; 2002-2005). The vertical pressure range for O3 is from 147 to 0.5 hPa. The input source data used to create this merged product are contained in a separate data product with the short name GozSmlpO3.

The GozMmlpO3 merged data are distributed in netCDF4 format.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1979 to 2012*

---
### AQUA
#### Source : FedEO (CEDA-CCI)
> **Description** : The dataset provides a Climate Data Record of Sea Ice Concentration (SIC) for the polar regions, derived from medium resolution passive microwave satellite data from the Advanced Microwave Scanning Radiometer series (AMSR-E and AMSR-2). It is processed with an algorithm using coarse resolution (6 GHz and 37 GHz) imaging channels, and has been gridded at 50km grid spacing. This version of the product is v2.1, which is an extension of the version 2.0 Sea_Ice_cci dataset and has identical data until 2015-12-25.This product was generated in the context of the ESA Climate Change Initiative Programme (ESA CCI) by the Sea_Ice_CCI project. The EUMETSAT OSI SAF contributed with access and re-use of part of its processing software and facilities.A SIC CDR at 25km grid spacing is also available.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2002 to 2017*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This data set provides a fire progression map for year 2015 and measures of burn severity and vegetation community biophysical data collected from areas that were burned by wildfires in 2014 and 2015 in the Northwest Territories, Canada. Field data collected in 2016 include an estimate of burn severity, woody seedling/sprouting data, soil moisture, peat depth, thaw depth, and vegetation cover for selected sites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2015 to 2016*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2002 to 2016*

---
### Aura
#### Source : FedEO (CEDA-CCI)
> **Description** : This dataset contains Level 3 nadir profile ozone data from the ESA Ozone Climate Change Initiative (CCI) project. The Level 3 data are monthly averages on a regular 3D grid derived from level 2 ozone profiles. In this version 2 of the dataset, data are available for 1997 and 2007 and 2008 only, and use data from the GOME instrument on ERS (1997) and the GOME-2 instrument on METOP-A (2007, 2008).
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1997 to 2008*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This dataset is part of MEaSUREs 2012 Program, and represent Aqua/AIRS-Aura/MLS collocation indexes, in netCDF-4 format. These data map AIRS profile indexes to those of MLS.

The A-Train provides water vapor (H2O) retrievals from both the Atmospheric Infrared Sounder (AIRS) and Microwave Limb Sounder (MLS). While AIRS loses sensitivity to H2O at the elevated portions of the upper troposphere (UT), MLS cannot detect H2O below 316 hPa. Therefore, to obtain a full profile of H2O in the whole column of air, this dataset manages to join the two products together by utilizing their own averaging kernels (AK). In doing so, the dataset builds a solid H2O of the whole column of air, which will help understand the H2O budget and many processes governing the humidity around the upper troposphere and lower stratosphere (UTLS). 

The short name for this collections is AIRS_MLS_IND


> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2004 to present*

---
### CHAMP
#### Source : FedEO (NASA_CMR)
> **Description** : In Satellite Laser Ranging (SLR), a short pulse of coherent light generated by a laser (Light Amplification by Stimulated Emission of Radiation) is transmitted in a narrow beam to illuminate corner cube retroreflectors on the satellite. The return signal, typically a few photons, is collected by a telescope and the time-of-flight is measured. Using information about the satellite's orbit, the time-of-flight, and the speed of light, the location of the ranging station can be determined. Similar data acquired by another station, many kilometers distant from the first, or on a different continent, can be used to determine the distance between stations to precisions of centimeters or better. Repetitive measurements over months and years yield the change in distance, or the motion of the Earth's crust.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1976 to present*

---
### CloudSat
#### Source : FedEO (NASA_CMR)
> **Description** : This is AIRS-CloudSat collocated subset, in NetCDF 4 format. These data contain collocated: AIRS/AMSU retrievals at AMSU footprints, CloudSat radar reflectivities, and MODIS cloud mask. These data are created within the frames of the MEaSUREs project.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2006 to 2012*

---
### DMSP 5D-2/F10
#### Source : FedEO (NASA_CMR)
> **Description** : A gridded data set has been assembled over the BOREAS hydro-meteorological study region that combines a precipitation data set based on a rain gauge network with precipitation estimates based on SSM/I satellite images.  The result is an hourly precipitation data set covering 122 consecutive days beginning on June 1, 1996.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1996 to 1996*

---
### DMSP 5D-2/F11
#### Source : FedEO (NASA_CMR)
> **Description** : This sea ice concentration data set was derived using measurements from the Scanning Multichannel Microwave Radiometer (SMMR) on the Nimbus-7 satellite and from the Special Sensor Microwave/Imager (SSM/I) sensors on the Defense Meteorological Satellite Program's (DMSP) -F8, -F11, and -F13 satellites. Measurements from the Special Sensor Microwave Imager/Sounder (SSMIS) aboard DMSP-F17 are also included. The data set has been generated using the Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) Bootstrap Algorithm with daily varying tie-points. Daily (every other day prior to July 1987) and monthly data are available for both the north and south polar regions. Data are gridded on the SSM/I polar stereographic grid (25 x 25 km) and provided in two-byte integer format.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1978 to 2020*

---
### DMSP 5D-2/F12
#### Source : FedEO (NASA_CMR)
> **Description** : The OLS Digital Derived Lightning from DMSP F12 dataset consists of global lightning signatures from the Defense Meteorological Satellite Program (DMSP) Operational Linescan System (OLS) flown on DMSP 5D-2/F12 that have been analyzed from the visible channel imagery. These signatures show up as horizontal streaks on the images. The time and location of each of these streaks have been extracted and are stored by month in HDF data files. Data are available from May 1, 1995 through November 30, 1995.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1995 to 1995*

---
### DMSP 5D-2/F13
#### Source : FedEO (NASA_CMR)
> **Description** : This sea ice concentration data set was derived using measurements from the Scanning Multichannel Microwave Radiometer (SMMR) on the Nimbus-7 satellite and from the Special Sensor Microwave/Imager (SSM/I) sensors on the Defense Meteorological Satellite Program's (DMSP) -F8, -F11, and -F13 satellites. Measurements from the Special Sensor Microwave Imager/Sounder (SSMIS) aboard DMSP-F17 are also included. The data set has been generated using the Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) Bootstrap Algorithm with daily varying tie-points. Daily (every other day prior to July 1987) and monthly data are available for both the north and south polar regions. Data are gridded on the SSM/I polar stereographic grid (25 x 25 km) and provided in two-byte integer format.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1978 to 2020*

---
### DMSP 5D-2/F14
#### Source : FedEO (NASA_CMR)
> **Description** : This dataset is derived under the Cross-Calibrated Multi-Platform (CCMP) project and contains a value-added monthly mean ocean surface wind and pseudostress to approximate a satellite-only climatological data record. The CCMP datasets combine cross-calibrated satellite winds obtained from Remote Sensing Systems (REMSS) using a Variational Analysis Method (VAM) to produce a high-resolution (0.25 degree) gridded analysis. The CCMP data set includes cross-calibrated satellite winds derived from SSM/I, SSMIS, AMSR-E, TRMM TMI, QuikSCAT, SeaWinds, WindSat and other satellite instruments as they become available from REMSS. REMSS uses a cross-calibrated sea-surface emissivity model function which improves the consistency between wind speed retrievals from microwave radiometers (i.e., SSM/I, SSMIS, AMSR, TMI, WindSat) and those from scatterometers (i.e., QuikSCAT and SeaWinds). The VAM combines these data with in situ measurements and a starting estimate (first guess) of the wind field. The European Center for Medium-Range Weather Forecasts (ECMWF) ERA-40 Reanalysis is used as the first-guess from 1987 to 1998. The ECMWF Operational analysis is used from January 1999 onward. All wind observations and analysis fields are referenced to a height of 10 meters. The ERA-40 can be obtained from the Computation and Information Systems Laboratory (CISL) at the National Center for Atmospheric Research (NCAR): http://rda.ucar.edu/datasets/ds117.0/. The ECMWF Operational analysis can also be obtained from CISL at NCAR: http://rda.ucar.edu/datasets/ds111.1/. Three products are distributed to complete the CCMP dataset series. L3.0 product contains high-resolution analyses every 6-hours. These data are then time averaged over monthly and 5-day periods to derive the L3.5 product. Directions from the L3.0 product are then assigned to the time and location of the passive microwave satellite wind speed observations to derive the L2.5 product.  All datasets are distributed on a 0.25 degree cylindrical coordinate grid. This dataset is one in a series of First-Look (FLK) CCMP datasets and is a continuation and expansion of the SSM/I surface wind velocity project that began under the NASA Pathfinder Program. Refinements and upgrades to the FLK version will be incorporated under a new release (date to be determined) known as Late-look (LLK) and may include additional satellite datasets. All satellite surface wind data are obtained from REMSS under the DISCOVER project: Distributed Information Services: Climate/Ocean Products and Visualizations for Earth Research (http://www.discover-earth.org/index.html). The CCMP project is the result of an investigation funded by the NASA Making Earth Science data records for Use in Research Environments (MEaSUREs) program (http://community.eosdis.nasa.gov/measures/). In accordance with the MEaSUREs program, the CCMP datasets are also known as Earth System Data Records (ESDRs). In collaboration with private and government institutions, a team led by Dr. Robert Atlas (PI; proposal originally solicited by REASoN, and currently funded by MEaSURES) has created the CCMP project to provide multi-instrument ocean surface wind velocity ESDRs, with wide ranging research applications in meteorology and oceanography.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1987 to 2011*

---
### DMSP 5D-2/F8
#### Source : FedEO (NASA_CMR)
> **Description** : This sea ice concentration data set was derived using measurements from the Scanning Multichannel Microwave Radiometer (SMMR) on the Nimbus-7 satellite and from the Special Sensor Microwave/Imager (SSM/I) sensors on the Defense Meteorological Satellite Program's (DMSP) -F8, -F11, and -F13 satellites. Measurements from the Special Sensor Microwave Imager/Sounder (SSMIS) aboard DMSP-F17 are also included. The data set has been generated using the Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) Bootstrap Algorithm with daily varying tie-points. Daily (every other day prior to July 1987) and monthly data are available for both the north and south polar regions. Data are gridded on the SSM/I polar stereographic grid (25 x 25 km) and provided in two-byte integer format.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1978 to 2020*

---
### DMSP 5D-3/F15
#### Source : FedEO (NASA_CMR)
> **Description** : This dataset is derived under the Cross-Calibrated Multi-Platform (CCMP) project and contains a value-added monthly mean ocean surface wind and pseudostress to approximate a satellite-only climatological data record. The CCMP datasets combine cross-calibrated satellite winds obtained from Remote Sensing Systems (REMSS) using a Variational Analysis Method (VAM) to produce a high-resolution (0.25 degree) gridded analysis. The CCMP data set includes cross-calibrated satellite winds derived from SSM/I, SSMIS, AMSR-E, TRMM TMI, QuikSCAT, SeaWinds, WindSat and other satellite instruments as they become available from REMSS. REMSS uses a cross-calibrated sea-surface emissivity model function which improves the consistency between wind speed retrievals from microwave radiometers (i.e., SSM/I, SSMIS, AMSR, TMI, WindSat) and those from scatterometers (i.e., QuikSCAT and SeaWinds). The VAM combines these data with in situ measurements and a starting estimate (first guess) of the wind field. The European Center for Medium-Range Weather Forecasts (ECMWF) ERA-40 Reanalysis is used as the first-guess from 1987 to 1998. The ECMWF Operational analysis is used from January 1999 onward. All wind observations and analysis fields are referenced to a height of 10 meters. The ERA-40 can be obtained from the Computation and Information Systems Laboratory (CISL) at the National Center for Atmospheric Research (NCAR): http://rda.ucar.edu/datasets/ds117.0/. The ECMWF Operational analysis can also be obtained from CISL at NCAR: http://rda.ucar.edu/datasets/ds111.1/. Three products are distributed to complete the CCMP dataset series. L3.0 product contains high-resolution analyses every 6-hours. These data are then time averaged over monthly and 5-day periods to derive the L3.5 product. Directions from the L3.0 product are then assigned to the time and location of the passive microwave satellite wind speed observations to derive the L2.5 product.  All datasets are distributed on a 0.25 degree cylindrical coordinate grid. This dataset is one in a series of First-Look (FLK) CCMP datasets and is a continuation and expansion of the SSM/I surface wind velocity project that began under the NASA Pathfinder Program. Refinements and upgrades to the FLK version will be incorporated under a new release (date to be determined) known as Late-look (LLK) and may include additional satellite datasets. All satellite surface wind data are obtained from REMSS under the DISCOVER project: Distributed Information Services: Climate/Ocean Products and Visualizations for Earth Research (http://www.discover-earth.org/index.html). The CCMP project is the result of an investigation funded by the NASA Making Earth Science data records for Use in Research Environments (MEaSUREs) program (http://community.eosdis.nasa.gov/measures/). In accordance with the MEaSUREs program, the CCMP datasets are also known as Earth System Data Records (ESDRs). In collaboration with private and government institutions, a team led by Dr. Robert Atlas (PI; proposal originally solicited by REASoN, and currently funded by MEaSURES) has created the CCMP project to provide multi-instrument ocean surface wind velocity ESDRs, with wide ranging research applications in meteorology and oceanography.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1987 to 2011*

---
### DMSP 5D-3/F16
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Special Sensor Microwave Imager/Sounder (SSMIS) continues the legacy of passive microwave instruments carried aboard Defense Meteorological Satellite Program (DMSP) satellites. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : The GPM Ground Validation CARE Satellite Overpass GCPEx Images are the satellite overpass images for the GPM Cold-season Precipitation Experiment (GCPEx), which occurred in Ontario, Canada, January 15, 2012 through February 28, 2012. GCPEx addressed limitations in the GPM snowfall retrieval algorithm through the collection of microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. The satellite tracks include the DMSP satellite numbers 15, 16, 17, 18, and 19. A list of starting overpass times per satellite and day is included.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2012 to 2012*

---
### DMSP 5D-3/F17
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Special Sensor Microwave Imager/Sounder (SSMIS) continues the legacy of passive microwave instruments carried aboard Defense Meteorological Satellite Program (DMSP) satellites. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This sea ice concentration data set was derived using measurements from the Scanning Multichannel Microwave Radiometer (SMMR) on the Nimbus-7 satellite and from the Special Sensor Microwave/Imager (SSM/I) sensors on the Defense Meteorological Satellite Program's (DMSP) -F8, -F11, and -F13 satellites. Measurements from the Special Sensor Microwave Imager/Sounder (SSMIS) aboard DMSP-F17 are also included. The data set has been generated using the Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) Bootstrap Algorithm with daily varying tie-points. Daily (every other day prior to July 1987) and monthly data are available for both the north and south polar regions. Data are gridded on the SSM/I polar stereographic grid (25 x 25 km) and provided in two-byte integer format.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1978 to 2020*

---
### DMSP 5D-3/F18
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Special Sensor Microwave Imager/Sounder (SSMIS) continues the legacy of passive microwave instruments carried aboard Defense Meteorological Satellite Program (DMSP) satellites. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:Background:Reference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.Requirement:Initiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.Pseudo-Invariant Calibration Sites (PICS):Algeria 3 is one of six CEOS reference Pseudo-Invariant Calibration Sites (PICS) that are CEOS Reference Test Sites. Besides the nominally good site characteristics (temporal stability, uniformity, homogeneity, etc.), these six PICS were selected by also taking into account their heritage and the large number of datasets from multiple instruments that already existed in the EO archives and the long history of characterization performed over these sites. The PICS have high reflectance and are usually made up of sand dunes with climatologically low aerosol loading and practically no vegetation. Consequently, these PICS can be used to evaluate the long-term stability of instrument and facilitate inter-comparison of multiple instruments.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1972 to present*

---
### DMSP 5D-3/F19
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Special Sensor Microwave Imager/Sounder (SSMIS) continues the legacy of passive microwave instruments carried aboard Defense Meteorological Satellite Program (DMSP) satellites. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : The GPM Ground Validation CARE Satellite Overpass GCPEx Images are the satellite overpass images for the GPM Cold-season Precipitation Experiment (GCPEx), which occurred in Ontario, Canada, January 15, 2012 through February 28, 2012. GCPEx addressed limitations in the GPM snowfall retrieval algorithm through the collection of microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. The satellite tracks include the DMSP satellite numbers 15, 16, 17, 18, and 19. A list of starting overpass times per satellite and day is included.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2012 to 2012*

---
### ERS-2
#### Source : FedEO (CEDA-CCI)
> **Description** : As part of the European Space Agency's (ESA) Sea Level Climate Change Initiative (CCI) project, a number of oceanic indicators of mean sea level changes have been produced from merging satellite altimetry measurements of sea level anomalies. The oceanic indicators dataset consists of static files covering the whole altimeter period, describing the evolution of the project's monthly sea level anomaly gridded product (see separate dataset record).The oceanic indicators that are provided are: 1) the temporal evolution of the global Mean Sea Level (MSL) DOI: 10.5270/esa-sea_level_cci-IND_MSL_MERGED-1993_2015-v_2.0-201612 ;2) the geographic distribution of Mean Sea Level changes (MSLTR) DOI: 10.5270/esa-sea_level_cci-IND_MSLTR_MERGED-1993_2015-v_2.0-201612 ;3) Maps of the amplitude and phase of the annual cycle (MSLAMPH) DOI: 10.5270/esa-sea_level_cci-IND_MSLAMPH_MERGED-1993_2015-v_2.0-201612.The complete collection of v2.0 products from the Sea Level CCI project can be referenced using the following DOI: 10.5270/esa-sea_level_cci-1993_2015-v_2.0-201612.When using or referring to the SL_cci products, please mention the associated DOIs and also use the following citation where a detailed description of the SL_cci project and products can be found:Ablain, M., Cazenave, A., Larnicol, G., Balmaseda, M., Cipollini, P., FaugÃƒÂ¨re, Y., Fernandes, M. J., Henry, O., Johannessen, J. A., Knudsen, P., Andersen, O., Legeais, J., Meyssignac, B., Picot, N., Roca, M., Rudenko, S., Scharffenberg, M. G., Stammer, D., Timms, G., and Benveniste, J.: Improved sea level record over the satellite altimetry era (1993Ã¢&#128;&#147;2010) from the Climate Change Initiative project, Ocean Sci., 11, 67-82, doi:10.5194/os-11-67-2015, 2015.For further information on the Sea Level CCI products, and to register for these products please email: info-sealevel@esa-sealevel-cci.org
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1993 to 2015*

---
#### Source : FedEO (EOP)
> **Description** : This collection provides access to images archived at ROSCOSMOS for ERS-2 mission.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1995 to 2011*

---
#### Source : FedEO (IMM)
> **Description** : This ERS Medium Resolution strip-line product is generated from the Image Mode Level 0 Product. Strip-line image products contain image data for an entire segment, up to a maximum size of 10 minutes per product for IM mode. The processor concatenates together several sub-images called 'slices' that were processed separately on a dataset-by-dataset basis in order to form the entire strip-line image. The product is processed to an approximately 150 m x 150 m resolution and has a radiometric resolution that is good enough for ice applications. This product has a lower spatial resolution than the SAR_IMP_1P and SAR_IMS_1P products. The SAR IM L0 full mission data archive has been bulk processed to Level 1 (SAR_IMM_1P) in Envisat format with the PF-ERS processor version 6.01. Product Characteristics: - Pixel size: 5 m (ground range â€“ across track) x 75 m (azimuth â€“ along track) - Scene area: 100 km (range) x at least 102.5 km - Scene Size: 1300 pixels (range) x at least 1350 lines (azimuth) - Pixel depth: 16 bits unsigned integer - Total product volume: at least 3.5 MB - Projection: Ground-range - Number of looks: 8 (azimuth) x 7 (range)
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1991 to 2011*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This dataset contains absolute dynamic topography (similar to sea level but with respect to the geoid) binned and averaged monthly on 1 degree grids. The coverage is from October 1992 to December 2010. These data were provided by AVISO (French space agency data provider) to support the CMIP5 (Coupled Model Intercomparison Project Phase 5) under the World Climate Research Program (WCRP) and was first made available via the JPL Earth System Grid. The dynamic topography are derived from sea surface height measured by several satellites including Envisat, TOPEX/Poseidon, Jason-1 and OSTM/Jason-2, and referenced to the geoid. Along with this dataset, two additional ancillary data files are included in the same directory which contain the number of observations and standard error co-located on the same 1 degree grids.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1992 to present*

---
#### Source : FedEO (SAR)
> **Description** : This SAR Level 0 product is acquired in Image Mode. The products consist of the SAR telemetry data and are supplied as full Level 0 segments, unprocessed. It also contains all the required auxiliary data necessary for data processing. The product serves two main purposes: For testing ERS SAR processors independently from the HDDR system For users interested in full SAR data processing. Product characteristics: - Scene area: 100 km (range - across track) x full segment length (azimuth - along track) - Scene size: 5616 samples (range) x full segment length (azimuth) - Pixel depth: 10 bits signed integer (5 bits I, 5 bits Q) - Projection: Slant range
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1991 to 2011*

---
### Elektro-L-N1
#### Source : FedEO (EOP)
> **Description** : This collection provides access to products derived from the Geostationary Operational Meteorological Satellite Elektro-L N1 and archived at ROSCOSMOS.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2011 to present*

---
### GOES-5
#### Source : FedEO (NASA_CMR)
> **Description** : The ISCCP_B3_NAT data is the International Satellite Cloud Climatology Project (ISCCP) Stage B3 Reduced Radiances in Native Format data product. This is the original radiance data, sampled to 30 Km and 3-hour spacing. Data collection for this product is complete and was collected using several instruments on multiple platforms, please see the instrument and platform list of this record for a comprehensive list. The normalization of all radiances to a standard calibration made these data a globally uniform set of measurements that can be used for detailed cloud process studies.ISCCP was the first project of the World Climate Research Program (WCRP) and was established in 1982 (WMO-35 1982, Schiffer and Rossow 1983) to: produce a global, reduced resolution, calibrated and normalized radiance data set containing basic information on the properties of the atmosphere from which cloud parameters can be derived; stimulate and coordinate basic research on techniques for inferring the physical properties of clouds from the condensed radiance data set and to apply the resulting algorithms to derive and validate a global cloud climatology for improving the parameterization of clouds in climate models; and promote research using ISCCP data that contributes to improved understanding of the Earth's radiation budget and hydrological cycle. Since 1983 an international group of institutions has collected and analyzed satellite radiance measurements from up to five geostationary and two polar orbiting satellites to infer the global distribution of cloud properties and their diurnal, seasonal and inter-annual variations. The primary focus of the first phase of the project (1983-1995) was the elucidation of the role of clouds in the radiation budget (top of the atmosphere and surface). In the second phase of the project (1995 onwards) the analysis also concerns improving understanding of clouds in the global hydrological cycle. ISCCP analysis combined satellite-measured radiances (Stage B3 data, Schiffer and Rossow 1985), Rossow et al. 1987) with the TOVS atmospheric temperature-humidity and ice/snow correlative data sets to obtain information about clouds and the surface. The analysis method first determined the presence of absence of clouds in each individual image pixel and retrieves the radiometric properties of the cloud for each cloudy pixel and of the surface for each clear pixel. The pixel analysis is performed separately for each satellite radiance data set and the results reported in the Stage DX data product, which has a nominal resolution of 30 km and 3 hours. The Stage D1 product is produced by summarizing the pixel-level results every 3 hours on an equal-area map with 280 km resolution and merging the results from separate satellites with the atmospheric and ice/snow data sets to produce global coverage at each time. The Stage D2 data product is produced by averaging the Stage D1 data over each month, first at each of the eight three hour time intervals and then over all time intervals.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1983 to 2009*

---
### GOES-6
#### Source : FedEO (NASA_CMR)
> **Description** : The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.A subset of the ISCCP Stage DX Cloud Product (Revised Algorithm) are included for the FIRE Cirrus 1 region.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *October 1986*

---
### GOES-7
#### Source : FedEO (NASA_CMR)
> **Description** : The level-1 BOREAS GOES-7 image data were collected by Remote Sensing Science Team 14 (RSS-14) personnel at Florida State University (FSU) and delivered to BORIS. The data cover the period of 01-Jan-1994 through 08-Jul-1995, with partial to complete coverage on the majority of the days. The data include three bands with eight-bit pixel values.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1994 to 1995*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : Phase II and III gridded data sets have been generated by an objective analysis scheme using all of the surface meteorological station data over BOREAS region for 1994-1996. The meteorological variables in this data set are surface air pressure, air temperature, dew point temperature, wind speed, wind direction, precipitation, incoming solar (shortwave) radiation, and incoming infrared (longwave) radiation.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1994 to 1997*

---
### GOES-8
#### Source : FedEO (NASA_CMR)
> **Description** : The BOREAS RSS-14 team collected and processed several Level-1 GOES-7 and GOES-8 image data sets for 1994-1996, and GOES-7 Level-2 for 1994 over the BOREAS study region.  This data set contains shortwave and longwave radiation images at the surface and top of the atmosphere derived from collected GOES-8 data. These GOES-8 Level-2 data cover the period from 12-Feb-1996 to 22-Oct-1996.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1996 to 1996*

---
### GOES-9
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
### GOSAT
#### Source : FedEO (CEDA-CCI)
> **Description** : The Greenhouse Gases Observing Satellite, also known as Ibuki, is an Earth observation satellite and the world's first satellite dedicated to greenhouse gas monitoring. It measures the densities of carbon dioxide and methane from 56,000 locations on the Earth's atmosphere.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *unknown*

---
#### Source : FedEO (NASA_CMR)
> **Description** : Version 9r is the current version of the data set. Older versions will no longer be available and are superseded by Version 9r.
The ACOS Lite files contain bias-corrected XCO2 along with other select fields aggregated as daily files. Orbital granules of the ACOS Level 2 standard product (ACOS_L2S) are used as input.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2009 to present*

---
### GPM
#### Source : FedEO (JAXA_CATS-I)
> **Description** : The GPM Microwave Imager (GMI) instrument is a multichannel conical-scanning microwave radiometer and is characterized by thirteen microwave channels ranging in frequency from 10 GHz to 183 GHz.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : The Global Precipitation Measurement (GPM) satellite was launched on February 27th, 2014 with the GPM Microwave Imager (GMI) instrument on board. The GPM mission is a joint effort between NASA, the Japan Aerospace Exploration Agency (JAXA) and other international partners. In march 2005, NASA has chosen the Ball Aerospace and Technologies Corp., Boulder, Colorado to build the GMI instrument on the continued success of the Tropical Rainfall Measuring Mission (TRMM) satellite by expanding current coverage of precipitation from the tropics to the entire world. GMI is a dual-polarization, multi-channel, conical-scanning, passive microwave radiometer with frequent revisit times. One of the primary differences between GPM and other satellites with microwave radiometers is the orbit, which is inclined 65 degrees, allowing a full sampling of all local Earth times repeated approximately every 2 weeks. The GPM platform undergoes yaw maneuvers approximately every 40 days to compensate for the sun's changing position and prevent the side of the spacecraft facing the sun from overheating. Today, the GMI instrument plays an essential role in the worldwide measurement of precipitation and environmental forecasting. Sea Surface Temperature (SST) is one of its major products. The GMI data from the Remote Sensing System (REMSS) have been produced using an updated RTM, Version-8. The V8 brightness temperatures from GMI are slightly different from the V7 brightness temperatures; The SST datasets are available in near-real time (NRT) as they arrive, with a delay of about 3 to 6 hours, including the Daily, 3-Day, Weekly, and Monthly time series products.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
### GRACE
#### Source : FedEO (NASA_CMR)
> **Description** : This dataset contains absolute dynamic topography (similar to sea level but with respect to the geoid) binned and averaged monthly on 1 degree grids. The coverage is from October 1992 to December 2010. These data were provided by AVISO (French space agency data provider) to support the CMIP5 (Coupled Model Intercomparison Project Phase 5) under the World Climate Research Program (WCRP) and was first made available via the JPL Earth System Grid. The dynamic topography are derived from sea surface height measured by several satellites including Envisat, TOPEX/Poseidon, Jason-1 and OSTM/Jason-2, and referenced to the geoid. Along with this dataset, two additional ancillary data files are included in the same directory which contain the number of observations and standard error co-located on the same 1 degree grids.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1992 to present*

---
### METEOR-3M
#### Source : FedEO (EOP)
> **Description** : The Meteor-3M satellite mission is a joint partnership between NASA and the Russian Aviation and Space Agency (RASA).The payload includes SAGE III and other instruments. Measurements Taken: 1. temperature and humidity profiles 2. clouds, 3. surface properties 4. high energy particles in the upper atmosphere. Solar measurements are collected twice each orbit when the satellite ascends or descends from behind the Earth. (Source http://gcmdservices.gsfc.nasa.gov/static/kms/platforms/platforms.rdf).
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2001 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : In Satellite Laser Ranging (SLR), a short pulse of coherent light generated by a laser (Light Amplification by Stimulated Emission of Radiation) is transmitted in a narrow beam to illuminate corner cube retroreflectors on the satellite. The return signal, typically a few photons, is collected by a telescope and the time-of-flight is measured. Using information about the satellite's orbit, the time-of-flight, and the speed of light, the location of the ranging station can be determined. Similar data acquired by another station, many kilometers distant from the first, or on a different continent, can be used to determine the distance between stations to precisions of centimeters or better. Repetitive measurements over months and years yield the change in distance, or the motion of the Earth's crust.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1976 to present*

---
### MFG
#### Source : FedEO (EUM_DAT_MFG)
> **Description** : Image data in the form of high rate transmissions in 3 spectral channels available at 30-minute intervals with coverage over Europe, Africa, North Atlantic and parts of South America. Level 1.5 images are pre-processed in such a way that all image pixels are remapped on to a reference image corresponding to an image taken by the MTP satellite located at its nominal position over the equator and with a nominal attitude, i.e. with the satellite spin axis parallel to the spin axis of the earth. In addition, all image lines are aligned and the coordinates of image pixels of the different radiometer channels are adjusted so that they correspond to information from the same point on the earth's surface.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1981 to 2006*

---
### MSG
#### Source : FedEO (EUM_DAT_MSG)
> **Description** : The Multi-Sensor Precipitation Estimate (MPE) product consists of the near-real-time rain rates in mm/hr for each Meteosat image in original pixel resolution. The algorithm is based on the combination of polar orbiter microwave measurements and images in the Meteosat IR channel by a so-called blending technique. The MPE is most suitable for convective precipitation. Applications and Users: Operational weather forecasting in areas with poor or no radar coverage, especially in Africa and Asia. The polar-orbiter microwave measurement data are crucial for the generation of the MPE product and any unavailability of the data has a direct impact on the availability of the MPE product. The polar-orbiter microwave measure data are provided by an external data provider, and any liability that may arise due to delays or interruptions in the delivery of these data and consequently of the MPE product service cannot be attributed to EUMETSAT.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2009 to 2019*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This is the first release of the reprocessed SEVIRI All-Sky Radiances (ASR) product. The ASR product contains information on mean brightness temperatures (16x16 pixels so around 50km at nadir) from all thermal (e.g. infrared and water vapour) channels. It includes both clear and cloudy sky brightness temperatures. The ASR product also contains the fraction of clear sky and the solar zenith angle. The final ASR product is BUFR encoded 3-hourly at every third quarter of the hour (e.g. 00:45, 01:45 ...).Note that the reprocessing was done using the latest version of the EUMETSAT software (Version 1.5.3, 2013) ingesting  original level 1.5 SEVIRI images and the ECMWF ERA-interim as a  as a forecast input re-analysis data.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2004 to 2012*

---
### MTSAT-1R
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
### MTSAT-2
#### Source : FedEO (NASA_CMR)
> **Description** : On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:Background:Reference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.Requirement:Initiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.Pseudo-Invariant Calibration Sites (PICS):Algeria 3 is one of six CEOS reference Pseudo-Invariant Calibration Sites (PICS) that are CEOS Reference Test Sites. Besides the nominally good site characteristics (temporal stability, uniformity, homogeneity, etc.), these six PICS were selected by also taking into account their heritage and the large number of datasets from multiple instruments that already existed in the EO archives and the long history of characterization performed over these sites. The PICS have high reflectance and are usually made up of sand dunes with climatologically low aerosol loading and practically no vegetation. Consequently, these PICS can be used to evaluate the long-term stability of instrument and facilitate inter-comparison of multiple instruments.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1972 to present*

---
### Megha-Tropiques
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The SAPHIR instrument is a 6-channel passive microwave humidity sounder. Atmospheric humidity profiles can be obtained by measuring brightness temperatures in different channels situated close to the 183.31 GHz water vapour absorption line. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
### Meteosat-10
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
### Meteosat-11
#### Source : FedEO (NASA_CMR)
> **Description** : CER_GEO_Ed4_MET11_NH_V01.2 is the Satellite ClOud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Meteosat-11 over the Northern Hemisphere (NH) Version 1.2 data product. Data was collected using the Spinning Enhanced Visible and Infrared Imager (SEVIRI) Instrument on the Meteosat-11 platform. Data collection for this product is in progress. 

This data set is comprised of cloud micro-physical and radiation properties derived hourly from Meteosat-11 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms in support of the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged together to create hourly global cloud properties that are used to estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4-km resolution (at nadir) and are sub-sampled to 8 km.

CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2018 to present*

---
### Meteosat-2
#### Source : FedEO (NASA_CMR)
> **Description** : The ISCCP_B3_NAT data is the International Satellite Cloud Climatology Project (ISCCP) Stage B3 Reduced Radiances in Native Format data product. This is the original radiance data, sampled to 30 Km and 3-hour spacing. Data collection for this product is complete and was collected using several instruments on multiple platforms, please see the instrument and platform list of this record for a comprehensive list. The normalization of all radiances to a standard calibration made these data a globally uniform set of measurements that can be used for detailed cloud process studies.ISCCP was the first project of the World Climate Research Program (WCRP) and was established in 1982 (WMO-35 1982, Schiffer and Rossow 1983) to: produce a global, reduced resolution, calibrated and normalized radiance data set containing basic information on the properties of the atmosphere from which cloud parameters can be derived; stimulate and coordinate basic research on techniques for inferring the physical properties of clouds from the condensed radiance data set and to apply the resulting algorithms to derive and validate a global cloud climatology for improving the parameterization of clouds in climate models; and promote research using ISCCP data that contributes to improved understanding of the Earth's radiation budget and hydrological cycle. Since 1983 an international group of institutions has collected and analyzed satellite radiance measurements from up to five geostationary and two polar orbiting satellites to infer the global distribution of cloud properties and their diurnal, seasonal and inter-annual variations. The primary focus of the first phase of the project (1983-1995) was the elucidation of the role of clouds in the radiation budget (top of the atmosphere and surface). In the second phase of the project (1995 onwards) the analysis also concerns improving understanding of clouds in the global hydrological cycle. ISCCP analysis combined satellite-measured radiances (Stage B3 data, Schiffer and Rossow 1985), Rossow et al. 1987) with the TOVS atmospheric temperature-humidity and ice/snow correlative data sets to obtain information about clouds and the surface. The analysis method first determined the presence of absence of clouds in each individual image pixel and retrieves the radiometric properties of the cloud for each cloudy pixel and of the surface for each clear pixel. The pixel analysis is performed separately for each satellite radiance data set and the results reported in the Stage DX data product, which has a nominal resolution of 30 km and 3 hours. The Stage D1 product is produced by summarizing the pixel-level results every 3 hours on an equal-area map with 280 km resolution and merging the results from separate satellites with the atmospheric and ice/snow data sets to produce global coverage at each time. The Stage D2 data product is produced by averaging the Stage D1 data over each month, first at each of the eight three hour time intervals and then over all time intervals.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1983 to 2009*

---
### Meteosat-3
#### Source : FedEO (NASA_CMR)
> **Description** : First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre de Meteorologie Spatiale (CMS) Downward Longwave Flux Data in Native format (FIRE_AX_CMS_LWFLUX)
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1992 to 1992*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution clouddata.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.These files are calculations of the daily solar irradiance at the surface, based on observations by the METEOSAT. The file naming convention is: esqDDMMYYx.fis where DDMMYY is the dateThese files are: I2 pixels, 376 pixels/row, 326 rows. Each pixel has a spatial resolution of 0.04 degrees.The header of each file claims there are two channels, although the provided documentation states that there is only one channel per file.The units are: flux [tenths of Joule/cm^2]
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from June 1992 to Jully 1992*

---
### Meteosat-4
#### Source : FedEO (NASA_CMR)
> **Description** : First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre de Meteorologie Spatiale (CMS) Downward Longwave Flux Data in Native format (FIRE_AX_CMS_LWFLUX)
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1992 to 1992*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution clouddata.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.These files are calculations of the daily solar irradiance at the surface, based on observations by the METEOSAT. The file naming convention is: esqDDMMYYx.fis where DDMMYY is the dateThese files are: I2 pixels, 376 pixels/row, 326 rows. Each pixel has a spatial resolution of 0.04 degrees.The header of each file claims there are two channels, although the provided documentation states that there is only one channel per file.The units are: flux [tenths of Joule/cm^2]
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from June 1992 to Jully 1992*

---
### Meteosat-5
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution clouddata.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.These files are calculations of the daily solar irradiance at the surface, based on observations by the METEOSAT. The file naming convention is: esqDDMMYYx.fis where DDMMYY is the dateThese files are: I2 pixels, 376 pixels/row, 326 rows. Each pixel has a spatial resolution of 0.04 degrees.The header of each file claims there are two channels, although the provided documentation states that there is only one channel per file.The units are: flux [tenths of Joule/cm^2]
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from June 1992 to Jully 1992*

---
### Meteosat-6
#### Source : FedEO (NASA_CMR)
> **Description** : The GPM Ground Validation Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks Cloud Classification System (PERSIANN-CCS) IFloodS dataset is a subset from the global 30-minute PERSIANN-CCS files generated in near-real time selected for the time period of the GPM Ground Validation Iowa Flood Studies (IFloodS) field campaign. The main goal of IFloodS were to collect detailed measurements of precipitation at the Earthâ€™s surface using ground instruments and advanced weather radars and to simultaneously collect data from satellites passing overhead. This PERSIANN-CCS data product is available in ASCII and netCDF-4 formats from April 1, 2013 thru July 1, 2013. 
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2013 to 2013*

---
### Meteosat-7
#### Source : FedEO (NASA_CMR)
> **Description** : On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:Background:Reference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.Requirement:Initiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.Pseudo-Invariant Calibration Sites (PICS):Algeria 3 is one of six CEOS reference Pseudo-Invariant Calibration Sites (PICS) that are CEOS Reference Test Sites. Besides the nominally good site characteristics (temporal stability, uniformity, homogeneity, etc.), these six PICS were selected by also taking into account their heritage and the large number of datasets from multiple instruments that already existed in the EO archives and the long history of characterization performed over these sites. The PICS have high reflectance and are usually made up of sand dunes with climatologically low aerosol loading and practically no vegetation. Consequently, these PICS can be used to evaluate the long-term stability of instrument and facilitate inter-comparison of multiple instruments.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1972 to present*

---
### Meteosat-8
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
### Meteosat-9
#### Source : FedEO (NASA_CMR)
> **Description** : CER_ISCCP-D2like-GEO_DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-D2like Format Daytime Edition3A data product. Data collection for this product is complete. The Monthly Gridded Cloud Averages (ISCCP-D2like-GEO) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean geostationary satellite (GEO) cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The ISCCP-D2like-GEO product is a 5-satellite, daytime 3-hourly GMT, 8-km nominal resolution, geostationary-only cloud product limited to . The ISCCP-D2like-GEO is a daytime-only product, where the cloud retrievals incorporate only the visible and IR channels common to all geostationary satellites for spatial consistency. Each ISCCP-D2like file covers a single month.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2000 to 2017*

---
### Metop-A
#### Source : FedEO (95c6d610-ba36-11de-8a39-0800200c9a66)
> **Description** : The 'ENDVI10' or EUMETSAT Polar System NDVI are near-global, 10-daily composite images which are synthesised from the 'best available' observations registered in the course of every 'dekad' by the orbiting earth observation system METOP-AVHRR. The product provides the Normalized Difference Vegetation Index (NDVI), togetehr with some ancillary data as the radiation reflectance bands. The European METOP satellites were conceived by ESA/EUMETSAT to complement the geostationary METEOSATs. In this way they are analogue to the North-American NOAA-platforms which accompagny the geostationaries GOES-East and -West. Since mid-2007, METOP thus occupies the 'morning orbit' while NOAA assumes the 'noon orbit': the local solar time of the overpasses is around 9h30' for METOP and 14h for NOAA. Both platforms carry the same AVHRR instrument which scans the full earth surface at 1km resolution in five spectral bands: RED, NIR, SWIR, TIR1, TIR2. (During the night the SWIR-band is switched to MIR, but the ENDVI10 only deal with daytime registrations). Compared to NOAA, the METOP-AVHRR has been enhanced in three ways: the platform is perfectly stabilised which guarantees an optimal geo-correction of the imagery, all registered 1km data are stored on board and chanelled via the antenna of Svalbard (Sweden) to the central processing centre of EUMETSAT (Germany), and the latter performs the most crucial enhancement steps (rectification, calibration, cloud/snow detection) and broadcasts the results in real-time via its EUMETcast system.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2007 to 2020*

---
#### Source : FedEO (CEDA-CCI)
> **Description** : The ESA Sea Surface Temperature Climate Change Initiative (ESA SST CCI) dataset accurately maps the surface temperature of the global oceans over the period 1991 to 2010, using observations from many satellites. The data provides an independently quantified SST to a quality suitable for climate research.The ESA SST CCI Analysis Long Term Product consists of daily, spatially complete fields of sea surface temperature (SST), obtained by combining the orbit data from the AVHRR and ATSR ESA SST CCI Long Term Products, using optimal interpolation to provide SSTs where there were no measurements. These data cover the period between 09/1991 and 12/2010.The Version 1.1 data is an update of the Version 1.0 dataset.Version 1.0 of this dataset is cited in: Merchant, C. J., Embury, O., Roberts-Jones, J., Fiedler, E., Bulgin, C. E., Corlett, G. K., Good, S., McLaren, A., Rayner, N., Morak-Bozzo, S. and Donlon, C. (2014), Sea surface temperature datasets for climate applications from Phase 1 of the European Space Agency Climate Change Initiative (SST CCI). Geoscience Data Journal. doi: 10.1002/gdj3.20
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1991 to 2010*

---
#### Source : FedEO (EUM_DAT_METOP)
> **Description** : The Soil Moisture (SM) product is derived from the Advanced SCATterometer (ASCAT) backscatter observations and given in swath orbit geometry (12.5 km sampling). This SM product provides an estimate of the water content of the 0-5 cm topsoil layer, expressed in degree of saturation between 0 and 100 [%]. The algorithm used to derive this parameter is based on a linear relationship of SM and scatterometer backscatter and uses change detection techniques to eliminate the contributions of vegetation, land cover and surface topography, considered invariant from year to year. Seasonal vegetation effects are modelled by exploiting the multi-angle viewing capabilities of ASCAT. The SM processor has been developed by Vienna University of Technology (TU Wien). Note that some of the data are reprocessed. Please refer to the associated product validation reports or product release notes for further information.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2007 to present*

---
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Microwave Humidity Sounder (MHS) is a five-channel passive microwave radiometer, with channels from 89 to 190 GHz. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : CNR MED Sea Surface Temperature provides daily gap-free maps (L4) at 0.0625 deg. x 0.0625 deg. horizontal resolution over the Black Sea. The data are obtained from infra-red measurements collected by satellite radiometers and statistical interpolation. It is the CMEMS sea surface temperature nominal operational product for the Black sea.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2007 to present*

---
### Metop-B
#### Source : FedEO (95c6d610-ba36-11de-8a39-0800200c9a66)
> **Description** : The 'ENDVI10' or EUMETSAT Polar System NDVI are near-global, 10-daily composite images which are synthesised from the 'best available' observations registered in the course of every 'dekad' by the orbiting earth observation system METOP-AVHRR. The product provides the Normalized Difference Vegetation Index (NDVI), togetehr with some ancillary data as the radiation reflectance bands. The European METOP satellites were conceived by ESA/EUMETSAT to complement the geostationary METEOSATs. In this way they are analogue to the North-American NOAA-platforms which accompagny the geostationaries GOES-East and -West. Since mid-2007, METOP thus occupies the 'morning orbit' while NOAA assumes the 'noon orbit': the local solar time of the overpasses is around 9h30' for METOP and 14h for NOAA. Both platforms carry the same AVHRR instrument which scans the full earth surface at 1km resolution in five spectral bands: RED, NIR, SWIR, TIR1, TIR2. (During the night the SWIR-band is switched to MIR, but the ENDVI10 only deal with daytime registrations). Compared to NOAA, the METOP-AVHRR has been enhanced in three ways: the platform is perfectly stabilised which guarantees an optimal geo-correction of the imagery, all registered 1km data are stored on board and chanelled via the antenna of Svalbard (Sweden) to the central processing centre of EUMETSAT (Germany), and the latter performs the most crucial enhancement steps (rectification, calibration, cloud/snow detection) and broadcasts the results in real-time via its EUMETcast system.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2007 to 2020*

---
#### Source : FedEO (CEDA-CCI)
> **Description** : The ESA Sea Surface Temperature Climate Change Initiative (ESA SST CCI) dataset accurately maps the surface temperature of the global oceans over the period 1991 to 2010, using observations from many satellites. The data provides an independently quantified SST to a quality suitable for climate research.The ESA SST CCI Analysis Long Term Product consists of daily, spatially complete fields of sea surface temperature (SST), obtained by combining the orbit data from the AVHRR and ATSR ESA SST CCI Long Term Products, using optimal interpolation to provide SSTs where there were no measurements. These data cover the period between 09/1991 and 12/2010.The Version 1.1 data is an update of the Version 1.0 dataset.Version 1.0 of this dataset is cited in: Merchant, C. J., Embury, O., Roberts-Jones, J., Fiedler, E., Bulgin, C. E., Corlett, G. K., Good, S., McLaren, A., Rayner, N., Morak-Bozzo, S. and Donlon, C. (2014), Sea surface temperature datasets for climate applications from Phase 1 of the European Space Agency Climate Change Initiative (SST CCI). Geoscience Data Journal. doi: 10.1002/gdj3.20
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1991 to 2010*

---
#### Source : FedEO (EUM_DAT_METOP)
> **Description** : The Soil Moisture (SM) product is derived from the Advanced SCATterometer (ASCAT) backscatter observations and given in swath orbit geometry (12.5 km sampling). This SM product provides an estimate of the water content of the 0-5 cm topsoil layer, expressed in degree of saturation between 0 and 100 [%]. The algorithm used to derive this parameter is based on a linear relationship of SM and scatterometer backscatter and uses change detection techniques to eliminate the contributions of vegetation, land cover and surface topography, considered invariant from year to year. Seasonal vegetation effects are modelled by exploiting the multi-angle viewing capabilities of ASCAT. The SM processor has been developed by Vienna University of Technology (TU Wien). Note that some of the data are reprocessed. Please refer to the associated product validation reports or product release notes for further information.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2007 to present*

---
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. The Microwave Humidity Sounder (MHS) is a five-channel passive microwave radiometer, with channels from 89 to 190 GHz. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : This data set provides 3-hourly estimates of gross ecosystem CO2 exchange (GEE) and respiration (autotrophic and heterotrophic) for the state of Alaska from 2012 to 2014. The data were generated using the Polar Vegetation Photosynthesis and Respiration Model (PolarVPRM) and are provided at ~ 1 km2 [1/4-degree (longitude) by 1/6-degree (latitude)] pixel resolution. The PolarVPRM produces high-frequency estimates of GEE of CO2 for North American biomes from remotely-sensed data sets. For Alaska, the model used meteorological inputs from the North American regional re-analysis (NARR) and inputs of fractional snow cover and land surface water index (LSWI) from the Moderate Resolution Imaging Spectroradiometer (MODIS). Land surface greenness was factored into the model from three sources: 1) Enhanced Vegetation Index (EVI) from MODIS; 2) Solar Induced Florescence (SIF) from the Orbiting Carbon Observatory 2 (OCO-2); and 3) SIF from the Global Ozone Monitoring Experiment 2 (GOME-2). Three independent estimates of GEE are included in the data set, one for each source of greenness observations.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2012 to 2014*

---
### Metop-C
#### Source : FedEO (NASA_CMR)
> **Description** : A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P data set containing multi-channel Sea Surface Temperature (SST) retrievals derived in real-time from the Advanced Very High Resolution Radiometer (AVHRR) level-1B data from the Meteorological Operational-C (MetOp-C) satellite. The SST data in this data set are used operationally in oceanographic analyses and forecasts by the US Naval Oceanographic Office (NAVO). The MetOp satellite program is a European multi-satellite program to provide weather data services for monitoring climate and improving weather forecasts. MetOp-A, MetOp-B and Metop-C were respectively launched on 19 Oct 2006, 17 September 2012 and 7 November 2018. The program was jointly established by the European Space Agency (ESA) and the European Organization for the Exploitation of Meteorological Satellites (EUMETSAT) with the US National Oceanic and Atmospheric Administration (NOAA) contributing the AVHRR sensor. AVHRR instruments measure the radiance of the Earth in 5 (or 6) relatively wide spectral bands. The first two are centered around the red (0.6 micron) and near-infrared (0.9 micron) regions, the third one is located around 4 (3.6) micron, and the last two sample the emitted thermal radiation, around 11 and 12 micron, respectively. The legacy 5 band instrument is known as AVHRR/2 while the more recent version, the AVHRR/3 (first carried on the NOAA-15 platform), acquires data in a 6th channel located at 1.6 micron. Typically, the 11 and 12 micron channels are used to derive SST sometimes in combination with the 3.5 micron channel. The swath of the AVHRR sensor is a relatively large 2400 km. All MetOp platforms are sun synchronous and generally view the same earth location twice a day (latitude dependent). The ground native resolution of the AVHRR instruments is approximately 1.1 km at nadir and degrades off nadir. This particular data set is produced from legacy Global Area Coverage (GAC) data that are derived from a sample averaging of the full resolution global AVHRR data. Four out of every five samples along the scan line are used to compute on average value and the data from only every third scan line are processed, yielding an effective 4 km spatial resolution at nadir. The v2.0 is the updated version from current v1.0 with extensive algorithm improvements and upgrades. The major improvements include: 1) Significant changes in contaminant/cloud detection; 2) Increased the spatial resolution from 9 km to 4 km; 3) Updated compliance with GDS2, ACDD 1.3, and CF 1.6; and 4) Removed the dependency on the High-resolution Infrared Radiation Sounder (HIRS) sensor (only available to MetOp-A/B), thus allowing for the consistent inter-calibration and the processing of MetOp-A/B/C data
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2020 to present*

---
### SCISAT-1
#### Source : FedEO (CEDA-CCI)
> **Description** : This dataset comprises gridded limb ozone monthly zonal mean profiles from the ACE FTS instrument on the SCISAT satellite. The data are zonal mean time series (10Ã‚Â° latitude bin) and include uncertainty/variability of the Monthly Zonal Mean.The monthly zonal mean (MZM) data set provides ozone profiles averaged in 10Ã‚Â° latitude zones from 90Ã‚Â°S to 90Ã‚Â°N, for each month. The monthly zonal mean data are structured into yearly netcdf files, for each instrument separately. The filename indicates the instrument and the year. For example, the file Ã¢&#128;&#156;ESACCI-OZONE-L3-LP-ACE_FTS_SCISAT-MZM-2008-fv0001.ncÃ¢&#128;&#157; contains monthly zonal mean data for ACE in 2008.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2004 to 2010*

---
### SMOS
#### Source : FedEO (NASA_CMR)
> **Description** : The Level 2 ECMWF SMOS Auxiliary data product, openly available to all users, contains ECMWF data on the ISEA 4-9 DGG corresponding to SMOS half-orbit. It is used by both the ocean salinity and soil moisture operational processors to store the geophysical parameters from ECMWF forecasts. Access to other SMOS Level 1 and Level 2 'dynamic' and 'static' auxiliary datasets is restricted to Cal/Val users. The detailed content of the SMOS Auxiliary Data Files (ADF) is described in the Products Specification documents available in the Resources section below.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2010 to present*

---
#### Source : FedEO (SMOS)
> **Description** : Level 1 SMOS data products are designed for scientific and operational users who need to work with calibrated MIRAS instrument measurements, while Level 2 SMOS data products are designed for scientific and operational users who need to work with geo-located soil moisture and sea surface salinity estimation as retrieved from Level 1 dataset. Products from the operational pipeline in the SMOS Data Processing Ground Segment (DPGS) https://earth.esa.int/eogateway/missions/smos/description, located at the European Space Astronomy Centre (ESAC), have File Class ''OPER'', while reprocessed data is tagged as ''REPR''. For an optimal exploitation of the current SMOS L1 and L2 data set please consult the read-me-first notes. The Level 1A product comprises all calibrated visibilities between receivers (i.e. the interferometric measurements from the sensor including the redundant visibilities), combined per integration time of 1.2s (snapshot). The snapshots are consolidated in a pole-to-pole product file (50 minutes of sensing time) with a maximum size of about 215MB per half orbit (29 half orbits per day). The Level 1B product comprises the result of the image reconstruction algorithm applied to the L1A data. As a result, the reconstructed image at L1B is simply the difference between the sensed scene by the sensor and the artificial scene. The brightness temperature image is available in its Fourier component in the antenna polarisation reference frame top of the atmosphere. Images are combined per integration time of 1.2 seconds (snapshot). The removal of foreign sources (Galactic, Direct Sun, Moon) is also included in the reconstruction. Snapshot consolidation is as per L1A, with a maximum product size of about 115MB per half orbit. ESA provides the Artificial Scene Library (ASL) to add the artificial scene in L1B for any user that wants to start from L1B products and derive the sensed scene. The Level 1C product contains multi-angular brightness temperatures in antenna frame (X-pol, Y-pol, T3 and T4) at the top of the atmosphere, geo-located in an equal-area grid system (ISEA 4H9 - Icosahedral Snyder Equal Area projection). Two L1C products are available: Land for soil moisture retrieval and Sea for sea surface salinity retrieval. The pixels are consolidated in a pole-to-pole product file (50 minutes of sensing time), with a maximum size of about 350MB per half orbit (29 half orbits per day). Spatial resolution is in the range of 30-50 km. For each L1C product there is also a corresponding Browse product containing brightness temperatures interpolated for an incidence angle of 42.5Â°. The Level 2 Soil Moisture (SM) product comprises soil moisture measurements geo-located in an equal-area grid system ISEA 4H9. The product contains not only the retrieved soil moisture, but also a series of ancillary data derived from the processing (nadir optical thickness, surface temperature, roughness parameter, dielectric constant and brightness temperature retrieved at top of atmosphere and on the surface) with the corresponding uncertainties. The pixels are consolidated in a pole-to-pole product file (50 minutes of sensing time), with a maximum size of about 7MB (25MB uncompressed data) per half orbit (29 half orbits per day). The Level 2 Ocean Salinity (OS) product comprises sea surface salinity measurements geo-located in an equal-area grid system ISEA 4H9. The product contains one single swath-based sea surface salinity retrieved with and without Land-Sea contamination correction, SSS anomaly based on WOA-2009 referred to Land-Sea corrected sea surface salinity, brightness temperature at the top of the atmosphere and at the sea surface with their corresponding uncertainties. The pixels are consolidated in a pole-to-pole product file (50 minutes of sensing time), with a maximum size of about 10MB (25MB uncompressed data) per half orbit (29 half orbits per day). The following Science data products, belonging to the latest processing baseline, are openly available to all users: MIR_SC_F1B/MIR_SC_D1B: Level 1B product, FULL/DUAL polarisation mode, in Earth Explorer format MIR_SCLF1C/MIR_SCLD1C: Level 1C product over Land, FULL/DUAL polarisation mode, in Earth Explorer format MIR_SCSF1C/MIR_SCSD1C: Level 1C product over Sea, FULL/DUAL polarisation mode, in Earth Explorer format MIR_BWLF1C/MIR_BWLD1C: Level 1C Browse product over Land, FULL/DUAL polarisation mode, in Earth Explorer format MIR_BWSF1C/MIR_BWSD1C: Level 1C Browse product over Sea, FULL/DUAL polarisation mode, in Earth Explorer format MIR_SMUDP2: Level 2 Soil Moisture product, in Earth Explorer and NetCDF format MIR_OSUDP2: Level 2 Sea Surface Salinity product, in Earth Explorer and NetCDF format Access to the following Science data products is restricted to SMOS CalVal users: MIR_SC_F1A/MIR_SC_D1A: Level 1A product, FULL/DUAL polarisation mode, in Earth Explorer format. For an optimal exploitation of the current SMOS L1 and L2 data set please consult the read-me-first notes available in the Resources section below.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2010 to present*

---
#### Source : FedEO (no_named_collections_set_1)
> **Description** : The SMOS Level 3 Sea Ice Thickness product, in NetCDf format, provides daily estimations of SMOS-retrieved sea ice thickness (and its uncertainty) at the edge of the Arctic Ocean during the October-April (winter) season, from year 2010 onwards. The sea ice thickness is retrieved from the SMOS L1C product, up to a depth of approximately 0.5-1 m, depending on the ice temperature and salinity. Daily maps, projected on polar stereographic grid of 12.5 km, are generated by the Alfred Wegener Institut (AWI). This product is complementary with sea ice thickness measurements from ESA's CryoSat and Copernicus Sentinel-3 missions.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2010 to present*

---
### SMS-1
#### Source : FedEO (NASA_CMR)
> **Description** : VISSRSMS1L1AOIPS is the Visible Infrared Spin-Scan Radiometer (VISSR) Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) data product from the first Synchronous Meteorological Satellite (SMS-1). There are typically three data files for a scene of the Earth with radiances that were measured in the visible (0.55 to 0.70 micrometer) and/or IR (10.5 to 12.6 micrometer) wavelengths with a spatial resolution of 0.9 and 8 km, respectively. Files also include time, geolocation, orbit, attitude, and telemetry information. There are three types of data files in this product: one contains IR data, one contains the IR grid information (blank before 1974/10/29), and another contains VIS data. Each data file is structured with an AOIPS label, followed by an IPD label, and then an optional 8 telemetry records followed by a set of data records. Visible data are typically 3904 pixels by either 4000 or 2000 scan lines (5 or 2.5 minute scenes respectively). IR data are typically 976 pixels by either 500 or 250 scan lines (5 or 2.5 minute scenes respectively). A full scan of the Earth was made every 20 minutes.

The data were used to make 70mm film negatives and 9.5â€� positive prints on a Dicomed Image Recording System. Data for this product are available from 1974/07/01 through 1979/04/19 (with gaps plus no data between 1975/08/20 and 1979/02/17). The SMS-1 satellite was initially parked over the equator at longitude 45W on June 7, 1974 viewing the hemisphere below the satellite to support the GARP Atlantic Tropical Experiment (GATE). It was moved to its operational position at 75W on Nov 15, 1974 where it remained until GOES-1 was launched, after which SMS 1 was moved to 105W and placed in stand-by-mode as a backup to GOES-1 or SMS-2. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.

This product was previously available from the NSSDC with the identifier ESAD-00018 (old ID 74-033A-01D).
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1974 to 1979*

---
### SMS-2
#### Source : FedEO (NASA_CMR)
> **Description** : VISSRSMS2L1AOIPS is the Visible Infrared Spin-Scan Radiometer (VISSR) Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) data product from the second Synchronous Meteorological Satellite (SMS-2). There are typically three data files for a scene of the Earth with radiances that were measured in the visible (0.55 to 0.70 micrometer) and/or IR (10.5 to 12.6 micrometer) wavelengths with a spatial resolution of 0.9 and 8 km, respectively. Files also include time, geolocation, orbit, attitude, and telemetry information. There are three types of data files in this product: one contains IR data, one contains the IR grid information, and another contains VIS data. Each data file is structured with an AOIPS label, followed by an IPD label, and then an optional 8 telemetry records followed by a set of data records. Visible data are typically 3904 pixels by either 4000 or 2000 scan lines (5 or 2.5 minute scenes respectively). IR data are typically 976 pixels by either 500 or 250 scan lines (5 or 2.5 minute scenes respectively). A full scan of the Earth was made every 20 minutes.

The data were used to make 70mm film negatives and 9.5â€� positive prints on a Dicomed Image Recording System. Data for this product are available from 1975/04/27 through 1980/08/22 (with gaps plus no data between 1975/07/31 and 1979/05/10). The SMS-2 satellite was initially parked over the equator at longitude 105W on Feb 22, 1975 viewing the hemisphere below the satellite. It was moved to its final operational position at 135W on Dec 19, 1975. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.

This product was previously available from the NSSDC with the identifier ESAD-00095 (old ID 75-011A-04D).
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1975 to 1980*

---
### SUOMI-NPP
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Calibrated brightness temperatures product for passive-microwave instrument. ATMS is the Advanced Technology Microwave Sounder. A constellation of several satellites developed by each international partner (space agency) will carry passive microwave radiometers and/or microwave sounders and be in operation around 2013. The DPR and GMI instruments on board the core satellite will serve as a calibrator for data obtained by constellation satellites.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2014 to present*

---
#### Source : FedEO (NASA_CMR)
> **Description** : The 2015 Urban Extents from VIIRS and MODIS for the Continental U.S. Using Machine Learning Methods data set models urban settlements in the Continental United States (CONUS) as of 2015. When applied to the combination of daytime spectral and nighttime lights satellite data, the machine learning methods achieved high accuracy at an intermediate-resolution of 500 meters at large spatial scales. The input data for these models were two types of satellite imagery: Visible Infrared Imaging Radiometer Suite (VIIRS) Nighttime Light (NTL) data from the Day/Night Band (DNB), and Moderate Resolution Imaging Spectroradiometer (MODIS) corrected daytime Normalized Difference Vegetation Index (NDVI). Although several machine learning methods were evaluated, including Random Forest (RF), Gradient Boosting Machine (GBM), Neural Network (NN), and the Ensemble of RF, GBM, and NN (ESB), the highest accuracy results were achieved with NN, and those results were used to delineate the urban extents in this data set.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2015 to 2015*

---
#### Source : FedEO (NASA_CWIC)
> **Description** : CER_ES4_NPP-FM5_Edition1-CV is the Clouds and the Earth's Radiant Energy System (CERES) Earth Radiation Budget Experiment (ERBE)-like Monthly Geographical Averages Suomi National Polar-orbiting Partnership (NPP) Flight Model 5 (FM5) Edition1-CV data product. Data for this product is collected by CERES FM-5 on Suomi-NPP. Data collection for this data product is ongoing.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 2012 to present*

---
### TRMM
#### Source : FedEO (JAXA_CATS-I)
> **Description** : Monthly Oceanic Rainfall, which is monthly accumulated rainfall on 5deg x 5deg grid.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1997 to 2015*

---
#### Source : FedEO (NASA_CMR)
> **Description** : CER_BDS_TRMM-PFM_Edition1 is the Clouds and the Earth's Radiant Energy System (CERES) BiDirectional Scans (BDS) Tropical Rainfall Measuring Mission (TRMM) Edition 1 data product. Data collection for this product is complete. CER_BDS_TRMM-PFM_Edition1 data are CERES geolocated and calibrated Top-of-Atmosphere (TOA) filtered radiances and other instrument data. Each CERES BDS data product contains twenty-four hours of Level-1B data for each CERES scanner instrument mounted on each spacecraft. The BDS includes samples taken in normal and short Earth scan elevation profiles in both fixed and rotating azimuth scan modes (including space, internal calibration, and solar calibration views). BDS contains Level-0 raw (unconverted) science and instrument data as well as the geolocated converted science and instrument data. Further, BDS contains additional data not found in the Level-0 input file, including converted satellite position and velocity data, celestial data, converted digital status data, and parameters used in the radiance count conversion equations. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the TRMM. Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1997 to 2000*

---
### UARS
#### Source : FedEO (NASA_CMR)
> **Description** : ACRIMII_TSI_UARS_NAT data are Active Cavity Radiometer Irradiance Monitor II (ACRIM II) Total Solar Irradiance (TSI) aboard the Upper Atmosphere Research Satellite (UARS) Data in Native (NAT) format.The ACRIMII_TSI_UARS_NAT data product consists of the Level 2 total solar irradiance in the form of daily means gathered by the ACRIM II instrument on the UARS satellite. The daily means are constructed from the shutter cycle results for each day. This data set is considered Version 2.
> **Spatial coverage** : *Global*
> **Temporal coverage** : *from 1991 to 2001*

---

# UCL & uAlberta: Overflow Topics for Future Consideration

This document captures topics from UCL's GEOG0111 Scientific Computing and uAlberta's engineering/computing programs that are *not* included in the immediate restructuring but are candidates for future volumes or companion materials.

## From UCL GEOG0111 (Scientific Computing Module)

### Advanced Image Analysis for Remote Sensing
- Deep specialization in image-based computation
- Algorithms for spectral analysis
- Optimization techniques for classification
- Could become Vol II companion or specialized topic library chapter

### Environmental Modelling (Advanced)
- Coupling multiple processes
- Sensitivity analysis
- Parameter estimation
- Could anchor Vol II.B (forecasting with ensembles)

### Scientific Visualization
- Advanced plotting techniques
- Interactive visualization libraries (Plotly, Bokeh, HoloViews)
- Communicating uncertainty through visualization
- Could be Vol II.A/B reference material or Methods Reference companion

### High-Performance Computing for Geospatial Data
- Vectorized operations (NumPy, xarray)
- Parallel processing (Dask, multiprocessing)
- GPU acceleration for image processing
- Likely Vol III or advanced topic library

## From uAlberta Engineering Programs

### Algorithm Design & Analysis
- Big-O notation, complexity analysis
- Common algorithms for geospatial/computational problems
- Data structures (lists, dicts, trees, graphs)
- Could be Methods Reference or Vol II foundational reading

### Linux System Administration Basics
- Users, permissions (chmod, chown)
- Processes and job management
- File systems and storage
- Useful for operational forecasting workflows (Vol II.B)

### Software Engineering Practices
- Testing (unit tests, integration tests)
- Documentation standards
- Code review workflows
- Refactoring and code quality
- Would fit well in Methods Reference or as advanced Vol II material

### Procedural Programming Depth
- Functions and modularity
- Object-oriented programming (classes, inheritance)
- Functional programming concepts
- Needed for Vol II applications but beyond Scientific Computing Foundations scope

## General Scientific Computing (Cross-Source)

### Numerical Methods
- Integration, differentiation, solving ODEs/PDEs
- Root finding, optimization
- Interpolation and regression
- Core to Vol II.A (validation) and Vol II.B (forecasting)

### Data Formats & I/O
- NetCDF, HDF5 (for earth science data)
- GeoTIFF, COG (for satellite imagery)
- CSV, JSON for metadata
- Reference material for Pathway A/B

### Debugging & Profiling
- Using debuggers (pdb, IDE debuggers)
- Profiling code for performance
- Finding and fixing bugs systematically
- Methods Reference material

### Documentation & Literate Programming
- Docstrings, type hints
- Jupyter notebooks as communication medium
- Markdown for technical writing
- Could enhance Scientific Computing Foundations

### Working with APIs & Data Services
- REST APIs
- Authentication (API keys, OAuth)
- Downloading data from NOAA, USGS, ESA Copernicus
- Operationally critical for Vol II.B forecasting

### Database Basics
- SQL queries, relational databases
- GIS databases (PostGIS)
- Time-series databases
- Lower priority; mostly for Vol II.B operational workflows

## Where These Fit (Rough Mapping)

| Topic | Best Home | Priority |
|---|---|---|
| Advanced image analysis | Topic Library: Advanced Remote Sensing | Later |
| Environmental modelling (advanced) | Vol II.B anchor chapters | Phase 2 |
| Scientific visualization | Vol II.A/B + Methods Reference | Phase 2 |
| HPC for geospatial | Vol III or Topic Library | Later |
| Algorithm design | Methods Reference + Vol II | Phase 2 |
| Linux sys admin | Reference appendix | Lower |
| Software engineering | Methods Reference | Phase 2 |
| Numerical methods | Vol II.A/B + Methods Reference | Phase 2 |
| Data formats & I/O | Pathway A/B reference appendix | Phase 2 |
| Debugging & profiling | Methods Reference | Phase 2 |
| Documentation | Enhance Scientific Computing Foundations | Phase 1.5 |
| APIs & data services | Vol II.B operational chapters | Phase 2 |
| Databases | Vol II.B optional deepdive | Later |

## Next Steps

As the project matures:
1. **Phase 1.5** — Polish Scientific Computing Foundations; add documentation/literate programming subsection
2. **Phase 2** — Create Methods Reference companion volume; pull in advanced image analysis, algorithm design, numerical methods, software engineering
3. **Vol II development** — Integrate advanced environmental modelling, APIs & data services, data formats
4. **Vol III / Topic Libraries** — HPC, databases, specialized algorithm deep-dives


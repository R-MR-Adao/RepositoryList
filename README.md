# RepositoryList
A public list of my private repositories. If you would like to get access to any of them, please contact me.
<p align="center">
<img src="https://user-images.githubusercontent.com/111191306/184558142-2f895d70-276f-4ec7-ae59-7171a51041e9.gif">
</p>

This public repository was created as a sharable list of my repositories, here added as clickable submodules. Due to Intellectual Property issues, I cannot publicly share some of those repositoies, so I kindly ask you to contact me if you would like to access any of the private ones:

Email: rm.ribeiro.adao@gmail.com

LindeIn: https://www.linkedin.com/in/rmradao/

Below you can find an overview of each repository, built from public data (either my papers or my [Ph.D. disseration](http://hdl.handle.net/11093/3437)).

## Table of Contents
- [NanoPhotonicsToolbox](#nanophotonicstoolbox)
- [WaveBox: O-FDTD](#wavebox)
- [Designer 3D TPP](#designer-3d)


# NanoPhotonicsToolbox

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184531861-a4b14d5b-bc39-478e-a5ff-008f40d0386d.png">
</p>

MATLAB toolbox for the analysis of 3D and 4D Fluorescence Lifetime Imaging Microscopy (FLIM) datasets, including the multi-exponential component analysis and application of customizable transducing models.
A “fast fitting of multi-exponential decay curves” algorithm developed by Enderlein et al. was integrated into a custom-made data analysis platform, implemented with a Graphical User Interface in MATLAB for user-friendly data analysis of FLIM data.
The curve-fitting routine deconvolves the experimentally-measured IRF from the TCSPC spectrum measured at each scanning position, performs a multi-exponential curve fitting. The FLIM images are obtained by the average lifetime in each pixel.

FLIM images can be directly converted into calibrated quantities (e.g., nanoscale distances, temperature) by loading the appropriate fluorescence lifetime-to-quantity conversion function.
The toolbox is pre-programmed with various RET models for distance conversions, such as the 2D, 3D, and graphene conversion functions derived by Gaudreau et al. Lifetime to distance conversions for multi-layer Metal-Induced Energy Transfer (MIET)-FLIM can be numerically simulated using an adapted version of the MIET_gui toolbox and directly imported to the software for FLIM image conversion.

## Features
- Import FLIM data from `*.HDF5`, `*.bin`, `*.spc` or `*.txt` files.
- Store, slice and represent fluorescence intensity images.
- Calculate the fluorescence lifetimes by choosing a phasor method or a single- or multi-exponential fitting of your preference.
- Deconvolve experimental Instrument Response Functions.
- Plot and analyze the results using several statistical methods such as Gaussian Curve-fitting.
- Perform component-wise statistical analysis of measured exponential decays.
- Import multi-sensor data and perform anysotropy analysis.
- Convert fluorescence intensity, lifetime, or anysotropy data into other physical quantities.
- Use previously-published nearfield energy-transfer methods.
- Import z-stack datasets and generate 3D renderings.

## Applications

<p align="center">
<img width=700 src="https://user-images.githubusercontent.com/111191306/184544268-e76a294f-78e6-463b-ac38-f7363a9185ea.png">
</p>

<p align="center">
Fluorescence Lifetime Imaging Microscopy (FLIM) of CsPbBr<sub>3</sub> perovskite and CdSe/ZnS Quantum Dot (QD) light-emitting films. (a) FLIM images of both active materials in Close-Packed Configuration (CPC) spin-coated films (no polymer embedding). (b) Fluorescence lifetime distributions (histograms) from both active materials in CPC and PMMA embedding polymer matrices. Correlated photoluminescence (PL) lifetime and intensity for CsPbBr<sub>3</sub> perovskite and CdSe/ZnS QD spin-coated films, with and without PMMA polymer embedding. (c-d) 2D histograms for the perovskite (c) and QD (d) cases. The dashed red lines in (a) show eye-guiding linear trend lines curve-fitted to the point-cloud data. 
</p>

<p align="center">
<img width=700 src="https://user-images.githubusercontent.com/111191306/184544803-1b80fd2d-5d27-4d41-8e94-eefc1eb339f2.png">
</p>

<p align="center">
Fluorescence lifetime quenching in thin and vertically extended films. (a) Fluorescence lifetime $\tau_f(z)$ of a molecule located at a distance $z$ from the Au surface (blue) and ensemble lifetime $\langle\tau\rangle(h)$ observed in a film of thickness $h$, calculated by numerical (black) and analytical (red) integration methods.
Nanotopography of a dried droplet. (b) Fluorescence Lifetime Imaging Microscopy (FLIM). (c) Distribution histogram of thicknesses up to 200 nm thickness, found at the inner part of the droplet. The black dotted line is the actual thickness distribution, and the red line is the sum of the underlying blue, green and orange Gaussians, obtained by fitting the overall histogram. Inset: 3D nanotopography map determined via the contactless nearfield-based method.
</p>


<p align="center">
<img width=700 src="https://user-images.githubusercontent.com/111191306/184544586-dd380302-1bdd-4d73-8dc6-7f51b11a21a4.png">
</p>

<p align="center">
Study of the molecular unfolding process occurring during the hybridization between a probe DNA and a target DNA. The unfolding of the probe DNA leads to the gradual displacement of a labeling fluorophore, restoring its fluorescence intensity as the distance to the functionalized graphene substrate increases.
Dynamic tracking of the DNA hybridization. (a-c) Sample of three dye-graphene distance distributions taken after 3 (a), 54 (b), and 105 (c) minutes after addition of complementary DNA. Triple-Gaussian curve-fittings identify the characteristic peaks G1, G2, and G3. (d-e) Sum of the fitted Gaussian components for the complete time-lapse series, represented by line plots (d) and transient false-color 2D histograms. (f) Isolated G1, G2, and G3 Gaussian components encoded by a blue, green, and red color code.
</p>

## Table of Contents
- [Graphical User Interface](#gui)
- [How to setup](#how-to-setup)
- [How to use](#how-to-use)
  - [Loading files](#loading-files)
  - [Observing data](#observing-data)
  - [Calculating fluorescence lifetimes](#claculating-fluorescence-lifetimes)
- [Publications](#publications)
- [Funding](#funding)

<a name="gui"/>

## Graphical User Interface

The GUI allows importing FLIM datasets and perform complex analysis of multi-exponential decay mappings

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184532062-b3c7911e-74d6-43aa-a964-32de61cdb257.png">
</p>

<p align="center">
Example of the FLIM analysis from an SZ2080 polymer TPP micro-structured sample fabricated by Dr. Christian Maibohm.
</p>

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184532111-9640c49a-dac2-4551-b0c6-d2c11439c4cb.png">
</p>

<p align="center">
Example of confocal z-stacking (obtained using an additional pinhole in the detection path to achieve confocal geometry).
</p>

<a name="how-to-setup"/>

## How to setup

The toolbox is implemented as a series of `.m` scripts, so there is no installation step needed. All you have to do is point MATLAB to the srouce code directory:
- Open the Home tab of MATLAB's IDE
- Press "Set path"
- Press "Add with Subfolders"
- Select all folders except `.git`
- Press "Save" &rarr; "Close"
- Call `NanoPhotonicsToolbox` on the command window. The GUI will open

<a name="how-to-use"/>

## How to use

The GUI, which is divided in two main sections: The folder explorer panel (on the left side), the data loading and processing tabs.
The folder explorer panel allows the user to dynamically browse through multiple datasets in a folder. In the Data tab, the user can visualise an intensity image, which is extracted by the program from the selected `*.hdf5` file and the decay curve (which is extracted by the program from the correspondent `*.bin` file) from a specific pixel selected by the user in the intensity image. In the Lifetime analysis tab, the user can test several single exponential decay models to the decay curves and use one of them to fit multiple curves and form a fluorescent lifetime image. Furthermore, it is possible to plot the lifetime histogram of that image and perform a Gaussian fit to that histogram, so as to determine the lifetime distribution in that image.
Distance conversion, z-stacking, multisensor data loading, and anysotropy analysis can be explored in the remaining tabs.

<a name="loading-files"/>

### Loading files
When working with multiple data sets, an efficient method of browsing through data can be very useful. The folder browsing tool allows the user to select a directory where data is stored by clicking in the "Select folder" button. By performing this action, the names of all the files with file extension `*.hdf5` in that directory will be loaded into the table. To open one file, the user needs only to click in the corresponding checkbox in the "Select" column.

<a name="observing-data"/>

### Observing data

After selecting a folder and specifying an `*.hdf5` file to be opened, its intensity image will be represented on the "Intensity Image" axes and the raw data extracted from the correspondent `*.bin` file will be represented in the "Curve Plot" axes. To plot the exponential decay from a specific pixel in the intensity image, press the "Select curve" button and select the desired pixel. Pressing the "Test fit curve" button in the "Lifetime analysis" tab will apply a selected fitting method to the selected pixel.


<a name="claculating-fluorescence-lifetimes"/>

### Calculating fluorescence lifetimes

To calculate the Fluorescence Lifetime image, the software will run the p fitting function through the data matrix and build an image with the calculated lifetime values. In this analysis, the number of pixels to be evaluated is defined by the "Intensity Threshold", which can be defined with the slider shown in. When the "Calculate FLIM Image" button is pressed, every pixel whose value is above the selected intensity threshold will be evaluated. This functionality can be used not only for a faster analysis of the most relevant data, but also for eliminating background pixels whose intensity may sometimes be too low to be fitted. By selecting the "Plot lifetimes histogram" checkbox, a histogram of the lifetime values obtained in the Lifetime image will be plotted in the "Fluorescence Lifetime Histogram" axes.

## Publications

<a name="ref-1"/>

\[1\] [Ricardo M. R. Adão, Tangyou Sun, Pedro Alpuim, Bruno Romeira, and Jana B. Nieder, " Spectral-temporal luminescence properties of Colloidal CdSe/ZnS Quantum Dots in relevant polymer matrices for integration in low turn-on voltage AC-driven LEDs," Optics Express, 30(7), 10563–10572 (2022).](https://doi.org/10.1364/OE.449037)

\[2\] [Ima Ghaeli,* Ricardo M. R. Adão,* Jana B. Nieder, "CLeANFIT – Contact-Less Axial Nearfield-Based Fluorescence Imaging Topography: A Method for 3D Micro- and Nanotopography Characterization," Advanced Material Interfaces 7, 2000581 (2020). *shared first authorship](https://doi.org/10.1002/admi.202000581)

\[3\] [Ricardo M. R. Adão, Rui Campos, Edite Figueiras, Pedro Alpuim, Jana B. Nieder, "Graphene setting the stage: Tracking DNA hybridization with nanoscale resolution," 2D Materials 6(4), 045056 (2019).](https://doi.org/10.1088/2053-1583/ab41e0)

\[4\] [Ana R. Faria, Oscar F. Silvestre, Christian. Maibohm, Ricardo M. R. Adão, Bruno F. B. Silva, and Jana B. Nieder, "Cubosome nanoparticles for enhanced delivery of mitochondria anticancer drug elesclomol and therapeutic monitoring via sub-cellular NAD(P)H multiphoton fluorescence lifetime imaging," Nano Res. 12(1), (2018).](https://doi.org/10.1007/s12274-018-2231-5)


## Funding

![image](https://user-images.githubusercontent.com/111191306/184532199-01ecd242-e1db-4673-99a4-df16c9e00c3c.png)


Title: ON4SupremeSens – Graphene and novel thin films for super resolution microscopy and bio-sensing

Project Description:

The modifications of the fluorescence lifetime by the presence of fluorescence quenchers can be used to increase the axial resolution of fluorescence lifetime imaging microscopy (FLIM). The axial spatial range of the quencher material depends on its refractive index (RI), so materials with different RI can be explored in order to improve and modify the imaging axial range and axial resolution of FLIM. The main goal of the project is to optimize the FLIM technique for different resolutions and distance ranges to study different biological processes. Applications range from DNA detection to the time lapse super resolution imaging of live cells to track specific molecular biological processes in real time.

Main Goal: Optimization of a Fluorescence Lifetime Microscopy Imaging (FLIM) technique for axial super-resolution using various functional substrates and its application for biosensing and bioimaging.

Approval Date: 26 April 2018

Start Date: 01 June 2018

End Date: 31 May 2021

Contract Number: 029417

Funding Programme: Sistema de Apoio à Investigação Científica e Tecnológica (SAICT)- Projetos de Investigação Científica e Desenvolvimento Tecnológico (IC&DT)

Region: Norte

INL Role: Coordinator (Participant Contact: Jana Nieder)

Partners:

Universidade do Minho
INL
Budget Total: € 239, 886.50

ERDF Funding: € 203, 903.53

National (PT) Funding: € 35, 982.97

<a name="wavebox"/>


# WaveBox: O-FDTD

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184547803-bb09303a-8a67-4e8f-ae1e-d41e6ecffb02.png">
</p>


A software implementation of the Oscillator-Based Finite-Difference Time-Domain (O-FDTD) electromagnetic radiation propagation simulation method
This package contains a Graphical User Interface (GUI)-powered Toolbox for MATLAB for designing and running simulations.

The published software can also be downloaded from [FigShare](http://dx.doi.org/10.6084/m9.figshare.14152595)

## The O-FDTD model

O-FDTD describes the propagation of electric field waves by modifying the Lorentz Oscillator Model (LOM). Similarly to the LOM, which considers the oscillation of atom-bound electrons driven by an incident electric field, O-FDTD uses a mesh of coupled oscillators whose orthogonal displacement relates to the electric field amplitude. However, O-FDTD’s oscillators are not electrons but abstract electric field carriers evenly distributed across space, including vacuum. Each oscillator is connected to its mesh neighbors by a refractive index-dependent coupling strength that defines the electric field transfer rate and, consequently, the wave propagation speed. The electric field E time propagation is obtained using the leap-frog backward differentiation method:

$$
E_i = E_{i-1} + \frac{\mathrm{d}E_{i-1}}{\mathrm{d}t} \delta t + \frac{1}{2}\frac{\mathrm{d}^2E_{i-1}}{\mathrm{d}t^2}\delta t^2
$$

where $t$ is the time, $\delta t$ is the temporal resolution, and the index $i$ refers to the current time step. The single motion equation is formulated as:

$$
\frac{\mathrm{d}^2E_{i-1}}{\mathrm{d}t^2} = \frac{8}{3n^2\delta t^2} \left(E_{i-1}^{\mathrm{neigh}} - E_{i-1}\right) -  \frac{\sqrt{2}c}{n}\frac{4\pi\kappa}{\lambda}\frac{\mathrm{d}E_{i-1}}{\mathrm{d}t}
$$

where $n$ and $\kappa$ are the real and imaginary parts of the refractive index, $E^{neigh}$ is the neighborhood electric field, and $c$ and $\lambda$ are the vacuum speed of light and wavelength. The first term is analogous to the restoring spring motion as a function of the neighborhood electric field and accounts for the wave propagation and interference effects. The second term relates to the energy damping or absorption. Using this simple formulation, O-FDTD allows simulating 2D maps of material-dependent electric field wave speed and absorption. The refractive index contrast induces signal reflections at the building walls.

## Features
- Design 2D structures with a MATLAB-based sintax for optimal parameter control and design reproducibility
- Design light sources and define their geometrical, spectral and temporal properties
- Set the simulation paramaters in a easy-to-use GUI
- Set the simulation parameters by script
- Run O-FDTD simulations and visualize the real-time propagation results
- Export the results to MATLAB
- Run extensions to apply local monitors or perform parameter sweeping

## Applications

<p align="center">
  <img width = 700 src="https://user-images.githubusercontent.com/111191306/184548921-42dd80eb-ba2d-48a7-ad3d-1215f7a3601e.png">
</p>

<p align="center">
  Photonic device simulations: Multimode Interferometer (MMI) and photonic crystals ($\lambda = 1550$ nm). (a) Steady-state $E^2$ and $E$ of a Si/SiO<sub>2</sub> core/shell $1 \times 4$ MMI. The dashed lines indicate the Si/SiO<sub>2</sub> interface. The top axes show the $E^2$ profiles at the input ($x = 2$ $\mathrm{\mu m}$) and output ($x = 22$ $\mathrm{\mu m}$). (b) $E$ map of a photonic crystal waveguide. (c-d) Steady-state $E^2$ and $E$ mappings for input wavelengths of $\lambda = 1.945$ (off-resonance, (c)) and $1.97$ $\mathrm{\mu m}$ (on resonance, (d)). Geometry parameters: $w = 200$ nm, $S = 130$ nm, $R = 3$ $\mathrm{\mu m}$.
</p>

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184548459-dc975c8f-5005-444d-9dd0-5f75661ded09.png">
</p>

<p align="center">
  TThe age of the Internet of Things (IoT) and smart cities calls for low-power wireless communication networks, for which the Long-Range (LoRa) is a rising star. Efficient network engineering requires the accurate prediction of the Received Signal Strength Indicator (RSSI) spatial distribution. However, the most commonly used models either lack the physical accurateness, resolution, or versatility for cityscape real-world building distribution-based RSSI predictions. For this purpose, we apply the 2D electric field wave-propagation Oscillator Finite-Difference Time-Domain (O-FDTD) method, using the complex dielectric permittivity to model reflection and absorption effects by concrete walls and the receiver sensitivity as the threshold to obtain a simulated coverage area in a $600 \times 600$ m<sup>2</sup> square. Further, we report a simple and low-cost method to experimentally determine the signal coverage area based on mapping communication response-time delays. The simulations show a strong building influence on the RSSI, compared against the Free-Space Path (FSPL) model. We obtain a spatial overlap of 84% between the O-FDTD simulated and experimental signal coverage maps. Our proof-of-concept approach is thoroughly discussed compared to previous works, outlining error sources and possible future improvements. O-FDTD is demonstrated to be most promising for both indoors and outdoors applications and presents a powerful tool for IoT and smart city planners (https://www.mdpi.com/1424-8220/21/8/2717).
</p>

## Table of Contents
- [Graphical User Interface](#gui)
- [How to setup](#how-to-setup)
- [How to use](#how-to-use)
- [Example](#example)
- [Publications](#publications)
- [Funding](#funding)

<a name="gui"/>

## Graphical User Interface

The GUI allows developing script-based designs for full parameter control and design reproducibility.
The center-left panel allows the user to see the function call of a few pre-dfined geometrical forms.
The top-left panel defines the most important simulatin parameters, such as the simulation space dimensions, resolution, boundary conditions, and the simulation and integration duration.
The right panel shows the design preview, by mapping the refractive index accross the simulation space.
The "Light Source" tab allows setting the light source parameters, such as it's position and geometry, wavelength, and pulse modulation.
The "Simulation" tab allows running the simulation, visualizing the real-time electric field propagation, and integrating the light intensity over time.
Every visualization can be exported as a MATLAB figure for storage or analysis.

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184547815-93ece290-b1ce-462e-9faf-264d5f1734eb.gif">
</p>

<a name="how-to-setup"/>

## How to setup

The toolbox is implemented as a series of `.m` scripts, so there is no installation step needed. All you have to do is point MATLAB to the srouce code directory:
- Open the Home tab of MATLAB's IDE
- Press "Set path"
- Press "Add with Subfolders"
- Select all folders except `.git`
- Press "Save" &rarr; "Close"
- Call `O_FDTD` on the command window. The GUI will open

<a name="how-to-use"/>

## How to use

Designs can be made simply by editing the `designCommands()` function in the GUI editor and pressing "Preview" to visualize.

```matlab
function n = designCommands(n,X,Y,dN)
  %
  %  pts = designCommands(n,X,Y,dN)
  % 
  %  Base function containing the design commmands.
  %
  %  Inputs:
  %     n     : 2D matrix containing the design. The designs are built
  %             by modifying regions of this matrix with the desired
  %             refractive index.
  %     X, Y  : 2D matrices containing the x, y coordinate meshgrids
  %     dN    : Depth of the boundary region
  %  
  %  Outputs:
  %    n      : 2D matrix containing the design
  %
  
  % your design. e.g.:
  % n = circle(n,X,Y,1.5,2.5e-6,2.5e-6,2e-6); % outer circle
  % n = circle(n,X,Y,1,2.5e-6,2.5e-6,1.7e-6); % inner circle
  
end

```

## Example

```matlab
function n = simulationDesign(n,X,Y,dN)

    lambda = 1375; % nm (wavelength) 1375, 1385
    % ring resonator

    % background
    N = 1.5;	% background refractive index
    n = rectg(n,X,Y,N,4e-6,4e-6,10e-6,10e-6);


    N = 3.5;              % core refractive index
    t = 0.2e-6;           % core thickness
    x0 = 4e-6; y0 = 4e-6; % ring center
    R = 3.147e-6;         % ring radius
    % top arm
    n = rectg(n,X,Y,N,4e-6,7.305e-6,10e-6,t);
    % bottom arm
    n = rectg(n,X,Y,N,4e-6,0.695e-6,10e-6,t);
    % ring

    n = circle(n,X,Y,N,x0,y0,R);
    n = circle(n,X,Y,1.5,x0,y0,R - t);


    % simulation settings: these will take effect after the "Preview" and "Setup" buttons are pressed
    fetd = evalin('base','fetd');
    set(fetd.gui.edits.design_config_dimensions_x,'string','8')
    set(fetd.gui.edits.design_config_dimensions_y,'string','8')
    set(fetd.gui.edits.design_config_R,'string',num2str(30/1370*lambda))
    set(fetd.gui.edits.design_config_wl,'string',num2str(lambda))
    set(fetd.gui.edits.source_config_wl,'string',num2str(lambda))
    set(fetd.gui.edits.design_config_stop_time,'string','1200')
    set(fetd.gui.edits.design_config_integration_start,'string','900')
    set(fetd.gui.edits.design_config_integration_end,'string','1200')
    set(fetd.gui.edits.source_config_geometry_x0,'string','0.5')
    set(fetd.gui.edits.source_config_geometry_xspan,'string','0.1')
    set(fetd.gui.edits.source_config_geometry_y0,'string','7.305')
    set(fetd.gui.edits.source_config_geometry_yspan,'string','0.3')
    set(fetd.gui.checkboxes.source_config_blockLeft,'value',1)
    set(fetd.gui.checkboxes.source_config_blockTop,'value',1)
    set(fetd.gui.checkboxes.source_config_blockBottom,'value',1)
    set(fetd.gui.edits.source_config_pulseLength,'string','300')
    set(fetd.gui.popups.source_config_type,'value',3)
end

```

![image](https://user-images.githubusercontent.com/111191306/184550380-e2f83866-0470-40c8-bd7f-550fe29c57d8.png)


## Publications

<a name="ref-1"/>

\[1\] [Ricardo M. R. Adão, Manuel Caño-García, Chistian Maibohm, Jana B. Nieder, "Photonic polymeric structures and electrodynamics simulation method based on a coupled Oscillator Finite-Difference Time-Domain (O-FDTD) approach," Optics Express 29(8), 11903–11916 (2021).](https://doi.org/10.1364/oe.414211)

\[2\] [Ricardo M. R. Adão, Eduardo Balvís, Alivia V. Carpentier, Humberto Michinel, Jana B. Nieder, "Cityscape LoRa Signal Propagation Predicted and Tested Using Real – World Building - Data Based O - FDTD Simulations and Experimental Characterization," Sensors 21(8), 2717 (2021).](https://doi.org/10.3390/s21082717)

\[3\] [Ricardo M. R. Adão, Manuel Caño-Garcia, Christian Maibohm, Bruno Romeira and Jana B. Nieder, "Oscillator Finite-Difference Time-Domain (O-FDTD) electric field propagation model: integrated photonics and networks", EPJ Web Conf., 255, 01005 (2021).](https://doi.org/10.1051/epjconf/202125501005)

## Funding

![image](https://user-images.githubusercontent.com/111191306/184507830-0aaa7067-0000-46c9-b29f-a3f04ecd5576.png)


CHIPAI_INLPROJECTPAGETitle: ChipAI: Energy-efficient and high-bandwidth neuromorphic nanophotonic Chips for Artificial Intelligence systems

Project Description

The same way the internet revolutionized our society, the rise of Artificial Intelligence (AI) that can learn without the need for explicit instructions is transforming our life. AI uses brain-inspired neural network algorithms powered by computers. However, these central processing units (CPU) are extremely energy inefficient at implementing these tasks. This represents a major bottleneck for energy-efficient, scalable and portable AI systems. Reducing the energy consumption of the massively dense interconnects in existing CPUs needed to emulate complex brain functions is a major challenge.

ChipAI aims at developing a nanoscale photonics-enabled technology capable of delivering compact, high-bandwidth and energy efficiency CPUs using optically interconnected spiking neuron-like sources and detectors. ChipAI will pursue its main goal through the exploitation of Resonant Tunnelling (RT) semiconductor nanostructures embedded in sub-wavelength metal cavities, with dimensions 100 times smaller over conventional devices, for efficient light confinement, emission and detection.

Key elements developed are non-linear RT nanoscale lasers, LEDs, detectors, and synaptic optical links on silicon substrates to make an economically viable technology. This platform will be able to fire and detect neuron-like light-spiking (pulsed) signals at rates 1 billion times faster than biological neurons (>10 GHz per spike rates) and requiring ultralow energy (<10 fJ). This radically new architecture will be tested for spike-encoding information processing towards validation for use in artificial neural networks. This will enable the development of real-time and offline portable AI and neuromorphic (brain-like) CPUs.

In perspective, ChipAI will not only lay the foundations of the new field of neuromorphic optical computing, as will enable new non-AI functional applications in biosensing, imaging and many other fields where masses of cheap miniaturized pulsed sources and detectors are needed.

URL: http://chipai.eu

Start Date: 01 March 2019

End Date: 28 February 2022

Type: H2020-EU.1.2.1. – FET Open

Grant agreement ID: 828841

Funding Agency: Horizon 2020

Funding Programme: FETOPEN-01-2018-2019-2020 – FET-Open Challenging Current Thinking

INL Role: Coordinator (Participant Contact: Bruno Romeira and Nuria Barros)

Partners:

- INL (Portugal)
- University of Glasgow (UK)
- University of Strathclyde (UK)
- Eindhoven University of Technology (NL)
- Faculty of Sciences (FCiencias.id) University of Lisbon (PT)
- University of the Balearic Islands (ES)
- IQE plc (UK),
- IBM Research Gmbh (CH)
- Budget Total: € 3, 892, 005.00

Budget INL: € 653, 625.00


<a name="designer-3d"/>

# Designer 3D TPP
<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184510385-b0e6a4e9-3568-494c-a996-e6c3f66434e3.png">
</p>

A MATLAB toolbox developed in the frame of the EU-funded FET-Open project Chip-AI (grant n. 828841), for the development of 3D optical waveguides for complexly-interconnected nano-photonic systems such as on-chip artificial neural netwaorks using femtosecond laser-based Two-Photon Polymerization (TPP).

## Features
- Design 3D structures using MATLAB scripts, to ensure optimal reproducibility and control
- User-friendly script builder GUI for less experienced MATLABers
- Use pre-defined macros do define suppor structures with tunable geometry and mesh dimensions
- Define new macros for your own applications
- Break large designs into mosaic-segments according to your experimental setup requirements
- Simulate the polymerized TPP structure depending on your material and experimental setup parameters using `voxelshape_Gauss.m`
- Export the designs to format-customizable g-code files
- Import designs from G-CODE files
- Export designs to [OpenSCAD](http://https://openscad.org/ "OpenSCAD") for better 3D visualization

## Applications
<p align="center">
   <img width = 700 src="https://user-images.githubusercontent.com/111191306/184509569-c08b9466-1290-48bc-bb0d-f9cf46ecb228.png">
</p>

<p align="center">
  Two-Photon Polymerization (TPP) structure modeling and 3D waveguide design. (a) 3D waveguide structure design (writing beam path trajectories) identifying the ellipsoid vertical $f^{elli}_z$ and circular horizontal $f^{circ}_y$ parametrizations for various bending amplitudes $R_y$ and bending radii $R_c$. The line colors indicate the tracing order starting in red and ending in blue. The blue labels identify the three main building blocks. (b) 3D structure surface rendering and waveguide building blocks. The black labels describe structural design.
</p>

<p align="center">
  <img width = 700 src="https://user-images.githubusercontent.com/111191306/184510002-d5cf5a47-3677-4de8-8d32-cc5fc7b7aab8.png">
</p>

<p align="center">
  3D support structure design and filling. (a) 3D design of a single, elongated support structure. (b) Freeform supported 3D waveguide with automatically designed support structures. (c) Point, vector, and width definitions for the support structures between two waveguide points $A$ and $B$. (d) Support structure horizontal filling mesh definitions ( $z = 0$ ). (e) Support structure vertical filing profile.
</p>

<p align="center">
  <img width = 700 src="https://user-images.githubusercontent.com/111191306/184510129-b0bbf347-56da-48b7-8993-890970623625.png">
</p>

<p align="center">
  Schematic representation of the exposure profile for a $z$-modulated laser beam tace. (a) Due to the vertically elongated voxel, the resulting waveguide cross-section is not constant, but curvature-dependent. (b) Additional lines can be traced to compensate for the voxel elongation.
</p>

<p align="center">
  <img width = 700 src="https://user-images.githubusercontent.com/111191306/184509523-8df1cd98-289f-4ed1-8890-580f42a6567d.png">
</p>

<p align="center">
  Design, morphological simulation, and fabrication of $f^{cos2}_z$-parameterized waveguides with hollow support structures via Two-Photon Polymerization (TPP) 3D microprinting. (a) Structure design (writing beam path trajectories). (b) Morphological simulation using a fluence $F = 20$ mJ/cm<sup>2</sup> (per pulse) and a writing speed $v = 50$ µm/s, thus leading to an exposure dose $D = 244$ mJ/cm<sup>2</sup>. (c) Scanning Electron Microscopy (SEM) image of the fabricated structure in OrmoCore. (d) Systematic sweep over the laser fluence and writing speed, comparing the simulation (left) and experimental fabrication (right) results. The inset labels represent the exposure dose $D(F,v)$ shared by the corresponding simulation and fabrication counterparts. The colors highlight structures obtained using a similar dose.
</p>


## Table of Contents
- [Graphical User Interface](#gui)
- [How to setup](#how-to-setup)
  - [MATLAB](#matlab)
  - [OpenSCAD]("openscad)
- [How to use](#how-to-use)
- [Examples](#examples)
- [Publications](#publications)
- [Funding](#funding)

<a name="gui"/>

## Graphical User Interface

The GUI allows developing script-based designs for full parameter control and design reproducibility.
The top-left panel helps less experienced MATLAB developers to build designs based on simple geometrical forms, methematical transformations, and loops.
The right panel allows visualizing and rotating the 3D design, splitting the design into mosaics (if necessary), exporting the visualization as a MATLAB figure, and exporting the design as a G-CODE file.

![image](https://user-images.githubusercontent.com/111191306/184509833-10ec286b-5e7f-43f3-b351-886a3c98072a.png)

<a name="how-to-setup"/>

## How to setup

### MATLAB
The toolbox is implemented as a series of `.m` scripts, so there is no installation step needed. All you have to do is point MATLAB to the srouce code directory:
- Open the Home tab of MATLAB's IDE
- Press "Set path"
- Press "Add with Subfolders"
- Select all folders except `.git`
- Press "Save" &rarr; "Close"
- Call `designer3D` on the command window. The GUI will open

### OpenSCAD

- Install [OpenSCAD](http://https://openscad.org/ "OpenSCAD") on your machine and use the `.scad (visual)` option to export the design into an OpenSCAD design.
- Open `import3D.scad` or `import3D_voxel.scad` in OpenSCAD and modify the include line to import the desired .scad file.

```scad
include <filePath\fileName.scad>
```

<a name="how-to-use"/>

## How to use

Designs can be made simply by editing the `designCommands()` function in the GUI editor and pressing "Preview" to visualize.

```matlab
function pts = designCommands(operator,pts,dx)
  %
  %  pts = designCommands(operator,pts,dx)
  % 
  %  Base function containing the design commmands.
  %
  %  Inputs:
  %    operator: a struct with mathematical operators. Uuse the GUI to
  %              check the options available and call syntax.
  %    pts     : a cell array containing the design. Each element in the 
  %              array corresponds to a line segmend to be printed.
  %    dx      : global resolution parameter used by the base functions.
  %              It can be set directly in the GUI or script.
  %  
  %  Outputs:
  %    pts     : a cell array containing the design.
  %
  
  % your design. e.g.:
  % pts{end+1} = [0,0,0]; // add one point at the origin
  
end

```

The right panel allows setting the experimental setup requirements such as writing field of view limitations and desired time delta between consecutive points, and exporting the design as G-CODE.
The `importPTSfromGcode()` function can be used to import previously-exported designs from G-CODE files

```matlab
pts = importPTSfromGcode();
```
For TPP applications, you can simulate the effective shape of the polymerized structures by adapting the parameters define in `voxelshape_Gauss.m` and running the script.
The mathematical derivation of the model used can be found in ref [\[1\]](#ref-1).

## Examples

The following codes exemplify some basic designs auto-generated using the GUI, which can be directly copied into the body of the `designCommands()` function via the "Add to script" button:

```matlab
for iz = 1:1:10; pts{end+1} = Circle([0,0,iz],iz,1); end
```
![image](https://user-images.githubusercontent.com/111191306/184511333-f596499f-f4a7-41a8-a36b-2859e3921348.png)

```matlab
for iy = -20:20:20; for ix = -20:20:20; for iz = 1:1:10;
    pts{end+1} = Circle([ix,iy,iz],iz,1);
end; end; end
```

![image](https://user-images.githubusercontent.com/111191306/184511430-237c44e4-b5ab-4e8e-bead-266f65c4a1eb.png)

```matlab
for iy = -15:15:15; for ix = -15:15:15; for it = 20:20:360;
    pts{end+1} = operator.rotXC(Circle([ix,iy,0],5,2),it);
end; end; end
```

![image](https://user-images.githubusercontent.com/111191306/184511506-c33a519a-8c7d-4db9-b8d7-577a1f47829b.png)

```matlab
for it = 0:1:1; for iy = -10:5:10; for iz = 0:0.5:5;
    pts{end+1} = operator.translate(operator.rotZC(Line([-10,0,iz],[10,0,iz],1),90*it),[iy*it,iy*(1-it),0]);
end; end; end
```

![image](https://user-images.githubusercontent.com/111191306/184511515-aaa5271b-84ed-42ae-896e-a85426d4667a.png)

```matlab
yoff = 17.25/2; xoff = 30;
for iy = -yoff*3:yoff:yoff*3; for ix = -xoff:xoff:xoff; for iz = 0:0.5:5;
    cond = mod(iy,yoff*2)==0;
    pts{end+1} = Circle([ix+xoff/2*cond,iy,iz],10,2*pi*10/6);
end; end; end
```

![image](https://user-images.githubusercontent.com/111191306/184511526-ee2344b5-6032-4461-be2d-83d1bb2c5e84.png)

```matlab
x = 2*pi*(0:0.05:6)'; f = 0.25;
pts{end+1} = [cos(x).*x*f, sin(x).*x*f, x*f+2];
x = 2*pi*(-3:0.1:3)';
for iy = -20:1.5:20; pts{end+1} = [x, iy*ones(size(x)), sin(x)]; end
```

![image](https://user-images.githubusercontent.com/111191306/184511537-532d7ed5-c3eb-4d01-baee-6e2d67d87423.png)

```matlab
im = imread('pika.png');
im = 255-im(:,:,:);
imbin = [zeros(size(im,1)+2,1),[[zeros(1,size(im,2))];sum(im,3)>3;[zeros(1,size(im,2))]],zeros(size(im,1)+2,1)];

skip = [1 3];
impts = abs(diff(imbin(1:skip(1):end,1:skip(2):end)));

xoff = -size(im,2)/skip(2);
yoff = -size(im,1)/skip(1)/2 ;
scale = 0.45;

for ii = 1 : size(impts,2)
    fd = find(impts(:,ii));
      for jj = 1:2:(length(fd)-1)
      pts{end+1} = Line([ii*skip(2)+xoff,fd(jj)*skip(1)+yoff,0]*scale,[ii*skip(2)+xoff,fd(jj+1)*skip(1)+yoff,0]*scale,dx);
    end
end
```

<img width=425 src=https://user-images.githubusercontent.com/111191306/184511814-139ea2ce-9d51-4fbb-b6da-1cbaf95ff334.png>


## Publications

<a name="ref-1"/>

\[1\] [Ricardo M. R. Adão, Tiago L. Alves, Christian Maibohm, Bruno Romeira, and Jana B. Nieder, "Two-photon polymerization simulation and fabrication of 3D microprinted suspended waveguides for on-chip optical interconnects," Opt. Express 30, 9623-9642 (2022)](https://doi.org/10.1364/OE.449641)

\[2\] [Beatriz N. L. Costa, Ricardo M. R. Adão, Christian Maibohm, Angelo Accardo, Vanessa F. Cardoso, and Jana B. Nieder, “Cellular Interaction of Bone Marrow Mesenchymal Stem Cells with Polymer and Hydrogel 3D Microscaffold Templates”, ACS Applied Materials & Interfaces, 14 (11), 13013-13024 (2022)](https://doi.org/10.1021/acsami.1c23442)

## Funding

![image](https://user-images.githubusercontent.com/111191306/184507830-0aaa7067-0000-46c9-b29f-a3f04ecd5576.png)


CHIPAI_INLPROJECTPAGETitle: ChipAI: Energy-efficient and high-bandwidth neuromorphic nanophotonic Chips for Artificial Intelligence systems

Project Description

The same way the internet revolutionized our society, the rise of Artificial Intelligence (AI) that can learn without the need for explicit instructions is transforming our life. AI uses brain-inspired neural network algorithms powered by computers. However, these central processing units (CPU) are extremely energy inefficient at implementing these tasks. This represents a major bottleneck for energy-efficient, scalable and portable AI systems. Reducing the energy consumption of the massively dense interconnects in existing CPUs needed to emulate complex brain functions is a major challenge.

ChipAI aims at developing a nanoscale photonics-enabled technology capable of delivering compact, high-bandwidth and energy efficiency CPUs using optically interconnected spiking neuron-like sources and detectors. ChipAI will pursue its main goal through the exploitation of Resonant Tunnelling (RT) semiconductor nanostructures embedded in sub-wavelength metal cavities, with dimensions 100 times smaller over conventional devices, for efficient light confinement, emission and detection.

Key elements developed are non-linear RT nanoscale lasers, LEDs, detectors, and synaptic optical links on silicon substrates to make an economically viable technology. This platform will be able to fire and detect neuron-like light-spiking (pulsed) signals at rates 1 billion times faster than biological neurons (>10 GHz per spike rates) and requiring ultralow energy (<10 fJ). This radically new architecture will be tested for spike-encoding information processing towards validation for use in artificial neural networks. This will enable the development of real-time and offline portable AI and neuromorphic (brain-like) CPUs.

In perspective, ChipAI will not only lay the foundations of the new field of neuromorphic optical computing, as will enable new non-AI functional applications in biosensing, imaging and many other fields where masses of cheap miniaturized pulsed sources and detectors are needed.

URL: http://chipai.eu

Start Date: 01 March 2019

End Date: 28 February 2022

Type: H2020-EU.1.2.1. – FET Open

Grant agreement ID: 828841

Funding Agency: Horizon 2020

Funding Programme: FETOPEN-01-2018-2019-2020 – FET-Open Challenging Current Thinking

INL Role: Coordinator (Participant Contact: Bruno Romeira and Nuria Barros)

Partners:

- INL (Portugal)
- University of Glasgow (UK)
- University of Strathclyde (UK)
- Eindhoven University of Technology (NL)
- Faculty of Sciences (FCiencias.id) University of Lisbon (PT)
- University of the Balearic Islands (ES)
- IQE plc (UK),
- IBM Research Gmbh (CH)
- Budget Total: € 3, 892, 005.00

Budget INL: € 653, 625.00
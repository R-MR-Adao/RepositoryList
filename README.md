# RepositoryList
A public list of my private repositories. If you would like to get access to any of them, please contact me.
<p align="center">
<img src="https://user-images.githubusercontent.com/111191306/186910047-3463fc94-a189-4b0b-b243-f3bb2c44272e.gif">
</p>

This public repository was created as a sharable list of my repositories, here added as clickable submodules. Due to Intellectual Property issues, I cannot publicly share some of those repositories, so I kindly ask you to contact me if you would like to access any of the private ones:

LindeIn: https://www.linkedin.com/in/rmradao/

Below you can find an overview of each repository, built from public data (either my papers or my [Ph.D. dissertation](http://hdl.handle.net/11093/3437)).

## Table of Contents
- [NanoPhotonicsToolbox](#nanophotonicstoolbox)
- [WaveBox: O-FDTD](#wavebox)
- [TPP RM21](#tpp_rm21)
- [TPP Designer 3D](#designer-3d)
- [LoRaComSensors](#loracomsensors)
- [PRR QRW](#prr_qrw)
- [CodinGame](#codingame)


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

\[3\] [Pedro L. Silva, Oleksandr A. Savchuk, Juan Gallo, Lorena García-Hevia, Manuel Bañobre-López and Jana B. Nieder, "Mapping intracellular thermal response of cancer cells to magnetic hyperthermia treatment", Nanoscale, 12, 21647-21656, (2020)](https://doi.org/10.1039/C9NR10370H)

\[4\] [Ricardo M. R. Adão, Rui Campos, Edite Figueiras, Pedro Alpuim, Jana B. Nieder, "Graphene setting the stage: Tracking DNA hybridization with nanoscale resolution," 2D Materials 6(4), 045056 (2019).](https://doi.org/10.1088/2053-1583/ab41e0)

\[5\] [Ana R. Faria, Oscar F. Silvestre, Christian. Maibohm, Ricardo M. R. Adão, Bruno F. B. Silva, and Jana B. Nieder, "Cubosome nanoparticles for enhanced delivery of mitochondria anticancer drug elesclomol and therapeutic monitoring via sub-cellular NAD(P)H multiphoton fluorescence lifetime imaging," Nano Res. 12(1), (2018).](https://doi.org/10.1007/s12274-018-2231-5)


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

# TPP_RM21

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184698850-1cc8caf0-7496-4a88-b889-f8e7c4afcc92.png">
</p>

A Python- and Arduino-based instrumentation control software to perform Two Photon Polymerization (TPP) microprinting using the MCL optical microscope platform RM21.
This platofm features a custom-built G-code file interpreter library, design visualization and rescaling tools, and an instrumentation control panel implemented by a basic (Tkinter) GUI. The MighTex V1.2.0 camera control software is used to visualize the sample, enabling-focus finding and live fabrication monitoring features.

## Features
- Import custom-built G-CODE designs from the TPP_designer3D tool
- Represent and transform designs prior to fabrication
- Move accross a sample to inspect it's contents and define the fabrication position
- Run fabrication and monitor the progress

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
- [Setup](#hsetup)
  - [Software architecture $ instrumentation control](#architecture)
  - [Optical setup](#optical-setup)
- [How to use](#how-to-use)
- [Publications](#publications)
- [Funding](#funding)

<a name="gui"/>

## Graphical User Interface

<p align=center>
<img src="https://user-images.githubusercontent.com/111191306/184703653-b7a475d3-a9a5-45fe-99ab-e3e68aca54b9.png">
</p>

<p align=center>
Left panel: shutter and stage control panel. Top-right: design visualization. Bottom-right: MighTex V1.2.0 camera control software for focus-finding and live fabrication monitoring.
</p>

## Setup

<a name="architecture"/>

### Software architecture & instrumentation control

The instrumentation control system can be divided into the design software, instrument control software, and instrumentation categories. The designs are created either in commercial Computer-Aided Design (CAD) software or in the custom-built design tool `TPP_designer3D`.
Commercial CAD software usually define solid objects that need to be processed by slicer software to generate beam trajectory coordinates. Such trajectory and associated tool operation commands are thus compiled into a list of sequential Computerized Numerical Control (CNC) operations, usually as a G-code file. Although most G-code commands are standardized, many configuration parameters are tool-specific, and most commercial slicer software resort to protocol libraries made available by the manufacturers. Examples of specific commands include the startup settings, the encoding of multiple tool functionalities, accounting for robotic arm degrees-of-freedom-related limitations, collision-avoiding routines, and the need for auxiliary support structures, to name a few. In this regard, a TPP 3D micro-printer is considerably simpler than most 3D stereolithography or machining tools since there is no direct contact between the tool (microscope objective) and the structure.
Commercial design software have obvious advantages over custom-built ones in terms of powerful 3D design features and automatic slicing routines. However, since this work uses custom-built setup and control software, no established fabrication protocol is available in commercial software. Hence, the simplest approach is to develop a design tool that directly encodes the laser beam trajectory and a small G-code compiler adjusted to the specificities of the system.
Regardless of the design method, the implemented control software expects a G-code file whose parameters and structure specified in `doc/RM21-TPP-FabStation-Control_Documentation.pdf`.
The control software schematized below consists of a master Python program (`RM21_main.py`) that commands and syncs all instrumentation controllers. The main program then resorts to both commercial and custom-built Python libraries: the commercial Madlib and MicroDrive (MCL - `mcl_lib.py`) libraries control the Micro-Drive and Nano-Dive stage controllers; the custom-built G-code (`gcodeInterp.py`) and Arduino (`arduinoCom.py`) libraries implement a simple G-code interpreter and command an Arduino board for the shutter operation.

For more detailed information, please refer to `doc/RM21-TPP-FabStation-Control_Documentation.pdf`.

<p align=center>
  <img width=700 src="https://user-images.githubusercontent.com/111191306/184706789-24417598-aeab-47d5-8a64-40dff1c5af62.png">
</p>

<p align=center>
Schematic of the custom-built TPP control instrumentation and software. (a) Structure design and G-code generation. (b) Instrumentation control software: Python-based
synced stages and shutter control. (c) Instrumentation for sample displacement and laser shutter operation.
</p>

<p align=center>
  <img width=700 src="https://user-images.githubusercontent.com/111191306/184708227-c3b875ea-64c3-4a50-af39-e8238e512577.png">
</p>

<p align=center>
Process flow of design file loading and execution: File loading; Design execution; Instant motion; Trajectory motion.
</p>


<a name="optical-setup"/>

### Optical setup

A custom-built DLW TPP setup illustrated below uses a femtosecond pulsed laser source
Tsunami (Spectra Physics) tunable between $\lambda = 730 - 800$ nm, with ~80 fs pulse length.  An external two-SF10 glass prism compressor (AFS-SF10-SF10, Thorlabs) is used for pulse optimization, counteracting the dispersion of the optical components. A reflective Neutral-Density (ND) filter wheel (NDC-50C-2M, Thorlabs) is used for power control. The laser power is monitored using a beam sampler (10B20-01NC.2, Newport) and a power meter (1918-R, Newport), whose reading is converted into the laser power at the back aperture of the microscope objective using a calibration curve. A periscope system raises the beam to the height of the microscope (RM21 microscope, MCL) input port. A Transistor–Transistor Logic (TTL) signal-controlled shutter (SHB1T, Thorlabs) controls the on-off laser exposure. A beam expander built from two cemented achromat lenses (fBE1 = 40 mm, fBE2 = 150 mm) ensures the over-illumination of the objective back aperture to achieve a difrraction-limited beam
focus. A refkective ND filter (Optical Density (OD) 0:2, NDUV02A, Thorlabs) deflects the laser beam into a $40\times$ dry objective (NA 0:75, MRH00401, Nikon), focused on the sample. The sample is translated using coupled XY Z micro-step motor and piezo stages (MicroStage Series, MCL; NanoLPS200, MCL), with traveling ranges of 20 mm (step motor) 200 $\mathrm{\mu m}$ (piezo). Real-time monitoring of the fabrication is achieved via wide-field imaging, using an LED light source and a CMOS camera (MCE-B013-UW, MighTex). The LED can be placed above the sample (transmission imaging) or below the ND filter (back illumination), using a 50/50 Beam splitter (BPD254S-FS, Thorlabs). A bandpass filter (FSQ- BG39, Newport) protects the camera from laser reflections.

<p align=center>
  <img width=700 src="https://user-images.githubusercontent.com/111191306/184704471-850db1ce-fd0d-4c15-84e3-b3a9d2cd8fe3.png">
</p>

<p align=center>
  Custom-built Two-photon Polymerization (TPP) optical setup diagram. From the fs laser to the beam expander: top-view representation; To the right of the beam expander: side-view representation. The red arrows around the first mirror show that the beam is steered slightly upwards, passing over the mirror on its return from the beam compressor. The shutter and beam expander are elevated from the optical table plane. The beam is raised using a two-mirror periscope (omitted from the figure).
</p>


<a name="how-to-use"/>

## How to use

Establishing communication with the hardware is the first step in any fabrication session. For the sake of facile troubleshooting, the hardware communication is initialized individually for each equipment via the respective "initialize" button. The Python console provides feedback on the communication attempt. Once the software establishes the communication with each hardware, its control buttons become enabled for user action.

For details regarding how to use the GUI, please refer to `doc/RM21-TPP-FabStation-Control_Documentation.pdf`


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



# LoRaComSensors

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184631638-c912e16f-bdef-4f78-b92b-b682e32e8cef.png">
</p>

Microcontroller-based LoRa communication for remote environmental monitoring. Microcontroller codes to send sensor readings to LoRa gateway: temperature, pressure, humidity, NO2 concentration, and sound level.

https://user-images.githubusercontent.com/111191306/184646263-58941e5d-964d-462f-ac08-a2603f994483.mp4

[See original video](https://mdpi-res.com/sensors/sensors-21-02717/article_deploy/sensors-21-02717-va.mp4) in [MADPI](https://www.mdpi.com/1424-8220/21/8/2717).

## Features
- `*.ino` codes for LoRa microcontrollers:
  - BSFrance LoRa324uII
  - Heltec ESP32 WiFi Lora 32 V2
- Read data from different environmental monitoring sensors:
  - Adafruit BME280 temperature and humidity
  - DFRobot BMP280 temperature pressure
  - FRobot Analog Sound Sensor V2.2
  - GS NO2_968 043 NO2 concentration and temperature
- Establish a communication between a portable microcontroller and a LoRa gateway (LPS8 Dragino)
- Send packets to MQTT sever

## Applications
<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/184548459-dc975c8f-5005-444d-9dd0-5f75661ded09.png">
</p>

<p align="center">
  TThe age of the Internet of Things (IoT) and smart cities calls for low-power wireless communication networks, for which the Long-Range (LoRa) is a rising star. Efficient network engineering requires the accurate prediction of the Received Signal Strength Indicator (RSSI) spatial distribution. However, the most commonly used models either lack the physical accurateness, resolution, or versatility for cityscape real-world building distribution-based RSSI predictions. For this purpose, we apply the 2D electric field wave-propagation Oscillator Finite-Difference Time-Domain (O-FDTD) method, using the complex dielectric permittivity to model reflection and absorption effects by concrete walls and the receiver sensitivity as the threshold to obtain a simulated coverage area in a $600 \times 600$ m<sup>2</sup> square. Further, we report a simple and low-cost method to experimentally determine the signal coverage area based on mapping communication response-time delays. The simulations show a strong building influence on the RSSI, compared against the Free-Space Path (FSPL) model. We obtain a spatial overlap of 84% between the O-FDTD simulated and experimental signal coverage maps. Our proof-of-concept approach is thoroughly discussed compared to previous works, outlining error sources and possible future improvements. O-FDTD is demonstrated to be most promising for both indoors and outdoors applications and presents a powerful tool for IoT and smart city planners (https://www.mdpi.com/1424-8220/21/8/2717).
</p>

## Table of Contents

- [How to setup](#how-to-setup)
  - [System](#system)
  - [Microcontroller wiring](#microcontroller)
  - [Install libraries](#install-libraries)
  - [Node-RED]("node-red)
- [Publications](#publications)
- [Funding](#funding)

<a name="how-to-setup"/>

## How to setup

### System

Even though microncontroller code should be transportable between different microcontrollers (here two were tested), most of the code was developed and optimized for (LoRa32u4 II, BSFrance).
Other implementations may require slight modifications, such as the signal initialization order.
The figure below describes implemented system. More details can be found in [my paper](https://www.mdpi.com/1424-8220/21/8/2717) regarding this work.

<p align="center">
  <img src="https://user-images.githubusercontent.com/111191306/184682481-69d36268-8e66-43f1-a19c-431af8a17d46.png">
</p>

<p align="center">
  Several environment monitoring sensors for temperature (BMP280, DFRobot), humidity (BME280, Adafruit), noise/sound (Analog Sound Sensor v2.2, DFRobot), and NO<sub>2</sub> concentration (DGS-NO2 968-043, Spec Sens) were wired to a microcontroller board (LoRa32u4 II, BSFrance). The board features a LoRa node chip microcontroller (SX1276, AtmegaQR 32u4 3:3 V @8 MHz MCU), with transmitter power +20 dBm, receiver sensitivity between 􀀀136 dBm @ LoRa 125 kHz SF12 293 bps and 􀀀118 dBm @ LoRa 125 kHz SF6 9380 bps, and an operating frequency of 868 MHz and transmission current-consumption of 128 mA. A 5 V portable power bank drives the micro-controller circuit. The LoRa gateway (LPS8, Dragino), with a transmitter power of +20 dBm, was placed indoors (University of Vigo office), while the micro-controller LoRa transceiver was taken outside for signal coverage measurements.
</p>

<a name="microcontroller"/>

### Microcontroller wiring

<p align="center">
  <img src="https://user-images.githubusercontent.com/111191306/184681334-acdb07e1-d5e8-4d00-8996-5cc0dd16a8da.png">
</p>

<p align="center">
Implemented Long Range (LoRa) gateway system. (a) Schematic of the LoRa communication test device equipped with various sensors on an electronic breadboard. (b) Diagram of the communication process.
</p>

<a name="install-libraries"/>

### Install libraries

The code was implemented, compiled and transfer to the microcontrollers using the Arduino IDE. The required Arduino libraries can be found in the `external` folder in this repository. The can also be installed directly from the Arduino IDE.

### Node-RED

The communication between the LoRa micrcontrollers and the gateway can be implemented in a number of ways. One possibility to quickly represent the data monitoring results is to setup a Node-RED server.
This implementation is not part of this repository, but can be summarized as follows:

Node-RED is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices. In this work, Node-RED was used to collect, store and display the data sent from the micro-controllers to the MQTT server.
A screenshot of the developed GUI can be found below. There, the user can select up to four measurements from any sensor to be displayed in real-time and plotted over time. Since the plotted data is stored in the memory of the computer hosting Node-RED (a Raspberry Pi in this case), it was found that plotting more than four mea-
surements at once may lead to program lagging. Also, the response time (ping) of the LoRa communication for each micro-controller can be displayed. This feature was crucial for the mapping of the signal coverage across the city.
Th overall flow of the developed Node-RED program is depicted below. The flow is responsible for the measurement monitors, and response time
display.
While Node-RED offers a large set of task-specific nodes, the java-script enabling function node was found to be a practical and versatile option for most operations, thereby reducing the number of nodes used in the flow. In Node-RED, a message (msg) object coming from an MQTT server contains the properties payload, topic, qos,
msgid and retain, however, only the topic and payload are used in this program. In this case, the topic is a string object used to describe the device and physical quantity from which the message originated. The payload can be either a String, an Integer a JSON object, or a Boolean and it carries the essential content of the message. As can be seen below, the MQTT node labeled ”#” is used to fetch all messaged transmitted to the server. The function node labeled "add timestamp and filename”" is used to filter the messages according to their topic and format specific messages to be saved in text files (see `src\Node-Red\add_sensor_timestamp_and_filename.js`).

The GUI is composed of dashboard nodes Gauge, Chart, used for data representation and Drop down menu, Button and Switch, with which the user can interact. Upon user interaction, the dashboard nodes can be used to inject a payload or trigger an action. For instance, the button node labeled "clear" injects a payload containing an empty JSON object into the chart nodes, thus clearing the displayed data.
Using a function node, additional tasks can be carried out upon user interaction. The function nodes labelled "format" are used to select the which topic shall be presented on each Gauge-Chart pair, using global variables showData Gauge1, showData Gauge2, showData Gauge3 and showData Gauge4. Additionally, they are used
to change the format of the Gauge nodes by changing the limits, units and label, according to the selected physical quantities (see `src\Node-Red\format_for_gauge.js`).

Upon the arrival of a new message from the MQTT server, the function nodes labelled "if right topic" are used to display the data according to the set global variables showData Gauge1, showData Gauge2, showData Gauge3 and showData Gauge4 (see `src\Node-Red\select_topic.js`).

<p align="center">
  <img src="https://user-images.githubusercontent.com/111191306/184685106-308a1465-de75-4d03-a99f-a9529c73093a.png">
</p>

<p align="center">
  (top) Node-RED: Implementation of the Graphical User Interface (GUI) for the display of collected data and sensor response time (ping).
  (bottom) Node-RED: Graphical User Interface (GUI) for data monitoring
</p>


## Publications

<a name="ref-1"/>

\[1\] [Ricardo M. R. Adão, Eduardo Balvís, Alivia V. Carpentier, Humberto Michinel, Jana B. Nieder, "Cityscape LoRa Signal Propagation Predicted and Tested Using Real – World Building - Data Based O - FDTD Simulations and Experimental Characterization," Sensors 21(8), 2717 (2021).](https://doi.org/10.3390/s21082717)

## Funding

![image](https://user-images.githubusercontent.com/111191306/184633801-13c5177d-c0af-41aa-ad8f-ba747dab807a.png)

Title: NANOEATERS: Valorization and transfer of NANOtechnologies to EArly adopTERS of the Euroregion Galicia-Norte Portugal.

Project Description

NANOEATERS is a network of Research Centers created with the objective of supporting Euroregional “early adopters” companies in the application of new nanotechnology-based solutions. Companies, Universities and Technology Centers will work together with INL in the definition of new nano-based commercially available products and /or services. The technologies targeted by the project will offer effective responses to the weaknesses detected in the cross border Smart Specialization Strategy (S3) Galicia – Northern Portugal, contributing to major social challenges as Health, Environmental Monitoring, Food Safety, Energy Efficiency or Industry 4.0.

Project mission:

Encourage synergic cooperation between crossborder RTD centers and universities; Improve the connection between RTD centers and companies so that RTD results can be commercially exploited; and increase private investment in Research and Innovation.

Project activities:

1 – NanoEaters Community Building;
2 – NanoEaters Use Cases: Development of 10 nanotechnology based “Use Cases” based on the synergic cooperation among INL, universities and RTD Centers from Galicia, allowing the development of TRL 3-4 nanotechnologies to TRL 7-8;
3 – Call For Experiments: 22 Experiments proposed by SMEs will be selected for the development of new nanotechnology-based products, services and / or markets;
4 – Experiments development: Technological and Business Support will be given to SMEs during the execution of their proposed experiments, enabling the commercial exploitation of the RTD results through an Acceleration Program.

Start Date: 01 January 2017

End Date: 31 December 2019

Type: INTERREG POCTEP

Contract Number: 0181_NANOEATERS_1_EP

Funding Agency: ERDF

Funding Programme: INTERREG V-A España-Portugal (POCTEP) 2014-2020

INL Role: Partner Beneficiary (Participant Contact: Paula Galvão)

Partners:

- GAIN, Axencia Galega de Innovación (Galician Innovation Agency)(Spain)
- INL (Portugal)
- Universidade de Vigo (Spain)
- Universidade de Santiago de Compostela (Spain)
- GRADIANT, Centro Tecnológico de Telecomunicaciones de Galicia (Spain)
- CTAG, Fundación para la promoción de la Innovación, Investigación y Desarrollo Tecnológico en la Industria de Automoción de Galicia (Spain)
- AIMEN, Asociación de Investigación Metalúrgica del Noroeste (Spain)
- FBGS , Fundación Biomédica Galicia Sur (Spain)

Budget Total: €4, 255, 750.69

Budget INL: €1, 471, 852.35

# PRR_QRW

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/186265433-0eb2ea45-1cd5-408b-8edf-46c4408e4575.png">
</p>

A demonstrator app implementing Markov Chain-based numerical simulations of the output probabilities (electric field intensity) of Quantum Random Walks (QRW) in series-coupled coupled Photonic Ring Resonators (PRR)

## Features
- Evaluate and visualize pre-defined PRR QRW examples
- Use the framework to implement your own PRR systems
- Perform steady-state and time-domain Classical and Quantum RW simulations
- Select the sweeping parameters using a simple GUI

## Applications
<p align="center">
   <img width = 700 src="https://user-images.githubusercontent.com/111191306/186266618-3217b2b7-c8b5-4afb-8458-3ddfca108d63.png">
</p>

<p align="center">
  Random walks in series-coupled ring resonators.
  (a) Series-coupled multi-ring resonator.
  $\kappa_i$ and $\alpha$ are the coupling coefficient between each indicated pair of waveguides, and loss coefficient, respectively.
  The indicated values correspond to a walker moving consecutively from one ring to the next without looping.
  (b) Graph proposed to model propagation in the series-coupled ring resonators.
  $k_i = \kappa_i^2$ are the walker hopping probabilities associated with each pair of nodes, where $k_i + t_i = 1$.
</p>

<p align="center">
  <img width = 600 src="https://user-images.githubusercontent.com/111191306/186269699-746c5591-0b12-4d89-9386-e75ef96a31c0.png">
</p>

<p align="center">
  An example of how to simulate the QRW outputs for a simple pre-defined example with two series-coupled PRRs.
</p>

## Table of Contents
- [Graphical User Interface](#gui)
- [How to setup](#how-to-setup)
- [How to use](#how-to-use)
  - [Add custom systems](#add-custom-systems)
  - [Modify the GUI](#modify-gui)
- [Example](#example)
- [Publications](#publications)
- [Funding](#funding)

<a name="gui"/>

## Graphical User Interface

This app is intended as a compact control center for the quick visualization of RW simulations for PRR system prototyping.
This enables you to quickly try and tune different parameters such as the number of rings and the coupling coefficients.
Hence, the developed GUI brings together a minimalist interface that can readily be adapted for other PRR systems.
A screenshot of the main GUI can be found below, illustrating the different options currently available.

Depending on the number of rings and the sweeping parameters, additional inputsm such as the coupling coefficients or time-limits, may be required from the user.
This is currently done via input dialogs, as illustrated in the [Applications](#applications) section.

<p align="center">
   <img src="https://user-images.githubusercontent.com/111191306/186271143-80049bf0-3e52-45bf-a672-cf32fac6d0e0.png">
<p/>

<a name="how-to-setup"/>

## How to setup

The toolbox is implemented as a series of `.m` scripts, so there is no installation step needed. All you have to do is point MATLAB to the srouce code directory:
- Open the Home tab of MATLAB's IDE
- Press "Set path"
- Press "Add with Subfolders"
- Select all folders except `.git`
- Press "Save" &rarr; "Close"
- Call `PRR_QRW` on the command window. The GUI will open


## How to use

Running pre-defined examples should be straightforward, and an example is show in the [Applications](#applications) section.
However, the most interesting feature of this tool is the framework in which you can define new simulation scenarios.
Hence, the following shows how to implement the RW simulations for custom systems and adapting the GUI accordingly, so the results can be tested and visualized in the same manner as the pre-defined examples.

<a name="add-custom-systems"/>

### Add custom systems

Custom PRR systems can be modelled by editing the `CRW_sweep()` function in `src/RW/CRW_sweep.m`
To execute a given system, the following parameters must be defined:
 - `RWc`: random walk command which specified which RW function shall be executed
 - `th` : coherent theta array. This can be imported from the sweep parameters KT or set to zero
 - `Tf` : transfer function matrix. A function handle that implements the specified RW transfer function
 - sweep parameters (example):
    - `v1` : sweep variable 1 (iterated over jj in main function)
    - `v2` : sweep variable 2 (iterated over kk in main function)
    - `vf` : fixed parameter
 - `Tc` : transfer command. A string that encodes the function call of `Tf` to be evaluated in main function
 - `vars` : sweep variable data. A cell array containing `v1` and `v2`, and the respective labels to be shown in output plot

Each of these parameters can be specified according to the user-defined settings in the GUI, and need only be fitted within the corresponding random walk mode, number of rings, and variable sweep config inside the `CRW_sweep()` `switch` selector.

The following pseudocode illustrates the structure of this `CRW_sweep()`.
A concrete example for the simple single-ring QRW system, sweeping over `k1` and `k2` is shown in the [Example](#example) section

```matlab
function [Thru,Drop,vars] = CRW_sweep(KT,Nw,nRings,sweepMode,RWmode)
    % [Thru,Drop] = CRW_sweep(KT,Nw,nRings,sweepMode)
    % Performs a 2D sweep over the random walk parameters
    % Inputs:
    %   KT        = sweep variables
    %   Nw        = number of walks (if RW mode is simulation)
    %   nRings    = number of rings
    %   sweepMode = sweep variable config
    %   RWmode    = randomwalk mode
    
    switch RWmode
        case {'Quantum','Classic'}
            switch nRings                    % Define transfer variables 
                case 1
                    switch RWmode
                        case 'Quantum'
                            RWc = 'QRW(T)';              % random walk command
                            th = KT.th;                  % roherent phase array
                            Tf = @(k1,k2,t1,t2,th) [...] % transfer function matrix
                            
                        case 'Classic'
                            RWc = 'CRW(T)';              % random walk command
                            th = 0;                      % no phase
                            Tf = @(k1,k2,t1,t2,th) [...] % transfer function matrix
                            
                    end
                    switch sweepMode
                        case 'x,y'                       % sweep over x and y parameters
                            v1 = x;                      % Sweeping variable 1
                            v2 = y;                      % Sweeping variable 2
                            vf = getValue()              % get fixe parameter from user
                                                         % Transfer command (string)
                            Tc = ['Tf(x(jj),'...         % sweep variable 1 (jj)
                                     'y(kk),'...         % sweep variable 2 (kk)
                                     'x_(jj),'...        % sweep variable 1 complementary (jj)
                                     'y_(kk),'...        % sweep variable 1 complementary (jj)
                                     'vf)'];             % fixed parameter
                                                         % sweep variables
                            vars = {x.^2,...             % sweep array 1
                                    y.^2,...             % sweep array 2
                                    'x^2',...            % sweep variable 1 label
                                    'y^2'};              % sweep variable 2 label
                    end
            end
    end
end
```


<a name="modify-gui"/>

### Modify the GUI

If custom RW systems are added to `PRR_QRW`, their configurations should appear in the GUI. Hence, the GUI drawing functions must be adapted accordingly in `src/PRR_GUI.m`.
This includes modifying the `initInterface()` function for the new options to appwar, and potentially adding new rules to the drop-down menu callbacks (i.e., `nRings_Callback()`, `sweepMode_Callback()`, `run_enable()`) to guide the user towards the suitable configurations for your system.

## Example

The following code shows the implementation within `CRW_sweep()` for the pre-defined use case of a QRW in a single-ring system, sweeping over `k1` and `k2`, with a fixed `th`:

```matlab
switch nRings                               % number of rings
    case 1
        switch RWmode                       % random walk mode
            case 'Quantum'
                RWc = 'QRW(T)';             % random walk command
                th = KT.th;                 % coherent phase array
                Tf = @(k1,k2,t1,t2,th) [... % transfer matric
                    [0;-k1;0;0;t1],...
                    [0;0;t2*exp(1i*th/2);k2*exp(1i*th/2);0],...
                    [0;t1*exp(1i*th/2);0;0;k1*exp(1i*th/2)],...
                    [0;0;0;1;0],...
                    [0;0;0;0;1]];
        end
         switch sweepMode                   % sweep mode
             case 'k1,k2'
                v1 = k1;                    % sweep variable 1
                v2 = k2;                    % sweep variable 2
                if strcmp(RWmode,'Quantum')
                    th = getValue('theta'); % get fixed variable
                end
                Tc = 'Tf(k1(jj),k2(kk),t1(jj),t2(kk),th)'; % transfer command
                vars = {k1.^2,k2.^2,'k_1^2','k_2^2'}; % variables and labels
         end
```

![image](https://user-images.githubusercontent.com/111191306/186271569-72e86057-d962-46c4-b6a3-955e13d20569.png)

## Publications

<a name="ref-1"/>

\[1\] [Ricardo M. R. Adão, Manuel Caño-García, Jana B. Nieder, Ernesto F. Galvão. "Quantum random walks in coupled photonic ring resonators," 
quant-ph>arXiv:2203.01719 (2021)](https://doi.org/10.48550/arXiv.2203.01719)

## Funding

![image](https://user-images.githubusercontent.com/111191306/186270914-728ac6b0-0919-46fe-8688-4593ee18d068.png)


2019 INL Internal Seed Grant

“Coherent light propagation in photonic quantum walk chips”


# CodinGame

<p align="center">
  <img src="https://user-images.githubusercontent.com/111191306/184722361-472db1d6-30ba-4f6c-97fb-c1dfe3c760a5.png">
</p>

Here is a simple repository with a few of my solutions to CodingGame's puzzles, competitions, and optimization challenges.
Keep in mind that playing CodinGame is something I do for fun when I have a few minutes to spare, so it should be no surprise that most of the solved puzzles in this repository belong to the "easy" cathegory 😊.

However, a quick search in the community discussions and comments shows that some of the puzzles seem to be cathegorized more based on the code length of a solution, rather than the algorithmic complexity.

Below you can find the links to the CondinGame challenges!

## Table of Contents
- [Puzzles](#puzzles)
- [Competitions](#competitions)
- [Optimization](#optimization)

## Puzzles

Solved puzzles:

- Easy puzzles
  - [1D SPREADSHEET](https://www.codingame.com/training/easy/1d-spreadsheet)
  - [ASCII Art](https://www.codingame.com/training/easy/ascii-art)
  - [ASTEROIDS](https://www.codingame.com/training/easy/asteroids)
  - [CROP-CIRCLES](https://www.codingame.com/training/easy/crop-circles)
  - [DEFIBRILLATORS](https://www.codingame.com/training/easy/defibrillators)
  - [DUNGEONS AND MAPS](https://www.codingame.com/training/easy/dungeons-and-maps)
  - [ENCRYPTION/DECRYPTION OF ENIGMA MACHINE](https://www.codingame.com/training/easy/encryptiondecryption-of-enigma-machine)
  - [EQUIVALENT RESISTANCE, CIRCUIT BUILDING](https://www.codingame.com/training/easy/equivalent-resistance-circuit-building)
  - [GHOST LEGS](https://www.codingame.com/training/easy/ghost-legs)
  - [HORSE-RACING DUALS](https://www.codingame.com/training/easy/horse-racing-duals)
  - [LOGIC GATES](https://www.codingame.com/training/easy/logic-gates)
  - [Mars Lander - Episode 1](https://www.codingame.com/training/easy/mars-lander-episode-1)
  - [MIME Type](https://www.codingame.com/training/easy/mime-type)
  - [OFFSET ARRAYS](https://www.codingame.com/training/easy/offset-arrays/solution)
  - [POWER OF THOR - EPISODE 1](https://www.codingame.com/training/easy/power-of-thor-episode-1)
  - [SNAIL RUN](https://www.codingame.com/training/easy/snail-run)
  - [Temperatures](https://www.codingame.com/training/easy/temperatures)
  - [The Descent](https://www.codingame.com/training/easy/the-descent)
  - [Unary](https://www.codingame.com/training/easy/unary)
  
- Medium puzzles 
  - [Death First Search - Episode 1](https://www.codingame.com/training/medium/death-first-search-episode-1)
  - [MAYAN CALCULATION](https://www.codingame.com/training/medium/mayan-calculation)
  - [Shadows of the Knight - Episode 1](https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1)
  - [THE OPTIMAL URINAL PROBLEM](https://www.codingame.com/training/medium/the-optimal-urinal-problem/solution)

## Cmmpetitions  
  - [LEGENDS OF CODE & MAGIC](https://www.codingame.com/multiplayer/bot-programming/legends-of-code-magic)
  
## Optimization
  - [MARS LANDER](https://www.codingame.com/multiplayer/optimization/mars-lander)

<p align="center">
  <img width=300 src="https://user-images.githubusercontent.com/111191306/184678983-c143912a-86b9-4a7f-a63d-8c09d300d55e.gif">
</p>



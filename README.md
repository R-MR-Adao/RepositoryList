# RepositoryList
A public list of my private repositories. If you would like to get access to any of them, please contact me.
<p align="center">
<img src="https://user-images.githubusercontent.com/111191306/186910047-3463fc94-a189-4b0b-b243-f3bb2c44272e.gif">
</p>

This public repository was created as a sharable list of my repositories, here added as clickable submodules. Due to Intellectual Property issues, I cannot publicly share some of those repositories, so I kindly ask you to contact me if you would like to access any of the private ones:

LindeIn: https://www.linkedin.com/in/rmradao/

Below you can find an overview of each repository, built from public data (either my papers or my [Ph.D. dissertation](http://hdl.handle.net/11093/3437)).

## Table of Contents
- [ADAS_SimWorld](#adassimworld)
- [MapAnimator](#mapanimator)
- [NanoPhotonicsToolbox](#nanophotonicstoolbox)
- [WaveBox: O-FDTD](#wavebox)
- [TPP RM21](#tpp_rm21)
- [TPP Designer 3D](#designer-3d)
- [LoRaComSensors](#loracomsensors)
- [PRR QRW](#prr_qrw)
- [CodinGame](#codingame)

# ADAS SimWorld

![ADAS_SimWorld_wide](https://user-images.githubusercontent.com/111191306/198900690-c87a708c-2ea7-41a6-b735-091224d945b8.png)


SimWorld is a synthetic data generation tool for the simulation of sensor-based object detection and tracking around an ego vehicle in an [Advanced Driver Assistance System (ADAS)](https://en.wikipedia.org/wiki/Advanced_driver-assistance_system). 
It was designed for mainly for didactic purposes, and the prototyping of simple detection and tracking algorithms. 

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_basic.gif" />
</p>

## Table Contents
 - [Introduction](#introduction)
 - [Graphical User Interface](#graphical-user-interface)
   - [Main control panel](#main-control-panel)
   - [Simulation visualizations](#simulation-visualizations)
   - [User code editor](#user-code-editor)
   - [Speedometer widget](#speedometer-widget)
 - [Data generation model](#data-generation-model)
   - [Road model](#road-model)
   - [Time progression](#time-progression)
   - [Coordinate rotations](#coordinate-rotations)
   - [3rd person perspective](#3rd-person-perspective)
   - [3D Terrain model](#3d-terrain-model)
   - [Sensor detections](#sensor-detections)
 - [User solutions](#user-solutions)
   - [Solution 1: No tracking](#solution-1-no-tracking)
   - [Solution 2: 2-cycle object tracking and classification](#solution-2-2-cycle-object-tracking-and-classification)
 - [A peek under the hood](#a-peek-under-the-hood)
   - [Software architecture](#software-architecture)
   - [SimWorld inhabitants](#simworld-inhabitants)
   - [Ego Vehicle](#ego-vehicle)
   - [Moving objects](#moving-objects)
   - [Standing Objects](#standing-objects)

## Introduction

ADAS SimWorld is a simple MATLAB toolbox for the quick visualization of synthetically-generated sensor detections and the prototyping of simple object tracking and classification algorithms. 
It simulates the motion of an ego vehicle along a (periodic) road, using four arbitrary sensors to analyze its surroundings. 

All data is generated "on the fly", using a set of base equations. 
As the ego vehicle progresses through the road, it comes across both stationary and moving objects, which get detected by the surrounding sensors. 

This tool provides a simple Graphical User Interface (GUI), which offers a visualization of the real-time simulated world, the object detections in each of the surrounding four sensors' field of view, and a text editor to implement the tracking algorithm code. 

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/pictures/ADAS_SimWorld_RoadMapTopView.png" />
</p>

## Graphical User Interface

The GUI is divided into 5 components, as illustrated in the figure below:
 1. [Main control panel](#main-control-panel)
 2. [Simulation visualizations](#simulation-visualizations)
 3. Sensors' Field of View (FoV)
 4. [User code editor](#user-code-editor)
 5. [Speedometer widget](#speedometer-widget)

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/pictures/ADAS_SimWorld_GUI.png" />
</p>

### Main control panel

The main control panel allows resetting, playing and stepping the simulation, as well as setting some basic configurations. 
These include toggling over the active sensors, and setting a few render parameters (such as speed and resolution). 

The sensor activation/deactivation is illustrated in the video below. 

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_GUI_chooseSensors.gif" />
</p>

### Simulation visualizations

These allow setting the 3D perspective view over the simulation space. 
The video below illustrates how the four sliders surrounding the 3rd person simulation visualization panel can be used to control the zoom (top slider), tilt (right slider), pan (left slider) and rotation (bottom slider). 

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_GUI_views.gif" />
</p>

### User code editor

The GUI offers a simple text editor for the user to implement and quickly test their code. 

As of version `1.0`, the user code API includes only the function `reconstruct_360_space`, which is meant to reconstruct the sensor readings from their sensor-specific coordinate systems to the global ego reference. 
Two solutions are provided for this code, with and without object classification algorithms. 
The GUI is prepared to host more than one code file to implement different functionalities. The code editor allows choosing the file by a drop-down menu at the top-left of the _Main playback_ panel. 

**_NOTE_**: User code files can also be edited directly in the MATLAB IDE

More information on the implementations can be found in [User solutions](#user-solutions) section.

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_userCode.gif" />
</p>

### Speedometer widget

Widget modules can be added to the code as extended visualization tool.
A simple speedometer widget is included as part of the base software as an example of an external add-on.
In this case, this speedometer displays the instant ego speed in km/h, as well as the cumulative traveled distance.

<p align="center">
<img width=250 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_widgetSpeedometer.gif" />
</p>

## Data generation model

All SimWorld data is synthetically generated in real-time as the simulation runs.
This section highlights the main principles and equations for the data generation.

### Road model

The ego's progression along the SimWorld road is obtained from a very simple set of principles and equations.

#### Base principles:
 - The road shape is defined by via a periodic parametric equation.
 - Every object on the road and the elements that build the road itself (e.g. lanes) are governed by the road equation.
 - Each moving object (including the ego vehicle) moved along the road by a fix time dependence equation.
 - The road's parameterization vector is the only pre-established data array. The position and dynamic properties of every moving objects is then deterministically calculated for each moment in time, from the step of equations that define their time-dependent p+properties.
 - The 3rd-person view of SimWorld in the perspective of the ego vehicle is obtained by rotating every environment element around the ego, by and angle $\theta$ defined by orientation of the road at the ego vehicle's position.

#### Base equations:

The road equation is the main SimWorld defining function.
In its most general form, the road shape $F_{\mathrm{road}}$ can be defined as:

$$
F_{\mathrm{road}}(s) =
\begin{bmatrix}
f_\mathrm{road}^{(x)}(s)\\
f_\mathrm{road}^{(y)}(s)\\
f_\mathrm{road}^{(z)}(s)
\end{bmatrix}
$$

where $s$ is a geometrical parameterization, and $f_\mathrm{road}^{(j)}(s),\ j = \{x,y,z\}$ are the road's Cartesian component functions.
Programmatically, $s$ is defined by an array, while $F_{\mathrm{road}}$ is defined by a set of equations.

For simplicity, this base implementation defines $f_\mathrm{road}^{(z)}(s)$,  $f_\mathrm{road}^{(x)}(s) = s$, and $f_\mathrm{road}^{(y)}(s)$ as a function of its $f_\mathrm{road}^{(x)}(s)$, i.e., 

$$
F_{\mathrm{road}}(s) =
\begin{bmatrix}
s\\
f_\mathrm{road}^{(y)}(s)\\
0
\end{bmatrix}
$$

or in other words, $f_\mathrm{road}^{(x)}(s) = x$ and $f_\mathrm{road}^{(y)}(s)=f_\mathrm{road}^{(y)}(x)$.

As mentioned in the [Base principles](#base-principles), $f_\mathrm{road}^{(y)}(x)$ must be periodic.
Moreover, the range of the parameterization array $s$ must be an integer multiple of the periodicity of $F_{\mathrm{road}}$.
This base implementation uses the following function, which complies with these requirements:

$$
f_\mathrm{road}^{(y)}(x) = \frac{T}{3}\sin \left(\frac{2\pi}{T}x\right) \cos \left(\frac{2\pi}{T/3}x\right)
$$

where $T$ is the road period, and thus $s\in\left[nT ,mT \right],\ n < m\ \mathrm{and}\ n,m\in\mathbb{Z}$.

Hence, for simplicity, let us from now on assume that the road is defined along the $XY$ plane (its $z$ component is null).
It is important to notice that $f_\mathrm{road}^{(y)}(x)$ only defines the _center_ of the road.
Since moving objects do not all move along the center, each road lane must be defined along a perpendicular expansion of $f_\mathrm{road}^{(y)}(x)$.
This can be achieved by calculating the vector $U(s)$ that is perpendicular to $F_{\mathrm{road}}(s)$ along the $s$ parameterization,

$$
U(s) = 
\begin{bmatrix}
u_x(s)\\
u_y(s)\\
u_z(s)
\end{bmatrix} =
\frac{\mathrm{d}}{\mathrm{d}s} 
\begin{bmatrix}
-f_\mathrm{road}^{(y)}(s)\\
f_\mathrm{road}^{(x)}(s)\\
0
\end{bmatrix}
$$

which, in its normalized form $U_n$,

$$
U_n(s) =
\frac{U_n(s)}{\lVert U_n(s) \rVert} = 
\frac{U(s)}{\sqrt{u_x^2(s) + u_y^2(s) + u_z^2(s)}}
$$

can be used to express the function $F_\mathrm{lane}$ for a lane displace from the road center by the distance $w,\ w \in \mathbb{R}$ as:

$$
F_\mathrm{lane}(s) =
\begin{bmatrix}
f_\mathrm{lane}^{(x)}(s)\\
f_\mathrm{lane}^{(y)}(s)\\
0
\end{bmatrix} =
F_\mathrm{road}(s) + wU_n(s)
$$

so that, effectively,

$$
F_\mathrm{lane}(s) = 
\begin{bmatrix}
f_\mathrm{road}^{(x)} - w \frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)} \Bigg/ \sqrt{ \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(x)}\right)^2 + \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)}\right)^2 }\\
f_\mathrm{road}^{(y)} + w \frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(x)} \Bigg/ \sqrt{ \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(x)}\right)^2 + \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)}\right)^2 }\\
0
\end{bmatrix}
$$

where the $s$ dependencies on the right side of the equals sign are omitted for syntax simplicity.
The figure below illustrates the lane widening obtained using the equations above.

<p align="center">
<img width=700 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/pictures/ADAS_SimWorld_model_roadLane.png">
</p>

As shown ahead in the [Time progression](#time-progression) section, $F_\mathrm{lane}(s)$ is used not only to draw the road edges, but also to define the trajectory of each moving object.

### Time progression

ADAS SimWorld uses a very simple time progression scheme, where the position of moving objects is governed by a universal equation

$$
s(t) = v_st
$$

where $v_s$ is a constant speed along the parameterization $s$ and $t$ is the time, obtained at iteration $k$ by

$$
t_k = t_{k-1} + \delta t
$$

where $\delta t$ is the simulation's temporal resolution.
Using this, the position of a given moving object (including the ego vehicle), given by

$$
P_\mathrm{mov}(s,t) = 
\begin{bmatrix}
p_\mathrm{mov}^{(x)}(s,t)\\
p_\mathrm{mov}^{(y)}(s,t)\\
p_\mathrm{mov}^{(z)}(s,t)
\end{bmatrix}
$$

becomes

$$
P_\mathrm{mov}(s,t) = F_\mathrm{lane}(s(t)) =
\begin{bmatrix}
f_\mathrm{lane}^{(x)}(s(t))\\
f_\mathrm{lane}^{(y)}(s(t))\\
f_\mathrm{lane}^{(z)}(s(t))
\end{bmatrix} = 
\begin{bmatrix}
f_\mathrm{lane}^{(x)}\bigg|\_{f_\mathrm{road}^{(x)}(s(t))}\\
f_\mathrm{lane}^{(y)}\bigg|\_{f_\mathrm{road}^{(y)}(s(t))}\\
f_\mathrm{lane}^{(z)}\bigg|\_{f_\mathrm{road}^{(z)}(s(t))}\\
\end{bmatrix}
$$

where the $A\big|\_f$ notation represents the application of operator $A$ to the function $f$. 

Using the above-mentioned simplified case where $f_\mathrm{road}^{(z)}(s) = 0$, $f_\mathrm{road}^{(x)}(s) = s \equiv x$ , and $f_\mathrm{road}^{(y)}(s)$ as a function of its $f_\mathrm{road}^{(x)}(s)$, then $P_\mathrm{mov}(s,t)$ becomes simply

$$
P_\mathrm{mov}(x,t) = 
\begin{bmatrix}
f_\mathrm{lane}^{(x)}\bigg|\_{x(t)}\\
f_\mathrm{lane}^{(y)}\bigg|\_{f_\mathrm{road}^{(y)}(x(t))}\\
0
\end{bmatrix} = 
\begin{bmatrix}
x(t) - w \frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)}(x(t)) \Bigg/ \sqrt{ \left(\frac{\mathrm{d}}{\mathrm{d}s} x(t)\right)^2 + \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)}(x(t))\right)^2 }\\
f_\mathrm{road}^{(y)}(x(t)) + w \frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(x)}(x(t)) \Bigg/ \sqrt{ \left(\frac{\mathrm{d}}{\mathrm{d}s} x(t)\right)^2 + \left(\frac{\mathrm{d}}{\mathrm{d}s} f_\mathrm{road}^{(y)}(x(t))\right)^2 }\\
0
\end{bmatrix}
$$

In the present implementation, moving objects are distinguished by their moving direction.
Objects moving in the same direction as the ego vehicle are labeled as _moving_ objects, while objects moving towards the ego are labeled as _oncoming_ objects.
The only distinctive feature between _moving_ and _oncoming_ objects is that the former are modeled using a negative $v_s$ value, while the later use a positive $v_s$.
The dynamic properties of the ego vehicle are equivalent to those of _moving_ objects.

The video below illustrates the result of this time progression scheme for all object types, using green, orange, and cyan circles to illustrate _standing_, _moving_, and _oncoming_ objects, respectively.
The ego vehicle is represented by a red circle.

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_model_timeProgression.gif" />
</p>

As the video shows, objects move continuously along the periodic road (an object moving out of one end of the map comes back from the opposite one).
This is done by keeping track of each object's total traveled distance along the $x$ axis and representing only the remainder of the division by the total length (in $x$) of the road using the [modulo function](https://en.wikipedia.org/wiki/Modulo_operation#:~:text=In%20computing%2C%20the%20modulo%20operation,the%20modulus%20of%20the%20operation).).

Each moving object's rotation about their own rotation center is then obtained from the orientation $\theta_l$ of the object's lane at their current position $P_\mathrm{mov}(x,t)$, relative to the $X$ axis

$$
\theta_l(t) = \arctan\left(
\frac{\mathrm{d}}{\mathrm{d}t} f_\mathrm{lane}^{(y)}(s(t))
\bigg/
\frac{\mathrm{d}}{\mathrm{d}t} f_\mathrm{lane}^{(x)}(s(t))
\right)
$$

**_NOTE:_** All usages of the $\arctan$ function should be regarded as its `atand2` range-modified implementation.

Details about how object rotations are obtained can be found in the [Coordinate rotations](#coordinate-rotations) section.

### Coordinate rotations

All coordinate transformations are performed using [rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix).

$$
R_{X}(\theta) = 
\begin{bmatrix}
1 & 0            & 0            \\
0 & \cos(\theta) & -\sin(\theta)\\
0 & \sin(\theta) & \cos(\theta)
\end{bmatrix},\ \  
R_{Y}(\theta) = 
\begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta)\\
0            & 1 & 0           \\
-\sin(\theta) & 0 & \cos(\theta)
\end{bmatrix},\ \  
R_{Z}(\theta) = 
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0\\
\sin(\theta) & \cos(\theta)  & 0\\
0            &               & 1
\end{bmatrix}
$$

where $R_X$, $R_Y$, and $R_Z$ are the rotation matrices that rotate a Cartesian matrix $A$ around the $X$, $Y$, and $Z$ axes, respectively by

$$
A_r^{(\theta)} = R_j(\theta)A
$$

where $A_r^{(\theta)}$ is the rotation of matrix $A$ by and angle $\theta$ about the $j$ axis, with $j = \{X,Y,Z\}$.

Since we have pre-established that in the present SimWorld implementation the road is limited to the $XY$ plane, all the necessary rotations are performed about the $Z$ axis.
Thus, instead of performing a lot of unnecessary calculations (multiplying and summing a lot of ones and zeros), it is computationally more efficient to simply reduce the rotation to a 2D problem 

$$
R(\theta) = 
\begin{bmatrix}
\cos(\theta) & -\sin(\theta)\\
\sin(\theta) & \cos(\theta)
\end{bmatrix}
$$

and allow all rotated objects to retain their $z$ components, i.e. for a matrix $P = [p_x\ \ p_y\ \ p_z]^\intercal$, its rotated matrix $P_r^{(\theta)}$ is given by

$$
P_r^{(\theta)} =
\begin{bmatrix}
R(\theta)P_{x:y} \\
p_z
\end{bmatrix}
\equiv \mathcal{R}(\theta,P)
$$

For syntax simplicity, let $\mathcal{R}(\theta,P)$ be the function that calculates $P_r^{(\theta)}$ from $P$ in the above manner.

**_NOTE_**: MATLAB allows multiplying a rotation matrix against a list of coordinates in one go using the following notation:
```
P_r = XYZ*R';
```

where `XYZ` is an $n\times3$ array containing the $xyz$ coordinates of $n$ points, `R` is a rotation matrix, and `P_r` stores the rotated coordinate list.
Applied to an explicit 2D example, this is equivalent to the following:

```
P_r = [x(:),y(:)]*[cos(t) -sin(t);...
                   sin(t)  cos(t)]';
``` 

where `x` and `y` are arrays containing the $x$ and $y$ coordinates to be rotated.

Objects' coordinates can be rotated using $\mathcal{R}(\theta,P)$ around the object's own center of rotation (e.g.as the object moves along the road), and/or about the ego vehicle (for 3rd person perspective).
The former does not change the objects position, but merely rotates the coordinates of the vertices that make up its cube around the $Z$ axis.
The latter is addressed in more detail in the [3rd person perspective](#3rd-person-perspective) section.
The application of $\mathcal{R}(\theta,P)$ is illustrated the video below.

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/videos/ADAS_SimWorld_model_Rotation.gif" />
</p>

### 3rd person perspective

The 3rd person perspective around the ego vehicle (bottom-right axes of the GUI) is obtained by rotating each object in the simulation space (including the road) around the ego vehicle.
Hence, the ego vehicle itself is represented (in red) as a stationary object at position $(0,0)$, while every other object is rotated about the $Z$ axis by the angle $\theta_\mathrm{ego}(t)$, the orientation of the ego vehicle at time $t$, relative to the $X$ axis.
$\theta_\mathrm{ego}(t)$ can be calculated analogously to $\theta_l(t)$.
Considering that the ego vehicle moves directly along the road function ( $w_\mathrm{ego} = 0$ ), then we can express it as

$$
\theta_\mathrm{ego}(t) = -\arctan\left(
\frac{\mathrm{d}}{\mathrm{d}t} f_\mathrm{road}^{(y)}(s(t))
\bigg/
\frac{\mathrm{d}}{\mathrm{d}t} f_\mathrm{road}^{(x)}(s(t))
\right) = -
\arctan\left(
\frac{\mathrm{d}}{\mathrm{d}t} f_\mathrm{road}^{(y)}(x(t))
\bigg/
\frac{\mathrm{d}}{\mathrm{d}t} x(t)
\right)
$$

where the minus sign is used by convention to simplify the notation of objects around the ego vehicle.

Hence, the total object rotation can be expressed as 

$$
C_{r,\mathrm{stand}}^{(\theta_\mathrm{ego})}(t) = \mathcal{R}(\theta_\mathrm{ego}(t),C_\mathrm{stand})
$$

for standing objects, and 

$$
C_{r,\mathrm{mov}}^{(\theta_\mathrm{ego}+\theta_l)}(t) = \mathcal{R}(\theta_\mathrm{ego}(t) + \theta_l(t),C_\mathrm{mov})
$$

for the moving objects, where $C_\mathrm{stand}$ and $C_\mathrm{stand}$ represent the list of vertices that make up the shape of standing and moving objects, respectively.

As to the objects' position, all objects (stationary and moving alike) have their position vectors $P$ rotated around the $Z$ axis by the angle $\theta_\mathrm{ego}(t)$, i.e.,

$$
P_{r,j}^{(\theta_\mathrm{ego})}(t) = \mathcal{R}(\theta_\mathrm{ego}(t),P_j(t))
$$

where $j = \{\mathrm{stand},\ \mathrm{mov}\}$.

The figure below illustrates both the orientation and position rotation around the ego vehicle performed to obtain the 3rd person's perspective view.

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc\pictures\ADAS_SimWorld_model_3rdPersonPerspective.png"/>
</p>

Including the road periodicity in this representation is obtained by always rendering half a road-length ahead and behind of the ego vehicle, while each object's position is represented always within the load length range (remember that in this perspective the ego is represented as stationary at $(0,0,0)$ ).

To optimize the rendering speed, objects outside the current zoom field of view are not represented.
Also, the 3D terrain surfaces is only represented using the `surf` function if the title angle is above $20^o$ and the terrain depth is larger than $5$ m.
Otherwise, the road is represented using a more efficient (and less pixelized) 2D patch.

### 3D Terrain model

SimWorld's terrain is modeled by defining its elevation ( $z$ component) using a 2D [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function), which is typically expressed as

$$
G_\mathrm{2D} = a\exp\left(-\left(\frac{
\sqrt{ (\mathcal{X} - b_1)^2 + (\mathcal{Y} -b_2)^2 } }
{c} \right)^2\right)
$$

where $\mathcal{X}$ and $\mathcal{Y}$ are the meshgrids that defined the $XY$ plane, $a$ and $c$ are the peak height and width of the Gaussian distribution, and $(b_1,b_2)$ are the $(x,y)$ coordinates of the Gaussian peak center.
This leads to a single-peaked distribution as depicted below.

In SimWorld, however, instead of a single-peak distribution, a modification of the 2D Gaussian is used to represent the 3D terrain along the road by modulating an _extended_ Gaussian peak along $\mathcal{Y} = f_\mathrm{road}^{(y)}(\mathcal{X})$, i.e.,

$$
G_\mathrm{road} = a\exp\left(-\left(\frac{
\sqrt{ \left(\mathcal{Y} - f_\mathrm{road}^{(y)}(\mathcal{X})\right)^2 }}
{c} \right)^2\right) =
a\exp\left(-\left(\frac{\mathcal{Y} - f_\mathrm{road}^{(y)}(\mathcal{X}) }{c} \right)^2\right)
$$

The figure below illustrates the difference between the typical single-peaked 2D Gaussian function, and the SimWorld road-Gaussian

<p align="center">
<img width=800 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc\pictures\ADAS_SimWorld_model_3DTerrain.png"/>
</p>

Yet, since the road is by convention of the current implementation restricted to the $XY$ plane ( $f_\mathrm{road}^{(z)}(s) = 0$ ), the terrain topography is effectively obtained by

$$
T_\mathrm{road} = a\left(\exp\left(-\left(\frac{\mathcal{Y} - f_\mathrm{road}^{(y)}(\mathcal{X}) }{c} \right)^2\right) - 1\right)
$$

where $a$ and $c$ are optimized to fit the road width, and the road area itself is cropped out of $T_\mathrm{road}$.

### Sensor detections

The sensor readings are obtained in two simple steps:
First, rotating the position of all SimWorld objects around the ego vehicle by the sensor mounting angle $\theta_s^{(0)}$

$$
P_{r,j}^{(\theta_s)}(t) = 
\begin{bmatrix}
p_{r,j}^{(\theta_s,x)}(t) \\
p_{r,j}^{(\theta_s,y)}(t) \\
p_{r,j}^{(\theta_s,z)}(t)
\end{bmatrix} =
\mathcal{R}\left(\theta_s,P_{r,j}^{(\theta_\mathrm{ego})}(t)\right) 
$$

where $j = \{\mathrm{stand},\ \mathrm{mov}\}$.
Then, determining which objects lie within the sensor field field of view, i.e., the objects whose distance $d_P^{(s)}(t)$ from the sensor

$$
d_P^{(s)}(t) = \left\lVert P_{r,j}^{(\theta_s)}(t) \right\rVert
$$

is shorter than the sensor range $r_s$, and azimuth $\theta_P^{(s)}(t)$ and polar $\phi_P^{(s)}(t)$ angular coordinates relative to the sensor frame

$$
\theta_P^{(s)}(t) = \arctan\left( 
p_{r,j}^{(\theta_s,y)}(t) \bigg/ p_{r,j}^{(\theta_s,x)}(t)
\right)
$$

$$
\phi_P^{(s)}(t) = \arccos\left(\frac{
p_{r,j}^{(\theta_s,z)}(t)}
{d_P^{(s)}(t)}
\right)
$$

lie within the sensor angular ranges $[-\theta_s/2, \theta_s/2]$, $[-\phi_s/2, \phi_s/2]$, respectively.

In this base implementation however, for simplicity, the vertical components of the objects' positions is ignored.
Hence, 

$$
d_P^{(s)}(t) \approx \left\lVert P_{r,j|x:y}^{(\theta_s)}(t) \right\rVert
$$

and only the azimuth range is considered, as illustrated in the figure blow.

<p align="center">
<img src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/pictures/ADAS_SimWorld_model_sensorDetections.png"/>
</p>


## User solutions

The main goal of ADAS SimWorld is to offer a simulation platform for detection processing algorithm prototyping.
This implementation is mainly focused in the synthetic generation of data that can be used to test new algorithms, or for didactic purposes, so that new-learners can get acquainted with tracking algorithms.

Hence, this base implementation offers two simple codes for processing the sensor-wise object detections and transform them from the sensor-specific coordinate systems to the combined 360 $^o$ environment around the ego vehicle, which are described below:
 1. Performing only the necessary coordinate transformations
 2. Performing a two-cycle object tracking to classify objects into _staning_, _moving_, or _oncoming_ objects, based on their kinematic properties.

As an input, the user receives up to two input arguments, `sensor` and `ego`, which contain the following dataset:

`sensor`:
 - `sensor.n`: number of sensors
 - `sensor.fov`: (m,deg) field of view distance and angular ranges
 - `sensor.theta`: (deg) sensor mounting angles
 - `sensor.pos`: sensor position (`FL`,`RL`,`RR`,`FR`)
 - `sensor.active`: boolean if sensor is active
 - `sensor.data`: (m) object xy data measured by each sensor
 
where `sensor.data` is restricted to the $XY$ plane.
Since the user is agnostic to the transformations performed internally to obtain the sensor-specific data, let $P_{x:y}^{(s)}$ represent the sensor measurements received as input by the user at the simulation timestamp $t$

$$
P_s = P_{r,j|x:y}^{(\theta_s)}(t)
$$
 
`ego` (optional):
 - `ego.Dtheta`: (deg) ego vehicle moving direction angle
 - `ego.v_xy`: (m/s) ego vehicle velocity
 - `ego.v`: ego speed
 - `ego.dt`: simulation cycle duration

### Solution 1: No tracking

The first ans simpler solution can be summarized as the trivial coordinate transformation from the sensor-specific reference system to the unified ego vehicle's.
This can be done by iterating over each sensor and using $\mathcal{R}(\theta_s^{(0)},P_s)$ to perform the rotation around the ego vehicle.

The key part of the first user solution is presented below.

```
% rotation matrix (degrees)
    rd = @(x,y,t) [x(:),y(:)]*[cosd(t) -sind(t);...
                               sind(t) cosd(t)]';
for ii = 1 : sensor.n                           % iterate over sensor array
    if sensor.active(ii)                        % sensor is active by the user
        theta = sensor.theta(ii);               % sensor mounting angle
        obj_x = sensor.data{ii}(:,1);           % object position x
        obj_y = sensor.data{ii}(:,2);           % object position y
        obj = cat(1,obj,rd(obj_x,obj_y,theta)); % object rotated
    end
end
```

### Solution 2: 2-cycle object tracking and classification

The second user-solution provided by this base implementation of ADAS SimWorld builds on the first solution by using the provided `get_obj_prev()` function to obtain the object positions in the previous cycle.
This allows calculating the object displacement since the previous cycle and the object absolute velocity, which allows a basic classification into _standing_, _moving_, or oncoming_ objects types.

Calculating the kinematic properties of the tracked objects is the challenging part of this solution, since we must validate the current cycle detections against those of the previous cycle, and determine which detections correspond to which.
This gets further complicated by the fact that some objects will have left the sensor field of view from one cycle to the next, while other will have entered it.

This filtering step is done by calculating the displacement between each pair of current and previous detections and finding the closest previous-to-current object detection.
If the calculated displacement tends to zero, we can be confident that this corresponds to a standing objects.
Otherwise, we must declare a maximum admissible inter-cycle displacement and discard detections whose displacement are above that threshold.
The remaining detections can then be classified into _moving_ or _oncoming_ depending on the $x$ component of their velocity:

 - Objects with a considerably negative and positive $x$ velocity are classified as _oncoming_ and _moving_ respectively.
 - Objects with an $x$ velocity close to zero get no classification, meaning that they are probably crossing objects moving sideways relative to the ego vehicle.

The key part of the second user solution is presented below.

```
% get identified object list from previous cycle
obj_prev = get_obj_prev(sensor,ego);    % object list previous cycle

if ~isempty(obj)
    % compensate ego rotation in previous cycle
    obj_prev = rd(obj_prev(:,1),obj_prev(:,2),ego.Dtheta);

    % calculate displacement matrix
    d_x = bsxfun(@minus,obj(:,1), obj_prev(:,1)');  % displacement x
    d_y = bsxfun(@minus,obj(:,2), obj_prev(:,2)');  % displacement x
    d_mat = sqrt(d_x.^2 + d_y.^2);                  % displacement abs

    % find the closest object from the previous cycle
    [dmin,imin] = min(abs(d_mat),[],2);                 % min d and ind
    ind = sub2ind(size(d_x), (1:length(imin))', imin);  % matrix ind

    % calculate object x y velocity
    obj_v = bsxfun(@plus,[d_x(ind),d_y(ind)]/ego.dt,ego.v_xy);% vel xy

    % identify tracked objects
    obj_tracked = obj(dmin <= thresh_d_max,:);  % tracked objects list
    obj_v(dmin > thresh_d_max,:) = [];          % tracked objects speed

    % calculate absolute velocity
    obj_speed = sqrt(obj_v(:,1).^2 + obj_v(:,2).^2); % obect speed
    obj_v_sign = obj_speed .* sign(obj_v(:,1)); % x-dir signed speed

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %                     Object classification                       %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % standing objetcs
    stand = obj_tracked(obj_speed < thresh_v_stand_max,:);

    % moving objects
    mov = obj_tracked(obj_v_sign > thresh_v_mov_min,:);

    % oncoming objects
    onc = obj_tracked(obj_v_sign < -thresh_v_mov_min,:);

    % output updated object list to base workspace
    assignin('base','obj_prev',obj);
end
```

**_NOTE_**:  The function `bsxfun()` is used for backwards compatibility with legacy MATLAB versions that do not allow inconsistent sized matrix operations.

## A peek under the hood

### Software architecture

ADAS SimWorld software architecture can be split into two main parts: the initialization and the simulation run.
The initialization architecture is done in a straightforward manner, as depicted in the diagram below.

<p align="center">
<img width=800 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/diagrams/ADAS_SimWorld_architecture_initialization.png"/>
</p>

Once all function handles are initialized, all interactions with the simulation tool are done via the GUI.
The last initialization step is to reset the simulation.
The simulation reset is done by calling the callback function of the GUI Reset button.
This function initializes all simulation objects and their associated graphics, i.e., the handles to the graphics that represent the simulation data in the visualization axes.

When the `Start` or `Step` buttons are called from the GUI, the simulation proper is executed as described in the diagram below.
The process is repeated as long as the play button is in a pressed state.

<p align="center">
<img width=700 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/diagrams/ADAS_SimWorld_architecture_SimulationRun.png"/>
</p>

### SimWorld inhabitants

The three types of SimWorld objects can be distinguished by their shape and color, as shown in the figure below.

<p align="center">
<img width=600 src="https://github.com/R-MR-Adao/ADAS_SimWorld/blob/master/doc/pictures/ADAS_SimWorld_Objects.png"/>
</p>

Apart from the _moving_ and _oncoming_ objects, which are both of the type moving object, each object type has unique properties, as listed below:

### Ego Vehicle
Kinematic properties:
 - `v`: (m/s) ego speed
 - `x(t,x_1)`: (m) ego $x$ position function
 - `y(x)`: (m) ego $y$ position function
 - `x_1`: (m) ego $x$ position in previous cycle
 - `theta`:(rad) ego orientation
 
**_NOTE_**: `ego.theta` is the only angle defined in radians.
 This is done by convention to clearly distinguish between the object rotation (translation about ego vehicle) and orientation (object's orientation) angles when implementing the 3rd person visualization.

Visualization properties:
 - `cube`: cube object for graphical representation
 - `cube.dimensions`: (m) cube dimensions
 - `center`: (m) cube center position
 - `cube.theta`: (deg) cube orientation
 
Sensor properties:
 - `sensor`: sensor object
 - `sensor.n`: number of sensors
 - `sensor.fov.range`: (m) sensor range
 - `sensor.fov.theta`: (deg) sensor angular range
 - `sensor.theta`: (deg) sensor orientation
 - `sensor.fov.draw`: sensor drawing object
 - `sensor.fov.draw.s`: sensor drawing parameter
 - `sensor.fov.draw.fov`: sensors field of view edge
 - `sensor.fov.draw.circ`: sensor-specific FoV edges
 - `sensor.key`: sensor mounting position

### Moving objects

Kinematic properties:
 - `n`: number of moving objects
 - `v`: (m/s) moving object speed
 - `t0`: (s) random starting position (modeled by a time $t_0$ along $x(t)$ )
 - `off`: (m) y offset relative to ego (lane position)
 - `lane`: lane object
 - `x_t(t,x_1)`: (m) moving object x position function
 - `x(t,dt,x_1)`: (m) in-lane moving object x position
 - `y(t,dt,x_1)`; (m) in-lane moving object y position
 - `x_1`: (m) moving object x position in previous cycle
 
 Visualization properties:
 - `cube`: list of cube objects
 - `cube(:).dimensions`: (m) moving object dimensions
 - `cube(:).theta`: (deg) cube orientation
 - `cube(:).x`: (m) cube center x position
 - `cube(:).y`: (m) cube center y position
 - `cube(:).z`: (m) cube center z position
 - `cube(:).idx`: cube vertex drawing indices

### Standing objects

Kinematic properties:
 - `n`: standing (static) objects properties
 - `x`: (m) standing object x position
 - `y`: (m) standing object y position
 - `z`: (m) standing object z position
 
Visualization properties
 - `faces`: indices of tree-shaped patch faces
 - `color`: standing object color map
 - `shape`: list of shape objects
 - `shape(:).dimensions`: randomized tree-shape dimensions
 - `shape(:).theta0`: shape initial orientation
 - `shape(:).theta`: ego orientation (required for 3rd person perspective rotation)
 - `shape(:).faces`: object-specific patch faces
 - `shape(:).vertices`: shape vertices


# MapAnimator

![](https://github.com/R-MR-Adao/map_animator/blob/master/doc/map_animator_wide.png)

A `Python`-based tool to animate a pre-set trajectory over a map.

<div align="center">
  <image src="https://github.com/R-MR-Adao/map_animator/blob/master/doc/example_output.gif" />
</div>

# Table of Contents
- [Map animator](#map-animator)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [`Python` Installation](#python-installation)
  - [Module Requirements](#module-requirements)
  - [Launch the tool](#launch-the-tool)
- [Using the tool](#using-the-tool)
  - [Designing your maps](#designing-your-maps)
  - [Generating the animation trajectory](#generating-the-animation-trajectory)
  - [Building the animation](#building-the-animation)
- [Configuration file](#configuration-file)
- [Example](#example)


# Getting Started

If you are already a `Python` user, you will have no trouble using this tool.
All you need to do is to make sure your environment fulfills the requirements and you're good to go.

However, for those less experienced with `Python`, the following sections explain how you can get your setup up and running.

## Installation

In this open-source repository, I am sharing the source code that implements the tool.
Thus, there is no installation package required to use it.

If you don't have it already, all you need to do is to
  1. Download the source code by cloning the repository or pressing the `Code` -> `Download ZIP` buttons and extracting the files into a directory of your choice.
  2. Install `Python`
  3. Install the required modules
  4. Launch the tool

## Launch the tool

Once you have completed the installation steps and installed the required modules, you can launch the tool by either:

1. double-clicking on the [launcher.bat](https://github.com/R-MR-Adao/map_animator/blob/master/launcher.bat) file, or
2. opening a terminal (or command prompt) and navigate to the directory where the source code is located. Then, run the following command:
    ```bash
    cd [map_animator_directory]
    python launcher.py
    ```

This will start the tool, and you can now proceed to use it as described in the next section.

# Using the tool

Producing a map animation with this tool can be done in just three steps:

1. [Designing your maps](#designing-your-maps)
2. [Generating the animation trajectory](#generating-the-animation-trajectory)
3. [building the animation](#building-the-animation)

When you [launch the tool](#launch-the-tool), you can choose the execution mode by editing the `mode` parameter in the [config.json](https://github.com/R-MR-Adao/map_animator/blob/master/config.json) file.
This parameter can take the following options:

- `"generate"`: to generate the animation trajectory
- `"animate"`: to build the animation
- `"CLI"` (default): to choose the execution mode by passing the designated keyword to the command line interpreter.

Upon launching the tool using the `"CLI"` mode option, you are presented with the following interface:

```
Please type one of the following options:
    'g' to generate a new trajectory
    'a': to build animation
    'q': to quit the CLI
 ("g", "a", "q"): _
```

which you can use to call the `Animator` methods.

The `"g"` and `"a"` commands can be called multiple times.
Every time a command is inserted, the config and data files are reloaded.
This allows you to iteratively optimize the animation parameters in the [configuration file](#configuration-file) described ahead

## Designing your maps

This step must be done using any `CAD` software of your choice.
IF you have no preference, I would personally recommend [Inkscape](https://inkscape.org/), an awesome free vector graphical editor that will allows building all sorts of illustrations.

In order to use this tool, you will have to export at least two images: (in any normal bitmap format such as `*.jpeg` or `*.png`):

1. The actual map that will show in the background
2. The trajectory map: almost empty image with the exact same dimensions as the background map, but containing only a fine line along the trajectory you wish to animate.

**Important**: Best results are obtained by exporting the road as a basic color (pure red, green, or blue). The chose color must match the `path->color` configuration in the [configuration file](#configuration-file)

Here is an example of a simple map design.

<div align="center">
  <image src="https://github.com/R-MR-Adao/map_animator/blob/master/doc/example_simulation.png" />
</div>

For better performance
   1. "simulate" the span of the visualization window
   2. take note of its dimensions (in pixels) and add them to the `display->figure_size` configuration in the [configuration file](#configuration-file)
   3. make sure to have enough of a margin around the visualization window, to prevent stepping out of your map design.

Once you have a design, save the background and road files in the [resources](https://github.com/R-MR-Adao/map_animator/blob/master/resources/) folder.
Make sure that the file names designated in the `maps->map_back` and `maps->map_road` settings of the [configuration file](#configuration-file) match the file names under which you stored your design images.

Examples of the two required map image files can be found in [map_back.png](https://github.com/R-MR-Adao/map_animator/blob/master/resources/map_back.png) and [map_road.png](https://github.com/R-MR-Adao/map_animator/blob/master/resources/map_road.png) in the [resources](https://github.com/R-MR-Adao/map_animator/blob/master/resources/) folder.

## Generating the animation trajectory

To generate a new trajectory either:
 - set `mode` to `"generate"` and execute the launcher script
 - set `mode` to `"cli"`, execute the launcher script, and choose the `"g"` option

Once launched, the `Animator` will identify the trajectory path from the input `map_road` and apply a recursive filter to sort the correct order of the points in the supplied image.
The path generation results can be optimized by editing the `filters->diff_threshold` and `filters->recursion_limit` parameters.

During the path generation, you will be informed of the trajectory filter progress

```
Apllying recursive positional filter 0/2
Apllying recursive positional filter 1/2
Apllying recursive positional filter 2/2
Save coordinates to data file? ("y", "n"): _
```

Despite the recursive filters, the generated path will likely contain a few unsorted points at the end of the trajectory.

The figure below illustrates the a map design and the generated trajectory.
As it can be seen, the generated path is mostly correct except for a few straight lines at the end of the path.

The best way to deal with this effect is to save the generated path as a text data file, and delete the last few points (it should be pretty simple to identify the erroneous points).

<div align="center">
  <image src="https://github.com/R-MR-Adao/map_animator/blob/master/doc/example_generated_path.png" />
</div>

Once you are done with generating and editing the animation path, make sure that the exported file name matches the `path->path_road` setting in the [configuration file](#configuration-file).
An example of an exported data file can be found in [path_road.dat](https://github.com/R-MR-Adao/map_animator/blob/master/resources/path_road.dat) in the [resources](https://github.com/R-MR-Adao/map_animator/blob/master/resources/) folder.

## Building the animation

To build the animation either:
 - set `mode` to `"animate"` and execute the launcher script
 - set `mode` to `"cli"`, execute the launcher script, and choose the `"g"` option

Cone launched, you will see the generation being rendered, and a loading bar will be shown on the terminal with a prediction of the remaining time

```
  1%|█                                                                | 4/342 [00:01<01:17,  4.34it/s]
```

Here is the result of using the current [config.json](https://github.com/R-MR-Adao/map_animator/blob/master/config.json) file and resources available in the [resources](https://github.com/R-MR-Adao/map_animator/blob/master/resources/) folder

<div align="center">
  <image src="https://github.com/R-MR-Adao/map_animator/blob/master/doc/example_output.gif" />
</div>

Once finished, if the `output->mode` setting is set to `"save"`, you will have a chance to browse an select a file in which to save the generated animation. 

# Configuration file

The configuration file has the following structure
```jsonc
{
    "mode": "cli",                                  # execution mode
    "maps": {                                       # list of maps to be imported
        "map_back": "resources/map_back.png",       # "actual" map to show on the background
        "map_road": "resources/map_road.png"        # map containing the path to thread along
    },
    "path":{                                        # path settings
        "path_road": "resources/path_road.dat",     # data file where generated path is stored
        "color": [0,0,255],                         # color of road line in map_road
        "starting_direction": "east"                # path starting direction
    },
    "filters": {                                    # path-generation filters
        "diff_threshold": 5,                        # derivative rejection threshold
        "recursion_limit": 2                        # number of filter iterations
    },
    "output": {                                     # output settings
        "mode": "save",                             # "save" / "preview"
        "skip": 5,                                  # number of points to skip for animation
        "frame_duration": 50,                       # (ms) duration of each frame
        "loop": 0                                   # number of git file loops (0 for infinite)
    },
    "display": {                                    # display settings
        "figure_size": [960, 540],                  # display figure size
        "FoV": [676, 384],                          # field of view size
        "camera_smooth": 10,                        # camera smooth box width
        "line_width": 8,                            # width of displayed line
        "line_color": [0.7, 0.3, 0],                # displayed line color
        "line_style": "-"                           # displayed line style
    }
}
```

# Example

Here is an example of a personal application used as part of my [video on Instagram](https://www.instagram.com/reel/Cu2I9lXoe4V/?igshid=MTc4MmM1YmI2Ng%3D%3D), to illustrate my trip from Águeda (Portugal) to Bertrange (Luxembourg) and Calais (France).

<div align="center">
  <image src="https://github.com/R-MR-Adao/map_animator/blob/master/doc/example_output_2.gif" />
  <p style="text">A reduced size example</p>
</div>


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



# SolarVault :: The DIY Solar Battery

![logo](https://github.com/carforge/solarvault/assets/29213494/9ef1d83a-3947-496c-854d-47b59f99cea7)
*[AI Generator: Midjourney](https://www.midjourney.com)*

### Video Demo
[![YouTube Video-Demo](https://img.youtube.com/vi/tJiyDAhUlIg/0.jpg)](https://youtu.be/tJiyDAhUlIg)

### Background [WIP]
I run a balcony power plant at home. Ultimately, it's nothing more than a small solar system with a capacity of 600Wp (an upgrade to 800Wp is already planned). The solar power is simply fed into the grid through the socket. Even when I work from home, with my laptop and two monitors running, I often produce more electricity on sunny days than I consume. This excess electricity simply flows back into the grid and is not compensated. Admittedly, it's not much. Nevertheless, I would like to store this surplus to charge my devices like phones or laptops at night.

### Concept [WIP]
In a more or less portable box, there will be a lithium battery that is to be charged with excess solar power. Whenever the solar system produces more electricity than I consume, the excess power will be stored in the battery. For this, I use a Raspberry Pi, which runs a web server and can set the voltage and current for charging via an API. A power supply with a USB interface is connected to the Raspberry Pi for this purpose.

### Bill Of Material [WIP]
* 1x Raspberry Pi 1 Model B
* 1x Hanmatek PSU with USB interface
* 1x Lithium Battery Pack (leftover of another project)

### To-Do
* Make the current output power readable

import numpy as np

k = 1.38064852e-23 #Boltzmann constant
c = 299792458.0    #speed of light m/s

#Transformacion de dBm's a potencia
P = lambda source: 10.0**((source - 30.) / 10.0)

def deg2arcsec(angle):
    """
        angle: antenna beam solid angle in deg for transformation to arcsecs.
        """

    asec = angle * 3600.0
    return asec


def Radio_source_trans(Radio_source, freqs, Bwidth):
    """
    Parameters:
        Radio_source: the data of the antenna that needs to be converted
        freqs: The frecuecy range in MHz
        Bwidth: the Bandwidth in Hz
        """

    area = 1.0           # m^2
    angle = 55.0    #degrees
    theta = deg2arcsec(angle)

    power = np.array(P(Radio_source), dtype=np.float64)

    #the units of the flux density are W m^-2 MHz^-1
    flux = np.array((2.0 * power / area) * Bwidth, dtype=np.float64)

    flux_Jy = np.array(flux * 1e26, dtype=np.float64)  # Jy
    flux_Jy = np.array(flux_Jy * 1e3, dtype=np.float64) # mJy

    freq = np.array(freqs * 1e6, dtype=np.float64) #Hz
    wavelength = np.array((c / freq) * 100., dtype=np.float64)  # cm

    T = np.array(1.36 * flux_Jy  * wavelength**2 / theta**2, dtype=np.float64)

    return T

def Res2Temp(res_source, Bwidth):
    """
    Transfomation to temperatura for a electronic source
    """
    power = P(res_source)
    T = power / (k * Bwidth)

    return T

#x = Radio_source_trans(-215.26, 124.91, 1.0)
#print (x)

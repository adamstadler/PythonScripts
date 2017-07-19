#import extra packages
import numpy as np
import sys

#import coronagraph package
import coronagraph as cg

#Initialize the specific telescope
telescope = cg.Telescope()

#Initialize specific planet
planet = cg.Planet()

#Initialize specific star
star = cg.Star()\

#read in the choice of planet wavelength and reflectance
#USAGE: Column 1 --> wavelength of planet
#       Column 2 --> reflectance spectra of planet
model = np.loadtxt(sys.argv[1])
lam = model[:,0]        #wavelength of planet in microns
refl = model[:,1]       #reflectance spectra of planet


#SKIP - Read for specific planet and star data
"""
#Read in wavelength, reflectance model
model = np.loadtxt('/home/astadler/coronagraph_noise/coronagraph/planets/Mars_geo_albedo.txt')
lam = model[:,0]            # wavelength (microns) Jupiter
refl = model[:,1]           # geometric albedo for Jupiter

#Read in solar flux
star_model = np.loadtxt('SOLAR_FLUX_G2V_pickles_uk_26.ascii.txt', skiprows = 38)
s_wavelength = star_model[:,0]/10000 #convert from angstrom to microns
solhr = star_model[:,1]          # solar flux


"""

#find which has higher resolution
diff_lam = np.mean(np.diff(lam))
diff_sol_wavelength = np.mean(np.diff(solhr))


#intepolate the lower resolution data into the higher one
if diff_lam < diff_sol_wavelength:
        wavelength_output = lam
        reflectance_interp = refl
        solhr_interp = np.interp(wavelength_output, s_wavelength, solhr, left=np.nan, right = np.nan)
else:
        wavelength_output = s_wavelength
        solhr_interp = solhr
        reflectance_interp = np.interp(wavelength_output, lam, refl, left=np.nan, right=np.nan)

#For debugging purposes, make sure they're the same size after interpolation.
print(wavelength_output.shape)
print(reflectance_interp.shape)
print(solhr_interp.shape)

# Specify telescope integration time in hours
integration_time = 10.0

# Observe!
lam, dlam, Cratio, spec, sig, SNR = \
      cg.generate_observation(wavelength_output, reflectance_interp, solhr_interp, integration_time, telescope, planet, star)
"""
lam, dlam, Cratio, spec, sig, SNR = \
      cg.generate_observation(lam, refl, solhr, integration_time, telescope, planet, star)
"""                                                                                                                                   62,0-1        50%

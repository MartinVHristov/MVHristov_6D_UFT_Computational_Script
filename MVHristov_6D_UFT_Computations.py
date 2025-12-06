#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MVHristov_6D_UFT_Computations.py
Computational Demonstrations for the 6D Unified Field Theory (6DUFT)
Author: Martin V. Hristov
Year: 2025

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.signal import butter, filtfilt, welch
import os

# ============================================================================
# PHYSICAL CONSTANTS
# ============================================================================

G = 6.67430e-11            # Gravitational constant [m^3 kg^-1 s^-2]
c = 299792458.0            # Speed of light [m/s]
hbar = 1.054571817e-34      # Reduced Planck constant [J·s]
m_p = 1.67262192369e-27     # Proton mass [kg]
M_sun = 1.98847e30          # Solar mass [kg]
kpc = 3.085677581e19        # Kiloparsec [m]

# ============================================================================
# THEORY PARAMETERS
# ============================================================================

class TheoryParameters:
    """Parameters for the 6D Unified Field Theory (illustrative values)."""

    def __init__(self):
        self.V_phi = 1.0e-8
        self.K_theta = 1.0e3
        self.kappa = 1.0e-19

        self.Phi_0 = 1.0
        self.psi_0 = 0.0
        self.theta_0 = 0.1

        self.m_Phi = 1.0 / (10 * kpc)
        self.m_theta = 1.0 / (1 * kpc)

        self.Q_factor = 1.0

    def compute_alpha_beta(self, M):
        """Compute α and β parameters for modified potential."""
        alpha = (self.kappa**2 * self.V_phi * self.Phi_0 *
                 (self.Q_factor * M)**2) / (G * M**2)
        beta = (self.K_theta * self.V_phi * self.theta_0**2) / (G * M**2)
        return alpha, beta

# ============================================================================
# GALAXY ROTATION CURVES
# ============================================================================

def rotation_velocity(r, M, params):
    """Compute circular rotation velocity."""
    alpha, beta = params.compute_alpha_beta(M)
    λΦ = 1.0 / params.m_Phi
    λθ = 1.0 / params.m_theta

    v2_newton = G * M / r
    expΦ = np.exp(-r / λΦ)
    expθ = np.exp(-r / λθ)

    v2_corr = (
        G * M * alpha * (1 / r + 1 / λΦ) * expΦ +
        G * M * beta * (1 / r + 1 / λθ) * expθ
    )

    return np.sqrt(v2_newton + v2_corr)

def plot_rotation_curves():
    """Plot Newtonian vs 6D rotation curves."""
    params = TheoryParameters()

    galaxies = [
        ("Milky Way", 1.0e11, "blue"),
        ("M31",        1.5e11, "red"),
        ("M33",        5.0e10, "green"),
        ("NGC 3198",   3.0e10, "purple")
    ]

    r_kpc = np.logspace(-1, 2, 200)
    r_m = r_kpc * kpc

    plt.figure(figsize=(12, 8))

    for name, mass_solar, color in galaxies:
        M = mass_solar * M_sun
        v6d = rotation_velocity(r_m, M, params) / 1000
        vN = np.sqrt(G * M / r_m) / 1000

        plt.plot(r_kpc, v6d, "-", color=color, label=f"{name} (6D)", linewidth=2)
        plt.plot(r_kpc, vN, "--", color=color, alpha=0.7, label=f"{name} (Newton)")

    plt.xscale("log")
    plt.xlabel("Radius (kpc)")
    plt.ylabel("Velocity (km/s)")
    plt.title("Galaxy Rotation Curves: 6D Unified Field Theory")
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.savefig("MVHristov_6D_UFT_outputs/rotation_curves.png", dpi=300)
    plt.show()

# ============================================================================
# DECOHERENCE SCALING
# ============================================================================

def decoherence_rate(mass, params):
    return (mass / m_p)**(2/3) * 1e-5

def plot_decoherence_scaling():
    params = TheoryParameters()
    masses = np.logspace(-15, -3, 200)
    rates = decoherence_rate(masses, params)
    tau = 1 / rates

    plt.figure(figsize=(10, 6))
    plt.loglog(masses, tau, "b-", linewidth=2)

    reference = {
        "Virus (1e-17 kg)": 1e-17,
        "Bacteria (1e-12 kg)": 1e-12,
        "Dust grain (1e-9 kg)": 1e-9,
        "1 mg object": 1e-6
    }

    for label, m in reference.items():
        plt.plot(m, 1 / decoherence_rate(m, params), "ro")
        plt.annotate(label, (m, 1 / decoherence_rate(m, params)),
                     textcoords="offset points", xytext=(8, 8))

    plt.xlabel("Mass (kg)")
    plt.ylabel("Coherence time τ (s)")
    plt.title("Decoherence Scaling from 6D Geometry")
    plt.grid(True, alpha=0.3)

    plt.savefig("MVHristov_6D_UFT_outputs/decoherence_scaling.png", dpi=300)
    plt.show()

# ============================================================================
# SHORT RANGE GRAVITY
# ============================================================================

def short_range_deviation():
    params = TheoryParameters()
    params.m_Phi = 1 / (1e-3)
    params.m_theta = 1 / (1e-4)

    r = np.logspace(-6, -2, 150)
    M = 1.0

    def F_newton(r):
        return G * M**2 / r**2

    alpha, beta = params.compute_alpha_beta(M)
    λΦ = 1 / params.m_Phi
    λθ = 1 / params.m_theta

    expΦ = np.exp(-r / λΦ)
    expθ = np.exp(-r / λθ)

    F6 = F_newton(r) * (
        1 + alpha * (1 + r / λΦ) * expΦ +
        beta * (1 + r / λθ) * expθ
    )

    deviation = (F6 - F_newton(r)) / F_newton(r) * 100

    plt.figure(figsize=(10, 7))
    plt.subplot(2, 1, 1)
    plt.loglog(r*1000, F6, "b-", label="6D")
    plt.loglog(r*1000, F_newton(r), "r--", label="Newton")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylabel("Force (N)")
    plt.title("Short-Range Gravity: Newton vs 6D")

    plt.subplot(2, 1, 2)
    plt.semilogx(r*1000, deviation, "g-", linewidth=2)
    plt.xlabel("Distance (mm)")
    plt.ylabel("Deviation (%)")
    plt.grid(True, alpha=0.3)

    plt.savefig("MVHristov_6D_UFT_outputs/short_range_gravity.png", dpi=300)
    plt.show()

# ============================================================================
# ATOMIC CLOCK FLUCTUATIONS
# ============================================================================

def clock_fluctuations(params, hours=24):
    t = np.linspace(0, hours, 1000)
    amplitude = np.sqrt(params.K_theta * params.V_phi) / hbar * params.theta_0

    noise = np.random.normal(0, 1, len(t))
    b, a = butter(2, 0.1)
    filtered = filtfilt(b, a, noise)
    filtered = amplitude * filtered / np.std(filtered)

    return t, filtered

def plot_clock_noise():
    params = TheoryParameters()
    t, fl = clock_fluctuations(params)

    plt.figure(figsize=(12, 7))
    plt.subplot(2, 1, 1)
    plt.plot(t, fl*1e18)
    plt.title("Atomic Clock Frequency Noise (6D Prediction)")
    plt.ylabel("δν/ν (×10⁻¹⁸)")
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 1, 2)
    f, Pxx = welch(fl, fs=1000/3600, nperseg=128)
    plt.loglog(f, Pxx)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("PSD")
    plt.grid(True, alpha=0.3)

    plt.savefig("MVHristov_6D_UFT_outputs/clock_fluctuations.png", dpi=300)
    plt.show()

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\nRunning 6D UFT Computational Demonstrations...\n")

    os.makedirs("MVHristov_6D_UFT_outputs", exist_ok=True)

    plot_rotation_curves()
    plot_decoherence_scaling()
    short_range_deviation()
    plot_clock_noise()

    print("\nAll computations completed successfully.")
    print("Output stored in MVHristov_6D_UFT_outputs/")

if __name__ == "__main__":
    main()

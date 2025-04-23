import numpy as np

def calculate_pdi_tsi(series):
    n = len(series)
    pdi = np.zeros(n - 2)
    tsi = np.zeros(n - 2)
    
    for t in range(n - 2):
        # PDI calculation
        pdi[t] = abs((series[t] + series[t + 2]) / 2 - series[t + 1])
        
        # TSI calculation
        segment = series[t:t + 3]
        mean_segment = np.mean(segment)
        sigma_t = np.sqrt(np.sum((segment - mean_segment) ** 2) / 3)
        tsi[t] = pdi[t] - sigma_t
    
    mpdi = np.mean(pdi)
    return pdi, tsi, mpdi

# Example usage
series_linear = np.array([2, 4, 6, 8, 10])
series_oscillatory = np.array([1, 3, 1, 3, 1])
pdi_lin, tsi_lin, mpdi_lin = calculate_pdi_tsi(series_linear)
pdi_osc, tsi_osc, mpdi_osc = calculate_pdi_tsi(series_oscillatory)

print("Linear Series: PDI =", pdi_lin, "TSI =", tsi_lin, "MPDI =", mpdi_lin)
print("Oscillatory Series: PDI =", pdi_osc, "TSI =", tsi_osc, "MPDI =", mpdi_osc)
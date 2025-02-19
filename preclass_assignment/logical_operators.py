
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []  # List to store cleaned values

    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_angles.append(-999)  # Mark bad values
        else:
            cleaned_angles.append(pitch)  # Keep good values unchanged

    return cleaned_angles

# Example usage:
pitch_angles = [10, 85, -5, 95, 40, 100, 70]
status_signals = [0, 0, 1, 0, 0, 2, 1]  # 1 or greater indicates a malfunction


cleaned_data = clean_pitch(pitch_angles, status_signals)
print(cleaned_data)  

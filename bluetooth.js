document.getElementById('scanBluetoothButton').addEventListener('click', async () => {
    try {
        // Check if the browser supports Bluetooth
        if (!navigator.bluetooth) {
            alert('Bluetooth is not supported by this browser.');
            return;
        }

        // Request Bluetooth device and get available devices
        const device = await navigator.bluetooth.requestDevice({
            acceptAllDevices: true,
            // Optionally, you can specify filters here
        });

        // Display the device information
        const deviceList = document.getElementById('deviceList');
        const li = document.createElement('li');
        li.textContent = `Device Name: ${device.name || 'Unknown'}, Device ID: ${device.id}`;
        deviceList.appendChild(li);
    } catch (error) {
        console.error('Error scanning for Bluetooth devices:', error);
        alert('Failed to scan for Bluetooth devices. Please try again.');
    }
});

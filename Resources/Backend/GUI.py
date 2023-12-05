import PySimpleGUI as sg

# Define layout
layout = [
    [sg.Button("Start Scrubbing", key="start")],
    [sg.Output(key="output", size=(60, 10))],
    [sg.Button("Tweak Whitelist", key="whitelist")],
]

# Create window
window = sg.Window("Data Scrubber", layout)

# Initialize whitelist filename (optional)
whitelist_filename = "whitelist.txt"

# Main loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "start":
        # Run your data scrubbing script here, capturing its output and updating the "output" element
        # ... (replace this with your actual script execution)
        window["output"].update(f"Starting scrub...\n")
        # Simulate some scrubbing process
        for i in range(10):
            window["output"].update(f"Scrubbing line {i+1}...\n")
        window["output"].update("Scrubbing complete!\n")
    elif event == "whitelist":
        # Open a separate window for whitelist editing
        whitelist_window = sg.Window("Whitelist Editor", [
            [sg.Multiline(key="whitelist_text", size=(40, 5), default_text="Enter whitelisted elements, each on a line")],
            [sg.Button("Add"), sg.Button("Remove"), sg.Button("Save")]
        ])
        while True:
            whitelist_event, whitelist_values = whitelist_window.read()
            if whitelist_event == sg.WIN_CLOSED:
                break
            # Handle whitelist editing events (add, remove, save)
            # ...
        whitelist_window.close()

window.close()

import tkinter as tk
from tkinter import scrolledtext, messagebox
from scanner import Scanner, ExploitDetector, Reporter
import json  # Import json module

class VulnerabilityScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vulnerability Scanner")

        # Target Input
        tk.Label(root, text="Enter Target URL or IP:").grid(row=0, column=0, padx=10, pady=10)
        self.target_entry = tk.Entry(root, width=50)
        self.target_entry.grid(row=0, column=1, padx=10, pady=10)

        # Run Scan Button
        self.scan_button = tk.Button(root, text="Run Scans", command=self.run_scans)
        self.scan_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Results Text Area
        self.results_area = scrolledtext.ScrolledText(root, width=60, height=20)
        self.results_area.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def run_scans(self):
        target = self.target_entry.get()
        if not target:
            messagebox.showwarning("Input Error", "Please enter a target URL or IP.")
            return

        scanner = Scanner()
        exploit_detector = ExploitDetector()
        reporter = Reporter()

        # Scanning
        try:
            nmap_results = scanner.nmap_scan(target)
            zap_results = scanner.zap_scan(target)
            nikto_results = scanner.nikto_scan(target)

            # Combine results
            results = {
                "nmap": nmap_results,
                "zap": zap_results,
                "nikto": nikto_results
            }

            # Exploit Detection
            for vulnerability in ["SQLi", "XSS"]:  # Example vulnerabilities
                exploits = exploit_detector.search_exploits(vulnerability)
                results[vulnerability] = exploits

            # Generate Report
            reporter.generate_report(results)

            # Display results in the text area
            self.results_area.delete(1.0, tk.END)  # Clear previous results
            self.results_area.insert(tk.END, json.dumps(results, indent=4))  # Correctly use json.dumps

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
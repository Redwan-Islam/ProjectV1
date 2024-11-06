# Vulnerability Scanner

## Overview

The Vulnerability Scanner is a simple application designed to help users identify potential security vulnerabilities in websites or IP addresses. It uses popular scanning tools like Nmap, OWASP ZAP, and Nikto to perform scans and generate a report of the findings.

## Features

- **Nmap Scan**: Identifies open ports and services running on the target.
- **OWASP ZAP Scan**: Performs security scans to find vulnerabilities.
- **Nikto Scan**: Checks for known vulnerabilities in web servers.
- **Report Generation**: Creates an HTML report summarizing the scan results.

## Prerequisites

Before you can run the Vulnerability Scanner, you need to have the following installed on your computer:

1. **Python 3.8 or higher**: The programming language used for this application.
2. **Nmap**: A network scanning tool. You can download it from [Nmap's official website](https://nmap.org/download.html).
3. **OWASP ZAP**: A security scanner. You can download it from [OWASP ZAP's official website](https://www.zaproxy.org/download/).
4. **Nikto**: A web server scanner. You can download it from [Nikto's official website](https://cirt.net/Nikto2).

## Installation

1. **Clone the Repository**: Download the project files to your local machine. You can do this by clicking the green "Code" button on the GitHub page and selecting "Download ZIP" or by using Git:
   ```bash
   git clone https://github.com/yourusername/vulnerability-scanner.git

Modified https://github.com/pallets/flask/tree/main/examples/tutorial

XSS: http://localhost:5000/vulns/xss?text=abc

flask --app vuln_webapp run -h 0.0.0.0 -p 5000

docker build -t vuln_webapp .

Windows Defender Firewall: Add rule
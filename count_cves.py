# count_cves.py - counts vulnerabilities in a pip-audit JSON report
import json
import sys
data = json.load(open(sys.argv[1]))
deps = data["dependencies"]
vulns = [v for d in deps for v in d.get("vulns", [])]
print(f"Packages audited: {len(deps)}")
print(f"Total vulnerabilities found: {len(vulns)}")
if not vulns:
   print("Critical: 0  High: 0  Medium: 0  Low: 0")
else:
   print("Vulnerabilities found - severity must be looked up per ID:")
   for d in deps:
       for v in d.get("vulns", []):
           print(d["name"], d["version"], v["id"], v.get("fix_versions"))

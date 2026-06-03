# Zadání úkolu: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slovniky/excs-2/zranitelnosti

vulnerabilities = [
    {
        "cve": "CVE-2023-2136",
        "product_name": "Google Chrome",
        "version_ranges": [
            {"low_range": "120.0.0", "high_range": "120.0.5615"},
        ],
    },
    {
        "cve": "CVE-2023-4863",
        "product_name": "Google Chrome",
        "version_ranges": [
            {"low_range": "119.0.0", "high_range": "119.0.6099"},
        ],
    },
    {
        "cve": "CVE-2023-21608",
        "product_name": "Adobe Acrobat Reader",
        "version_ranges": [
            {"low_range": "20.0.0", "high_range": "20.5.9"},
            {"low_range": "22.0.0", "high_range": "22.3.9"},
        ],
    },
    {
        "cve": "CVE-2024-20656",
        "product_name": "VLC Media Player",
        "version_ranges": [
            {"low_range": "3.0.0", "high_range": "3.0.9"},
        ],
    },
    {
        "cve": "CVE-2022-41325",
        "product_name": "VLC Media Player",
        "version_ranges": [
            {"low_range": "1.0.0", "high_range": "3.0.17"},
            {"low_range": "4.0.0", "high_range": "4.0.3"},
        ],
    },
]

computers = [
    {
        "computer_name": "maria",
        "installed_software": [
            {"software": "Google Chrome", "version": "119.0.5790"},
            {"software": "Adobe Acrobat Reader", "version": "23.1.4"},
            {"software": "VLC Media Player", "version": "3.0.8"},
        ],
    },
    {
        "computer_name": "jakub",
        "installed_software": [
            {"software": "Microsoft Edge", "version": "124.0.2478"},
            {"software": "Adobe Acrobat Reader", "version": "22.3.0"},
            {"software": "Google Chrome", "version": "120.0.6099"},
        ],
    },
    {
        "computer_name": "anna",
        "installed_software": [
            {"software": "Google Chrome", "version": "120.0.4745"},
            {"software": "VLC Media Player", "version": "4.0.1"},
        ],
    },
    {
        "computer_name": "petra",
        "installed_software": [
            {"software": "Microsoft Edge", "version": "121.0.2277"},
            {"software": "Adobe Acrobat Reader", "version": "20.4.3"},
            {"software": "VLC Media Player", "version": "3.1.1"},
        ],
    },
]

computers_vulnerabilities = {}

for computer in computers:
    for software in computer['installed_software']:
        for vulnerabity in vulnerabilities:
            if software['software'] == vulnerabity['product_name']:
                for version in vulnerabity['version_ranges']:
                    vulnerability_high_range = version['high_range'].split(".")
                    installed_version = software['version'].split(".")
                    vulnerability_low_range = version['low_range'].split(".")
                    low = [int(vulnerability_low_range[0]), int(vulnerability_low_range[1]), int(vulnerability_low_range[2])]
                    high = [int(vulnerability_high_range[0]), int(vulnerability_high_range[1]), int(vulnerability_high_range[2])]
                    installed = [int(installed_version[0]), int(installed_version[1]), int(installed_version[2])]
                    if low <= installed <= high:
                        if computer['computer_name'] not in computers_vulnerabilities:
                            computers_vulnerabilities[computer['computer_name']] = []
                        if vulnerabity['cve'] not in computers_vulnerabilities[computer['computer_name']]:
                            computers_vulnerabilities[computer['computer_name']].append(vulnerabity['cve'])

print(computers_vulnerabilities)
                            


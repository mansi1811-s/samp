# Trivy scanning

Dempo for security scanning in CI CD workflow using Trivy 

    1) In the requiremnets.txt we are using the old version of flask i.e Flask==2.0.1 which is causing  CVE-2023-30861: Flask (METADATA)  vulnerability 
       To fix this we will update the requirements.txt file by adding  
          Flask==2.3.2

    2) To fix CVE-2022-40897 : setuptools (METADATA) ,Regular Expression Denial of Service (ReDoS) in package_index.py
       We will upgrade setuptools by adding upgrade command in Dockerfile
         pip install --upgrade setuptools

   
   

   

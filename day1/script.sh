# Check if we have Linux instances and run the command
if [ -s linux_instances.txt ]; then
    echo "Running Tomcat check on Linux instances..."
    LINUX_INSTANCES=$(cat linux_instances.txt | tr '\t' ',' | tr '\n' ',')
    
    aws ssm send-command --no-verify-ssl \
        --document-name "AWS-RunShellScript" \
        --parameters 'commands=[
            "echo \"=== Tomcat Version Check - Linux ===\"",
            "echo \"Instance: $(hostname) ($(curl -s http://169.254.169.254/latest/meta-data/instance-id 2>/dev/null || echo Unknown))\"",
            "echo \"OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2 | tr -d \\\")\")\"",
            "echo \"Date: $(date)\"",
            "echo",
            "echo \"--- Searching for Tomcat installations ---\"",
            "find /opt /usr /var /home -name \"catalina.sh\" 2>/dev/null | head -10 | while read catalina; do",
            "  echo \"Found Catalina script: $catalina\"",
            "  tomcat_home=$(dirname \"$(dirname \"$catalina\")\")",
            "  echo \"Tomcat Home: $tomcat_home\"",
            "  if [[ -f \"$catalina\" ]]; then",
            "    \"$catalina\" version 2>/dev/null | grep -E \"(Server version|Server number)\" || echo \"Version check failed\"",
            "  fi",
            "  echo \"---\"",
            "done",
            "echo \"--- Running Tomcat processes ---\"",
            "ps aux | grep -i java | grep -i tomcat | grep -v grep || echo \"No running Tomcat processes found\"",
            "echo \"--- Tomcat services ---\"",
            "systemctl list-units --type=service 2>/dev/null | grep -i tomcat || echo \"No Tomcat services found\""
        ]' \
        --targets "Key=InstanceIds,Values=${LINUX_INSTANCES%,}" \
        --comment "Tomcat version check - Linux instances"
    
    LINUX_COMMAND_ID=$(aws ssm send-command --no-verify-ssl \
        --document-name "AWS-RunShellScript" \
        --parameters 'commands=["echo \"Linux Tomcat Check Completed\""]' \
        --targets "Key=InstanceIds,Values=${LINUX_INSTANCES%,}" \
        --query 'Command.CommandId' --output text)
    
    echo "Linux command ID: $LINUX_COMMAND_ID"
else
    echo "No Linux instances found"
fi

# Check if we have Windows instances and run the command
if [ -s windows_instances.txt ]; then
    echo "Running Tomcat check on Windows instances..."
    WINDOWS_INSTANCES=$(cat windows_instances.txt | tr '\t' ',' | tr '\n' ',')
    
    aws ssm send-command --no-verify-ssl \
        --document-name "AWS-RunPowerShellScript" \
        --parameters 'commands=[
            "Write-Host \"=== Tomcat Version Check - Windows ===\"",
            "Write-Host \"Instance: $env:COMPUTERNAME ($(Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/instance-id -ErrorAction SilentlyContinue))\"",
            "Write-Host \"OS: $((Get-WmiObject Win32_OperatingSystem).Caption)\"",
            "Write-Host \"Date: $(Get-Date)\"",
            "Write-Host \"\"",
            "Write-Host \"--- Searching for Tomcat installations ---\"",
            "$tomcatPaths = @(\"C:\\Program Files\\Apache Software Foundation\\Tomcat*\", \"C:\\Program Files (x86)\\Apache Software Foundation\\Tomcat*\", \"C:\\apache-tomcat*\", \"C:\\tomcat*\")",
            "foreach ($path in $tomcatPaths) {",
            "    Get-ChildItem $path -ErrorAction SilentlyContinue | ForEach-Object {",
            "        Write-Host \"Found Tomcat at: $($_.FullName)\"",
            "        $versionFile = Join-Path $_.FullName \"RELEASE-NOTES\"",
            "        if (Test-Path $versionFile) {",
            "            Get-Content $versionFile | Select-String \"Apache Tomcat\" | Select-Object -First 1",
            "        }",
            "        $catalinaPs1 = Join-Path $_.FullName \"bin\\catalina.ps1\"",
            "        $catalinaBat = Join-Path $_.FullName \"bin\\catalina.bat\"",
            "        if (Test-Path $catalinaBat) {",
            "            Write-Host \"Catalina script: $catalinaBat\"",
            "        }",
            "        Write-Host \"---\"",
            "    }",
            "}",
            "Write-Host \"--- Running Tomcat processes ---\"",
            "Get-Process | Where-Object {$_.ProcessName -like \"*tomcat*\" -or $_.ProcessName -like \"*catalina*\" -or $_.ProcessName -like \"*java*\"} | Where-Object {$_.CommandLine -like \"*tomcat*\" -or $_.Path -like \"*tomcat*\"} | Format-Table ProcessName,Id,Path -AutoSize",
            "Write-Host \"--- Tomcat services ---\"",
            "Get-Service | Where-Object {$_.Name -like \"*tomcat*\"} | Format-Table Name,Status,DisplayName -AutoSize"
        ]' \
        --targets "Key=InstanceIds,Values=${WINDOWS_INSTANCES%,}" \
        --comment "Tomcat version check - Windows instances"
    
    WINDOWS_COMMAND_ID=$(aws ssm send-command --no-verify-ssl \
        --document-name "AWS-RunPowerShellScript" \
        --parameters 'commands=["Write-Host \"Windows Tomcat Check Completed\""]' \
        --targets "Key=InstanceIds,Values=${WINDOWS_INSTANCES%,}" \
        --query 'Command.CommandId' --output text)
    
    echo "Windows command ID: $WINDOWS_COMMAND_ID"
else
    echo "No Windows instances found"
fi
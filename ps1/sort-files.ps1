# sort files 

$dir = Get-Location
$filesList = $mydir | Get-ChildItem

foreach ($file in $filesList) {
    if (!($file.BaseName -match "sort_files")) {
        if (!($file.Attributes -eq "Directory")) {
            if (!($file.Extension)) {
                $extension = "no_extension"
            }
            if ($file.Extension.Length -gt 0 ) {
                $extension = $file.Extension.Substring(1)
            }
            $dest = Join-Path -Path $dir -ChildPath $extension
            if (Test-Path $dest) {
                Move-Item -Path $file.FullName -Destination $dest
            }
            else {
                New-Item -Name "$extension" -ItemType Directory
                Move-Item -Path $file.FullName -Destination $dest
            }
        }
    }
}

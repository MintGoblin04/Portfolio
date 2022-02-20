$Number = Read-Host "Do you want to see even/odd/all numbers"
try{
    $data = Get-Content -Path .\number.txt
}
catch{
    Write-Output "number.txt not found, to use this program this file has to be created"
}

if ($number -eq "all") {
    Write-Output "all"
    Write-Output $data
}

elseif ($number -eq "even") {
    Write-Output "even"
    Foreach ($i in $data)
    {
        $x = $i
        $x = $x % 2
        if ($x -eq 0){
            Write-Output $i
        }
    }
}


elseif ($number -eq "odd") {
    Write-Output "odd"
    Foreach ($i in $data)
    {
        $x = $i
        $x = $x % 2
        if ($x -ne 0){
            Write-Output $i
        }
    }
}

else {
    Write-Output "Error"
    Write-Output "Restart"
}


